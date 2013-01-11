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


# Minecraft Backu Manager
from minecraft_backup.core.configuration import load_config
from minecraft_backup.core.configuration import save_new_config

# PyQt4.QtGui
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QFileDialog
from PyQt4.QtGui import QDialogButtonBox
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtGui import QHBoxLayout

# PyQt4.QtCore
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QSize


class config_window(QDialog):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setMaximumSize(QSize(0, 0))
        self.setMinimumSize(500, 0)
        self.setWindowTitle('Minecraft Backup Manager - Configuration')

        #STANNDARD BUTTONS
        self.button_box = QDialogButtonBox(self)
        self.button_box.setStandardButtons(QDialogButtonBox.Cancel |
             QDialogButtonBox.Save)

        #input_save_folder
        self.input_save_folder = QLineEdit(self)
        self.input_save_folder.setText(load_config('save_backup_folder'))
        self.input_save_folder.setToolTip('Default folder save backup')

        #change_save_folder
        self.btn_save_folder = QPushButton('Change', self)

        #LAYOUTS
        #Save Folder Layout
        self.layout_save_folder = QHBoxLayout()
        self.layout_save_folder.addWidget(QLabel('Save folder:', self))
        self.layout_save_folder.addWidget(self.input_save_folder)
        self.layout_save_folder.addWidget(self.btn_save_folder)

        #Button Box Layout
        self.layout_button_box = QHBoxLayout()
        self.layout_button_box.setContentsMargins(0, 25, 0, 0)
        self.layout_button_box.addWidget(self.button_box)

        #Vertical Container Layout
        self.Vcontainer = QVBoxLayout(self)
        self.Vcontainer.addLayout(self.layout_save_folder)
        self.Vcontainer.addLayout(self.layout_button_box)

        #CONNECT SIGNALS
        self.connect(self.btn_save_folder, SIGNAL('clicked()'),
                     self.change_save_folder)
        self.connect(self.button_box, SIGNAL('accepted()'),
                     self.save_configurations)
        self.connect(self.button_box, SIGNAL('rejected()'), self.close)

    def change_save_folder(self):
        self.file_dialog = QFileDialog.getExistingDirectory(self,
                           'Change Default folder save backup',
                           directory=self.input_save_folder.text())

        if self.file_dialog != '':
            self.input_save_folder.setText(self.file_dialog)

    def save_configurations(self):
        self.backup_folder = str(self.input_save_folder.text().toUtf8())

        save_new_config(self.backup_folder)
        self.close()
