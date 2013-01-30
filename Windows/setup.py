# -*- coding: utf-8 -*-
#
# This file is part of Minecraft Backup Manager
#
# Minecraft Backup Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# Minecraft Backup Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Minecraft Backup Manager. If not, see <http://www.gnu.org/licenses/>.
#
# Source: https://github.com/LuqueDaniel/Minecraft_backup.git


# Minecraft Backup Manager
from minecraft_backup import resources
import minecraft_backup

# setuptools
from setuptools import find_packages

# distutils.core
from distutils.core import setup

# py2exe
import py2exe


packages = find_packages()


information = {'script': 'minecraft-backup.py',
              'Version': '1.1',
              'copyright': 'GPL3',
              'name': 'Minecraft Backup Manager',
              'dest_base': 'Minecraft Backup Manager',
              'icon_resources': [(1, 'minebackup.ico')]}


# Add image files
resources_files = [('images', [])]
for img in resources.IMAGES.items():
    resources_files[0][1].append(img[1])


parameters = {
                'name': minecraft_backup.__prj__,
                'version': minecraft_backup.__version__,
                'description': minecraft_backup.__docu__,
                'author': minecraft_backup.__author__,
                'author_email': minecraft_backup.__mail__,
                'license': minecraft_backup.__license__,

                'windows': [information],

                'data_files': resources_files,
                'zipfile': None,
                'options': {
                    'py2exe': {
                        'dll_excludes': ['MSVCP90.dll'],
                        'compressed': 0,
                        'optimize': 0,
                        'includes': ['sip', 'win32com'],
                        'excludes': ['bsddb', 'curses', 'email',
                            'pywin.debugger', 'pywin.debugger.dbgcon',
                            'pywin.dialogs'],
                        'packages': packages,
                        'bundle_files': 1,
                        'dist_dir': 'dist',
                        'xref': False,
                        'skip_archive': False,
                        'ascii': False}
                    }
                }


setup(**parameters)
