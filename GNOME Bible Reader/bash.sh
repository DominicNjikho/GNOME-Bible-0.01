# Create build directory
meson setup builddir --prefix=/usr

# Build
ninja -C builddir

# Install
sudo ninja -C builddir install