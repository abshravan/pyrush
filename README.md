# Python Workshop Programs

This repository contains Python workshop programs for learning **Computer Vision with OpenCV** and **Web Automation with Playwright**.

## 📚 Contents

- **Original Notebook**: `workshop_programs_colab.ipynb` - Google Colab notebook format
- **Workshop Programs**: `workshop_programs/` - Individual Python files for each program

## 🎯 Workshop Programs

All programs have been extracted from the Google Colab notebook and converted to standalone Python files for easier demonstration and learning.

### Topics Covered

1. **Computer Vision with OpenCV** (Programs 1-23)
   - Image loading, manipulation, and properties
   - Image transformations (resize, rotate, crop)
   - Color conversions and detection
   - Drawing shapes and text
   - Image masking and bitwise operations
   - Thresholding and edge detection
   - Contour detection and shape recognition
   - Face and eye detection using Haar Cascades

2. **Web Automation with Playwright** (Programs 24-37)
   - Basic browser automation
   - Page navigation and interactions
   - Element selection and clicking
   - Form automation (checkboxes, dropdowns, text input)
   - Data extraction (links, tables)
   - Screenshots and PDF generation
   - Login automation
   - Web scraping

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

```bash
cd workshop_programs

# Linux/Mac:
./setup_workshop.sh

# Windows:
setup_workshop.bat
```

### Option 2: Manual Setup

1. **Install dependencies:**
   ```bash
   cd workshop_programs
   pip install -r requirements.txt
   playwright install chromium
   ```

2. **Download required files:**
   ```bash
   # Sample image for OpenCV programs
   wget https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg -O sample.jpg

   # Haar Cascade files for face detection
   wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
   wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml
   ```

3. **Run a program:**
   ```bash
   python3 01_introduction_check_opencv_installation.py
   ```

## 📖 Key Changes from Colab Version

The programs have been converted from Google Colab format to standard Python:

### Image Display
- **Before (Colab):** `cv2_imshow(image)`
- **After (Standard):**
  ```python
  cv2.imshow("Window Name", image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  ```

### File Handling
- **Before (Colab):** Used file upload widgets
- **After (Standard):** Direct file paths (e.g., `sample.jpg`)

### Dependencies
- Removed Google Colab-specific imports (`google.colab.patches`, `ipywidgets`)
- Added standard library equivalents
- All programs are now self-contained Python scripts

### Webcam Programs
- Colab used JavaScript-based webcam capture
- Converted to use OpenCV's `VideoCapture` where applicable

## 📁 Repository Structure

```
pyrush/
├── README.md                          # This file
├── workshop_programs_colab.ipynb      # Original Colab notebook
├── extract_programs.py                # Extraction script
└── workshop_programs/                 # Extracted programs
    ├── README.md                      # Detailed workshop guide
    ├── requirements.txt               # Python dependencies
    ├── setup_workshop.sh              # Setup script (Linux/Mac)
    ├── setup_workshop.bat             # Setup script (Windows)
    ├── 01_introduction_check_opencv_installation.py
    ├── 02_get_image_properties.py
    ├── ...                            # 37 program files total
    └── [downloaded files]             # sample.jpg, cascade files, etc.
```

## 💡 Workshop Tips

1. **Run programs in order** - they increase in complexity
2. **Read the code** - each program has explanatory comments
3. **Experiment** - modify parameters to see different results
4. **Check output** - many programs create files or display results
5. **Use the README** - `workshop_programs/README.md` has detailed instructions

## 🔧 Requirements

- **Python 3.7+**
- **OpenCV** - For computer vision programs
- **Playwright** - For web automation programs
- **Operating System:** Linux, macOS, or Windows

## 📝 Program List

See `workshop_programs/README.md` for the complete list of all 37 programs with descriptions.

## 🤝 For Workshop Instructors

Each program is:
- ✅ Self-contained (runs independently)
- ✅ Commented with explanations
- ✅ Free of Colab dependencies
- ✅ Ready for live demonstration
- ✅ Easily modifiable for variations

## 🐛 Troubleshooting

### Image Display Issues
If running in a headless environment (no display):
```python
# Replace cv2.imshow() with:
cv2.imwrite('output.jpg', image)
```

### Playwright Browser Issues
```bash
# Reinstall browsers
playwright install chromium
```

For more troubleshooting, see `workshop_programs/README.md`.

## 📄 License

Educational use. Programs are designed for workshop and learning purposes.

## 🌟 Getting Started

```bash
# 1. Clone or download this repository
# 2. Navigate to workshop_programs
cd workshop_programs

# 3. Run setup
./setup_workshop.sh

# 4. Start with the first program
python3 01_introduction_check_opencv_installation.py

# 5. Press any key to close image windows
# 6. Continue with the next programs!
```

Happy Learning! 🎓
