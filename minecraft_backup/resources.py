# -*- coding: utf-8 *-*
# This file is part of Minecraft Backup Manager
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
