from sneks.engine.core.action import Action
from sneks.engine.core.direction import Direction
from sneks.engine.interface.snek import Snek


class CustomSnek(Snek):
    """
    This snek wants to stay still, but will run away
    from obstacles that get too close.
    """

    def get_next_action(self) -> Action:
        # move away from close obstacles
        for direction in Direction:
            if self.look(direction) < 4:
                return direction.get_opposite().get_action()

        # get back to not moving
        if self.get_bearing().x > 0:
            return Action.LEFT
        elif self.get_bearing().x < 0:
            return Action.RIGHT
        elif self.get_bearing().y > 0:
            return Action.DOWN
        elif self.get_bearing().y < 0:
            return Action.UP
        else:
            return Action.MAINTAIN
