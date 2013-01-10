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


# Minecraft Backup Manager
from minecraft_backup.core.configuration import load_config
from minecraft_backup.core.backup_manager import make_backup_thread
from minecraft_backup.gui.center_widget import center_widget
from minecraft_backup.gui.msg_box import msg_no_backup_name
from minecraft_backup.gui.msg_box import msg_name_exists
from minecraft_backup.gui.msg_box import msg_dir_exists
from minecraft_backup.gui.msg_box import msg_make_backup_finishied

# PyQt4.QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QFileDialog

# PyQt4.QtCore
from PyQt4.QtCore import QRect
from PyQt4.QtCore import SIGNAL

# os
from os import path


class new_backup_window(QDialog):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setGeometry(QRect(0, 0, 450, 200))
        self.setMaximumSize(450, 200)
        self.setMinimumSize(450, 200)
        self.setWindowTitle('Create a new backup')
        center_widget(self, parent)

        # STANNDARD BUTTONS
        self.btn_cancel = QPushButton('Cancel', self)
        self.btn_cancel.setGeometry(QRect(135, 160, 80, 28))
        self.btn_cancel.setAutoDefault(False)

        # btn_create_backup
        self.btn_create_backup = QPushButton('Create backup', self)
        self.btn_create_backup.setGeometry(QRect(235, 160, 200, 28))

        # LABELS
        self.generate_label('Name', 15, 20)
        self.generate_label('Save folder', 15, 70)

        # input_backup_name
        self.input_backup_name = QLineEdit(self)
        self.input_backup_name.setGeometry(QRect(100, 17, 335, 25))
        self.input_backup_name.text().toUtf8()
        self.input_backup_name.setToolTip('Name of backup')
        self.input_backup_name.setFocus()

        # btn_change_save_backup
        self.btn_change_save_backup = QPushButton(
                                      load_config('save_backup_folder'), self)
        self.btn_change_save_backup.setGeometry(QRect(100, 64, 335, 30))
        self.btn_change_save_backup.setAutoDefault(False)

        # CONNECT SIGNALS
        self.connect(self.btn_change_save_backup, SIGNAL('clicked()'),
                     self.change_save_backup)
        self.connect(self.btn_cancel, SIGNAL('clicked()'), self.close)
        self.connect(self.btn_create_backup, SIGNAL('clicked()'),
                     self.create_backup)

    def generate_label(self, text, h, v):
        self.label = QLabel(self)
        self.label.setText(text)
        self.label.adjustSize()
        self.label.move(h, v)

    def change_save_backup(self):
        self.file_dialog = QFileDialog.getExistingDirectory(self,
                           'Select folder saved for backup',
                           directory=self.btn_change_save_backup.text())

        if self.file_dialog != '':
            self.btn_change_save_backup.setText(self.file_dialog)

    def create_backup(self):
        if self.input_backup_name.text() == '':
            msg_no_backup_name(self)

        else:
            self.dst = path.join(str(self.btn_change_save_backup.text()),
                                 str(self.input_backup_name.text().toUtf8()))

            self.make_backup = make_backup_thread()

            # CONNECT SIGNALS
            self.connect(self.make_backup, SIGNAL('nameexists()'),
                         lambda: msg_name_exists(self))
            self.connect(self.make_backup, SIGNAL('direxists()'),
                         lambda: msg_dir_exists(self))
            self.connect(self.make_backup, SIGNAL('makeend()'),
                         lambda: msg_make_backup_finishied(self))

            self.make_backup.run(self.dst,
                                 str(self.input_backup_name.text().toUtf8()))
