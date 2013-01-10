# -*- coding: utf-8 *-*
#
# This fail is part of Minecraft Backup Manager
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
from PyQt4.QtGui import QDesktopWidget


def center_widget(widget, parent=None):
    """Center widget in screen"""

    if parent is None:
        center_widget = widget.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        center_widget.moveCenter(center)
        widget.move(center_widget.topLeft())
    else:
        center_widget = widget.frameGeometry()
        center = parent.geometry().center()
        center_widget.moveCenter(center)
        widget.move(center_widget.topLeft())
