# This file is part of the py-draughts library.
# Copyright (C) 2023-2023 Michał Skibiński
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
A draughts library with advanced (customizable) WEB UI move generation and validation,
PDN parsing and writing. Supports multiple variants of game.
"""
from typing import Literal, Optional, Type

# create board type
from .base import BaseBoard
from .american import Board as AmericanBoard

def get_board(variant: Literal["standard", "american", "frisian"], fen: Optional[str] = None) -> BaseBoard:
    """
    Board factory method.
    - ``standard`` - standard draughts board
    - ``american`` - american checkers board
    - ``frisian`` - frisian draughts board
    """

    print("get_board function")

    BOARDS: dict[str, Type[BaseBoard]] = {
        "american": AmericanBoard,
    }
    board_cls = BOARDS[variant]
    if fen:
        return board_cls.from_fen(fen)
    return board_cls()
