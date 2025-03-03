from worlds.tloz_oos.data.EntranceType import OoSEntranceType
from worlds.tloz_oos.data.logic.LogicPredicates import *


def make_subrosia_logic(player: int):
    return [
        # Vanilla connections ###################################################
        ["eastern suburbs portal", "volcanoes east portal", OoSEntranceType.Portal, None],
        ["spool swamp portal", "subrosia market portal", OoSEntranceType.Portal, None],
        ["mt. cucco portal", "strange brothers portal", OoSEntranceType.Portal, None],
        ["horon village portal", "house of pirates portal", OoSEntranceType.Portal, None],
        ["eyeglass lake portal", "great furnace portal", OoSEntranceType.Portal, None],
        ["temple remains lower portal", "volcanoes west portal", OoSEntranceType.Portal, None],
        ["temple remains upper portal", "d8 entrance portal", OoSEntranceType.Portal, None],

        # Portals ###############################################################

        ["volcanoes east portal", "subrosia temple sector", OoSEntranceType.TwoWay, None],
        ["subrosia market portal", "subrosia market sector", OoSEntranceType.TwoWay, None],
        ["strange brothers portal", "subrosia hide and seek sector", OoSEntranceType.TwoWay, lambda state: oos_has_feather(state, player)],
        ["house of pirates portal", "subrosia pirates sector", OoSEntranceType.TwoWay, None],
        ["great furnace portal", "subrosia furnace sector", OoSEntranceType.TwoWay, None],
        ["volcanoes west portal", "subrosia volcano sector", OoSEntranceType.TwoWay, None],
        ["d8 entrance portal", "d8 entrance", OoSEntranceType.TwoWay, None],

        # Regions ###############################################################

        ["subrosia temple sector", "subrosia market sector", OoSEntranceType.OneWay, lambda state: \
            oos_can_jump_1_wide_liquid(state, player, False)],
        ["subrosia market sector", "subrosia temple sector", OoSEntranceType.OneWay, lambda state: \
            oos_can_jump_1_wide_liquid(state, player, False)],

        ["subrosia market sector", "enter Rosa corridor right", OoSEntranceType.TwoWay, lambda state: oos_can_date_rosa(state, player)],
        ["enter Rosa corridor right", "inside Rosa corridor right", OoSEntranceType.DoorComplexTwoWay, lambda state: oos_can_date_rosa(state, player)],
        ["inside Rosa corridor right", "enter Rosa corridor right", OoSEntranceType.DoorComplexTwoWay, None],
        ["inside Rosa corridor right", "inside Rosa corridor left", OoSEntranceType.TwoWay, lambda state: oos_can_date_rosa(state, player)],
        ["enter Rosa corridor left", "inside Rosa corridor left", OoSEntranceType.DoorTwoWay, lambda state: oos_can_date_rosa(state, player)],
        ["subrosia temple sector", "enter Rosa corridor left", OoSEntranceType.TwoWay, lambda state: oos_can_date_rosa(state, player)],

        ["subrosia market sector", "subrosia east junction", OoSEntranceType.OneWay, lambda state: any([
            oos_has_magnet_gloves(state, player),
            # As it is a "diagonal" pit, it is considered as a 3.5-wide pit
            oos_can_jump_3_wide_liquid(state, player)
        ])],
        ["subrosia east junction", "subrosia market sector", OoSEntranceType.OneWay, lambda state: any([
            # This backwards route adds itself on top of the two-way route right above this one, adding the option
            # to remove the rock using the bracelet to turn this pit into a 2-wide jump
            all([
                oos_has_bracelet(state, player),
                oos_can_jump_2_wide_pit(state, player)
            ]),
            oos_has_magnet_gloves(state, player),
            # As it is a "diagonal" pit, it is considered as a 3.5-wide pit
            oos_can_jump_3_wide_liquid(state, player)
        ])],

        ["subrosia temple sector", "subrosia bridge sector", OoSEntranceType.TwoWay, lambda state: oos_has_feather(state, player)],
        ["subrosia volcano sector", "subrosia bridge sector", OoSEntranceType.OneWay, lambda state: all([
            oos_has_bracelet(state, player),
            oos_can_jump_3_wide_liquid(state, player)
        ])],

        ["subrosia volcano sector", "enter volcano cave", OoSEntranceType.TwoWay, None],
        ["enter volcano cave", "inside volcano cave", OoSEntranceType.DoorTwoWay, None],
        ["inside volcano cave", "bomb temple remains", OoSEntranceType.OneWay, lambda state: oos_has_bombs(state, player)],

        ["subrosia hide and seek sector", "subrosia market sector", OoSEntranceType.OneWay, lambda state: all([
            oos_has_bracelet(state, player),
            oos_has_feather(state, player),
            any([
                oos_can_jump_2_wide_liquid(state, player),
                oos_has_magnet_gloves(state, player)
            ])
        ])],
        ["subrosia hide and seek sector", "subrosia temple sector", OoSEntranceType.TwoWay, lambda state: oos_can_jump_4_wide_liquid(state, player)],
        ["subrosia hide and seek sector", "subrosia pirates sector", OoSEntranceType.TwoWay, lambda state: oos_has_feather(state, player)],

        ["subrosia east junction", "subrosia furnace sector", OoSEntranceType.TwoWay, lambda state: oos_has_feather(state, player)],

        # Locations ###############################################################

        ["subrosia temple sector", "enter boomerang cave", OoSEntranceType.TwoWay, lambda state: oos_can_jump_1_wide_pit(state, player, False)],
        ["enter boomerang cave", "inside boomerang cave", OoSEntranceType.DoorTwoWay, None],
        ["inside boomerang cave", "subrosian secret", OoSEntranceType.OneWay, lambda state: oos_has_magic_boomerang(state, player)],

        ["subrosia temple sector", "enter dance hall", OoSEntranceType.TwoWay, None],
        ["enter dance hall", "inside dance hall", OoSEntranceType.DoorTwoWay, None],
        ["inside dance hall", "subrosian dance hall", OoSEntranceType.OneWay, None],

        ["subrosia temple sector", "enter smithy", OoSEntranceType.TwoWay, None],
        ["enter smithy", "inside smithy", OoSEntranceType.DoorTwoWay, None],
        ["inside smithy", "subrosian smithy ore", OoSEntranceType.OneWay, lambda state: any([
            state.has("Hard Ore", player),
            all([
                not state.multiworld.worlds[player].options.secret_locations,
                oos_self_locking_item(state, player, "subrosian smithy ore", "Hard Ore")
            ])
        ])],
        ["inside smithy", "subrosian smithy bell", OoSEntranceType.OneWay, lambda state: any([
            state.has("Rusty Bell", player),
            all([
                not state.multiworld.worlds[player].options.secret_locations,
                oos_self_locking_item(state, player, "subrosian smithy bell", "Rusty Bell")
            ])
        ])],
        ["inside smithy", "smith secret", OoSEntranceType.OneWay, lambda state: oos_has_shield(state, player)],

        ["subrosia temple sector", "enter useless subrosian house", OoSEntranceType.TwoWay, None],
        ["enter useless subrosian house", "inside useless subrosian house", OoSEntranceType.DoorTwoWay, None],

        ["subrosia temple sector", "enter temple of seasons", OoSEntranceType.TwoWay, None],
        ["enter temple of seasons", "inside temple of seasons", OoSEntranceType.DoorTwoWay, None],
        ["inside temple of seasons", "temple of seasons", OoSEntranceType.OneWay, None],

        ["subrosia temple sector", "enter temple of winter", OoSEntranceType.TwoWay, None],
        ["enter temple of winter", "inside temple of winter", OoSEntranceType.DoorTwoWay, None],
        ["inside temple of winter", "tower of winter", OoSEntranceType.OneWay, lambda state: any([
            oos_has_feather(state, player),
            oos_can_trigger_far_switch(state, player)
        ])],

        ["subrosia temple sector", "enter tower of summer", OoSEntranceType.TwoWay, None],
        ["enter tower of summer", "inside tower of summer", OoSEntranceType.DoorTwoWay, lambda state: oos_can_date_rosa(state, player)],
        ["inside tower of summer", "tower of summer", OoSEntranceType.OneWay, lambda state: oos_has_bracelet(state, player)],

        ["subrosia temple sector", "enter tower of autumn", OoSEntranceType.TwoWay, lambda state: all([
            oos_has_feather(state, player),
            state.has("Bomb Flower", player)
        ])],
        ["enter tower of autumn", "inside tower of autumn", OoSEntranceType.DoorTwoWay, None],
        ["inside tower of autumn", "tower of autumn", OoSEntranceType.OneWay, lambda state: oos_has_feather(state, player)],

        ["subrosia market sector", "subrosia seaside", OoSEntranceType.OneWay, lambda state: oos_has_shovel(state, player)],
        ["subrosia market sector", "enter subrosian market", OoSEntranceType.TwoWay, None],
        ["enter subrosian market", "inside subrosian market", OoSEntranceType.DoorTwoWay, None],
        ["inside subrosian market", "subrosia market star ore", OoSEntranceType.OneWay, lambda state: any([
            state.has("Star Ore", player),
            oos_self_locking_item(state, player, "subrosia market star ore", "Star Ore")
        ])],
        ["inside subrosian market", "subrosia market ore chunks", OoSEntranceType.OneWay, lambda state: \
            oos_can_buy_market(state, player)],

        ["subrosia hide and seek sector", "enter strange brothers right", OoSEntranceType.TwoWay, None],
        ["enter strange brothers right", "inside strange brothers right", OoSEntranceType.DoorTwoWay, None],
        ["inside strange brothers right", "inside strange brothers left", OoSEntranceType.TwoWay, None],
        ["inside strange brothers left", "enter strange brothers left", OoSEntranceType.DoorTwoWay, None],
        ["enter strange brothers left", "subrosia hide and seek", OoSEntranceType.OneWay, lambda state: all([
            state.has("_met_strange_brothers", player),
            oos_has_shovel(state, player)
        ])],
        ["subrosia hide and seek sector", "tower of spring", OoSEntranceType.OneWay, lambda state: oos_has_feather(state, player)],
        ["subrosia hide and seek sector", "subrosian wilds chest", OoSEntranceType.OneWay, lambda state: all([
            oos_has_feather(state, player),
            any([
                oos_has_magnet_gloves(state, player),
                oos_can_jump_4_wide_pit(state, player)
            ])
        ])],
        ["subrosian wilds chest", "subrosian wilds digging spot", OoSEntranceType.OneWay, lambda state: all([
            any([
                oos_can_jump_3_wide_pit(state, player),
                oos_has_magnet_gloves(state, player)
            ]),
            oos_has_feather(state, player),
            oos_has_shovel(state, player)
        ])],

        ["subrosia hide and seek sector", "enter house above hide and seek", OoSEntranceType.TwoWay, None],
        ["enter house above hide and seek", "inside house above hide and seek", OoSEntranceType.DoorTwoWay, None],
        ["inside house above hide and seek", "subrosian house", OoSEntranceType.OneWay, lambda state: oos_has_feather(state, player)],

        ["subrosia hide and seek sector", "enter staircase to tower of spring", OoSEntranceType.TwoWay, None],
        ["enter staircase to tower of spring", "inside staircase to tower of spring", OoSEntranceType.DoorTwoWay, None],
        ["inside staircase to tower of spring", "subrosian 2d cave", OoSEntranceType.TwoWay, lambda state: oos_has_feather(state, player)],
        ["subrosian 2d cave", "inside tower of spring staircase", OoSEntranceType.TwoWay, None],
        ["inside tower of spring staircase", "enter tower of spring staircase", OoSEntranceType.DoorTwoWay, None],
        ["enter tower of spring staircase", "enter tower of spring", OoSEntranceType.TwoWay, None],
        ["enter tower of spring", "inside tower of spring", OoSEntranceType.DoorTwoWay, None],
        ["inside tower of spring", "tower of spring", OoSEntranceType.OneWay, lambda state: oos_has_feather(state, player)],

        ["subrosia pirates sector", "enter pirate house", OoSEntranceType.TwoWay, None],
        ["enter pirate house", "inside pirate house", OoSEntranceType.DoorTwoWay, None],
        ["inside pirate house", "pirate captain", OoSEntranceType.TwoWay, None],
        ["enter pirate staircase", "subrosia pirates sector", OoSEntranceType.OneWay, None],
        ["enter pirate staircase", "inside pirate staircase", OoSEntranceType.DoorTwoWay, None],
        ["inside pirate staircase", "pirate captain", OoSEntranceType.TwoWay, None],
        ["subrosia pirates sector", "enter subrosia ship", OoSEntranceType.TwoWay, None],
        ["enter subrosia ship", "inside subrosia ship", OoSEntranceType.DoorTwoWay, None],

        ["subrosia bridge sector", "enter subrosia open cave", OoSEntranceType.TwoWay, None],
        ["enter subrosia open cave", "inside subrosia open cave", OoSEntranceType.DoorTwoWay, None],

        ["subrosia bridge sector", "enter subrosia locked door", OoSEntranceType.TwoWay, lambda state: oos_can_date_rosa(state, player)],
        ["enter subrosia locked door", "inside subrosia locked door", OoSEntranceType.DoorComplexTwoWay, lambda state: oos_can_date_rosa(state, player)],
        ["inside subrosia locked door", "enter subrosia locked door", OoSEntranceType.DoorComplexTwoWay, None],
        ["inside subrosia locked door", "subrosia, locked cave", OoSEntranceType.OneWay, None],

        ["subrosia bridge sector", "enter subrosian cook", OoSEntranceType.TwoWay, None],
        ["enter subrosian cook", "inside subrosian cook", OoSEntranceType.DoorTwoWay, None],
        ["inside subrosian cook", "subrosian chef trade", OoSEntranceType.OneWay, lambda state: any([
            state.has("Iron Pot", player),
            oos_self_locking_item(state, player, "subrosian chef trade", "Iron Pot")
        ])],

        ["subrosia east junction", "enter red ore cave", OoSEntranceType.TwoWay, lambda state: any([
            oos_has_magnet_gloves(state, player),
            oos_can_jump_4_wide_pit(state, player),
        ])],
        ["enter red ore cave", "inside red ore cave", OoSEntranceType.DoorTwoWay, None],
        ["inside red ore cave", "inside red ore stairs", OoSEntranceType.TwoWay, None],
        ["inside red ore stairs", "enter red ore stairs", OoSEntranceType.DoorTwoWay, None],
        ["enter red ore stairs", "subrosia village chest", OoSEntranceType.OneWay, None],

        ["subrosia furnace sector", "enter furnace", OoSEntranceType.TwoWay, None],
        ["enter furnace", "inside furnace", OoSEntranceType.DoorTwoWay, None],
        ["inside furnace", "great furnace", OoSEntranceType.OneWay, lambda state: all([
            state.has("_opened_tower_of_autumn", player),
            any([
                state.has("Red Ore", player),
                oos_self_locking_item(state, player, "great furnace", "Red Ore")
            ]),
            any([
                state.has("Blue Ore", player),
                oos_self_locking_item(state, player, "great furnace", "Blue Ore")
            ]),
        ])],
        ["subrosia furnace sector", "enter sign guy", OoSEntranceType.TwoWay, None],
        ["enter sign guy", "inside sign guy", OoSEntranceType.DoorTwoWay, None],
        ["inside sign guy", "subrosian sign guy", OoSEntranceType.OneWay, lambda state: oos_can_break_sign(state, player)],
        ["subrosia furnace sector", "subrosian buried bomb flower", OoSEntranceType.OneWay, lambda state: all([
            oos_has_feather(state, player),
            oos_has_bracelet(state, player)
        ])],

        ["subrosia temple sector", "subrosia temple digging spot", OoSEntranceType.OneWay, lambda state: oos_has_shovel(state, player)],
        ["subrosia temple sector", "subrosia bath digging spot", OoSEntranceType.OneWay, lambda state: all([
            oos_can_jump_1_wide_pit(state, player, False),
            any([
                oos_can_jump_3_wide_liquid(state, player),
                oos_has_magnet_gloves(state, player)
            ]),
            oos_has_shovel(state, player)
        ])],
        ["subrosia market sector", "subrosia market digging spot", OoSEntranceType.OneWay, lambda state: oos_has_shovel(state, player)],

        ["subrosia bridge sector", "subrosia bridge digging spot", OoSEntranceType.OneWay, lambda state: oos_has_shovel(state, player)],
    ]
