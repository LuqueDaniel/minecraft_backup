# -*- coding: utf-8 *-*
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


# os
from os import path
from os import environ

# sys
import sys


###############################################################################
# PATHS
###############################################################################

#Select minecraft folder
if sys.platform == 'win32':
    GAME_PATH = path.join(environ['APPDATA'], '.minecraft')
elif sys.platform == 'darwin':
    GAME_PATH = path.join(path.expanduser('~'), 'Library',
                          'Application Support', 'minecraft')
else:
    GAME_PATH = path.join(path.expanduser('~'), '.minecraft')


#Path minebackup config
CONFIG_FOLDER = path.join(path.expanduser('~'), '.minebackup')


#Default save directory
SAVE_BACKUP_FOLDER = path.expanduser('~')

#Project_path
PROJECT_PATH = path.abspath(path.dirname(__file__))


#Only for py2exe
frozen = getattr(sys, 'frozen', '')
if frozen in ('dll', 'console_exe', 'windows_exe'):
    # py2exe:
    PROJECT_PATH = path.abspath(path.dirname(sys.executable))


###############################################################################
# DEFAULT TEMPLATE FILE config.json
###############################################################################

D_TEMPLATE_CONFIG_JSON = {
                            'save_backup_folder': SAVE_BACKUP_FOLDER
                         }


###############################################################################
# STYLES
###############################################################################

STYLES = {}


###############################################################################
# IMAGES
###############################################################################

IMAGES = {
          'header': path.join(PROJECT_PATH, 'images', 'header.png'),
          'minebackup_icon': path.join(PROJECT_PATH, 'images',
                              'minebackup_icon.png'),
          'minebackup_icon_128': path.join(PROJECT_PATH, 'images',
                                  'minebackup_icon_128.png'),
          'config_icon': path.join(PROJECT_PATH, 'images', 'config_icon.png')
          }
