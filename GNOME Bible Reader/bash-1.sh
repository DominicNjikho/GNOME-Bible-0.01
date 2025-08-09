# Create source tarball
tar czvf gnome-bible-reader-1.0.tar.gz --transform s/^/gnome-bible-reader-1.0/ *

# Build RPM
rpmbuild -ba gnome-bible-reader.spec