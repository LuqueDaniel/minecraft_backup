# -*- coding: utf-8 *-*

# Imports os
from os import path

#############################################################################
# PATHS
#############################################################################


game_paths = {'Linux': path.join(path.expanduser('~'), '.minecraft'),
              'Windows': path.join('%AppData%', '.minecraft'),
              'MacOS': path.join(path.expanduser('~'), 'Library',
                       'Application Support', 'minecraft')}

config_folder = {'Linux': path.join(path.expanduser('~'), '.minebackup'),
                 'Windows': path.join('%AppData%', '.minebackup'),
                 'MacOS': path.join(path.expanduser('~'), 'Library',
                          'Application Support', 'minebackup')}

save_backup_folder = path.expanduser('~')


#############################################################################
# TEMPLATE FILE config.json
#############################################################################

template_config_json = {
                            'save_backup_folder': save_backup_folder
                       }
