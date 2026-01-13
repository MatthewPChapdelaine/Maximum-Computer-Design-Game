#!/bin/bash
# Build script for creating .deb package

set -e

echo "Building Maximum PC Builder .deb package..."

# Variables
PACKAGE_NAME="maximum-pc-builder"
VERSION="1.0.0"
BUILD_DIR="build"
PACKAGE_DIR="${BUILD_DIR}/${PACKAGE_NAME}_${VERSION}"

# Clean previous build
echo "Cleaning previous build..."
rm -rf ${BUILD_DIR}
mkdir -p ${BUILD_DIR}

# Create directory structure
echo "Creating package structure..."
mkdir -p ${PACKAGE_DIR}/DEBIAN
mkdir -p ${PACKAGE_DIR}/usr/bin
mkdir -p ${PACKAGE_DIR}/usr/share/applications
mkdir -p ${PACKAGE_DIR}/usr/share/pixmaps
mkdir -p ${PACKAGE_DIR}/usr/share/${PACKAGE_NAME}
mkdir -p ${PACKAGE_DIR}/usr/share/doc/${PACKAGE_NAME}

# Copy DEBIAN control files
echo "Copying control files..."
cp DEBIAN/control ${PACKAGE_DIR}/DEBIAN/
cp DEBIAN/postinst ${PACKAGE_DIR}/DEBIAN/
cp DEBIAN/postrm ${PACKAGE_DIR}/DEBIAN/
chmod 755 ${PACKAGE_DIR}/DEBIAN/postinst
chmod 755 ${PACKAGE_DIR}/DEBIAN/postrm

# Copy application files
echo "Copying application files..."
cp src/maximum_pc_game.py ${PACKAGE_DIR}/usr/share/${PACKAGE_NAME}/

# Create launcher script
cat > ${PACKAGE_DIR}/usr/bin/${PACKAGE_NAME} << 'EOF'
#!/bin/bash
python3 /usr/share/maximum-pc-builder/maximum_pc_game.py "$@"
EOF
chmod 755 ${PACKAGE_DIR}/usr/bin/${PACKAGE_NAME}

# Copy desktop file
echo "Copying desktop file..."
cp ${PACKAGE_NAME}.desktop ${PACKAGE_DIR}/usr/share/applications/

# Create icon (simple text-based placeholder)
echo "Creating icon..."
convert -size 256x256 xc:transparent \
    -font "DejaVu-Sans-Bold" -pointsize 48 -fill '#00ff00' \
    -gravity center -annotate +0+0 "MAX\nPC" \
    ${PACKAGE_DIR}/usr/share/pixmaps/${PACKAGE_NAME}.png 2>/dev/null || \
    echo "Note: ImageMagick not found, skipping icon creation"

# If icon creation failed, create a basic text file as placeholder
if [ ! -f ${PACKAGE_DIR}/usr/share/pixmaps/${PACKAGE_NAME}.png ]; then
    echo "Creating placeholder icon..."
    # Create a simple 1x1 PNG
    echo -n "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==" | base64 -d > ${PACKAGE_DIR}/usr/share/pixmaps/${PACKAGE_NAME}.png
fi

# Copy documentation
echo "Copying documentation..."
cp README.md ${PACKAGE_DIR}/usr/share/doc/${PACKAGE_NAME}/
cp LICENSE ${PACKAGE_DIR}/usr/share/doc/${PACKAGE_NAME}/ 2>/dev/null || echo "No LICENSE file found"

# Set permissions
echo "Setting permissions..."
find ${PACKAGE_DIR} -type f -exec chmod 644 {} \;
find ${PACKAGE_DIR} -type d -exec chmod 755 {} \;
chmod 755 ${PACKAGE_DIR}/usr/bin/${PACKAGE_NAME}
chmod 755 ${PACKAGE_DIR}/DEBIAN/postinst
chmod 755 ${PACKAGE_DIR}/DEBIAN/postrm

# Build the package
echo "Building .deb package..."
dpkg-deb --build ${PACKAGE_DIR}

# Move to root directory
mv ${BUILD_DIR}/${PACKAGE_NAME}_${VERSION}.deb ./

echo ""
echo "✓ Package built successfully!"
echo "Package: ${PACKAGE_NAME}_${VERSION}.deb"
echo ""
echo "To install:"
echo "  sudo dpkg -i ${PACKAGE_NAME}_${VERSION}.deb"
echo "  sudo apt-get install -f  # If there are dependency issues"
echo ""
echo "To remove:"
echo "  sudo apt-get remove ${PACKAGE_NAME}"
