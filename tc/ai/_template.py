"""Defines a drunken CombatTurtle object."""

### Add full instructions, including the game mechanics and what is and is not allowed to be used.

import tc.tcplayer

class CombatTurtle(tc.tcplayer.CombatTurtleParent):
    """Template Combat Turtle class."""

    #-------------------------------------------------------------------------

    def class_name():
        """CombatTurtle.class_name() -> str
        Static method to return the name of the Combat Turtle AI.
        """

        return "TemplateTurtle"

    #-------------------------------------------------------------------------

    def class_desc():
        """CombatTurtle.class_desc() -> str
        Static method to return a description of the Combat Turtle AI.
        """

        return "This is a template class that does nothing on its own."

    #=========================================================================

    def setup(self):
        """CombatTurtle.setup() -> None
        Initialization code for Combat Turtle.
        """

        pass

    #-------------------------------------------------------------------------

    def step(self):
        """CombatTurtle.setup() -> None
        Step event code for Combat Turtle.
        """

        pass
