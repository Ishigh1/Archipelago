from .LogicPredicates import *
from ..EntranceType import OoSEntranceType


def make_holodrum_logic(player: int):
    return [
        ["Menu", "impa", OoSEntranceType.OneWay, None],

        ["impa", "horon village", OoSEntranceType.TwoWay, None],
        ["horon village", "enter mayor's house", OoSEntranceType.TwoWay, None],
        ["enter mayor's house", "inside mayor's house", OoSEntranceType.DoorTwoWay, None],
        ["inside mayor's house", "mayor's gift", OoSEntranceType.OneWay, None],
        ["inside mayor's house", "mayor's house secret room", OoSEntranceType.OneWay, lambda state: oos_has_bombs(state, player)],

        ["horon village", "enter vasu", OoSEntranceType.TwoWay, None],
        ["enter vasu", "inside vasu", OoSEntranceType.DoorTwoWay, None],
        ["inside vasu", "vasu's gift", OoSEntranceType.OneWay, None],

        ["horon village", "horon heart piece", OoSEntranceType.OneWay, lambda state: oos_can_use_ember_seeds(state, player, False)],
        ["horon village", "enter dr left", OoSEntranceType.TwoWay, None],
        ["enter dr left", "inside dr left", OoSEntranceType.DoorTwoWay, None],
        ["inside dr left", "dr. left reward", OoSEntranceType.OneWay, lambda state: oos_can_use_ember_seeds(state, player, True)],
        ["inside dr left", "inside dr left side", OoSEntranceType.TwoWay, lambda state: oos_has_bombs(state, player)],
        ["inside dr left side", "enter dr left side", OoSEntranceType.DoorTwoWay, None],
        ["enter dr left side", "horon village SE chest", OoSEntranceType.OneWay, lambda state, season: any([
            oos_can_swim(state, player, False),
            season == SEASON_WINTER,
            oos_can_jump_2_wide_liquid(state, player)
        ])],

        ["horon village", "enter dr left old man", OoSEntranceType.TwoWay, None],
        ["enter dr left old man", "inside dr left old man", OoSEntranceType.DoorTwoWay, lambda state: \
            oos_can_use_ember_seeds(state, player, False)],
        ["inside dr left old man", "old man in horon", OoSEntranceType.OneWay, None],

        ["horon village", "enter tick tock", OoSEntranceType.TwoWay, None],
        ["enter tick tock", "inside tick tock", OoSEntranceType.DoorTwoWay, None],
        ["inside tick tock", "tick tock trade", OoSEntranceType.OneWay, lambda state: any([
            state.has("Wooden Bird", player),
            oos_self_locking_item(state, player, "tick tock trade", "Wooden Bird")
        ])],
        ["horon village", "enter hidden stairs behind clock shop", OoSEntranceType.TwoWay, None],
        ["enter hidden stairs behind clock shop", "inside hidden stairs behind clock shop", OoSEntranceType.DoorTwoWay, lambda state: \
            oos_has_shovel(state, player)],

        ["horon village", "maku tree", OoSEntranceType.OneWay, lambda state: oos_has_sword(state, player, False)],
        ["horon village", "horon village SW chest", OoSEntranceType.OneWay, lambda state, season: all([
            season == SEASON_AUTUMN,
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
        ["horon shop", "member's shop", OoSEntranceType.OneWay, lambda state: all([
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

        ["horon village", "d0 entrance", OoSEntranceType.TwoWay, None],

        ["d0 entrance", "black beast's chest", OoSEntranceType.OneWay, lambda state: all([
            all([
                oos_has_slingshot(state, player),
                oos_can_use_ember_seeds(state, player, True),
            ]),
            oos_can_use_mystery_seeds(state, player),
            oos_can_kill_armored_enemy(state, player),
        ])],

        ["d0 entrance", "enter beach fairy cave", OoSEntranceType.TwoWay, None],
        ["enter beach fairy cave", "inside beach fairy cave", OoSEntranceType.DoorTwoWay, None],

        ["d0 entrance", "western coast after ship", OoSEntranceType.TwoWay, lambda state: all([
            state.has("Pirate's Bell", player),
            state.has("_met_pirates", player)
        ])],

        ["western coast after ship", "enter pirate ship", OoSEntranceType.TwoWay, None],
        ["enter pirate ship", "inside pirate ship", OoSEntranceType.DoorTwoWay, lambda state: state.has("Pirate's Bell", player)],

        ["western coast after ship", "enter coast house", OoSEntranceType.TwoWay, None],
        ["enter coast house", "inside coast house", OoSEntranceType.DoorTwoWay, None],
        ["inside coast house", "inside coast house side", OoSEntranceType.TwoWay, lambda state: all([
            oos_has_bombs(state, player),
            any([
                oos_has_feather(state, player),
                oos_option_hard_logic(state, player)
            ])
        ])],
        ["inside coast house side", "enter coast house side", OoSEntranceType.DoorTwoWay, None],
        ["enter coast house side", "coast stump", OoSEntranceType.TwoWay, None],

        ["western coast after ship", "enter old man near western coast house", OoSEntranceType.TwoWay, None],
        ["enter old man near western coast house", "inside old man near western coast house", OoSEntranceType.DoorTwoWay, lambda state: \
            oos_can_use_ember_seeds(state, player, False)],
        ["inside old man near western coast house", "old man near western coast house", OoSEntranceType.OneWay, None],

        ["western coast after ship", "graveyard", OoSEntranceType.OneWay, lambda state, season: season == SEASON_SUMMER],
        ["graveyard", "western coast after ship", OoSEntranceType.OneWay, None],
        ["western coast after ship", "enter graveyard cave", OoSEntranceType.TwoWay, None],
        ["enter graveyard cave", "inside graveyard cave", OoSEntranceType.DoorTwoWay, None],
        ["inside graveyard cave", "inside graveyard chimney", OoSEntranceType.TwoWay, lambda state: \
            oos_can_jump_3_wide_pit(state, player)],
        ["inside graveyard chimney", "outside graveyard chimney", OoSEntranceType.DoorOneWay, None],
        ["outside graveyard chimney", "graveyard", OoSEntranceType.OneWay, None],

        ["graveyard", "enter hidden graveyard stairs", OoSEntranceType.TwoWay, None],
        ["enter hidden graveyard stairs", "inside hidden graveyard stairs", OoSEntranceType.DoorTwoWay, lambda state: \
            oos_has_shovel(state, player)],

        ["graveyard", "d7 entrance", OoSEntranceType.OneWay, lambda state, season: any([
            oos_can_remove_snow(state, player, False),
            season != SEASON_WINTER
        ])],
        ["d7 entrance", "graveyard", OoSEntranceType.OneWay, None],

        ["graveyard", "graveyard heart piece", OoSEntranceType.OneWay, lambda state, season: all([
            oos_can_break_mushroom(state, player, False),
            season == SEASON_AUTUMN
        ])],

        # EASTERN SUBURBS #############################################################################################

        ["horon village", "suburbs", OoSEntranceType.TwoWay, lambda state: oos_can_use_ember_seeds(state, player, False)],

        ["suburbs", "enter guru guru", OoSEntranceType.TwoWay, None],
        ["suburbs", "enter winter guru guru", OoSEntranceType.OneWay, lambda state, season: season == SEASON_WINTER],
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

        ["suburbs", "enter suburb spring cave", OoSEntranceType.OneWay, lambda state, season: all([
            oos_has_bracelet(state, player),
            season == SEASON_SPRING
        ])],
        ["enter suburb spring cave", "suburbs", OoSEntranceType.OneWay, lambda state: oos_has_bracelet(state, player)],
        ["enter suburb spring cave", "inside suburb spring cave", OoSEntranceType.DoorTwoWay, None],
        ["inside suburb spring cave", "eastern suburbs spring cave", OoSEntranceType.OneWay, lambda state: any([
            oos_has_magnet_gloves(state, player),
            oos_can_jump_3_wide_pit(state, player)
        ])],

        ["eastern suburbs portal", "suburbs", OoSEntranceType.OneWay, lambda state: oos_can_break_bush(state, player, False)],
        ["suburbs", "eastern suburbs portal", OoSEntranceType.OneWay, lambda state: oos_can_break_bush(state, player, True)],

        ["suburbs", "suburbs fairy fountain", OoSEntranceType.TwoWay, lambda state, season: any([
            oos_can_swim(state, player, True),
            oos_can_jump_1_wide_liquid(state, player, True),
            season == SEASON_WINTER
        ])],

        ["suburbs fairy fountain", "top of suburbs", OoSEntranceType.OneWay, lambda state, season: \
            season == SEASON_SPRING],
        ["top of suburbs", "suburbs fairy fountain", OoSEntranceType.OneWay, lambda state, season: any([
            season == SEASON_SPRING,
            oos_has_season(state, player, SEASON_SPRING),
            oos_can_warp(state, player)
        ])],

        ["top of suburbs", "sunken city", OoSEntranceType.TwoWay, None],

        # WOODS OF WINTER / 2D SECTOR ################################################################################

        ["suburbs fairy fountain", "suburbs NE", OoSEntranceType.TwoWay, lambda state, season: season == SEASON_WINTER],
        ["suburbs NE", "moblin road", OoSEntranceType.TwoWay, None],

        ["sunken city", "woods of winter, 2nd cave", OoSEntranceType.OneWay, lambda state, season: all([
            oos_has_flippers(state, player),
            season != SEASON_WINTER,
            any([
                oos_can_warp(state, player),
                all([
                    # We need both seasons to be able to climb back up
                    oos_season_in_eastern_suburbs(state, player, SEASON_WINTER),
                    oos_has_spring(state, player)
                ])
            ])
        ])],

        ["moblin road", "enter first woods of winter cave", OoSEntranceType.TwoWay, None],
        ["enter first woods of winter cave", "inside first woods of winter cave", OoSEntranceType.DoorTwoWay, lambda state, season: all([
            oos_can_remove_rockslide(state, player, True),
            season != SEASON_WINTER,
        ])],
        ["inside first woods of winter cave", "woods of winter, 1st cave", OoSEntranceType.OneWay, lambda state: \
            oos_can_break_bush(state, player, False)],

        ["moblin road", "enter second woods of winter cave", OoSEntranceType.TwoWay, None],
        ["enter second woods of winter cave", "inside second woods of winter cave", OoSEntranceType.DoorTwoWay, None],
        ["inside second woods of winter cave", "woods of winter, 2nd cave", OoSEntranceType.TwoWay, lambda state: any([
            oos_can_swim(state, player, False),
            oos_can_jump_3_wide_liquid(state, player)
        ])],

        ["moblin road", "enter holly chimney", OoSEntranceType.TwoWay, lambda state, season: \
            season == SEASON_WINTER],
        ["enter holly chimney", "inside holly chimney", OoSEntranceType.DoorOneWay, None],
        ["inside holly chimney", "holly's house", OoSEntranceType.OneWay, None],
        ["moblin road", "enter holly house", OoSEntranceType.TwoWay, None],
        ["enter holly house", "inside holly house", OoSEntranceType.DoorTwoWay, lambda state, season: \
            season == SEASON_WINTER],
        ["inside holly house", "holly's house", OoSEntranceType.TwoWay, None],

        ["moblin road", "enter suburbs old man", OoSEntranceType.TwoWay, None],
        ["enter suburbs old man", "inside suburbs old man", OoSEntranceType.DoorTwoWay, lambda state: oos_can_use_ember_seeds(state, player, False)],
        ["inside suburbs old man", "old man near holly's house", OoSEntranceType.OneWay, None],

        ["enter suburbs old man", "woods of winter heart piece", OoSEntranceType.OneWay, lambda state: any([
            oos_can_swim(state, player, True),
            oos_has_bracelet(state, player),
            oos_can_jump_1_wide_liquid(state, player, True)
        ])],
        ["enter suburbs old man", "suburbs fairy fountain", OoSEntranceType.TwoWay, lambda state, season: season == SEASON_WINTER],

        ["suburbs fairy fountain", "central woods of winter", OoSEntranceType.OneWay, lambda state, season: any([
            oos_can_jump_1_wide_pit(state, player, True),
            oos_can_remove_snow(state, player, True),
            season != SEASON_WINTER
        ])],
        ["central woods of winter", "suburbs fairy fountain", OoSEntranceType.OneWay, None],

        ["central woods of winter", "woods of winter tree", OoSEntranceType.OneWay, lambda state: oos_can_harvest_tree(state, player, True)],
        ["central woods of winter", "d2 entrance", OoSEntranceType.TwoWay, lambda state: oos_can_break_bush(state, player, True)],

        ["central woods of winter", "enter peek cave near d2", OoSEntranceType.TwoWay, None],
        ["enter peek cave near d2", "inside peek cave near d2", OoSEntranceType.DoorTwoWay, lambda state, season: any([
            oos_can_jump_1_wide_liquid(state, player, False),
            oos_can_swim(state, player, False),
            season == SEASON_WINTER
        ])],

        ["central woods of winter", "enter magnet cave near d2", OoSEntranceType.OneWay, lambda state, season: all([
            season == SEASON_AUTUMN,
            oos_can_break_mushroom(state, player, True),
        ])],
        ["enter magnet cave near d2", "central woods of winter", OoSEntranceType.OneWay, lambda state: all([
            oos_get_default_season(state, player, "WOODS_OF_WINTER") == SEASON_AUTUMN,
            oos_can_break_mushroom(state, player, False),
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

        ["impa", "old man trade", OoSEntranceType.OneWay, lambda state: any([
            state.has("Fish", player),
            oos_self_locking_item(state, player, "old man trade", "Fish")
        ])],

        ["impa", "eyeglass lake, across bridge", OoSEntranceType.OneWay, lambda state, season: any([
            oos_can_jump_4_wide_pit(state, player),
            all([
                season == SEASON_AUTUMN,
                oos_has_feather(state, player)
            ])
        ])],

        ["impa", "d1 stump", OoSEntranceType.TwoWay, lambda state: oos_can_break_bush(state, player, True)],
        ["d1 stump", "north horon", OoSEntranceType.TwoWay, lambda state: oos_has_bracelet(state, player)],
        ["d1 stump", "enter lon lon", OoSEntranceType.TwoWay, None],
        ["enter lon lon", "inside lon lon", OoSEntranceType.DoorTwoWay, None],
        ["inside lon lon", "malon trade", OoSEntranceType.OneWay, lambda state: any([
            state.has("Cuccodex", player),
            oos_self_locking_item(state, player, "malon trade", "Cuccodex")
        ])],
        ["d1 stump", "d1 island", OoSEntranceType.TwoWay, lambda state: oos_can_break_bush(state, player, True)],
        ["d1 stump", "enter d1 old man", OoSEntranceType.TwoWay, None],
        ["enter d1 old man", "inside d1 old man", OoSEntranceType.DoorTwoWay, lambda state: oos_can_use_ember_seeds(state, player, False)],
        ["inside d1 old man", "old man near d1", OoSEntranceType.OneWay, None],

        ["d1 island", "d1 entrance", OoSEntranceType.TwoWay, lambda state: state.has("Gnarled Key", player)],
        ["d1 island", "enter red ring old man", OoSEntranceType.TwoWay, None],
        ["enter red ring old man", "inside red ring old man", OoSEntranceType.DoorTwoWay, lambda state, season: season == SEASON_SUMMER],
        ["inside red ring old man", "golden beasts old man", OoSEntranceType.OneWay, lambda state, season: \
            oos_can_beat_required_golden_beasts(state, player)],

        ["d1 stump", "eyeglass lake", OoSEntranceType.TwoWay, lambda state, season: any([
            all([
                any([
                    season == SEASON_SPRING,
                    season == SEASON_AUTUMN,
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
            ]),
            all([
                any([
                    season == SEASON_SUMMER,
                    season == SEASON_WINTER,
                ]),
                oos_can_jump_1_wide_pit(state, player, True)
            ])
        ])],

        ["d5 stump", "eyeglass lake", OoSEntranceType.OneWay, lambda state, season: any([
            all([
                any([
                    season == SEASON_SPRING,
                    season == SEASON_SUMMER,
                    season == SEASON_AUTUMN,
                ]),
                oos_can_swim(state, player, True)
            ]),
            season == SEASON_WINTER
        ])],

        ["eyeglass lake", "d5 stump", OoSEntranceType.OneWay, lambda state, season: any([
            any([
                season == SEASON_SPRING,
                season == SEASON_AUTUMN,
                season == SEASON_WINTER
            ]),
        ])],

        ["eyeglass lake portal", "eyeglass lake", OoSEntranceType.OneWay, lambda state, season: any([
            all([
                any([
                    season == SEASON_AUTUMN,
                    season == SEASON_SPRING
                ]),
                oos_can_swim(state, player, False)
            ]),
            all([
                season == SEASON_WINTER,
                any([
                    oos_can_swim(state, player, False),
                    oos_can_jump_5_wide_liquid(state, player)
                ])
            ]),
            season == SEASON_SUMMER
        ])],
        ["eyeglass lake", "eyeglass lake portal", OoSEntranceType.OneWay, lambda state, season: any([
            season == SEASON_SPRING,
            season == SEASON_AUTUMN,
            all([
                season == SEASON_WINTER,
                any([
                    oos_can_swim(state, player, True),
                    oos_can_jump_5_wide_liquid(state, player)
                ])
            ])
        ])],

        ["eyeglass lake", "enter lake bomb cave", OoSEntranceType.OneWay, None],
        ["enter lake bomb cave", "eyeglass lake", OoSEntranceType.OneWay, lambda state, season: any([
            season == SEASON_SUMMER,
            all([
                season != SEASON_SUMMER,
                oos_can_swim(state, player, False)
            ])
        ])],
        ["enter lake bomb cave", "inside lake bomb cave", OoSEntranceType.DoorTwoWay, lambda state, season: all([
            season == SEASON_SUMMER,
            oos_can_remove_rockslide(state, player, True)
        ])],
        ["inside lake bomb cave", "dry eyeglass lake, west cave", OoSEntranceType.OneWay, lambda state: \
            oos_can_swim(state, player, False)],

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

        ["d5 stump", "enter lake boulder", OoSEntranceType.TwoWay, None],
        ["enter lake boulder", "inside lake boulder", OoSEntranceType.DoorTwoWay, lambda state, season: all([
            season == SEASON_SUMMER,
            oos_has_bracelet(state, player),
        ])],
        ["inside lake boulder", "dry eyeglass lake, east cave", OoSEntranceType.OneWay, None],

        # NORTH HORON / HOLODRUM PLAIN ###############################################################################

        ["north horon", "north horon tree", OoSEntranceType.OneWay, lambda state: oos_can_harvest_tree(state, player, True)],

        ["north horon", "enter Blaino", OoSEntranceType.TwoWay, None],
        ["enter Blaino", "inside Blaino", OoSEntranceType.DoorTwoWay, None],
        ["inside Blaino", "blaino prize", OoSEntranceType.OneWay, lambda state: oos_can_farm_rupees(state, player)],

        ["north horon", "enter autumn water cave", OoSEntranceType.TwoWay, lambda state, season: all([
            season == SEASON_AUTUMN,
            oos_can_break_mushroom(state, player, True),
            oos_has_flippers(state, player)
        ])],
        ["enter autumn water cave", "inside autumn water cave", OoSEntranceType.DoorTwoWay, lambda state: oos_can_swim(state, player, False)],
        ["inside autumn water cave", "cave north of D1", OoSEntranceType.OneWay, lambda state: oos_can_swim(state, player, False)],

        ["north horon", "enter old man near blaino", OoSEntranceType.OneWay, lambda state, season: any([
            season == SEASON_SUMMER,
            oos_can_summon_ricky(state, player)
        ])],
        ["enter old man near blaino", "north horon", OoSEntranceType.OneWay, None],
        ["enter old man near blaino", "inside old man near blaino", OoSEntranceType.DoorTwoWay, lambda state: \
            oos_can_use_ember_seeds(state, player, False)],
        ["inside old man near blaino", "old man near blaino", OoSEntranceType.OneWay, None],

        ["north horon", "underwater item below natzu bridge", OoSEntranceType.OneWay, lambda state: oos_can_swim(state, player, False)],

        ["north horon", "temple remains lower stump", OoSEntranceType.TwoWay, lambda state: oos_can_jump_3_wide_pit(state, player)],

        ["ghastly stump", "enter Mrs Ruul", OoSEntranceType.TwoWay, None],
        ["enter Mrs Ruul", "inside Mrs Ruul", OoSEntranceType.DoorTwoWay, None],
        ["inside Mrs Ruul", "mrs. ruul trade", OoSEntranceType.OneWay, lambda state: any([
            state.has("Ghastly Doll", player),
            oos_self_locking_item(state, player, "mrs. ruul trade", "Ghastly Doll")
        ])],

        ["ghastly stump", "enter ruul old man", OoSEntranceType.TwoWay, None],
        ["enter ruul old man", "inside ruul old man", OoSEntranceType.DoorTwoWay, lambda state: oos_can_use_ember_seeds(state, player, False)],
        ["inside ruul old man", "old man near mrs. ruul", OoSEntranceType.OneWay, None],

        ["north horon", "ghastly stump", OoSEntranceType.TwoWay, lambda state, season: any([
            oos_can_jump_1_wide_pit(state, player, True),
            season == SEASON_WINTER
        ])],

        ["spool swamp north", "ghastly stump", OoSEntranceType.OneWay, None],
        ["ghastly stump", "spool swamp north", OoSEntranceType.OneWay, lambda state, season: all([
            any([
                season == SEASON_SUMMER,
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
        ["d1 island", "holodrum plain waters", OoSEntranceType.TwoWay, lambda state: oos_can_swim(state, player, True)],
        ["spool swamp south", "holodrum plain waters", OoSEntranceType.TwoWay, lambda state: oos_can_swim(state, player, True)],
        ["north horon", "holodrum plain waters", OoSEntranceType.TwoWay, lambda state: oos_can_swim(state, player, True)],
        ["north horon", "goron mountain entrance", OoSEntranceType.TwoWay, lambda state: oos_can_swim(state, player, True)],
        ["goron mountain entrance", "enter natzu north stairs", OoSEntranceType.TwoWay, lambda state: oos_can_swim(state, player, True)],
        ["ghastly stump", "holodrum plain waters", OoSEntranceType.TwoWay, lambda state: all([
            oos_can_break_bush(state, player, True),
            oos_can_swim(state, player, True)
        ])],

        ["holodrum plain waters", "enter treehouse", OoSEntranceType.TwoWay, lambda state: oos_can_swim(state, player, True)],
        ["enter treehouse", "inside treehouse", OoSEntranceType.DoorTwoWay, None],
        ["inside treehouse", "old man in treehouse", OoSEntranceType.OneWay, lambda state: all([
            oos_can_swim(state, player, True),
            oos_has_essences_for_treehouse(state, player)
        ])],
        ["holodrum plain waters", "enter ruul water cave", OoSEntranceType.TwoWay, lambda state: oos_can_swim(state, player, False)],
        ["enter ruul water cave", "inside ruul water cave", OoSEntranceType.DoorTwoWay, lambda state: oos_can_swim(state, player, False)],
        ["inside ruul water cave", "cave south of mrs. ruul", OoSEntranceType.OneWay, lambda state: any([
            oos_can_swim(state, player, False),
            oos_can_jump_3_wide_liquid(state, player)
        ])],

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

        ["spool swamp north", "spool swamp digging spot", OoSEntranceType.OneWay, lambda state, season: all([
            season == SEASON_SUMMER,
            oos_has_shovel(state, player)
        ])],

        ["spool swamp north", "enter floodgate right", OoSEntranceType.TwoWay, lambda state: any([
            state.has("_flipped_floodgate_lever", player),
            oos_can_swim(state, player, False)
        ])],
        ["enter floodgate right", "inside floodgate right", OoSEntranceType.DoorTwoWay, lambda state: state.has("_flipped_floodgate_lever", player)],
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
        ["enter floodgate left", "floodgate keyhole", OoSEntranceType.OneWay, lambda state: state.has("Floodgate Key", player)],
        ["enter floodgate left", "spool swamp north", OoSEntranceType.OneWay, lambda state: oos_can_swim(state, player, True)],
        ["enter floodgate left", "spool stump", OoSEntranceType.OneWay, lambda state: state.has("_opened_floodgate", player)],

        ["spool stump", "spool swamp north", OoSEntranceType.OneWay, None],
        ["spool swamp north", "spool stump", OoSEntranceType.OneWay, lambda state: state.has("_opened_floodgate", player)],
        ["spool stump", "d3 entrance", OoSEntranceType.OneWay, lambda state, season: season == SEASON_SUMMER],
        ["d3 entrance", "spool stump", OoSEntranceType.OneWay, lambda state, season: any([
            # Jumping down D3 entrance without having a way to put summer is a risky situation, so expect player
            # to have a way to warp out
            season == SEASON_SUMMER,
            oos_can_warp(state, player)
        ])],

        ["spool stump", "spool swamp middle", OoSEntranceType.OneWay, lambda state, season: any([
            season != SEASON_SPRING,
            oos_has_flippers(state, player),
            oos_can_summon_dimitri(state, player)
        ])],
        ["spool swamp middle", "spool stump", OoSEntranceType.OneWay, lambda state, season: all([
            any([
                season != SEASON_SPRING,
                oos_has_flippers(state, player),
                oos_can_summon_dimitri(state, player)
            ]),
            state.has("_opened_floodgate", player)
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

        ["spool swamp south", "spool swamp south near gasha spot", OoSEntranceType.TwoWay, lambda state, season: \
            any([
                all([
                    oos_can_break_flowers(state, player, True),
                    season == SEASON_SPRING
                ]),
                season == SEASON_SUMMER,
                season == SEASON_AUTUMN,
                all([
                    season == SEASON_WINTER,
                    oos_can_remove_snow(state, player, True)
                ]),
            ])
         ],

        ["spool swamp south", "enter swamp bomb cave", OoSEntranceType.OneWay, lambda state, season: all([
            season == SEASON_WINTER,
            oos_can_remove_snow(state, player, True)
        ])],
        ["enter swamp bomb cave", "spool swamp south", OoSEntranceType.OneWay, lambda state, season: all([
            season == SEASON_WINTER,
            oos_can_remove_snow(state, player, False)
        ])],
        ["spool swamp south", "open swamp bomb cave", OoSEntranceType.OneWay, lambda state, season: all([
            season == SEASON_WINTER,
            oos_can_summon_ricky(state, player)
        ])],
        ["enter swamp bomb cave", "open swamp bomb cave", OoSEntranceType.OneWay, lambda state: oos_has_bombs(state, player)],
        ["enter swamp bomb cave", "inside swamp bomb cave", OoSEntranceType.DoorTwoWay, lambda state: \
            state.has("_opened_swamp_bomb_cave", player)],
        ["inside swamp bomb cave", "spool swamp cave", OoSEntranceType.OneWay, None],

        ["spool swamp south", "spool swamp heart piece", OoSEntranceType.OneWay, lambda state, season: all([
            season == SEASON_SPRING,
            oos_can_swim(state, player, True),
        ])],

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
        ["natzu east (dimitri)", "enter natzu north stairs", OoSEntranceType.OneWay, lambda state: \
            oos_can_jump_5_wide_liquid(state, player)],
        ["enter natzu north stairs", "natzu east (dimitri)", OoSEntranceType.OneWay, lambda state: all([
            oos_can_jump_5_wide_liquid(state, player),
            oos_is_companion_dimitri(state, player)
        ])],
        ["enter natzu north stairs", "inside natzu north stairs", OoSEntranceType.DoorTwoWay, None],
        ["inside natzu north stairs", "natzu region, across water", OoSEntranceType.OneWay, None],

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

        ["sunken city entrance", "sunken city", OoSEntranceType.TwoWay, lambda state, season: any([
            oos_has_feather(state, player),
            oos_can_swim(state, player, True),
            season == SEASON_WINTER
        ])],

        ["sunken city dimitri", "sunken city entrance", OoSEntranceType.OneWay, None],

        # This allows to reset the season
        ["sunken city", "warp to sunken city", OoSEntranceType.OneWay, lambda state: oos_can_warp_using_gale_seeds(state, player)],
        ["warp to sunken city", "sunken city", OoSEntranceType.OneWay, None],

        ["sunken city", "sunken city tree", OoSEntranceType.OneWay, lambda state: \
            oos_can_harvest_tree(state, player, True)],

        ["sunken city", "sunken city stump", OoSEntranceType.TwoWay, lambda state, season: any([
            season == SEASON_WINTER,
            oos_can_swim(state, player, True)
        ])],

        ["sunken city dimitri", "sunken city stump", OoSEntranceType.OneWay, None],

        ["sunken city", "sunken city dimitri", OoSEntranceType.OneWay, lambda state, season: any([
            oos_can_summon_dimitri(state, player),
            oos_has_bombs(state, player)
        ])],

        ["sunken city", "enter ingo", OoSEntranceType.TwoWay, None],
        ["enter ingo", "inside ingo", OoSEntranceType.DoorTwoWay, None],
        ["inside ingo", "ingo trade", OoSEntranceType.OneWay, lambda state: any([
            state.has("Goron Vase", player),
            oos_self_locking_item(state, player, "ingo trade", "Goron Vase")
        ])],
        ["sunken city", "enter syrup", OoSEntranceType.TwoWay, lambda state, season: season == SEASON_WINTER],
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

        ["sunken city", "enter sunken city, summer cave", OoSEntranceType.OneWay, lambda state, season: all([
            season == SEASON_SUMMER,
            oos_has_flippers(state, player),
        ])],
        ["enter sunken city, summer cave", "sunken city", OoSEntranceType.OneWay, lambda state: \
            oos_has_flippers(state, player)],
        ["enter sunken city, summer cave", "inside sunken city, summer cave", OoSEntranceType.DoorTwoWay, None],
        ["inside sunken city, summer cave", "sunken city, summer cave", OoSEntranceType.OneWay, lambda state: all([
            any([
                oos_has_flippers(state, player),
                oos_can_jump_1_wide_liquid(state, player, False)
            ]),
            oos_can_break_bush(state, player, False)
        ])],

        ["mount cucco", "sunken city", OoSEntranceType.OneWay, lambda state: oos_has_flippers(state, player)],
        ["sunken city", "mount cucco", OoSEntranceType.OneWay, lambda state, season: all([
            oos_has_flippers(state, player),
            season == SEASON_SUMMER
        ])],
        ["sunken city gasha spot", "enter flooded house", OoSEntranceType.OneWay, lambda state: any([
            oos_can_swim(state, player, False),
            oos_can_jump_3_wide_liquid(state, player)  # TODO : test that
        ])],
        ["enter flooded house", "sunken city gasha spot", OoSEntranceType.OneWay, None],
        ["sunken city gasha spot", "sunken city stump", OoSEntranceType.OneWay, None],
        ["enter flooded house", "inside flooded house", OoSEntranceType.DoorTwoWay, None],
        ["sunken city", "enter treasure hunter", OoSEntranceType.TwoWay, None],
        ["enter treasure hunter", "inside treasure hunter", OoSEntranceType.DoorTwoWay, None],
        ["sunken city", "enter bomb house", OoSEntranceType.TwoWay, None],
        ["enter bomb house", "inside bomb house", OoSEntranceType.DoorTwoWay, None],

        # MT. CUCCO / GORON MOUNTAINS ##############################################################################

        ["mount cucco", "mt. cucco portal", OoSEntranceType.TwoWay, None],

        ["mount cucco", "enter mountain fairy cave", OoSEntranceType.TwoWay, None],
        ["enter mountain fairy cave", "inside mountain fairy cave", OoSEntranceType.DoorTwoWay, lambda state, season: \
            season == SEASON_WINTER],

        ["mount cucco", "rightmost rooster ledge", OoSEntranceType.OneWay, lambda state, season: all([
            any([  # to reach the rooster
                all([
                    season == SEASON_SPRING,
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
        ["rightmost rooster ledge", "spring banana tree", OoSEntranceType.OneWay, lambda state, season: all([
            oos_has_feather(state, player),
            season == SEASON_SPRING,
            any([  # can harvest tree
                oos_has_sword(state, player),
                oos_has_fools_ore(state, player)
            ])
        ])],

        ["mount cucco", "mt. cucco, talon's cave entrance", OoSEntranceType.OneWay, lambda state, season: \
            season == SEASON_SPRING],

        ["mt. cucco, talon's cave entrance", "enter talon cave", OoSEntranceType.TwoWay, None],
        ["enter talon cave", "inside talon cave", OoSEntranceType.DoorTwoWay, lambda state, season: season != SEASON_WINTER],
        ["inside talon cave", "talon trade", OoSEntranceType.OneWay, lambda state: state.has("Megaphone", player)],

        ["mt. cucco, talon's cave entrance", "mt. cucco heart piece", OoSEntranceType.OneWay, None],

        ["mt. cucco, talon's cave entrance", "diving spot outside D4", OoSEntranceType.OneWay, lambda state: oos_has_flippers(state, player)],

        ["mt. cucco, talon's cave entrance", "enter winter cave in cucco mountain", OoSEntranceType.TwoWay, None],
        ["enter winter cave in cucco mountain", "inside winter cave in cucco mountain", OoSEntranceType.DoorTwoWay,
         lambda state, season: season == SEASON_WINTER],
        ["inside winter cave in cucco mountain", "inside top of cucco mountain", OoSEntranceType.TwoWay, lambda state: any([
            all([
                oos_has_bracelet(state, player),
                oos_can_jump_1_wide_pit(state, player, False)
            ]),
            oos_can_jump_2_wide_pit(state, player)
        ])],
        ["inside top of cucco mountain", "enter top of cucco mountain", OoSEntranceType.DoorTwoWay, None],
        ["enter top of cucco mountain", "dragon keyhole", OoSEntranceType.OneWay, lambda state: all([
            oos_has_bracelet(state, player),
            state.has("Dragon Key", player)
        ])],
        ["enter top of cucco mountain", "mt. cucco, talon's cave entrance", OoSEntranceType.OneWay, lambda state: oos_has_bracelet(state, player)],

        ["mt. cucco, talon's cave entrance", "d4 entrance", OoSEntranceType.OneWay, lambda state, season: all([
            state.has("_opened_d4", player),
            season == SEASON_SUMMER
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

        ["goron blocked cave entrance", "enter goron mountain middle", OoSEntranceType.TwoWay, None],
        ["enter goron mountain middle", "inside goron mountain middle", OoSEntranceType.DoorTwoWay, None],
        ["inside goron mountain middle", "goron mountain", OoSEntranceType.TwoWay, lambda state: oos_has_bracelet(state, player)],

        ["goron blocked cave entrance", "enter goron mountain bomb cave", OoSEntranceType.TwoWay, None],
        ["enter goron mountain bomb cave", "inside goron mountain bomb cave", OoSEntranceType.DoorTwoWay, lambda state: oos_has_bombs(state, player)],
        ["inside goron mountain bomb cave", "inside goron outside stairs", OoSEntranceType.TwoWay, None],
        ["inside goron outside stairs", "enter goron outside stairs", OoSEntranceType.DoorTwoWay, None],
        ["enter goron outside stairs", "goron's gift", OoSEntranceType.OneWay, None],

        ["goron mountain", "inside goron mountain top", OoSEntranceType.TwoWay, None],
        ["inside goron mountain top", "enter goron mountain top", OoSEntranceType.DoorTwoWay, None],
        ["enter goron mountain top", "biggoron trade", OoSEntranceType.OneWay, lambda state: all([
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
        ["enter goron mountain middle", "enter goron old man", OoSEntranceType.TwoWay, None],
        ["enter goron old man", "inside goron old man", OoSEntranceType.DoorTwoWay, lambda state: \
            oos_can_use_ember_seeds(state, player, False)],
        ["inside goron old man", "old man in goron mountain", OoSEntranceType.OneWay, None],

        ["goron mountain entrance", "enter goron mountain bottom", OoSEntranceType.TwoWay, None],
        ["enter goron mountain bottom", "inside goron mountain bottom", OoSEntranceType.DoorTwoWay, None],
        ["inside goron mountain bottom", "goron mountain", OoSEntranceType.TwoWay, lambda state: any([
            oos_has_flippers(state, player),
            oos_can_jump_4_wide_liquid(state, player),
        ])],

        ["goron mountain entrance", "temple remains lower stump", OoSEntranceType.TwoWay, lambda state: \
            oos_can_jump_3_wide_pit(state, player)],

        # TARM RUINS ###############################################################################################

        ["spool swamp north", "tarm ruins", OoSEntranceType.OneWay, lambda state: oos_has_required_jewels(state, player)],
        ["tarm ruins", "lost woods plateau", OoSEntranceType.OneWay, lambda state, season: season == SEASON_SUMMER],
        ["lost woods plateau", "tarm ruins", OoSEntranceType.OneWay, None],
        ["lost woods plateau", "lost woods statue", OoSEntranceType.OneWay, lambda state, season: season != SEASON_WINTER],
        ["tarm ruins", "lost woods statues stump", OoSEntranceType.OneWay, lambda state, season: all([
            season == SEASON_WINTER,
            state.has("_pushed_lost_woods_statue", player)
        ])],
        ["lost woods statues stump", "lost woods plateau", OoSEntranceType.OneWay, lambda state, season: any([
            season == SEASON_WINTER,
            oos_can_jump_2_wide_liquid(state, player),
            oos_can_swim(state, player, False)
        ])],
        ["lost woods statues stump", "lost woods post statues stump", OoSEntranceType.OneWay, lambda state, season: \
            season == SEASON_WINTER],
        ["lost woods post statues stump", "lost woods stump", OoSEntranceType.TwoWay, lambda state, season: all([
            season == SEASON_AUTUMN,
            oos_can_break_mushroom(state, player, False)
        ])],

        ["lost woods plateau", "enter lost woods deku", OoSEntranceType.TwoWay, lambda state, season: all([
            season == SEASON_AUTUMN,
            oos_can_break_mushroom(state, player, False)
        ])],
        ["enter lost woods deku", "inside lost woods deku", OoSEntranceType.DoorTwoWay, None],
        ["inside lost woods deku", "lost woods deku", OoSEntranceType.OneWay, lambda state: oos_has_shield(state, player)],

        ["lost woods stump", "enter phonograph deku", OoSEntranceType.OneWay, None],
        ["enter phonograph deku", "inside phonograph deku", OoSEntranceType.DoorTwoWay, lambda state: oos_can_use_ember_seeds(state, player, False)],
        ["inside phonograph deku", "phonograph deku", OoSEntranceType.OneWay, lambda state: state.has("Phonograph", player)],

        ["lost woods stump", "lost woods", OoSEntranceType.OneWay, lambda state: oos_can_reach_lost_woods_pedestal(state, player)],
        ["lost woods stump", "d6 sector", OoSEntranceType.OneWay, lambda state: oos_can_complete_lost_woods_main_sequence(state, player)],
        ["d6 sector", "lost woods stump", OoSEntranceType.OneWay, None],

        ["d6 sector", "tarm ruins tree", OoSEntranceType.OneWay, lambda state: oos_can_harvest_tree(state, player, False)],
        ["d6 sector", "enter tarm ruins, under tree", OoSEntranceType.TwoWay, lambda state, season: all([
            season == SEASON_AUTUMN,
            oos_can_break_mushroom(state, player, False),
        ])],
        ["enter tarm ruins, under tree", "warp to d6 sector", OoSEntranceType.OneWay, lambda state: \
            oos_can_warp_using_gale_seeds(state, player)],
        ["warp to d6 sector", "d6 sector", OoSEntranceType.OneWay, None],
        ["enter tarm ruins, under tree", "inside tarm ruins, under tree", OoSEntranceType.DoorTwoWay, lambda state: \
            oos_can_use_ember_seeds(state, player, False)],
        ["inside tarm ruins, under tree", "tarm ruins, under tree", OoSEntranceType.OneWay, None],

        ["d6 sector", "tarm ruins top", OoSEntranceType.OneWay, lambda state, season: any([
            all([
                season == SEASON_WINTER,
                any([
                    oos_has_shovel(state, player),
                    oos_can_use_ember_seeds(state, player, False)
                ]),
            ]),
            all([
                season == SEASON_SPRING,
                state.has("_pushed_tarm_statue", player)
            ])
        ])],
        ["tarm ruins top", "d6 sector", OoSEntranceType.OneWay, None],
        ["tarm ruins top", "d6 entrance", OoSEntranceType.TwoWay, lambda state, season: all([
            season == SEASON_SPRING,
            oos_can_break_flowers(state, player, False)
        ])],
        ["tarm ruins top", "old man near d6", OoSEntranceType.TwoWay, lambda state, season: all([
            season == SEASON_SPRING,
            oos_can_break_flowers(state, player, False),
            oos_can_use_ember_seeds(state, player, False)
        ])],

        # SAMASA DESERT ######################################################################################

        ["suburbs", "samasa desert", OoSEntranceType.OneWay, lambda state: state.has("_met_pirates", player)],
        ["samasa desert", "samasa desert pit", OoSEntranceType.OneWay, lambda state: oos_has_bracelet(state, player)],
        ["samasa desert", "samasa desert chest", OoSEntranceType.OneWay, lambda state: oos_has_flippers(state, player)],
        ["samasa desert", "enter desert fairy cave", OoSEntranceType.TwoWay, lambda state: any([
            oos_can_swim(state, player, False),
            oos_can_jump_2_wide_pit(state, player)  # It's a liquid but the jump distance is 1.5
        ])],
        ["enter desert fairy cave", "inside desert fairy cave", OoSEntranceType.DoorTwoWay, lambda state: oos_has_bombs(state, player)],

        # TEMPLE REMAINS ####################################################################################

        ["temple remains lower stump", "temple remains upper stump", OoSEntranceType.OneWay, lambda state, season: any([
            all([  # Winter rule
                season == SEASON_WINTER,
                oos_can_remove_snow(state, player, False),
                oos_can_break_bush(state, player, False),
                oos_can_jump_6_wide_pit(state, player)
            ]),
            all([  # Summer rule
                season == SEASON_SUMMER,
                oos_can_break_bush(state, player, False),
                oos_can_jump_6_wide_pit(state, player)
            ]),
            all([  # Spring rule
                season == SEASON_SPRING,
                oos_can_break_flowers(state, player, False),
                oos_can_break_bush(state, player, False),
                oos_can_jump_6_wide_pit(state, player)
            ]),
            all([  # Autumn rule
                season == SEASON_AUTUMN,
                oos_can_break_bush(state, player)
            ])
        ])],
        ["temple remains upper stump", "temple remains lower stump", OoSEntranceType.OneWay, lambda state, season: any([
            # Winter rule
            season == SEASON_WINTER,
            all([  # Summer rule
                season == SEASON_SUMMER,
                oos_can_break_bush(state, player, False),
                oos_can_jump_6_wide_pit(state, player)
            ]),
            all([  # Spring rule
                season == SEASON_SPRING,
                oos_can_break_flowers(state, player, False),
                oos_can_break_bush(state, player, False),
                oos_can_jump_6_wide_pit(state, player)
            ]),
            all([  # Autumn rule
                season == SEASON_AUTUMN,
                oos_can_break_bush(state, player)
            ])
        ])],

        ["temple remains upper stump", "temple remains lower portal access", OoSEntranceType.OneWay, lambda state, season: all([
            season == SEASON_WINTER,
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

        ["temple remains lower stump", "enter d8 fairy room", OoSEntranceType.OneWay, lambda state, season: all([
            state.has("_triggered_volcano", player),
            season == SEASON_SUMMER,
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

        ["enter d8 fairy room", "temple remains lower portal access", OoSEntranceType.OneWay, lambda state, season: \
            season == SEASON_WINTER],

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

        ["d0 entrance", "golden darknut", OoSEntranceType.OneWay, lambda state, season: all([
            season == SEASON_SPRING,
            any([
                oos_has_sword(state, player),
                oos_has_fools_ore(state, player)
            ])
        ])],
        ["lost woods plateau", "golden lynel", OoSEntranceType.OneWay, lambda state, season: all([
            season == SEASON_WINTER,
            any([
                oos_has_sword(state, player),
                oos_has_fools_ore(state, player)
            ])
        ])],
        ["d2 entrance", "golden moblin", OoSEntranceType.OneWay, lambda state, season: all([
            season == SEASON_AUTUMN,
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
        ["spool swamp south", "golden octorok", OoSEntranceType.OneWay, lambda state, season: all([
            any([
                oos_has_sword(state, player),
                oos_has_fools_ore(state, player)
            ]),
            season == SEASON_SUMMER
        ])],

        # GASHA TREES #############################################################################################

        ["horon village", "horon gasha spot", OoSEntranceType.OneWay, None],
        ["impa", "impa gasha spot", OoSEntranceType.OneWay, lambda state: oos_can_break_bush(state, player, True)],
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
        ["sunken city", "sunken city gasha spot", OoSEntranceType.OneWay, lambda state, season: all([
            season == SEASON_SUMMER,
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
        ["mount cucco", "mt cucco gasha spot", OoSEntranceType.OneWay, lambda state, season: all([
            season == SEASON_AUTUMN,
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
