# -*- coding: utf-8 *-*
# This file is part of Minecraft Backup


# Others imports
from os import path


#############################################################################
# PATHS
#############################################################################


GAME_PATH = {'Linux': path.join(path.expanduser('~'), '.minecraft'),
             'Windows': path.join('%AppData%', '.minecraft'),
             'MacOS': path.join(path.expanduser('~'), 'Library',
                      'Application Support', 'minecraft')}

CONFIG_FOLDER = {'Linux': path.join(path.expanduser('~'), '.minebackup'),
                 'Windows': path.join('%AppData%', '.minebackup'),
                 'MacOS': path.join(path.expanduser('~'), 'Library',
                          'Application Support', 'minebackup')}

SAVE_BACKUP_FOLDER = path.expanduser('~')

PROJECT_PATH = path.abspath(path.dirname(__file__))


#############################################################################
# DEFAULT TEMPLATE FILE config.json
#############################################################################

D_TEMPLATE_CONFIG_JSON = {
                            'save_backup_folder': SAVE_BACKUP_FOLDER
                         }


#############################################################################
# IMAGES
#############################################################################

IMAGES = {'header': path.join(PROJECT_PATH, 'images', 'header.png')}
