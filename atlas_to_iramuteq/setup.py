# -*- coding: utf-8 -*-

from cx_Freeze import setup, Executable

setup(
    name = "atlas_to_iramuteq",
    version = "1.0.0",
    description = ".py to .exe",
    options = {"build_exe": {
        'packages': ["sys", "reader", "sub"],
        'include_msvcr': True,
    }},
    executables = [Executable("convert_file.py", base="Win32GUI")]
)
