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

# PyQt4.QtGui
from PyQt4.QtGui import QMessageBox

# PyQt4.QtCore
from PyQt4.QtCore import SIGNAL


###############################################################################
# main.py
###############################################################################


def msg_about_qt(self):
    about_qt = QMessageBox.aboutQt(self, 'About Qt')


def msg_backup_folder_not_exists(self, name_backup):
    exists_msg = 'folder of "%s" not exists' % name_backup

    msg_backup_exists = QMessageBox.warning(self, 'Backup folder not exists',
                                            exists_msg)


###############################################################################
# new_backup_window.py
###############################################################################


def msg_no_backup_name(self):
    msg_backup_name = QMessageBox.information(self, 'Backup name',
                                 'Enter a name for the backup')
    self.input_backup_name.setFocus()


###############################################################################
# Make backup
###############################################################################

def msg_name_exists(self):
    msg_exists_name = QMessageBox.warning(self, 'Name already exists',
                            'Already a backup with this name')


def msg_dir_exists(self):
    exists_msg = 'there is already a folder named "%s"' % (
                 self.input_backup_name.text())

    msg_dir_exists = QMessageBox.warning(self, 'Folder already exists',
                                         exists_msg)


def msg_IO_denied(self):
    msg_io_denied = QMessageBox.warning(self, 'Permission denied',
    """Permission denied, check if you have permission.\nRecommend closing
    Minecraft for create backup""")


def msg_make_backup_finishied(self):
    msg_backup_finishied = QMessageBox.information(self,
                                'Minecraft backup created',
                                'Backup has been created')

    self.emit(SIGNAL('close()'))
    self.close()


###############################################################################
# Remove backup
###############################################################################


def msg_remove_backup(self):
    msg_backup_remove = QMessageBox.question(self, 'Remove backup',
                                    'Want to delete backup?', QMessageBox.Yes,
                                    QMessageBox.No)

    if msg_backup_remove == QMessageBox.Yes:
        return True
    else:
        return False


###############################################################################
# Restore backup
###############################################################################


def msg_restore_backup(self):
    msg_backup_restore = QMessageBox.question(self, 'Restore backup',
                                     'Restore backup?', QMessageBox.Yes,
                                     QMessageBox.No)

    if msg_backup_restore == QMessageBox.Yes:
        return True
    else:
        return False


def msg_restore_finishied(self, backup_name):
    msg_restore_finishied = QMessageBox.information(self,
                                'Minecraft backup restored',
                                'Backup "%s" has been restored' % backup_name)
