# -*- coding: utf-8 *-*
# This file is part of Minecraft Backup Manager

# PyQt4.QtGui
from PyQt4.QtGui import QMessageBox


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


def msg_make_backup_finishied(self):
    msg_backup_finishied = QMessageBox.information(self,
                                'Minecraft backup created',
                                'Backup has been created')
    self.close()
