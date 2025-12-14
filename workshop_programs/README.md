# Workshop Programs

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

For Playwright web automation programs (Programs 24-37):
```bash
pip install playwright pillow
playwright install chromium
```

**Alternative: Use the setup scripts**
```bash
# Linux/Mac:
./setup_workshop.sh

# Windows:
setup_workshop.bat
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

### Computer Vision with OpenCV (Programs 1-23)

- 01. 1. Introduction (5 min)
 Program 1.1: Check OpenCV Installation -> 01_introduction_check_opencv_installation.py
- 02. Program 2.2: Get Image Properties -> 02_get_image_properties.py
- 03. Program 2.3: Save an Image -> 03_save_an_image.py
- 04. Program 2.3: Save an Image - Part 2 -> 04_save_an_image_part_2.py
- 05. Program 3.2: Rotate Image -> 05_rotate_image.py
- 06. Program 3.3: Crop Image -> 06_crop_image.py
- 07. Program 3.4: Color Conversion -> 07_color_conversion.py
- 08. Program 3.4: Color Conversion - Part 2 -> 08_color_conversion_part_2.py
- 09. Program 4.2: Draw Rectangles -> 09_draw_rectangles.py
- 10. Program 4.3: Draw Circles -> 10_draw_circles.py
- 11. Program 4.4: Add Text to Image -> 11_add_text_to_image.py
- 12. Program 4.5: Combined Drawing (Mini Project) -> 12_combined_drawing.py
- 13. Program 4.5: Combined Drawing (Mini Project) - Part 2 -> 13_combined_drawing_part_2.py
- 14. Program 5.2: Detect Blue Color -> 14_detect_blue_color.py
- 15. Program 5.3: Color Detection with Sliders (Colab Version)

**Note:** Since Colab doesn't support cv2 trackbars, we use ipywidgets instead. -> 15_color_detection_with_sliders_note_since_colab_does.py
- 16. Program 5.3: Color Detection with Sliders (Colab Version)

**Note:** Since Colab doesn't support cv2 trackbars, we use ipywidgets instead. - Part 2 -> 16_color_detection_with_sliders_note_since_colab_does.py
- 17. Program 6.2: Thresholding -> 17_thresholding.py
- 18. Program 6.3: Edge Detection (Canny) -> 18_edge_detection.py

### Web Automation with Playwright (Programs 24-37)

- 19. Program 6.4: Find and Draw Contours -> 19_find_and_draw_contours.py
- 20. Program 6.5: Shape Detection using Contours -> 20_shape_detection_using_contours.py
- 21. Program 6.5: Shape Detection using Contours - Part 2 -> 21_shape_detection_using_contours_part_2.py
- 22. Program 7.2: Face + Eye Detection -> 22_face_eye_detection.py
- 23. Program 7.3: Webcam Face Detection (Colab Version)

**Note:** This uses Colab's JavaScript webcam capture instead of cv2.VideoCapture -> 23_webcam_face_detection_note_this_uses_colabs_javasc.py
- 24. Program 1.2: Basic Script Structure -> 24_basic_script_structure.py
- 25. Program 2.2: Open Multiple Pages (Tabs) -> 25_open_multiple_pages.py
- 26. Program 3.2: Click Elements -> 26_click_elements.py
- 27. Program 3.3: Checkbox and Radio Buttons -> 27_checkbox_and_radio_buttons.py
- 28. Program 3.4: Dropdown Selection -> 28_dropdown_selection.py
- 29. Program 3.5: Keyboard Actions -> 29_keyboard_actions.py
- 30. Program 5.2: Extract Links -> 30_extract_links.py
- 31. Program 5.3: Extract Table Data -> 31_extract_table_data.py
- 32. Program 6.2: Element Screenshot -> 32_element_screenshot.py
- 33. Program 6.3: Generate PDF -> 33_generate_pdf.py
- 34. Program 6.4: Multiple Screenshots (Website Comparison) -> 34_multiple_screenshots.py
- 35. Program 7.2: Login Automation (Demo Site) -> 35_login_automation.py
- 36. Program 7.3: Product Scraper -> 36_product_scraper.py
- 37. Program 7.4: Form Automation Complete Flow -> 37_form_automation_complete_flow.py

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

### Playwright Programs

```bash
cd workshop_programs
python3 24_basic_script_structure.py
```

**Note:**
- Playwright browsers must be installed first: `playwright install chromium`
- Browser windows will open (or run headless based on the script)
- Internet connection required for web scraping examples

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

### Playwright Issues

**Error: "Playwright browser not found"**
- Run: `playwright install chromium`
- Make sure you have internet connection

**Browser doesn't open:**
- Some scripts use `headless=True` - they won't show a browser window
- Check if Chromium was installed successfully
- Try running with `headless=False` in the script

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
