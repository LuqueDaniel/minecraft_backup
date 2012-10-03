# -*- coding: utf-8 *-*
# This file is part of Minecraft Backup Manager

# PyQt4.QtGui
from PyQt4.QtGui import QMessageBox

# PyQt4.QtCore
from PyQt4.QtCore import SIGNAL


def msg_about_qt(self):
    about_qt = QMessageBox.aboutQt(self, 'About Qt')


def msg_no_backup_name(self):
    msg_backup_name = QMessageBox.information(self, 'Backup name',
                                 'Enter a name for the backup')
    self.input_backup_name.setFocus()


def msg_dir_exists(self):
    exists_msg = 'there is already a folder named "%s"' % (
                 self.input_backup_name.text())

    msg_dir_exists = QMessageBox.warning(self, 'folder already exists',
                                         exists_msg)


def msg_remove_backup(self):
    msg_backup_remove = QMessageBox.question(self, 'Remove backup',
                                    'Want to delete backup?', QMessageBox.Yes,
                                    QMessageBox.No)

    if msg_backup_remove == QMessageBox.Yes:
        return True
    else:
        return False


def msg_backup_folder_not_exists(self, name_backup):
    exists_msg = 'folder of "%s" not exists' % name_backup

    msg_backup_exists = QMessageBox.warning(self, 'Backup folder not exists',
                                            exists_msg)


def msg_make_backup_finishied(self):
    msg_backup_finishied = QMessageBox.information(self,
                                'Minecraft backup created',
                                'Backup has been created')

    self.emit(SIGNAL('close()'))
    self.close()
