# -*- coding: utf-8 *-*
# This file is part of Minecraft Backup Manager
# Source: https://github.com/LuqueDaniel/Minecraft_backup.git


# Minecraft Backup Manager
from minecraft_backup import resources
import minecraft_backup

# sys
import sys

# setuptools
from setuptools import setup
from setuptools import find_packages


if sys.platform == 'win32':
    NEEDED_MODULES = [("PyQt4",
        "http://www.riverbankcomputing.co.uk/software/pyqt/intro"),
        ('win32con', "http://sourceforge.net/projects/pywin32/files/pywin32/")]
else:
    NEEDED_MODULES = [("PyQt4",
        "http://www.riverbankcomputing.co.uk/software/pyqt/intro"), ]


# Add image files
resources_files = [('images', [])]
for img in resources.IMAGES.items():
    resources_files[0][1].append(img[1])


params = {
    'name': minecraft_backup.__prj__,
    'version': minecraft_backup.__version__,
    'description': minecraft_backup.__docu__,
    'author': minecraft_backup.__author__,
    'author_email': minecraft_backup.__mail__,
    'license': minecraft_backup.__license__,

    'include_package_data': True,
    'package_data': {'': ['*.png']},

    'packages': find_packages() + ['minecraft_backup/images'],
    'data_files': resources_files}

setup(**params)
