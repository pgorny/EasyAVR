# Easy AVR USB Keyboard Firmware Keymapper
# Copyright (C) 2013-2017 David Howland
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

"""The boards package contains the config files for supported keyboards."""

required_board_attributes = [
    'firmware', 'description', 'unique_id', 'cfg_name', 'teensy', 'hw_boot_key',
    'display_height', 'display_width', 'num_rows', 'num_cols', 'strobe_cols',
    'strobe_low', 'matrix_hardware', 'matrix_strobe', 'matrix_sense', 'num_leds',
    'num_ind', 'num_bl_enab', 'led_definition', 'led_hardware', 'backlighting',
    'bl_modes', 'KMAC_key', 'keyboard_definition', 'alt_layouts'
]
