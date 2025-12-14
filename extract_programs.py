import json
import os
import re

def clean_code(code):
    """Clean up code - remove duplicates, fix formatting"""
    lines = code.split('\n')
    cleaned_lines = []
    seen_imports = set()

    for line in lines:
        # Handle imports - avoid duplicates
        if line.strip().startswith('import ') or line.strip().startswith('from '):
            import_key = line.strip()
            if import_key not in seen_imports:
                seen_imports.add(import_key)
                cleaned_lines.append(line)
        else:
            cleaned_lines.append(line)

    return '\n'.join(cleaned_lines)

def convert_colab_to_standard(code, title):
    """Convert Colab-specific code to standard Python"""

    # Remove Colab-specific imports
    code = re.sub(r'from google\.colab\.patches import cv2_imshow\n?', '', code)
    code = re.sub(r'from google\.colab import files\n?', '', code)

    # Create a meaningful window name from title
    window_name = title.replace('Program ', '').replace(':', '-')[:40]

    # Replace cv2_imshow with standard cv2.imshow
    if 'cv2_imshow' in code:
        code = code.replace('cv2_imshow(', f'cv2.imshow("{window_name}", ')

        # Add waitKey and destroyAllWindows if not present
        if 'cv2.waitKey' not in code and 'cv2.destroyAllWindows' not in code:
            code = code.rstrip() + '\ncv2.waitKey(0)\ncv2.destroyAllWindows()\n'

    # If cv2.imshow is used but no waitKey/destroyAllWindows
    elif 'cv2.imshow' in code:
        if 'cv2.waitKey' not in code and 'cv2.destroyAllWindows' not in code:
            code = code.rstrip() + '\ncv2.waitKey(0)\ncv2.destroyAllWindows()\n'

    # Handle file upload/download - add comments with instructions
    if 'files.upload()' in code:
        code = code.replace('files.upload()', '# Place your image file in the same directory\n# Update the path below if needed')

    # Handle print statements before cv2.imshow - these are labels
    code = re.sub(r'print\("([^"]+):"\)\s*\n\s*cv2\.imshow\("Image",',
                  lambda m: f'cv2.imshow("{m.group(1)}",', code)

    # Clean up code
    code = clean_code(code)

    # Add shebang and encoding for Python files
    header = "#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n"
    header += f'"""\n{title}\n\nWorkshop Program - Converted from Google Colab\n"""\n\n'

    return header + code

def sanitize_filename(title):
    """Convert title to valid filename"""
    # Remove program numbering and clean up
    filename = title.lower()
    filename = re.sub(r'program \d+\.?\d*:?\s*', '', filename)
    filename = re.sub(r'^\d+\.\s*', '', filename)
    filename = re.sub(r'\(.*?\)', '', filename)  # Remove parenthetical notes
    filename = re.sub(r'[^\w\s-]', '', filename)
    filename = re.sub(r'[-\s]+', '_', filename)
    filename = filename.strip('_')
    return filename[:50] + '.py'  # Limit length

# Read notebook
with open('workshop_programs_colab.ipynb', 'r') as f:
    nb = json.load(f)

programs = {}
current_section = ""
current_program = ""
skip_next_code = False

for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        text = ''.join(cell['source']).strip()

        # Track sections (##)
        if text.startswith('##') and not text.startswith('###'):
            current_section = text.replace('#', '').strip()

        # Track program titles (###)
        elif text.startswith('###'):
            current_program = text.replace('#', '').strip()
            skip_next_code = False

    elif cell['cell_type'] == 'code':
        code = ''.join(cell['source']).strip()

        # Skip empty cells
        if not code:
            continue

        # Skip setup cells
        if any(skip_pattern in code for skip_pattern in [
            '# Install required packages',
            '# Import Colab-specific',
            '# Download a sample',
            '!pip install',
        ]):
            skip_next_code = True
            continue

        # Skip standalone wget commands
        if code.startswith('!wget') and len(code.split('\n')) == 1:
            continue

        if skip_next_code:
            skip_next_code = False
            continue

        # Use current program title or section
        title = current_program if current_program else current_section

        if title and title not in ["", "---"]:
            # For multi-cell programs, append with separator
            if title in programs:
                # Check if this looks like a new program (starts with import)
                if code.strip().startswith('import ') and len(programs[title]['code']) > 50:
                    # Create a new variant
                    variant_num = 2
                    new_title = f"{title} - Part {variant_num}"
                    while new_title in programs:
                        variant_num += 1
                        new_title = f"{title} - Part {variant_num}"
                    title = new_title
                    programs[title] = {
                        'title': title,
                        'code': code,
                        'section': current_section
                    }
                else:
                    # Append to existing
                    programs[title]['code'] += '\n\n' + code
            else:
                programs[title] = {
                    'title': title,
                    'code': code,
                    'section': current_section
                }

# Create output directory
os.makedirs('workshop_programs', exist_ok=True)

# Write programs to files
file_mapping = []
for i, (key, prog) in enumerate(programs.items(), 1):
    filename = f"{i:02d}_{sanitize_filename(prog['title'])}"
    filepath = f"workshop_programs/{filename}"

    # Convert and write
    converted_code = convert_colab_to_standard(prog['code'], prog['title'])

    with open(filepath, 'w') as f:
        f.write(converted_code)

    file_mapping.append(f"{i:02d}. {prog['title']} -> {filename}")
    print(f"Created: {filename}")

# Create README
readme_content = """# Workshop Programs

This directory contains Python programs extracted from the Google Colab notebook.
Each program is in a separate file for easier demonstration during the workshop.

## Setup

### Prerequisites

1. **Python 3.7+** installed on your system

2. **Install required packages:**

For OpenCV programs (Programs 1-18):
```bash
pip install opencv-python opencv-contrib-python numpy matplotlib
```

For Selenium programs (Programs 19-32):
```bash
pip install selenium webdriver-manager pillow
```

3. **Download sample image:**
```bash
# For Linux/Mac:
wget https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg -O sample.jpg

# Or download manually and save as sample.jpg in the workshop_programs directory
```

4. **For face detection programs**, download Haar Cascade files:
```bash
wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml
```

## Programs List

### Computer Vision with OpenCV (Programs 1-18)

"""

# Split by section
opencv_programs = [m for m in file_mapping if int(m.split('.')[0]) <= 18]
selenium_programs = [m for m in file_mapping if int(m.split('.')[0]) > 18]

for mapping in opencv_programs:
    readme_content += f"- {mapping}\n"

readme_content += "\n### Web Automation with Selenium (Programs 19-32)\n\n"

for mapping in selenium_programs:
    readme_content += f"- {mapping}\n"

readme_content += """
## Running Programs

### OpenCV Programs

```bash
cd workshop_programs
python3 01_check_opencv_installation.py
```

**Note:**
- Make sure `sample.jpg` is in the same directory
- Press any key to close image windows
- Some programs create output files (saved images, etc.)

### Selenium Programs

```bash
cd workshop_programs
python3 19_basic_script_structure.py
```

**Note:**
- Web driver will be downloaded automatically
- Browser windows will open automatically
- Internet connection required

## Important Changes from Colab Version

1. **Display Images**: Replaced `cv2_imshow()` with `cv2.imshow()` + `cv2.waitKey(0)` + `cv2.destroyAllWindows()`

2. **File Paths**: Changed from uploaded files to local file paths. Make sure to:
   - Place `sample.jpg` in the workshop_programs directory
   - Update file paths in programs if needed

3. **Webcam Programs**: Some programs that used IPython widgets in Colab now use standard OpenCV windows

4. **Dependencies**: All Colab-specific dependencies removed

## Troubleshooting

### OpenCV Issues

**Error: "sample.jpg not found"**
- Download sample image or use your own image
- Update file path in the program

**Error: "module 'cv2' has no attribute 'imshow'"**
- You might be in a headless environment
- Use `cv2.imwrite()` to save images instead

### Selenium Issues

**Error: "WebDriver not found"**
- The webdriver-manager should handle this automatically
- Make sure you have internet connection

**Browser doesn't open:**
- Check if Chrome/Firefox is installed
- Update the browser to latest version

## Workshop Tips

1. **Start with simple programs** (01-05) to verify setup
2. **Run programs in order** - they increase in complexity
3. **Modify and experiment** - change parameters to see effects
4. **Check output** - many programs create files or display results
5. **Read comments** - each program has explanatory comments

## Support

For issues or questions:
- Check the program comments for specific requirements
- Verify all dependencies are installed
- Make sure sample files are in the correct location

Happy Learning! 🎓
"""

with open('workshop_programs/README.md', 'w') as f:
    f.write(readme_content)

print(f"\n✓ Total programs extracted: {len(programs)}")
print("✓ README.md created with setup instructions")
print("\nNext steps:")
print("1. cd workshop_programs")
print("2. Download sample.jpg (see README)")
print("3. Run: python3 01_check_opencv_installation.py")
