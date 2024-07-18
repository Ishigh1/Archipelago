from BaseClasses import CollectionState
from .squad.SquadInfo import squad_names
from .squad.TagSystem import add_tags


def count_if_in(state: CollectionState, player: int, items: [str]) -> int:
    return sum(state.has(item, player) for item in items)


def has_defense(state: CollectionState, player: int, count: int) -> bool:
    return state.has("3 Starting Grid Defense", player, count / 3)


def has_starting_energy(state: CollectionState, player: int, count: int) -> bool:
    return state.prog_items[player]["start_power"] >= count


def has_starting_cores(state: CollectionState, player: int, count: int) -> bool:
    return state.has("1 Starting Power Core", player, count)


def can_get_2_cores(state: CollectionState, player: int) -> bool:
    return has_starting_energy(state, player, 1)


def can_get_3_cores(state: CollectionState, player: int) -> bool:
    return has_defense(state, player, 6) and has_starting_energy(state, player, 2)


def can_get_4_cores(state: CollectionState, player: int) -> bool:
    return (has_defense(state, player, 6)
            and has_starting_energy(state, player, 3)
            and has_starting_energy(state, player, 1))


def can_get_5_cores(state: CollectionState, player: int) -> bool:
    return (has_defense(state, player, 12)
            and has_starting_energy(state, player, 4)
            and has_starting_energy(state, player, 1))


def unlocked_tags(state: CollectionState, player: int) -> dict[str, int]:
    tags = {}
    for squad_name in squad_names:
        if state.has(squad_name, player):
            add_tags(tags, state.multiworld.worlds[player].squads[squad_name].get_tags())

    return tags


core_function = {
    2: can_get_2_cores,
    3: can_get_3_cores,
    4: can_get_4_cores,
    5: can_get_5_cores,
}
