from BaseClasses import CollectionState
from ..dlcquest import DLCqworld


def can_dlc_gift(state: CollectionState, player: int, world: DLCqworld):
    if world.options.campaign != 1:
        if state.has("Movement Pack", player):
            if world.options.item_shuffle:
                if state.has("Sword", player):
                    return True
            elif world.options.time_is_money == 1 or state.has("Time is Money Pack", player):
                return True
    if world.options.campaign != 0:
        if world.options.item_shuffle:
            if state.has("Wooden Sword", player) or state.has("Pickaxe", player):
                return True
        elif state.has("Incredibly Important Pack", player):
            return True
    return False