#!/usr/bin/env python3

import sys
from .application import BibleApplication

if __name__ == '__main__':
    app = BibleApplication()
    app.run(sys.argv)