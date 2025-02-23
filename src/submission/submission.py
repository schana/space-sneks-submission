from sneks.engine.core.action import Action
from sneks.engine.interface.snek import Snek


class CustomSnek(Snek):
    def get_next_action(self) -> Action:
        return Action.MAINTAIN
