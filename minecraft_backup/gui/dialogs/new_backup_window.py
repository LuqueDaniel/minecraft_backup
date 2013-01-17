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
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtGui import QHBoxLayout

# PyQt4.QtCore
from PyQt4.QtCore import Qt
from PyQt4.QtCore import QSize
from PyQt4.QtCore import SIGNAL

# os
from os import path


class new_backup_window(QDialog):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setMaximumSize(QSize(0, 0))
        self.setMinimumSize(450, 0)
        self.setWindowTitle('Create a new backup')

        #input_backup_name
        self.input_backup_name = QLineEdit(self)
        self.input_backup_name.setToolTip('Name of backup')
        self.input_backup_name.setFocus()

        #btn_change_save_backup
        self.btn_change_save_backup = QPushButton(
                                      load_config('save_backup_folder'), self)
        self.btn_change_save_backup.sizeHint()
        self.btn_change_save_backup.setAutoDefault(False)

        #btn_cancel
        self.btn_cancel = QPushButton('Cancel', self)
        self.btn_cancel.setAutoDefault(False)

        #btn_create_backup
        self.btn_create_backup = QPushButton('Create backup', self)

        #LAYOUTS
        #Backup name layout
        self.layout_name = QHBoxLayout()
        self.layout_name.addWidget(QLabel('Name:', self))
        self.layout_name.addWidget(self.input_backup_name)

        #Save Backup Folder Layout
        self.layout_save_folder = QHBoxLayout()
        self.layout_save_folder.addWidget(QLabel('Save folder:', self))
        self.layout_save_folder.addWidget(self.btn_change_save_backup,
                                          Qt.AlignCenter)

        #Standard Buttons Layout
        self.layout_standard_buttons = QHBoxLayout()
        self.layout_standard_buttons.setContentsMargins(90, 20, 0, 0)
        self.layout_standard_buttons.addWidget(self.btn_cancel)
        self.layout_standard_buttons.addWidget(self.btn_create_backup)

        #Vertical Container Layout
        self.Vcontainer = QVBoxLayout(self)
        self.Vcontainer.addLayout(self.layout_name)
        self.Vcontainer.addLayout(self.layout_save_folder)
        self.Vcontainer.addLayout(self.layout_standard_buttons)

        #CONNECT SIGNALS
        self.connect(self.btn_change_save_backup, SIGNAL('clicked()'),
                     self.change_save_backup)
        self.connect(self.btn_cancel, SIGNAL('clicked()'), self.close)
        self.connect(self.btn_create_backup, SIGNAL('clicked()'),
                     self.create_backup)

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
