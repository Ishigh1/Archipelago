from BaseClasses import CollectionState
from .Items import itb_island_items
from .squad.Squads import squad_names
from .squad.TagSystem import add_tags


def count_if_in(state: CollectionState, player: int, items: [str]) -> int:
    return sum(state.has(item, player) for item in items)


def has_islands(state, player: int, count: int) -> bool:
    return count_if_in(state, player, itb_island_items) >= count


def has_defense(state: CollectionState, player: int, count: int) -> bool:
    return state.item_count("3 Starting Grid Defense", player) * 3 >= count


def has_starting_energy(state: CollectionState, player: int, count: int) -> bool:
    return state.item_count("2 Starting Grid Power", player) * 2 + 1 >= count


def can_beat_the_game(state: CollectionState, player: int) -> bool:
    return has_defense(state, player, 10) and has_starting_energy(state, player, 3)


def unlocked_tags(state: CollectionState, player: int) -> set[str]:
    tags = set()
    for squad_name in squad_names:
        if state.has(squad_name, player):
            add_tags(tags, state.multiworld.worlds[player].squads[squad_name].get_tags())

    return tags
