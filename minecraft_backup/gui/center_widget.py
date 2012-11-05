# -*- coding: utf-8 *-*
# This fail is part of Minecraft Backup Manager
# Source: https://github.com/LuqueDaniel/Minecraft_backup.git

# PyQt4.QtGui
from PyQt4.QtGui import QDesktopWidget


def center_widget(widget):
    """Center widget in screen"""

    center_widget = widget.frameGeometry()
    center = QDesktopWidget().availableGeometry().center()
    center_widget.moveCenter(center)
    widget.move(center_widget.topLeft())
