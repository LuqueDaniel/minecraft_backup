# -*- coding: utf-8 *-*
# This file is part of Minecraft Backup Manager


# os
from os import path

# sys
import sys


###############################################################################
# PATHS
###############################################################################


GAME_PATH = {'Linux': path.join(path.expanduser('~'), '.minecraft'),
             'Windows': path.join(path.expanduser('~'), 'AppData', 'Roaming',
                        '.minecraft'),
             'MacOS': path.join(path.expanduser('~'), 'Library',
                      'Application Support', 'minecraft')}

CONFIG_FOLDER = {'Linux': path.join(path.expanduser('~'), '.minebackup'),
                 'Windows': path.join(path.expanduser('~'), '.minebackup'),
                 'MacOS': path.join(path.expanduser('~'), 'Library',
                          'Application Support', 'minebackup')}

SAVE_BACKUP_FOLDER = path.expanduser('~')


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
# IMAGES
###############################################################################

IMAGES = {'header': path.join(PROJECT_PATH, 'images', 'header.png')}
