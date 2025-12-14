#!/bin/bash
# Setup script for workshop programs

echo "Workshop Programs Setup"
echo "======================="
echo ""

# Install Python packages
echo "1. Installing Python packages..."
pip install -r requirements.txt

# Install Playwright browsers
echo ""
echo "2. Installing Playwright browsers..."
playwright install chromium

# Download sample image
echo ""
echo "3. Downloading sample image..."
if [ ! -f "sample.jpg" ]; then
    wget https://raw.githubusercontent.com/opencv/opencv/master/samples/data/lena.jpg -O sample.jpg
    echo "✓ Sample image downloaded"
else
    echo "✓ sample.jpg already exists"
fi

# Download Haar Cascade files for face detection
echo ""
echo "4. Downloading Haar Cascade files..."
if [ ! -f "haarcascade_frontalface_default.xml" ]; then
    wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
    echo "✓ Face cascade downloaded"
else
    echo "✓ haarcascade_frontalface_default.xml already exists"
fi

if [ ! -f "haarcascade_eye.xml" ]; then
    wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml
    echo "✓ Eye cascade downloaded"
else
    echo "✓ haarcascade_eye.xml already exists"
fi

echo ""
echo "======================="
echo "Setup complete!"
echo ""
echo "To test your setup:"
echo "  python3 01_introduction_check_opencv_installation.py"
echo ""
echo "Press any key in the image window to continue."
