#!/usr/bin/env python3

import os
import subprocess

if not os.environ.get('DESTDIR'):
    print('Compiling GSettings schemas...')
    subprocess.call(['glib-compile-schemas', os.path.join(os.environ['MESON_INSTALL_PREFIX'], 'share/glib-2.0/schemas')])