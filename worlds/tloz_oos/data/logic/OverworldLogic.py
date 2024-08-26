from .LogicPredicates import *
from ..EntranceType import OoSEntranceType


def make_holodrum_logic(player: int):
    return [
        ["Menu", "horon village", OoSEntranceType.OneWay, None],

        ["horon village", "enter mayor's house", OoSEntranceType.TwoWay, None],
        ["enter mayor's house", "inside mayor's house", OoSEntranceType.DoorTwoWay, None],
        ["inside mayor's house", "mayor's gift", OoSEntranceType.OneWay, None],
        ["inside mayor's house", "mayor's house secret room", OoSEntranceType.OneWay, lambda state: oos_has_bombs(state, player)],

        ["horon village", "enter vasu", OoSEntranceType.TwoWay, None],
        ["enter vasu", "inside vasu", OoSEntranceType.DoorTwoWay, None],
        ["inside vasu", "vasu's gift", OoSEntranceType.OneWay, None],

        ["horon village", "horon heart piece", OoSEntranceType.OneWay, lambda state: oos_can_use_ember_seeds(state, player, False)],
        ["horon village", "dr. left reward", OoSEntranceType.OneWay, lambda state: oos_can_use_ember_seeds(state, player, True)],

        ["horon village", "enter dr left old man", OoSEntranceType.OneWay, lambda state: oos_can_use_ember_seeds(state, player, False)],
        ["enter dr left old man", "inside dr left old man", OoSEntranceType.DoorTwoWay, None],
        ["inside dr left old man", "old man in horon", OoSEntranceType.OneWay, None],

        ["horon village", "old man trade", OoSEntranceType.OneWay, lambda state: any([
            state.has("Fish", player),
            oos_self_locking_item(state, player, "old man trade", "Fish")
        ])],

        ["horon village", "enter tick tock", OoSEntranceType.TwoWay, None],
        ["enter tick tock", "inside tick tock", OoSEntranceType.DoorTwoWay, None],
        ["inside tick tock", "tick tock trade", OoSEntranceType.OneWay, lambda state: any([
            state.has("Wooden Bird", player),
            oos_self_locking_item(state, player, "tick tock trade", "Wooden Bird")
        ])],

        ["horon village", "maku tree", OoSEntranceType.OneWay, lambda state: oos_has_sword(state, player, False)],
        ["horon village", "horon village SE chest", OoSEntranceType.OneWay, lambda state: all([
            oos_has_bombs(state, player),
            any([
                oos_can_swim(state, player, False),
                oos_season_in_horon_village(state, player, SEASON_WINTER),
                oos_can_jump_2_wide_liquid(state, player)
            ])
        ])],
        ["horon village", "horon village SW chest", OoSEntranceType.OneWay, lambda state: all([
            oos_season_in_horon_village(state, player, SEASON_AUTUMN),
            oos_can_break_mushroom(state, player, True)
        ])],

        ["horon village", "maple trade", OoSEntranceType.OneWay, lambda state: all([
            oos_can_meet_maple(state, player),
            any([
                state.has("Lon Lon Egg", player),
                oos_self_locking_item(state, player, "maple trade", "Lon Lon Egg")
            ])
        ])],

        ["horon village", "enter village portal room", OoSEntranceType.TwoWay, None],
        ["enter village portal room", "inside village portal room", OoSEntranceType.DoorTwoWay, None],
        ["inside village portal room", "horon village portal", OoSEntranceType.OneWay, lambda state: any([
            oos_has_magic_boomerang(state, player),
            oos_can_jump_6_wide_pit(state, player)
        ])],
        ["horon village portal", "inside village portal room", OoSEntranceType.OneWay, lambda state: any([
            oos_can_trigger_lever(state, player),
            oos_can_jump_6_wide_pit(state, player)
        ])],

        ["horon village", "horon village tree", OoSEntranceType.OneWay, lambda state: oos_can_harvest_tree(state, player, True)],

        ["horon village", "enter shop", OoSEntranceType.TwoWay, None],
        ["enter shop", "inside shop", OoSEntranceType.DoorTwoWay, None],
        ["inside shop", "horon shop", OoSEntranceType.OneWay, lambda state: oos_has_rupees(state, player, 150)],
        ["horon village", "enter advance shop", OoSEntranceType.TwoWay, None],
        ["enter advance shop", "inside advance shop", OoSEntranceType.DoorTwoWay, None],
        ["inside advance shop", "advance shop", OoSEntranceType.OneWay, lambda state: oos_has_rupees(state, player, 300)],
        ["horon village", "member's shop", OoSEntranceType.OneWay, lambda state: all([
            state.has("Member's Card", player),
            oos_has_rupees(state, player, 450)
        ])],

        ["horon village", "enter know-it-all birds", OoSEntranceType.TwoWay, None],
        ["enter know-it-all birds", "inside know-it-all birds", OoSEntranceType.DoorTwoWay, None],

        ["horon village", "enter bipin left", OoSEntranceType.TwoWay, None],
        ["enter bipin left", "inside bipin left", OoSEntranceType.DoorTwoWay, None],
        ["horon village", "enter bipin right", OoSEntranceType.TwoWay, None],
        ["enter bipin right", "inside bipin right", OoSEntranceType.DoorTwoWay, None],
        ["inside bipin left", "inside bipin right", OoSEntranceType.TwoWay, None],

        # WESTERN COAST ##############################################################################################

        ["horon village", "black beast's chest", OoSEntranceType.OneWay, lambda state: all([
            all([
                oos_has_slingshot(state, player),
                oos_can_use_ember_seeds(state, player, True),
            ]),
            oos_can_use_mystery_seeds(state, player),
            oos_can_kill_armored_enemy(state, player),
        ])],

        ["horon village", "d0 entrance", OoSEntranceType.TwoWay, None],

        ["western coast after ship", "coast stump", OoSEntranceType.OneWay, lambda state: all([
            oos_has_bombs(state, player),
            any([
                oos_has_feather(state, player),
                oos_option_hard_logic(state, player)
            ])
        ])],

        ["western coast after ship", "old man near western coast house", OoSEntranceType.OneWay, lambda state: \
            oos_can_use_ember_seeds(state, player, False)],

        ["western coast after ship", "graveyard (winter)", OoSEntranceType.OneWay, lambda state: all([
            oos_can_jump_3_wide_pit(state, player),
            oos_season_in_western_coast(state, player, SEASON_WINTER)
        ])],

        ["western coast after ship", "graveyard (autumn)", OoSEntranceType.OneWay, lambda state: all([
            oos_can_jump_3_wide_pit(state, player),
            oos_season_in_western_coast(state, player, SEASON_AUTUMN)
        ])],

        ["western coast after ship", "graveyard (summer or spring)", OoSEntranceType.OneWay, lambda state: any([
            oos_can_jump_3_wide_pit(state, player),
            oos_season_in_western_coast(state, player, SEASON_SUMMER)
        ])],

        ["graveyard (winter)", "d7 entrance", OoSEntranceType.OneWay, lambda state: oos_can_remove_snow(state, player, False)],
        ["graveyard (autumn)", "d7 entrance", OoSEntranceType.OneWay, None],
        ["graveyard (summer or spring)", "d7 entrance", OoSEntranceType.OneWay, None],

        ["d7 entrance", "graveyard (winter)", OoSEntranceType.OneWay, lambda state: \
            oos_get_default_season(state, player, "WESTERN_COAST") == SEASON_WINTER],
        ["d7 entrance", "graveyard (autumn)", OoSEntranceType.OneWay, lambda state: \
            oos_get_default_season(state, player, "WESTERN_COAST") == SEASON_AUTUMN],
        ["d7 entrance", "graveyard (summer or spring)", OoSEntranceType.OneWay, lambda state: \
            oos_get_default_season(state, player, "WESTERN_COAST") in [SEASON_SUMMER, SEASON_SPRING]],

        ["graveyard (autumn)", "graveyard heart piece", OoSEntranceType.OneWay, lambda state: oos_can_break_mushroom(state, player, False)],

        # EASTERN SUBURBS #############################################################################################

        ["horon village", "suburbs", OoSEntranceType.TwoWay, lambda state: oos_can_use_ember_seeds(state, player, False)],

        ["suburbs", "enter guru guru", OoSEntranceType.TwoWay, None],
        ["suburbs", "enter winter guru guru", OoSEntranceType.OneWay, lambda state: oos_season_in_eastern_suburbs(state, player, SEASON_WINTER)],
        ["enter winter guru guru", "suburbs", OoSEntranceType.OneWay, None],
        ["enter winter guru guru", "inside winter guru guru", OoSEntranceType.DoorTwoWay, None],
        ["inside winter guru guru", "windmill heart piece", OoSEntranceType.OneWay, None],
        ["windmill heart piece", "inside guru guru", OoSEntranceType.OneWay, None],
        ["enter guru guru", "inside guru guru", OoSEntranceType.DoorTwoWay, None],
        ["inside guru guru", "top guru guru staircase", OoSEntranceType.TwoWay, None],
        ["top guru guru staircase", "top of guru guru", OoSEntranceType.DoorTwoWay, None],
        ["top of guru guru", "guru-guru trade", OoSEntranceType.OneWay, lambda state: any([
            state.has("Engine Grease", player),
            oos_self_locking_item(state, player, "guru-guru trade", "Engine Grease")
        ])],

        ["suburbs", "enter suburb spring cave", OoSEntranceType.OneWay, lambda state: all([
            oos_has_bracelet(state, player),
            oos_season_in_eastern_suburbs(state, player, SEASON_SPRING)
        ])],
        ["enter suburb spring cave", "suburbs", OoSEntranceType.OneWay, lambda state: oos_has_bracelet(state, player)],
        ["enter suburb spring cave", "inside suburb spring cave", OoSEntranceType.DoorTwoWay, None],
        ["inside suburb spring cave", "eastern suburbs spring cave", OoSEntranceType.OneWay, lambda state: any([
            oos_has_magnet_gloves(state, player),
            oos_can_jump_3_wide_pit(state, player)
        ])],

        ["eastern suburbs portal", "suburbs", OoSEntranceType.OneWay, lambda state: oos_can_break_bush(state, player, False)],
        ["suburbs", "eastern suburbs portal", OoSEntranceType.OneWay, lambda state: oos_can_break_bush(state, player, True)],

        ["suburbs", "suburbs fairy fountain", OoSEntranceType.TwoWay, lambda state: any([
            oos_can_swim(state, player, True),
            oos_can_jump_1_wide_liquid(state, player, True)
        ])],
        ["suburbs", "suburbs fairy fountain (winter)", OoSEntranceType.TwoWay, lambda state: any([
            oos_season_in_eastern_suburbs(state, player, SEASON_WINTER)
        ])],
        ["suburbs fairy fountain (winter)", "suburbs fairy fountain", OoSEntranceType.OneWay, lambda state: \
            oos_can_remove_season(state, player, SEASON_WINTER)],
        ["suburbs fairy fountain", "suburbs fairy fountain (winter)", OoSEntranceType.OneWay, lambda state: \
            oos_has_winter(state, player)],

        ["suburbs fairy fountain", "sunken city", OoSEntranceType.OneWay, lambda state: \
            oos_season_in_eastern_suburbs(state, player, SEASON_SPRING)],
        ["sunken city", "suburbs fairy fountain", OoSEntranceType.OneWay, lambda state: any([
            oos_season_in_eastern_suburbs(state, player, SEASON_SPRING),
            oos_can_warp(state, player)
        ])],

        # WOODS OF WINTER / 2D SECTOR ################################################################################

        ["suburbs fairy fountain (winter)", "moblin road", OoSEntranceType.OneWay, lambda state: None],
        ["moblin road", "suburbs fairy fountain (winter)", OoSEntranceType.OneWay, lambda state: \
            oos_season_in_eastern_suburbs(state, player, SEASON_WINTER)],

        ["sunken city", "moblin road", OoSEntranceType.OneWay, lambda state: all([
            oos_has_flippers(state, player),
            any([
                oos_get_default_season(state, player, "SUNKEN_CITY") != SEASON_WINTER,
                oos_can_remove_season(state, player, SEASON_WINTER)
            ]),
            any([
                oos_can_warp(state, player),
                all([
                    # We need both seasons to be able to climb back up
                    oos_season_in_eastern_suburbs(state, player, SEASON_WINTER),
                    oos_has_spring(state, player)
                ])
            ])
        ])],

        ["moblin road", "woods of winter, 1st cave", OoSEntranceType.OneWay, lambda state: all([
            oos_can_remove_rockslide(state, player, True),
            oos_can_break_bush(state, player, False),
            any([
                oos_get_default_season(state, player, "WOODS_OF_WINTER") != SEASON_WINTER,
                oos_can_remove_season(state, player, SEASON_WINTER)
            ])
        ])],

        ["moblin road", "woods of winter, 2nd cave", OoSEntranceType.OneWay, lambda state: any([
            oos_can_swim(state, player, False),
            oos_can_jump_3_wide_liquid(state, player)
        ])],

        ["moblin road", "holly's house", OoSEntranceType.OneWay, lambda state: \
            oos_season_in_woods_of_winter(state, player, SEASON_WINTER)],

        ["moblin road", "old man near holly's house", OoSEntranceType.OneWay, lambda state: oos_can_use_ember_seeds(state, player, False)],

        ["moblin road", "woods of winter heart piece", OoSEntranceType.OneWay, lambda state: any([
            oos_can_swim(state, player, True),
            oos_has_bracelet(state, player),
            oos_can_jump_1_wide_liquid(state, player, True)
        ])],

        ["suburbs fairy fountain", "central woods of winter", OoSEntranceType.OneWay, lambda state: None],
        ["suburbs fairy fountain (winter)", "central woods of winter", OoSEntranceType.OneWay, lambda state: any([
            oos_can_jump_1_wide_pit(state, player, True),
            oos_can_remove_snow(state, player, True)
        ])],

        ["central woods of winter", "woods of winter tree", OoSEntranceType.OneWay, lambda state: oos_can_harvest_tree(state, player, True)],
        ["central woods of winter", "d2 entrance", OoSEntranceType.TwoWay, lambda state: oos_can_break_bush(state, player, True)],

        ["central woods of winter", "enter peek cave near d2", OoSEntranceType.OneWay, lambda state: any([
            oos_can_jump_1_wide_liquid(state, player, False),
            oos_can_swim(state, player, False),
            oos_get_default_season(state, player, "WOODS_OF_WINTER") == SEASON_AUTUMN
        ])],
        ["enter peek cave near d2", "central woods of winter", OoSEntranceType.OneWay, lambda state: any([
            oos_can_jump_1_wide_liquid(state, player, False),
            oos_can_swim(state, player, False),
            oos_season_in_central_woods_of_winter(state, player, SEASON_AUTUMN)
        ])],
        ["enter peek cave near d2", "inside peek cave near d2", OoSEntranceType.DoorTwoWay, None],

        ["central woods of winter", "enter magnet cave near d2", OoSEntranceType.OneWay, lambda state: all([
            oos_season_in_central_woods_of_winter(state, player, SEASON_AUTUMN),
            oos_can_break_mushroom(state, player, True),
        ])],
        ["enter magnet cave near d2", "inside magnet cave near d2", OoSEntranceType.DoorTwoWay, None],
        ["inside magnet cave near d2", "cave outside D2", OoSEntranceType.OneWay, lambda state: any([
            oos_can_jump_4_wide_pit(state, player),
            oos_has_magnet_gloves(state, player)
        ])],

        ["central woods of winter", "d2 stump", OoSEntranceType.TwoWay, None],

        ["d2 stump", "d2 roof", OoSEntranceType.TwoWay, lambda state: oos_has_bracelet(state, player)],
        ["d2 roof", "d2 alt entrances", OoSEntranceType.TwoWay, lambda state: not oos_option_no_d2_alt_entrance(state, player)],

        # EYEGLASS LAKE SECTOR #########################################################################################

        ["horon village", "eyeglass lake, across bridge", OoSEntranceType.OneWay, lambda state: any([
            oos_can_jump_4_wide_pit(state, player),
            all([
                oos_season_in_eyeglass_lake(state, player, SEASON_AUTUMN),
                oos_has_feather(state, player)
            ])
        ])],

        ["horon village", "d1 stump", OoSEntranceType.TwoWay, lambda state: oos_can_break_bush(state, player, True)],
        ["d1 stump", "north horon", OoSEntranceType.TwoWay, lambda state: oos_has_bracelet(state, player)],
        ["d1 stump", "enter lon lon", OoSEntranceType.TwoWay, None],
        ["enter lon lon", "inside lon lon", OoSEntranceType.DoorTwoWay, None],
        ["inside lon lon", "malon trade", OoSEntranceType.OneWay, lambda state: any([
            state.has("Cuccodex", player),
            oos_self_locking_item(state, player, "malon trade", "Cuccodex")
        ])],
        ["d1 stump", "d1 island", OoSEntranceType.TwoWay, lambda state: oos_can_break_bush(state, player, True)],
        ["d1 stump", "old man near d1", OoSEntranceType.OneWay, lambda state: oos_can_use_ember_seeds(state, player, False)],

        ["d1 island", "d1 entrance", OoSEntranceType.TwoWay, lambda state: state.has("Gnarled Key", player)],
        ["d1 island", "golden beasts old man", OoSEntranceType.OneWay, lambda state: all([
            oos_season_in_eyeglass_lake(state, player, SEASON_SUMMER),
            oos_can_beat_required_golden_beasts(state, player)
        ])],

        ["d1 stump", "eyeglass lake (default)", OoSEntranceType.TwoWay, lambda state: all([
            any([
                oos_season_in_eyeglass_lake(state, player, SEASON_SPRING),
                oos_season_in_eyeglass_lake(state, player, SEASON_AUTUMN),
            ]),
            oos_can_jump_1_wide_pit(state, player, True),
            any([
                oos_can_swim(state, player, False),
                all([
                    # To be able to use Dimitri, we need the bracelet to throw him above the pit
                    oos_option_medium_logic(state, player),
                    oos_can_summon_dimitri(state, player),
                    oos_has_bracelet(state, player)
                ])
            ])
        ])],
        ["d1 stump", "eyeglass lake (dry)", OoSEntranceType.TwoWay, lambda state: all([
            oos_season_in_eyeglass_lake(state, player, SEASON_SUMMER),
            oos_can_jump_1_wide_pit(state, player, True)
        ])],
        ["d1 stump", "eyeglass lake (frozen)", OoSEntranceType.TwoWay, lambda state: all([
            oos_season_in_eyeglass_lake(state, player, SEASON_WINTER),
            oos_can_jump_1_wide_pit(state, player, True)
        ])],

        ["d5 stump", "eyeglass lake (default)", OoSEntranceType.TwoWay, lambda state: all([
            any([
                oos_season_in_eyeglass_lake(state, player, SEASON_SPRING),
                oos_season_in_eyeglass_lake(state, player, SEASON_AUTUMN),
            ]),
            oos_can_swim(state, player, True)
        ])],
        ["d5 stump", "eyeglass lake (dry)", OoSEntranceType.OneWay, lambda state: all([
            oos_season_in_eyeglass_lake(state, player, SEASON_SUMMER),
            oos_can_swim(state, player, False)
        ])],
        ["d5 stump", "eyeglass lake (frozen)", OoSEntranceType.TwoWay,
         lambda state: oos_season_in_eyeglass_lake(state, player, SEASON_WINTER)],

        ["eyeglass lake portal", "eyeglass lake (default)", OoSEntranceType.OneWay, lambda state: all([
            oos_get_default_season(state, player, "EYEGLASS_LAKE") in [SEASON_AUTUMN, SEASON_SPRING],
            oos_can_swim(state, player, False)
        ])],
        ["eyeglass lake (default)", "eyeglass lake portal", OoSEntranceType.OneWay, None],
        ["eyeglass lake portal", "eyeglass lake (frozen)", OoSEntranceType.OneWay, lambda state: all([
            oos_get_default_season(state, player, "EYEGLASS_LAKE") == SEASON_WINTER,
            any([
                oos_can_swim(state, player, False),
                oos_can_jump_5_wide_liquid(state, player)
            ])
        ])],
        ["eyeglass lake (frozen)", "eyeglass lake portal", OoSEntranceType.OneWay, lambda state: any([
            oos_can_swim(state, player, True),
            oos_can_jump_5_wide_liquid(state, player)
        ])],
        ["eyeglass lake portal", "eyeglass lake (dry)", OoSEntranceType.OneWay, lambda state: \
            oos_get_default_season(state, player, "EYEGLASS_LAKE") == SEASON_SUMMER],

        ["eyeglass lake (dry)", "dry eyeglass lake, west cave", OoSEntranceType.OneWay, lambda state: all([
            oos_can_remove_rockslide(state, player, True),
            oos_can_swim(state, player, False)  # chest is surrounded by water
        ])],

        ["d5 stump", "d5 entrance", OoSEntranceType.OneWay, lambda state: all([
            # If we don't have autumn, we need to ensure we were able to reach that node with autumn as default
            # season without changing to another season which we wouldn't be able to revert back.
            # For this reason, "default season is autumn" case is handled through direct routes from the lake portal
            # and from D1 stump.
            oos_has_autumn(state, player),
            oos_can_break_mushroom(state, player, True)
        ])],
        # Direct route #1 to reach D5 entrance taking advantage of autumn as default season
        ["d1 stump", "d5 entrance", OoSEntranceType.OneWay, lambda state: all([
            oos_get_default_season(state, player, "EYEGLASS_LAKE") == SEASON_AUTUMN,
            oos_can_jump_1_wide_pit(state, player, True),
            oos_can_break_mushroom(state, player, True),
            any([
                oos_can_swim(state, player, False),
                all([
                    # To be able to use Dimitri, we need the bracelet to throw him above the pit
                    oos_option_medium_logic(state, player),
                    oos_can_summon_dimitri(state, player),
                    oos_has_bracelet(state, player)
                ])
            ]),
        ])],
        # Direct route #2 to reach D5 entrance taking advantage of autumn as default season
        ["eyeglass lake portal", "d5 entrance", OoSEntranceType.OneWay, lambda state: all([
            oos_get_default_season(state, player, "EYEGLASS_LAKE") == SEASON_AUTUMN,
            oos_can_swim(state, player, False),
            oos_can_break_mushroom(state, player, True)
        ])],

        ["d5 entrance", "d5 stump", OoSEntranceType.OneWay, lambda state: any([
            # Leaving D5 entrance is a risky action since you need quite a few things to be able to get
            # back to that entrance. Ensure player can warp if that's not the case.
            all([
                oos_can_jump_1_wide_pit(state, player, False),
                oos_has_autumn(state, player),
                oos_can_break_mushroom(state, player, True)
            ]),
            oos_can_warp(state, player)
        ])],

        ["d5 stump", "dry eyeglass lake, east cave", OoSEntranceType.OneWay, lambda state: all([
            oos_has_summer(state, player),
            oos_has_bracelet(state, player),
        ])],

        ["d5 entrance", "dry eyeglass lake, east cave", OoSEntranceType.OneWay, lambda state: all([
            oos_get_default_season(state, player, "EYEGLASS_LAKE") == SEASON_SUMMER,
            oos_has_bracelet(state, player),
        ])],

        # NORTH HORON / HOLODRUM PLAIN ###############################################################################

        ["north horon", "north horon tree", OoSEntranceType.OneWay, lambda state: oos_can_harvest_tree(state, player, True)],

        ["north horon", "enter Blaino", OoSEntranceType.TwoWay, None],
        ["enter Blaino", "inside Blaino", OoSEntranceType.DoorTwoWay, None],
        ["inside Blaino", "blaino prize", OoSEntranceType.OneWay, lambda state: oos_can_farm_rupees(state, player)],

        ["north horon", "cave north of D1", OoSEntranceType.OneWay, lambda state: all([
            oos_season_in_holodrum_plain(state, player, SEASON_AUTUMN),
            oos_can_break_mushroom(state, player, True),
            oos_has_flippers(state, player)
        ])],

        ["north horon", "enter old man near blaino", OoSEntranceType.TwoWay, lambda state: all([
            any([
                oos_season_in_holodrum_plain(state, player, SEASON_SUMMER),
                oos_can_summon_ricky(state, player)
            ]),
            oos_can_use_ember_seeds(state, player, False)
        ])],
        ["enter old man near blaino", "inside old man near blaino", OoSEntranceType.DoorTwoWay, None],
        ["inside old man near blaino", "old man near blaino", OoSEntranceType.OneWay, None],

        ["north horon", "underwater item below natzu bridge", OoSEntranceType.OneWay, lambda state: oos_can_swim(state, player, False)],

        ["north horon", "temple remains lower stump", OoSEntranceType.TwoWay, lambda state: oos_can_jump_3_wide_pit(state, player)],

        ["ghastly stump", "enter Mrs Ruul", OoSEntranceType.TwoWay, None],
        ["enter Mrs Ruul", "inside Mrs Ruul", OoSEntranceType.DoorTwoWay, None],
        ["inside Mrs Ruul", "mrs. ruul trade", OoSEntranceType.OneWay, lambda state: any([
            state.has("Ghastly Doll", player),
            oos_self_locking_item(state, player, "mrs. ruul trade", "Ghastly Doll")
        ])],
        ["ghastly stump", "old man near mrs. ruul", OoSEntranceType.OneWay, lambda state: oos_can_use_ember_seeds(state, player, False)],

        ["north horon", "ghastly stump", OoSEntranceType.TwoWay, lambda state: any([
            oos_can_jump_1_wide_pit(state, player, True),
            oos_season_in_holodrum_plain(state, player, SEASON_WINTER)
        ])],

        ["spool swamp north", "ghastly stump", OoSEntranceType.OneWay, None],
        ["ghastly stump", "spool swamp north", OoSEntranceType.OneWay, lambda state: all([
            any([
                oos_season_in_holodrum_plain(state, player, SEASON_SUMMER),
                oos_can_jump_4_wide_pit(state, player),
                oos_can_summon_ricky(state, player),
                oos_can_summon_moosh(state, player)
            ])
        ])],

        ["ghastly stump", "spool swamp south", OoSEntranceType.TwoWay, lambda state: all([
            oos_can_swim(state, player, True),
            oos_can_break_bush(state, player, True),
        ])],

        # Goron Mountain <-> North Horon <-> D1 island <-> Spool swamp waterway
        ["spool swamp south", "d1 island", OoSEntranceType.TwoWay, lambda state: oos_can_swim(state, player, True)],
        ["d1 island", "north horon", OoSEntranceType.TwoWay, lambda state: oos_can_swim(state, player, True)],
        ["north horon", "goron mountain entrance", OoSEntranceType.TwoWay, lambda state: oos_can_swim(state, player, True)],
        ["goron mountain entrance", "natzu region, across water", OoSEntranceType.TwoWay, lambda state: oos_can_swim(state, player, True)],
        ["ghastly stump", "d1 island", OoSEntranceType.TwoWay, lambda state: all([
            oos_can_break_bush(state, player, True),
            oos_can_swim(state, player, True)
        ])],

        ["d1 island", "enter treehouse", OoSEntranceType.TwoWay, lambda state: oos_can_swim(state, player, True)],
        ["enter treehouse", "inside treehouse", OoSEntranceType.DoorTwoWay, None],
        ["inside treehouse", "old man in treehouse", OoSEntranceType.OneWay, lambda state: all([
            oos_can_swim(state, player, True),
            oos_has_essences_for_treehouse(state, player)
        ])],
        ["d1 island", "cave south of mrs. ruul", OoSEntranceType.OneWay, lambda state: oos_can_swim(state, player, False)],

        # SPOOL SWAMP #############################################################################################

        ["spool swamp north", "spool swamp tree", OoSEntranceType.OneWay, lambda state: oos_can_harvest_tree(state, player, True)],

        ["spool swamp north", "enter floodgate house", OoSEntranceType.TwoWay, None],
        ["enter floodgate house", "inside floodgate house", OoSEntranceType.DoorTwoWay, None],
        ["inside floodgate house", "floodgate keeper's house", OoSEntranceType.OneWay, lambda state: any([
            oos_can_trigger_lever(state, player),
            all([
                oos_option_hard_logic(state, player),
                oos_has_bracelet(state, player)
            ])
        ])],

        ["spool swamp north", "spool swamp digging spot", OoSEntranceType.OneWay, lambda state: all([
            oos_season_in_spool_swamp(state, player, SEASON_SUMMER),
            oos_has_shovel(state, player)
        ])],

        ["spool swamp north", "enter floodgate right", OoSEntranceType.TwoWay, lambda state: any([
            state.has("_flipped_floodgate_lever", player),
            oos_can_swim(state, player, False)
        ])],
        ["enter floodgate right", "inside floodgate right", OoSEntranceType.DoorComplexTwoWay, lambda state: state.has("_flipped_floodgate_lever", player)],
        ["inside floodgate right", "enter floodgate right", OoSEntranceType.DoorComplexTwoWay, None],
        ["inside floodgate right", "inside floodgate left", OoSEntranceType.OneWay, lambda state: all([
            any([
                oos_can_use_pegasus_seeds(state, player),
                oos_has_flippers(state, player),
                oos_has_feather(state, player)
            ]),
            oos_has_bracelet(state, player)
        ])],
        ["inside floodgate left", "inside floodgate right", OoSEntranceType.OneWay, lambda state: all([
            any([
                oos_can_jump_3_wide_liquid(state, player),
                oos_has_flippers(state, player),
                oos_has_bracelet(state, player)
            ]),
        ])],
        ["inside floodgate left", "enter floodgate left", OoSEntranceType.DoorTwoWay, None],
        ["enter floodgate left", "floodgate keyhole", OoSEntranceType.OneWay, None],
        ["floodgate keyhole", "spool swamp north", OoSEntranceType.OneWay, lambda state: oos_can_swim(state, player, True)],
        ["floodgate keyhole", "spool stump", OoSEntranceType.OneWay, lambda state: state.has("Floodgate Key", player)],

        ["spool stump", "d3 entrance", OoSEntranceType.OneWay, lambda state: oos_season_in_spool_swamp(state, player, SEASON_SUMMER)],
        ["d3 entrance", "spool stump", OoSEntranceType.OneWay, lambda state: any([
            # Jumping down D3 entrance without having a way to put summer is a risky situation, so expect player
            # to have a way to warp out
            oos_season_in_spool_swamp(state, player, SEASON_SUMMER),
            oos_can_warp(state, player)
        ])],

        ["spool stump", "spool swamp middle", OoSEntranceType.OneWay, lambda state: any([
            oos_get_default_season(state, player, "SPOOL_SWAMP") != 'spring',
            oos_can_remove_season(state, player, 'spring'),
            oos_has_flippers(state, player),
            oos_can_summon_dimitri(state, player)
        ])],

        ["spool swamp middle", "spool swamp south near gasha spot", OoSEntranceType.OneWay, lambda state: oos_can_summon_ricky(state, player)],
        ["spool swamp south near gasha spot", "spool swamp middle", OoSEntranceType.OneWay, lambda state: any([
            oos_has_feather(state, player),
            oos_can_break_bush(state, player, True)
        ])],

        ["spool swamp south near gasha spot", "spool swamp portal", OoSEntranceType.TwoWay, lambda state: oos_has_bracelet(state, player)],

        ["spool swamp middle", "spool swamp south", OoSEntranceType.TwoWay, lambda state: any([
            oos_can_jump_2_wide_pit(state, player),
            oos_can_summon_moosh(state, player),
            oos_can_summon_dimitri(state, player),
            oos_has_flippers(state, player)
        ])],

        ["spool swamp south", "spool swamp south (winter)", OoSEntranceType.OneWay, lambda state: \
            oos_season_in_spool_swamp(state, player, SEASON_WINTER)],
        ["spool swamp south", "spool swamp south (spring)", OoSEntranceType.OneWay, lambda state: \
            oos_season_in_spool_swamp(state, player, SEASON_SPRING)],
        ["spool swamp south", "spool swamp south (summer)", OoSEntranceType.OneWay, lambda state: \
            oos_season_in_spool_swamp(state, player, SEASON_SUMMER)],
        ["spool swamp south", "spool swamp south (autumn)", OoSEntranceType.OneWay, lambda state: \
            oos_season_in_spool_swamp(state, player, SEASON_AUTUMN)],
        ["spool swamp south (winter)", "spool swamp south", OoSEntranceType.OneWay, None],
        ["spool swamp south (spring)", "spool swamp south", OoSEntranceType.OneWay, None],
        ["spool swamp south (summer)", "spool swamp south", OoSEntranceType.OneWay, None],
        ["spool swamp south (autumn)", "spool swamp south", OoSEntranceType.OneWay, None],

        ["spool swamp south (spring)", "spool swamp south near gasha spot", OoSEntranceType.OneWay, lambda state: \
            oos_can_break_flowers(state, player, True)
         ],
        ["spool swamp south (winter)", "spool swamp south near gasha spot", OoSEntranceType.OneWay, lambda state: \
            oos_can_remove_snow(state, player, True)
         ],
        ["spool swamp south (summer)", "spool swamp south near gasha spot", OoSEntranceType.OneWay, None],
        ["spool swamp south (autumn)", "spool swamp south near gasha spot", OoSEntranceType.OneWay, None],

        ["spool swamp south near gasha spot", "spool swamp south (spring)", OoSEntranceType.OneWay, lambda state: all([
            oos_season_in_spool_swamp(state, player, SEASON_SPRING),
            oos_can_break_flowers(state, player, True)
        ])],
        ["spool swamp south near gasha spot", "spool swamp south (winter)", OoSEntranceType.OneWay, lambda state: all([
            oos_season_in_spool_swamp(state, player, SEASON_WINTER),
            oos_can_remove_snow(state, player, True)
        ])],
        ["spool swamp south near gasha spot", "spool swamp south (summer)", OoSEntranceType.OneWay, lambda state: \
            oos_season_in_spool_swamp(state, player, SEASON_SUMMER)],
        ["spool swamp south near gasha spot", "spool swamp south (autumn)", OoSEntranceType.OneWay, lambda state: \
            oos_season_in_spool_swamp(state, player, SEASON_AUTUMN)],

        ["spool swamp south (winter)", "spool swamp cave", OoSEntranceType.OneWay, lambda state: all([
            oos_can_remove_snow(state, player, True),
            oos_can_remove_rockslide(state, player, True)
        ])],

        ["spool swamp south (spring)", "spool swamp heart piece", OoSEntranceType.OneWay, lambda state: \
            oos_can_swim(state, player, True)],

        # NATZU REGION #############################################################################################

        ["north horon", "natzu west", OoSEntranceType.TwoWay, lambda state: any([
            oos_can_jump_1_wide_pit(state, player, True),
            oos_can_swim(state, player, True)
        ])],

        ["natzu west", "natzu west (ricky)", OoSEntranceType.TwoWay, lambda state: oos_is_companion_ricky(state, player)],
        ["natzu west", "natzu west (moosh)", OoSEntranceType.TwoWay, lambda state: oos_is_companion_moosh(state, player)],
        ["natzu west", "natzu west (dimitri)", OoSEntranceType.TwoWay, lambda state: oos_is_companion_dimitri(state, player)],

        ["natzu east (ricky)", "sunken city", OoSEntranceType.TwoWay, lambda state: oos_is_companion_ricky(state, player)],
        ["natzu east (moosh)", "sunken city", OoSEntranceType.TwoWay, lambda state: all([
            oos_is_companion_moosh(state, player),
            any([
                oos_can_summon_moosh(state, player),
                oos_can_jump_3_wide_liquid(state, player)  # Not a liquid, but it's a diagonal jump so that's the same
            ])
        ])],
        ["natzu east (dimitri)", "sunken city", OoSEntranceType.TwoWay, lambda state: all([
            oos_is_companion_dimitri(state, player),
            oos_can_jump_1_wide_pit(state, player, False)
        ])],
        ["natzu east (dimitri)", "natzu region, across water", OoSEntranceType.OneWay, lambda state: \
            oos_can_jump_5_wide_liquid(state, player)],

        ["natzu west (ricky)", "natzu east (ricky)", OoSEntranceType.TwoWay, lambda state: oos_can_summon_ricky(state, player)],
        ["natzu west (moosh)", "natzu east (moosh)", OoSEntranceType.TwoWay, lambda state: any([
            oos_can_summon_moosh(state, player),
            all([
                oos_option_medium_logic(state, player),
                oos_can_break_bush(state, player, True),
                oos_can_jump_3_wide_pit(state, player)
            ])
        ])],
        ["natzu west (dimitri)", "natzu east (dimitri)", OoSEntranceType.TwoWay, lambda state: oos_can_swim(state, player, True)],

        ["natzu east (ricky)", "moblin keep bridge", OoSEntranceType.OneWay, None],
        ["natzu east (moosh)", "moblin keep bridge", OoSEntranceType.OneWay, lambda state: any([
            oos_can_summon_moosh(state, player),
            all([
                oos_can_break_bush(state, player),
                oos_can_jump_3_wide_pit(state, player)
            ])
        ])],
        ["natzu east (dimitri)", "moblin keep bridge", OoSEntranceType.OneWay, lambda state: any([
            oos_can_summon_dimitri(state, player),
            all([
                oos_option_hard_logic(state, player),
                state.has("Swimmer's Ring", player)
            ])
        ])],
        ["moblin keep bridge", "moblin keep", OoSEntranceType.OneWay, lambda state: any([
            oos_has_flippers(state, player),
            oos_can_jump_4_wide_liquid(state, player)
        ])],
        ["moblin keep", "moblin keep chest", OoSEntranceType.OneWay, lambda state: any([
            oos_has_bracelet(state, player)
        ])],
        ["moblin keep", "sunken city", OoSEntranceType.OneWay, lambda state: oos_can_warp(state, player)],

        ["natzu east (ricky)", "natzu river bank", OoSEntranceType.TwoWay, lambda state: oos_can_summon_ricky(state, player)],
        ["natzu east (moosh)", "natzu river bank", OoSEntranceType.TwoWay, lambda state: oos_is_companion_moosh(state, player)],
        ["natzu east (dimitri)", "natzu river bank", OoSEntranceType.TwoWay, lambda state: oos_is_companion_dimitri(state, player)],
        ["natzu river bank", "goron mountain entrance", OoSEntranceType.TwoWay, lambda state: oos_can_swim(state, player, True)],

        # SUNKEN CITY ############################################################################################

        ["sunken city", "sunken city tree", OoSEntranceType.OneWay, lambda state: all([
            any([
                oos_has_feather(state, player),
                oos_has_flippers(state, player),
                oos_can_summon_dimitri(state, player),
                oos_get_default_season(state, player, "SUNKEN_CITY") == SEASON_WINTER
            ]),
            oos_can_harvest_tree(state, player, True)
        ])],

        ["sunken city", "sunken city dimitri", OoSEntranceType.OneWay, lambda state: any([
            oos_can_summon_dimitri(state, player),
            all([
                oos_has_bombs(state, player),
                any([
                    oos_has_feather(state, player),
                    oos_has_flippers(state, player),
                    oos_get_default_season(state, player, "SUNKEN_CITY") == SEASON_WINTER
                ])
            ])
        ])],

        ["sunken city", "enter ingo", OoSEntranceType.TwoWay, None],
        ["enter ingo", "inside ingo", OoSEntranceType.DoorTwoWay, None],
        ["inside ingo", "ingo trade", OoSEntranceType.OneWay, lambda state: any([
            state.has("Goron Vase", player),
            oos_self_locking_item(state, player, "ingo trade", "Goron Vase")
        ])],
        ["sunken city", "enter syrup", OoSEntranceType.OneWay, lambda state: all([
            any([
                oos_get_default_season(state, player, "SUNKEN_CITY") == SEASON_WINTER,
                all([
                    oos_has_winter(state, player),
                    any([
                        oos_can_swim(state, player, True),
                        state.has("_saved_dimitri_in_sunken_city", player)
                    ])
                ])
            ]),
        ])],
        ["enter syrup", "inside syrup", OoSEntranceType.DoorTwoWay, None],
        ["inside syrup", "syrup trade", OoSEntranceType.OneWay, lambda state: state.has("Mushroom", player)],
        ["syrup trade", "syrup shop", OoSEntranceType.OneWay, lambda state: oos_has_rupees(state, player, 600)],

        # Use Dimitri to get the tree seeds, using dimitri to get seeds being medium difficulty
        ["sunken city dimitri", "sunken city tree", OoSEntranceType.OneWay, lambda state: all([
            oos_option_medium_logic(state, player),
            oos_can_use_seeds(state, player)
        ])],

        ["sunken city dimitri", "master diver's challenge", OoSEntranceType.OneWay, lambda state: all([
            oos_has_sword(state, player, False),
            any([
                oos_has_feather(state, player),
                oos_has_flippers(state, player)
            ])
        ])],

        ["sunken city dimitri", "master diver's reward", OoSEntranceType.OneWay, lambda state: any([
            state.has("Master's Plaque", player),
            oos_self_locking_item(state, player, "master diver's reward", "Master's Plaque")
        ])],
        ["sunken city dimitri", "chest in master diver's cave", OoSEntranceType.OneWay, None],

        ["sunken city", "enter sunken city, summer cave", OoSEntranceType.TwoWay, lambda state: all([
            oos_season_in_sunken_city(state, player, SEASON_SUMMER),
            oos_has_flippers(state, player),
        ])],
        ["enter sunken city, summer cave", "inside sunken city, summer cave", OoSEntranceType.DoorTwoWay, None],
        ["inside sunken city, summer cave", "sunken city, summer cave", OoSEntranceType.OneWay, lambda state: all([
            any([
                oos_has_flippers(state, player),
                oos_can_jump_1_wide_liquid(state, player, False)
            ]),
            oos_can_break_bush(state, player, False)
        ])],

        ["mount cucco", "sunken city", OoSEntranceType.OneWay, lambda state: oos_has_flippers(state, player)],
        ["sunken city", "mount cucco", OoSEntranceType.OneWay, lambda state: all([
            oos_has_flippers(state, player),
            oos_season_in_sunken_city(state, player, SEASON_SUMMER)
        ])],
        ["sunken city gasha spot", "enter flooded house", OoSEntranceType.TwoWay, lambda state: oos_can_swim(state, player, False)],
        ["enter flooded house", "sunken city", OoSEntranceType.OneWay, lambda state: oos_can_swim(state, player, False)],
        ["enter flooded house", "inside flooded house", OoSEntranceType.DoorTwoWay, None],
        ["sunken city", "enter treasure hunter", OoSEntranceType.TwoWay, None],
        ["enter treasure hunter", "inside treasure hunter", OoSEntranceType.DoorTwoWay, None],
        ["sunken city", "enter bomb house", OoSEntranceType.TwoWay, None],
        ["enter bomb house", "inside bomb house", OoSEntranceType.DoorTwoWay, None],

        # MT. CUCCO / GORON MOUNTAINS ##############################################################################

        ["mount cucco", "mt. cucco portal", OoSEntranceType.TwoWay, None],

        ["mount cucco", "rightmost rooster ledge", OoSEntranceType.OneWay, lambda state: all([
            any([  # to reach the rooster
                all([
                    oos_season_in_mt_cucco(state, player, SEASON_SPRING),
                    any([
                        oos_can_break_flowers(state, player, False),
                        # Moosh can break flowers one way, but it won't be of any help when coming back so we need
                        # to be able to warp out
                        state.has("Spring Banana", player) and oos_can_warp(state, player),
                    ])
                ]),
                oos_option_hard_logic(state, player) and oos_can_warp(state, player),
            ]),
            oos_has_bracelet(state, player),  # to grab the rooster
        ])],

        ["rightmost rooster ledge", "mt. cucco, platform cave", OoSEntranceType.OneWay, None],
        ["rightmost rooster ledge", "spring banana tree", OoSEntranceType.OneWay, lambda state: all([
            oos_has_feather(state, player),
            oos_season_in_mt_cucco(state, player, SEASON_SPRING),
            any([  # can harvest tree
                oos_has_sword(state, player),
                oos_has_fools_ore(state, player)
            ])
        ])],

        ["mount cucco", "mt. cucco, talon's cave entrance", OoSEntranceType.OneWay, lambda state: \
            oos_season_in_mt_cucco(state, player, SEASON_SPRING)],

        ["mt. cucco, talon's cave entrance", "talon trade", OoSEntranceType.OneWay, lambda state: state.has("Megaphone", player)],
        ["talon trade", "mt. cucco, talon's cave", OoSEntranceType.OneWay, None],

        ["mt. cucco, talon's cave entrance", "mt. cucco heart piece", OoSEntranceType.OneWay, None],

        ["mt. cucco, talon's cave entrance", "diving spot outside D4", OoSEntranceType.OneWay, lambda state: oos_has_flippers(state, player)],

        ["mt. cucco, talon's cave entrance", "dragon keyhole", OoSEntranceType.OneWay, lambda state: all([
            oos_has_winter(state, player),  # to reach cave
            oos_has_feather(state, player),  # to jump in cave
            oos_has_bracelet(state, player)  # to grab the rooster
        ])],

        ["dragon keyhole", "d4 entrance", OoSEntranceType.OneWay, lambda state: all([
            state.has("Dragon Key", player),
            oos_has_summer(state, player)
        ])],
        ["d4 entrance", "mt. cucco, talon's cave entrance", OoSEntranceType.OneWay, lambda state: oos_can_warp(state, player)],

        ["mount cucco", "goron mountain, across pits", OoSEntranceType.OneWay, lambda state: any([
            state.has("Spring Banana", player),
            oos_can_jump_4_wide_pit(state, player),
        ])],

        ["mount cucco", "goron blocked cave entrance", OoSEntranceType.OneWay, lambda state: any([
            oos_can_remove_snow(state, player, False),
            state.has("Spring Banana", player)
        ])],
        ["goron blocked cave entrance", "mount cucco", OoSEntranceType.OneWay, lambda state: \
            oos_can_remove_snow(state, player, False)],

        ["goron blocked cave entrance", "goron mountain", OoSEntranceType.TwoWay, lambda state: oos_has_bracelet(state, player)],

        ["goron blocked cave entrance", "goron's gift", OoSEntranceType.OneWay, lambda state: oos_has_bombs(state, player)],

        ["goron mountain", "biggoron trade", OoSEntranceType.OneWay, lambda state: all([
            oos_can_jump_1_wide_liquid(state, player, False),
            any([
                state.has("Lava Soup", player),
                oos_self_locking_item(state, player, "biggoron trade", "Lava Soup")
            ])
        ])],

        ["goron mountain", "chest in goron mountain", OoSEntranceType.OneWay, lambda state: all([
            oos_has_bombs(state, player),
            oos_can_jump_3_wide_liquid(state, player)
        ])],
        ["goron mountain", "old man in goron mountain", OoSEntranceType.OneWay, lambda state: \
            oos_can_use_ember_seeds(state, player, False)],

        ["goron mountain entrance", "goron mountain", OoSEntranceType.TwoWay, lambda state: any([
            oos_has_flippers(state, player),
            oos_can_jump_4_wide_liquid(state, player),
        ])],

        ["goron mountain entrance", "temple remains lower stump", OoSEntranceType.TwoWay, lambda state: \
            oos_can_jump_3_wide_pit(state, player)],

        # TARM RUINS ###############################################################################################

        ["spool swamp north", "tarm ruins", OoSEntranceType.OneWay, lambda state: oos_has_required_jewels(state, player)],

        ["tarm ruins", "lost woods stump", OoSEntranceType.OneWay, lambda state: all([
            oos_has_summer(state, player),
            oos_has_winter(state, player),
            oos_has_autumn(state, player),
            oos_can_break_mushroom(state, player, False)
        ])],

        ["lost woods stump", "enter lost woods deku", OoSEntranceType.OneWay, None],
        ["enter lost woods deku", "inside lost woods deku", OoSEntranceType.DoorTwoWay, None],
        ["inside lost woods deku", "lost woods deku", OoSEntranceType.OneWay, lambda state: oos_has_shield(state, player)],

        ["lost woods stump", "enter phonograph deku", OoSEntranceType.OneWay, lambda state: oos_can_use_ember_seeds(state, player, False)],
        ["enter phonograph deku", "inside phonograph deku", OoSEntranceType.DoorTwoWay, None],
        ["inside phonograph deku", "phonograph deku", OoSEntranceType.OneWay, lambda state: state.has("Phonograph", player)],

        ["lost woods stump", "lost woods", OoSEntranceType.OneWay, lambda state: oos_can_reach_lost_woods_pedestal(state, player)],
        ["lost woods stump", "d6 sector", OoSEntranceType.OneWay, lambda state: oos_can_complete_lost_woods_main_sequence(state, player)],

        ["d6 sector", "tarm ruins tree", OoSEntranceType.OneWay, lambda state: oos_can_harvest_tree(state, player, False)],
        ["d6 sector", "enter tarm ruins, under tree", OoSEntranceType.OneWay, lambda state: all([
            oos_season_in_tarm_ruins(state, player, SEASON_AUTUMN),
            oos_can_break_mushroom(state, player, False),
            oos_can_use_ember_seeds(state, player, False)
        ])],
        ["enter tarm ruins, under tree", "inside tarm ruins, under tree", OoSEntranceType.DoorTwoWay, None],
        ["inside tarm ruins, under tree", "tarm ruins, under tree", OoSEntranceType.OneWay, None],

        ["d6 sector", "d6 entrance", OoSEntranceType.OneWay, lambda state: all([
            oos_season_in_tarm_ruins(state, player, SEASON_WINTER),
            any([
                oos_has_shovel(state, player),
                oos_can_use_ember_seeds(state, player, False)
            ]),
            oos_season_in_tarm_ruins(state, player, SEASON_SPRING),
            oos_can_break_flowers(state, player, False)
        ])],
        ["d6 sector", "old man near d6", OoSEntranceType.OneWay, lambda state: all([
            oos_season_in_tarm_ruins(state, player, SEASON_WINTER),
            oos_season_in_tarm_ruins(state, player, SEASON_SPRING),
            oos_can_break_flowers(state, player, False),
            oos_can_use_ember_seeds(state, player, False)
        ])],
        # When coming from D6 entrance, the pillar needs to be broken during spring to be able to go backwards
        ["d6 entrance", "d6 sector", OoSEntranceType.OneWay, lambda state:
        oos_get_default_season(state, player, "TARM_RUINS") == SEASON_SPRING],

        # SAMASA DESERT ######################################################################################

        ["suburbs", "samasa desert", OoSEntranceType.OneWay, lambda state: state.has("_met_pirates", player)],
        ["samasa desert", "samasa desert pit", OoSEntranceType.OneWay, lambda state: oos_has_bracelet(state, player)],
        ["samasa desert", "samasa desert chest", OoSEntranceType.OneWay, lambda state: oos_has_flippers(state, player)],

        # TEMPLE REMAINS ####################################################################################

        ["temple remains lower stump", "temple remains upper stump", OoSEntranceType.OneWay, lambda state: any([
            all([  # Winter rule
                oos_season_in_temple_remains(state, player, SEASON_WINTER),
                oos_can_remove_snow(state, player, False),
                oos_can_break_bush(state, player, False),
                oos_can_jump_6_wide_pit(state, player)
            ]),
            all([  # Summer rule
                oos_season_in_temple_remains(state, player, SEASON_SUMMER),
                oos_can_break_bush(state, player, False),
                oos_can_jump_6_wide_pit(state, player)
            ]),
            all([  # Spring rule
                oos_season_in_temple_remains(state, player, SEASON_SPRING),
                oos_can_break_flowers(state, player, False),
                oos_can_break_bush(state, player, False),
                oos_can_jump_6_wide_pit(state, player)
            ]),
            all([  # Autumn rule
                oos_season_in_temple_remains(state, player, SEASON_AUTUMN),
                oos_can_break_bush(state, player)
            ])
        ])],
        ["temple remains upper stump", "temple remains lower stump", OoSEntranceType.OneWay, lambda state: any([
            # Winter rule
            oos_season_in_temple_remains(state, player, SEASON_WINTER),
            all([  # Summer rule
                oos_season_in_temple_remains(state, player, SEASON_SUMMER),
                oos_can_break_bush(state, player, False),
                oos_can_jump_6_wide_pit(state, player)
            ]),
            all([  # Spring rule
                oos_season_in_temple_remains(state, player, SEASON_SPRING),
                oos_can_break_flowers(state, player, False),
                oos_can_break_bush(state, player, False),
                oos_can_jump_6_wide_pit(state, player)
            ]),
            all([  # Autumn rule
                oos_season_in_temple_remains(state, player, SEASON_AUTUMN),
                oos_can_break_bush(state, player)
            ])
        ])],

        ["temple remains upper stump", "temple remains lower portal access", OoSEntranceType.OneWay, lambda state: all([
            oos_season_in_temple_remains(state, player, SEASON_WINTER),
            oos_can_jump_1_wide_pit(state, player, False)
        ])],

        ["temple remains lower portal access", "temple remains upper stump", OoSEntranceType.OneWay, lambda state: any([
            # Portal can be escaped only if default season is winter or if volcano erupted
            all([
                oos_get_default_season(state, player, "TEMPLE_REMAINS") == SEASON_WINTER,
                oos_can_jump_1_wide_pit(state, player, False)
            ]),
            all([
                state.has("_triggered_volcano", player),
                oos_can_jump_2_wide_liquid(state, player)
            ]),
        ])],

        ["temple remains lower portal access", "temple remains lower portal", OoSEntranceType.TwoWay, None],

        ["temple remains lower portal", "temple remains lower stump", OoSEntranceType.OneWay, lambda state: \
            # There is an added ledge in rando that enables jumping from the portal down to the stump, whatever
        # the season is, but it is a risky action so we ask for the player to be able to warp back
        oos_can_warp(state, player)],

        ["temple remains lower stump", "temple remains heart piece", OoSEntranceType.OneWay, lambda state: all([
            state.has("_triggered_volcano", player),
            oos_can_jump_2_wide_liquid(state, player),
            oos_can_remove_rockslide(state, player, False),
        ])],

        ["temple remains lower stump", "enter d8 fairy room", OoSEntranceType.OneWay, lambda state: all([
            state.has("_triggered_volcano", player),
            oos_season_in_temple_remains(state, player, SEASON_SUMMER),
            oos_can_jump_2_wide_liquid(state, player),
            any([
                oos_has_magnet_gloves(state, player),
                oos_can_jump_6_wide_pit(state, player)
            ])
        ])],
        ["enter d8 fairy room", "inside d8 fairy room", OoSEntranceType.DoorTwoWay, None],
        ["inside d8 fairy room", "temple remains upper portal", OoSEntranceType.TwoWay, None],
        ["enter d8 fairy room", "temple remains lower stump", OoSEntranceType.OneWay, lambda state: all([
            state.has("_triggered_volcano", player),
            oos_can_jump_1_wide_liquid(state, player, False)
        ])],

        ["enter d8 fairy room", "temple remains upper stump", OoSEntranceType.OneWay, lambda state: \
            oos_can_jump_1_wide_pit(state, player, False)],

        ["enter d8 fairy room", "temple remains lower portal access", OoSEntranceType.OneWay, lambda state: \
            oos_get_default_season(state, player, "TEMPLE_REMAINS") == SEASON_WINTER],

        # ONOX CASTLE #############################################################################################

        ["maku tree", "maku seed", OoSEntranceType.OneWay, lambda state: oos_has_essences_for_maku_seed(state, player)],
        ["maku tree", "maku tree, 3 essences", OoSEntranceType.OneWay, lambda state: oos_has_essences(state, player, 3)],
        ["maku tree", "maku tree, 5 essences", OoSEntranceType.OneWay, lambda state: oos_has_essences(state, player, 5)],
        ["maku tree", "maku tree, 7 essences", OoSEntranceType.OneWay, lambda state: oos_has_essences(state, player, 7)],

        ["north horon", "d9 entrance", OoSEntranceType.OneWay, lambda state: state.has("Maku Seed", player)],
        ["d9 entrance", "onox beaten", OoSEntranceType.OneWay, lambda state: all([
            oos_can_kill_armored_enemy(state, player),
            oos_has_bombs(state, player),
            oos_has_sword(state, player, False),
            oos_has_feather(state, player),
            any([
                oos_option_hard_logic(state, player),
                oos_has_rod(state, player)
            ])
        ])],

        ["onox beaten", "ganon beaten", OoSEntranceType.OneWay, lambda state: all([
            oos_has_sword(state, player, False),
            oos_has_slingshot(state, player),
            oos_can_use_ember_seeds(state, player, True),
        ])],

        # GOLDEN BEASTS #############################################################################################

        ["d0 entrance", "golden darknut", OoSEntranceType.OneWay, lambda state: all([
            oos_season_in_western_coast(state, player, SEASON_SPRING),
            any([
                oos_has_sword(state, player),
                oos_has_fools_ore(state, player)
            ])
        ])],
        ["tarm ruins", "golden lynel", OoSEntranceType.OneWay, lambda state: all([
            oos_season_in_lost_woods(state, player, SEASON_SUMMER),
            oos_season_in_lost_woods(state, player, SEASON_WINTER),
            any([
                oos_has_sword(state, player),
                oos_has_fools_ore(state, player)
            ])
        ])],
        ["d2 entrance", "golden moblin", OoSEntranceType.OneWay, lambda state: all([
            oos_season_in_central_woods_of_winter(state, player, SEASON_AUTUMN),
            any([
                oos_has_sword(state, player),
                oos_has_fools_ore(state, player),
                # Moblin has the interesting property of being one-shottable using an ember seed
                all([
                    oos_option_medium_logic(state, player),
                    oos_can_use_ember_seeds(state, player, False)
                ])
            ])
        ])],
        ["spool swamp south (summer)", "golden octorok", OoSEntranceType.OneWay, lambda state: any([
            oos_has_sword(state, player),
            oos_has_fools_ore(state, player)
        ])],

        # GASHA TREES #############################################################################################

        ["horon village", "horon gasha spot", OoSEntranceType.OneWay, None],
        ["horon village", "impa gasha spot", OoSEntranceType.OneWay, lambda state: oos_can_break_bush(state, player, True)],
        ["suburbs", "suburbs gasha spot", OoSEntranceType.OneWay, lambda state: oos_can_break_bush(state, player, True)],
        ["ghastly stump", "holodrum plain gasha spot", OoSEntranceType.OneWay, lambda state: all([
            oos_can_break_bush(state, player, True),
            oos_has_shovel(state, player),
        ])],
        ["d1 island", "holodrum plain island gasha spot", OoSEntranceType.OneWay, lambda state: all([
            oos_can_swim(state, player, True),
            any([
                oos_can_break_bush(state, player, False),
                oos_can_summon_dimitri(state, player),  # Only Dimitri can be brought here
            ]),
        ])],
        ["floodgate keyhole", "spool swamp north gasha spot", OoSEntranceType.OneWay, lambda state: oos_has_bracelet(state, player)],
        ["spool swamp south near gasha spot", "spool swamp south gasha spot", OoSEntranceType.OneWay, lambda state: oos_has_bracelet(state, player)],
        ["sunken city", "sunken city gasha spot", OoSEntranceType.OneWay, lambda state: all([
            oos_season_in_sunken_city(state, player, SEASON_SUMMER),
            oos_can_swim(state, player, False),
            oos_can_break_bush(state, player, False),
        ])],
        ["sunken city dimitri", "sunken city gasha spot", OoSEntranceType.OneWay, None],
        ["goron mountain entrance", "goron mountain left gasha spot", OoSEntranceType.OneWay, lambda state: oos_has_shovel(state, player)],
        ["goron mountain entrance", "goron mountain right gasha spot", OoSEntranceType.OneWay, lambda state: oos_has_bracelet(state, player)],
        ["d5 stump", "eyeglass lake gasha spot", OoSEntranceType.OneWay, lambda state: all([
            oos_has_shovel(state, player),
            oos_can_break_bush(state, player),
        ])],
        ["mount cucco", "mt cucco gasha spot", OoSEntranceType.OneWay, lambda state: all([
            oos_season_in_mt_cucco(state, player, SEASON_AUTUMN),
            oos_can_break_mushroom(state, player, False),
        ])],
        ["d6 sector", "tarm ruins gasha spot", OoSEntranceType.OneWay, lambda state: oos_has_shovel(state, player)],
        ["samasa desert", "samasa desert gasha spot", OoSEntranceType.OneWay, None],
        ["western coast after ship", "western coast gasha spot", OoSEntranceType.OneWay, None],
        ["north horon", "onox gasha spot", OoSEntranceType.OneWay, lambda state: oos_has_shovel(state, player)],

        ["Menu", "gasha tree 1", OoSEntranceType.OneWay, lambda state: oos_can_harvest_gasha(state, player, 1)],
        ["gasha tree 1", "gasha tree 2", OoSEntranceType.OneWay, lambda state: oos_can_harvest_gasha(state, player, 2)],
        ["gasha tree 2", "gasha tree 3", OoSEntranceType.OneWay, lambda state: oos_can_harvest_gasha(state, player, 3)],
        ["gasha tree 3", "gasha tree 4", OoSEntranceType.OneWay, lambda state: oos_can_harvest_gasha(state, player, 4)],
        ["gasha tree 4", "gasha tree 5", OoSEntranceType.OneWay, lambda state: oos_can_harvest_gasha(state, player, 5)],
        ["gasha tree 5", "gasha tree 6", OoSEntranceType.OneWay, lambda state: oos_can_harvest_gasha(state, player, 6)],
        ["gasha tree 6", "gasha tree 7", OoSEntranceType.OneWay, lambda state: oos_can_harvest_gasha(state, player, 7)],
        ["gasha tree 7", "gasha tree 8", OoSEntranceType.OneWay, lambda state: oos_can_harvest_gasha(state, player, 8)],
        ["gasha tree 8", "gasha tree 9", OoSEntranceType.OneWay, lambda state: oos_can_harvest_gasha(state, player, 9)],
        ["gasha tree 9", "gasha tree 10", OoSEntranceType.OneWay, lambda state: oos_can_harvest_gasha(state, player, 10)],
        ["gasha tree 10", "gasha tree 11", OoSEntranceType.OneWay, lambda state: oos_can_harvest_gasha(state, player, 11)],
        ["gasha tree 11", "gasha tree 12", OoSEntranceType.OneWay, lambda state: oos_can_harvest_gasha(state, player, 12)],
        ["gasha tree 12", "gasha tree 13", OoSEntranceType.OneWay, lambda state: oos_can_harvest_gasha(state, player, 13)],
        ["gasha tree 13", "gasha tree 14", OoSEntranceType.OneWay, lambda state: oos_can_harvest_gasha(state, player, 14)],
        ["gasha tree 14", "gasha tree 15", OoSEntranceType.OneWay, lambda state: oos_can_harvest_gasha(state, player, 15)],
        ["gasha tree 15", "gasha tree 16", OoSEntranceType.OneWay, lambda state: oos_can_harvest_gasha(state, player, 16)],
    ]
