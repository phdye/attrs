#!/usr/bin/env python
"""Run the attrs test suite under Python 3.2.5 and capture output.

This script must be executed using a Python 3.2.5 interpreter.
It will run ``pytest`` and write the full output to
``doc/python-3.2.5/baseline/test-output.txt``.
"""

from __future__ import print_function

import os
import sys
import platform
import subprocess


OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "baseline")


def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    output_file = os.path.join(OUTPUT_DIR, "test-output.txt")

    f = open(output_file, "w")
    try:
        f.write("Python executable: %s\n" % sys.executable)
        f.write("Python version: %s\n" % platform.python_version())
        f.write("Platform: %s\n\n" % platform.platform())
        f.flush()

        cmd = [sys.executable, "-m", "pytest", "-v"]
        proc = subprocess.Popen(cmd, stdout=f, stderr=subprocess.STDOUT)
        proc.wait()
        f.write("\nReturn code: %s\n" % proc.returncode)
    finally:
        f.close()

    print("Baseline test output written to %s" % output_file)


if __name__ == "__main__":
    sys.exit(main())
