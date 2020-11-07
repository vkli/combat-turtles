"""Defines a direct CombatTurtle object."""

import math
import tc.tkturtle

class CombatTurtle(tc.tkturtle.TkTurtle):
    """Direct combat turtle.

    Its main strategy is to try to move directly towards the opponent, firing
    missiles when it has clear line of sight. It does not pay much attention
    to obstacles.
    """

    #-------------------------------------------------------------------------

    def class_name():
        """CombatTurtle.class_name() -> str
        Static method to return the name of the Combat Turtle AI.
        """

        return "DirectTurtle"

    #-------------------------------------------------------------------------

    def class_desc():
        """CombatTurtle.class_desc() -> str
        Static method to return a description of the Combat Turtle AI.
        """

        return "Moves directly towards opponent while ignoring obstacles."

    #-------------------------------------------------------------------------

    def class_shape():
        """CombatTurtle.class_shape() -> (int or tuple)
        Static method to define the Combat Turtle's shape image.

        The return value can be either an integer or a tuple of tuples.

        Returning an integer index selects one of the following preset shapes:
            0 -- arrowhead (also default in case of unrecognized index)
            1 -- turtle
            2 -- plow
            3 -- triangle
            4 -- kite
            5 -- pentagon
            6 -- hexagon
            7 -- star

        A custom shape can be defined by returning a tuple of the form
        (radius, angle), where radius is a tuple of radii and angle is a tuple
        of angles (in radians) describing the polar coordinates of a polygon's
        vertices. The shape coordinates should be given for a turtle facing
        east.
        """

        return 0

    #=========================================================================

    def setup(self):
        """CombatTurtle.setup() -> None
        Initialization code for direct Combat Turtle.
        """

        # Define constant linear and angular speed factors
        self.spd = 1.0
        self.turn_spd = 1.0

        ###
        self.counter = 0

    #-------------------------------------------------------------------------

    def step(self):
        """CombatTurtle.setup() -> None
        Step event code for direct Combat Turtle.
        """

        # Turn towards opponent
        ###self.turn_towards()
        #self.left(0.075)
        ###print(self.relative_position())
        #print("-"*20)
        # print(self.relative_heading((self.x - 100, self.y))) # 180
        # print(self.relative_heading((self.x - 100, self.y - 100))) # 135
        # print(self.relative_heading((self.x, self.y - 100))) # 90
        # print(self.relative_heading((self.x + 100, self.y - 100))) # 45
        # print(self.relative_heading((self.x + 100, self.y))) # 0
        # print(self.relative_heading((self.x + 100, self.y + 100))) # -45
        # print(self.relative_heading((self.x, self.y + 100))) # -90
        # print(self.relative_heading((self.x - 100, self.y + 100))) # -135
        ###print("heading = " + str(self.heading))###
        # print(self.relative_heading_towards((self.x - 100, self.y))) # 90
        # print(self.relative_heading_towards((self.x - 100, self.y - 100))) # 45
        # print(self.relative_heading_towards((self.x, self.y - 100))) # 0
        # print(self.relative_heading_towards((self.x + 100, self.y - 100))) # -45
        # print(self.relative_heading_towards((self.x + 100, self.y))) # -90
        # print(self.relative_heading_towards((self.x + 100, self.y + 100))) # -135
        # print(self.relative_heading_towards((self.x, self.y + 100))) # 180
        # print(self.relative_heading_towards((self.x - 100, self.y + 100))) # 135
        self.turn_towards()
        ###self.turn_towards((self.x - 100, self.y))
        # for t in range(12):
        #     print(self.relative_heading((self.x + 100*math.cos(t*math.pi/6),
        #                                  self.y + 100*math.sin(t*math.pi/6))))

        # self.counter += 1
        # if self.heading < 180:
        #     self.rt()
        # elif self.heading > 180:
        #     self.lt()
        # else:
        #     if self.x > self.arena_right/2:
        #         self.forward()
        #     if self.can_shoot:
        #         self.shoot()

        self.forward()

        # Move towards opponent (or away if too close)
        # if self.distance() > self.missile_radius:
        #     self.forward(self.speed)
        # else:
        #     self.backward(self.speed)

        ### Shoot if facing opponent

        #print(self.turn_speed)
