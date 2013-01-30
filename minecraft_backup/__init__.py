#-*- conding: utf-8 -*-
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


__prj__ = 'Minecraft Backup Manager'
__author__ = 'Daniel Luque'
__mail__ = 'danielluque14@gmail.com'
__url__ = 'http://luquedaniel.github.com/Minecraft_backup'
__source__ = 'http://github.com/LuqueDaniel/Minecraft_backup'
__version__ = '1.1'
__version_name__ = 'Stone'
__license__ = 'GPL v3'
__docu__ = """Minecraft Backup Manager is an application for managing Minecraft
backups quickly and easily."""


def run():
    from minecraft_backup import core

    core.run_minebackup()
