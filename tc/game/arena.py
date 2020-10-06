"""Defines the arena container class."""

import math
from .block import Block

class Arena:
    """Arena class.

    Acts as a container to store the contents of the arena, including all of
    the blocks. The arrangement of blocks is chosen by passing a numerical ID
    to the constructor.

    The arena layouts are defined as follows:
        0 -- empty
        1 -- large square in middle
        2 -- four columns near corners
        3 -- wall with a central passage
        4 -- plus sign
    """

    #-------------------------------------------------------------------------

    def get_names():
        """Arena.get_names() -> list
        Static method to return list of arena layout names.
        """

        return ["Empty Arena", "Central Column Arena", "Corner Column Arena",
                "Doorway Arena", "Plus-Shaped Arena"]

    #-------------------------------------------------------------------------

    def get_p1_coords(index):
        """Arena.get_p1_coords() -> (int, int)
        Static method to return the default starting coordinates of Player 1.

        Requires the following positional arguments:
            index (int) -- arena layout index
        """

        # All currently-defined arenas use the same initial coordinates
        return (200, 400)

    #-------------------------------------------------------------------------

    def get_p2_coords(index):
        """Arena.get_p2_coords() -> (int, int)
        Static method to return the default starting coordinates of Player 2.

        Requires the following positional arguments:
            index (int) -- arena layout index
        """

        # All currently-defined arenas use the same initial coordinates
        return (600, 400)

    #-------------------------------------------------------------------------

    def get_p1_heading(index):
        """Arena.get_p1_heading() -> int
        Static method to return the default starting heading of Player 1.

        Requires the following positional arguments:
            index (int) -- arena layout index
        """

        # All currently-defined arenas use the same initial headings
        return 90

    #-------------------------------------------------------------------------

    def get_p2_heading(index):
        """Arena.get_p2_heading() -> int
        Static method to return the default starting heading of Player 2.

        Requires the following positional arguments:
            index (int) -- arena layout index
        """

        # All currently-defined arenas use the same initial headings
        return -90

    #=========================================================================

    def __init__(self, game, size=(800, 800), layout=0):
        """Arena([size], [layout], [walls]) -> Arena
        Arena constructor, including obstacle setup.

        Requires the following positional arguments:
            game (tcgame.TurtleCombatGame) -- game driver object

        Accepts the following optional keyword arguments:
            size (tuple (int, int)) [(800, 800)] -- arena width/height (px)
            layout (int) [0] -- arena obstacle layout ID (see class docstring)

        The arena is centered at the origin and has the specified total width
        and height.
        """

        # Assign given attributes
        self.game = game
        self.size = size

        # Initialize block object list
        self.blocks = []

        # Generate the walls defined by the layout (default to empty)
        if layout == 1:
            # Large square in middle
            self._single_block()
        elif layout == 2:
            # Four small squares near corners
            self._corner_blocks()
        elif layout == 3:
            # Central wall with passage
            self._doorway_blocks()
        elif layout == 4:
            # Plus sign
            self._plus_blocks()

    #-------------------------------------------------------------------------

    def __del__(self):
        """~Arena() -> None
        Arena destructor deletes all blocks in arena.
        """

        del self.blocks[:]

    #-------------------------------------------------------------------------

    def _single_block(self):
        """Arena._single_block() -> None
        Generates the blocks of the Central Column arena type.
        """

        # Define column block
        self.blocks.append(Block(self.game, (self.size[0]/2)-80,
                                 (self.size[0]/2)+80, (self.size[1]/2)-80,
                                 (self.size[1]/2)+80))

    #-------------------------------------------------------------------------

    def _corner_blocks(self):
        """Arena._corner_blocks() -> None
        Generates the blocks of the Corner Column arena type.
        """

        # Define four small columns
        self.blocks.append(Block(self.game, 200, 260, 200, 260))
        self.blocks.append(Block(self.game, self.size[0]-260,
                                 self.size[0]-200, 200, 260))
        self.blocks.append(Block(self.game, 200, 260, self.size[1]-260,
                                 self.size[1]-200))
        self.blocks.append(Block(self.game, self.size[0]-260,
                                 self.size[0]-200, self.size[1]-260,
                                 self.size[1]-200))

    #-------------------------------------------------------------------------

    def _doorway_blocks(self):
        """Arena._doorway_blocks() -> None
        Generates the blocks of the Central Doorway arena type.
        """

        # Define two wall portions
        self.blocks.append(Block(self.game, (self.size[0]/2)-30,
                                 (self.size[0]/2)+30, -40,
                                 (self.size[1]/2)-60))
        self.blocks.append(Block(self.game, (self.size[0]/2)-30,
                                 (self.size[0]/2)+30, (self.size[1]/2)+60,
                                 self.size[1]+40))

    #-------------------------------------------------------------------------

    def _plus_blocks(self):
        """Arena._plus_blocks() -> None
        Generates the blocks of the Plus-Shaped arena type.
        """

        # Define two crossing wall portions
        self.blocks.append(Block(self.game, (self.size[0]/2)-30,
                                 (self.size[0]/2)+30,
                                 math.floor(self.size[1]/3),
                                 math.ceil(2*self.size[1]/3)))
        self.blocks.append(Block(self.game, math.floor(self.size[0]/3),
                                 math.ceil(2*self.size[0]/3),
                                 (self.size[1]/2)-30, (self.size[1]/2)+30))

    #-------------------------------------------------------------------------

    def intersections(self, coords):
        """Arena.intersections(coords) -> list
        Returns a list of block objects that intersect a given coordinate.

        Requires the following positional arguments:
            coords (tuple (int, int)) -- coordinate to test

        If the coordinate intersects no blocks, an empty list will be
        returned.
        """

        # Return a list of all blocks that intersect the given coordinate
        return [b for b in self.blocks if b.contains(coords)]

    #-------------------------------------------------------------------------

    def get_blocks(self):
        """Arena.get_blocks() -> list
        Returns a list of all block objects in the arena.
        """

        return self.blocks
