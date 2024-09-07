from worlds.tloz_oos.data.EntranceType import OoSEntranceType
from worlds.tloz_oos.data.logic.LogicPredicates import *


def make_d0_logic(player: int):
    return [
        # 0 keys
        ["enter d0", "d0 key chest", OoSEntranceType.OneWay, None],
        ["enter d0", "d0 rupee chest", OoSEntranceType.OneWay, lambda state: \
            # If hole is removed, stairs are added inside dungeon to make the chest reachable
        oos_option_no_d0_alt_entrance(state, player)
         ],
        ["d0 entrance", "enter d0 chimney", OoSEntranceType.TwoWay, None],
        ["enter d0 chimney", "inside d0 chimney", OoSEntranceType.DoorOneWay, lambda state: all([
            oos_can_break_bush(state, player, True),
            # If dungeons are shuffled, jumping down the hole is a dangerous action and requires
            # a way of warping back to be in logic
            any([
                not oos_option_shuffled_dungeons(state, player),
                oos_can_warp(state, player)
            ])
        ])],
        ["inside d0 chimney", "d0 rupee chest", OoSEntranceType.OneWay, None],
        ["d0 rupee chest", "enter d0", OoSEntranceType.OneWay, None],
        ["enter d0", "d0 hidden 2d section", OoSEntranceType.OneWay, lambda state: any([
            oos_can_kill_normal_enemy(state, player),
            all([
                # Keese can be killed using boomerang as well, but that's kind of obscure so not in casual logic
                oos_option_medium_logic(state, player),
                oos_has_boomerang(state, player),
            ])
        ])],

        # 1 key
        ["enter d0", "d0 sword chest", OoSEntranceType.OneWay, lambda state: any([
            oos_has_small_keys(state, player, 0, 1),
            oos_self_locking_small_key(state, player, "d0 sword chest", 0)
        ])],
    ]


def make_d1_logic(player: int):
    return [
        # 0 keys
        ["enter d1", "d1 stalfos drop", OoSEntranceType.OneWay, lambda state: any([
            oos_can_kill_stalfos(state, player),
            all([
                # Medium logic expects the player to be able to use bushes
                oos_option_medium_logic(state, player),
                oos_has_bracelet(state, player)
            ])
        ])],

        ["enter d1", "d1 floormaster room", OoSEntranceType.OneWay, lambda state: oos_can_use_ember_seeds(state, player, True)],

        ["d1 floormaster room", "d1 boss", OoSEntranceType.OneWay, lambda state: all([
            oos_has_boss_key(state, player, 1),
            oos_can_kill_armored_enemy(state, player)
        ])],

        # 1 key
        ["enter d1", "d1 stalfos chest", OoSEntranceType.OneWay, lambda state: all([
            oos_has_small_keys(state, player, 1, 1),
            oos_can_kill_stalfos(state, player)
        ])],

        ["d1 stalfos chest", "d1 goriya chest", OoSEntranceType.OneWay, lambda state: all([
            oos_can_use_ember_seeds(state, player, True),
            oos_can_kill_normal_enemy(state, player, True)
        ])],

        ["d1 stalfos chest", "d1 lever room", OoSEntranceType.OneWay, None],

        ["d1 stalfos chest", "d1 block-pushing room", OoSEntranceType.OneWay, lambda state: any([
            oos_can_kill_normal_enemy(state, player),
            all([
                oos_option_hard_logic(state, player),
                oos_has_bracelet(state, player)
            ])
        ])],

        ["d1 stalfos chest", "d1 railway chest", OoSEntranceType.OneWay, lambda state: any([
            oos_can_trigger_lever(state, player),
            all([
                oos_option_hard_logic(state, player),
                oos_has_bracelet(state, player)
            ])
        ])],

        ["d1 railway chest", "d1 button chest", OoSEntranceType.OneWay, None],

        # 2 keys
        ["d1 railway chest", "d1 basement", OoSEntranceType.OneWay, lambda state: all([
            oos_has_bombs(state, player),
            any([
                oos_has_small_keys(state, player, 1, 2),
                oos_self_locking_small_key(state, player, "d1 basement", 1)
            ]),
            oos_can_kill_armored_enemy(state, player)
        ])],
    ]


def make_d2_logic(player: int):
    return [
        # 0 keys
        ["enter d2", "d2 torch room", OoSEntranceType.OneWay, None],
        ["d2 torch room", "d2 left from entrance", OoSEntranceType.OneWay, None],
        ["d2 torch room", "d2 rope drop", OoSEntranceType.OneWay, lambda state: oos_can_kill_normal_enemy(state, player)],
        ["d2 torch room", "d2 arrow room", OoSEntranceType.OneWay, lambda state: oos_can_use_ember_seeds(state, player, True)],

        ["d2 arrow room", "d2 torch room", OoSEntranceType.OneWay, lambda state: all([
            oos_can_kill_normal_enemy(state, player),
            any([
                # Backwards path is one-way if we don't have ember seeds, so ensure we have a way to warp out in case
                # something goes wrong
                oos_can_use_ember_seeds(state, player, True),
                oos_can_warp(state, player)
            ])
        ])],
        ["d2 arrow room", "d2 rupee room", OoSEntranceType.OneWay, lambda state: oos_has_bombs(state, player)],
        ["d2 arrow room", "d2 rope chest", OoSEntranceType.OneWay, lambda state: oos_can_kill_normal_enemy(state, player)],
        ["d2 arrow room", "d2 blade chest", OoSEntranceType.OneWay, lambda state: oos_can_kill_normal_enemy(state, player)],

        ["d2 blade chest", "d2 arrow room", OoSEntranceType.OneWay, None],  # Backwards path
        ["d2 blade chest", "inside d2 side entrance left", OoSEntranceType.TwoWay, None],
        ["inside d2 side entrance left", "enter d2 side entrance left", OoSEntranceType.D2Stairs, None],
        ["enter d2 side entrance left", "d2 alt entrances", OoSEntranceType.TwoWay, lambda state: oos_has_bracelet(state, player)],
        ["d2 blade chest", "d2 roller chest", OoSEntranceType.OneWay, lambda state: all([
            oos_has_bombs(state, player),
            oos_has_bracelet(state, player),
        ])],
        ["d2 alt entrances", "enter d2 side entrance right", OoSEntranceType.TwoWay, None],
        ["enter d2 side entrance right", "inside d2 side entrance right", OoSEntranceType.D2Stairs, None],
        ["inside d2 side entrance right", "d2 spiral chest", OoSEntranceType.OneWay, lambda state: all([
            oos_can_break_bush(state, player, False),
            oos_has_bombs(state, player),
        ])],

        # 2 keys
        ["d2 roller chest", "d2 spinner", OoSEntranceType.OneWay, lambda state: oos_has_small_keys(state, player, 2, 2)],
        ["d2 spinner", "dodongo owl", OoSEntranceType.OneWay, lambda state: oos_can_use_mystery_seeds(state, player)],
        ["d2 spinner", "d2 boss", OoSEntranceType.OneWay, lambda state: all([
            oos_has_boss_key(state, player, 2),
            oos_has_bombs(state, player),
            oos_has_bracelet(state, player)
        ])],

        # 3 keys
        ["d2 arrow room", "d2 hardhat room", OoSEntranceType.OneWay, lambda state: oos_has_small_keys(state, player, 2, 3)],
        ["d2 hardhat room", "d2 pot chest", OoSEntranceType.OneWay, lambda state: oos_can_break_pot(state, player)],
        ["d2 hardhat room", "d2 moblin chest", OoSEntranceType.OneWay, lambda state: any([
            all([
                oos_can_kill_d2_hardhat(state, player),
                oos_can_kill_d2_far_moblin(state, player)
            ])
        ])],
        ["d2 spinner", "d2 terrace chest", OoSEntranceType.OneWay, lambda state: any([
            oos_has_small_keys(state, player, 2, 3),
            oos_self_locking_small_key(state, player, "d2 terrace chest", 2)
        ])],
    ]


def make_d3_logic(player: int):
    return [
        # 0 keys
        ["enter d3", "spiked beetles owl", OoSEntranceType.OneWay, lambda state: oos_can_use_mystery_seeds(state, player)],
        ["enter d3", "d3 center", OoSEntranceType.OneWay, lambda state: any([
            oos_can_kill_spiked_beetle(state, player),
            all([
                oos_option_medium_logic(state, player),
                oos_can_flip_spiked_beetle(state, player),
                oos_has_bracelet(state, player)
            ])
        ])],

        ["d3 center", "d3 water room", OoSEntranceType.OneWay, lambda state: oos_has_feather(state, player)],
        ["d3 center", "d3 mimic stairs", OoSEntranceType.OneWay, lambda state: oos_has_bracelet(state, player)],
        ["d3 center", "trampoline owl", OoSEntranceType.OneWay, lambda state: all([
            oos_has_feather(state, player),
            oos_can_use_mystery_seeds(state, player)
        ])],
        ["d3 center", "d3 trampoline chest", OoSEntranceType.OneWay, lambda state: oos_has_feather(state, player)],
        ["d3 center", "d3 zol chest", OoSEntranceType.OneWay, lambda state: oos_has_feather(state, player)],

        ["d3 mimic stairs", "d3 water room", OoSEntranceType.TwoWay, None],
        ["d3 mimic stairs", "d3 roller chest", OoSEntranceType.OneWay, lambda state: oos_has_bracelet(state, player)],
        ["d3 mimic stairs", "d3 quicksand terrace", OoSEntranceType.OneWay, lambda state: oos_has_feather(state, player)],
        ["d3 mimic stairs", "omuai owl", OoSEntranceType.OneWay, lambda state: all([
            oos_has_feather(state, player),
            oos_can_use_mystery_seeds(state, player)
        ])],
        ["d3 mimic stairs", "d3 moldorm chest", OoSEntranceType.OneWay, lambda state: oos_can_kill_armored_enemy(state, player)],
        ["d3 mimic stairs", "d3 bombed wall chest", OoSEntranceType.OneWay, lambda state: oos_has_bombs(state, player)],

        # 2 keys
        ["d3 water room", "d3 mimic chest", OoSEntranceType.OneWay, lambda state: all([
            any([
                oos_has_small_keys(state, player, 3, 2),
                oos_self_locking_small_key(state, player, "d3 mimic chest", 3)
            ]),
            oos_can_kill_normal_enemy(state, player)
        ])],
        ["d3 mimic stairs", "d3 omuai stairs", OoSEntranceType.OneWay, lambda state: all([
            oos_has_feather(state, player),
            oos_has_small_keys(state, player, 3, 2),
            oos_has_bracelet(state, player),
            oos_can_kill_armored_enemy(state, player)
        ])],
        ["d3 omuai stairs", "d3 giant blade room", OoSEntranceType.OneWay, None],
        ["d3 omuai stairs", "d3 boss", OoSEntranceType.OneWay, lambda state: oos_has_boss_key(state, player, 3)],
    ]


def make_d4_logic(player: int):
    return [
        # 0 keys
        ["enter d4", "d4 north of entrance", OoSEntranceType.OneWay, lambda state: any([
            oos_has_flippers(state, player),
            oos_has_cape(state, player)
        ])],
        ["d4 north of entrance", "d4 pot puzzle", OoSEntranceType.OneWay, lambda state: all([
            oos_has_bombs(state, player),
            oos_has_bracelet(state, player)
        ])],
        ["d4 north of entrance", "d4 maze chest", OoSEntranceType.OneWay, lambda state: any([
            oos_can_trigger_lever_from_minecart(state, player),
            all([
                oos_option_hard_logic(state, player),
                oos_has_bracelet(state, player)
            ])
        ])],
        ["d4 maze chest", "d4 dark room", OoSEntranceType.OneWay, lambda state: oos_has_feather(state, player)],

        # 1 key
        ["enter d4", "d4 water ring room", OoSEntranceType.OneWay, lambda state: all([
            oos_has_small_keys(state, player, 4, 1),
            any([
                oos_has_cape(state, player),
                all([
                    # Feather is required to jump above spike lines
                    oos_has_feather(state, player),
                    oos_has_flippers(state, player)
                ])
            ]),
            oos_has_bombs(state, player),
            any([
                oos_can_kill_normal_enemy(state, player),
                all([  # killing enemies with pots
                    oos_option_medium_logic(state, player),
                    oos_has_bracelet(state, player),
                ]),
                all([  # pushing enemies in the water
                    oos_has_rod(state, player),
                    oos_has_boomerang(state, player)
                ])
            ])
        ])],

        ["enter d4", "d4 roller minecart", OoSEntranceType.OneWay, lambda state: all([
            oos_has_flippers(state, player),
            oos_has_small_keys(state, player, 4, 1),
            oos_has_feather(state, player)
        ])],

        ["d4 roller minecart", "d4 pool", OoSEntranceType.OneWay, lambda state: all([
            oos_has_flippers(state, player),
            any([
                oos_can_kill_normal_enemy(state, player),
                all([
                    oos_option_medium_logic(state, player),
                    oos_has_bracelet(state, player)
                ])
            ]),
            any([
                oos_can_trigger_lever_from_minecart(state, player),
                all([
                    oos_option_hard_logic(state, player),
                    oos_has_bracelet(state, player)
                ])
            ])
        ])],

        # 2 keys
        ["d4 roller minecart", "greater distance owl", OoSEntranceType.OneWay, lambda state: all([
            oos_has_small_keys(state, player, 4, 2),
            oos_can_use_mystery_seeds(state, player)
        ])],

        ["d4 roller minecart", "d4 stalfos stairs", OoSEntranceType.OneWay, lambda state: all([
            oos_has_small_keys(state, player, 4, 2),
            any([
                oos_can_kill_stalfos(state, player),
                all([
                    oos_option_medium_logic(state, player),
                    oos_has_bracelet(state, player)
                ])
            ])
        ])],

        ["d4 stalfos stairs", "d4 terrace", OoSEntranceType.OneWay, None],

        ["d4 stalfos stairs", "d4 torch chest", OoSEntranceType.OneWay, lambda state: all([
            oos_has_slingshot(state, player),
            oos_has_ember_seeds(state, player)
        ])],

        ["d4 stalfos stairs", "d4 miniboss room", OoSEntranceType.OneWay, None],
        ["d4 miniboss room", "d4 miniboss room wild embers", OoSEntranceType.OneWay, lambda state: \
            oos_can_harvest_regrowing_bush(state, player)],

        ["d4 miniboss room", "d4 final minecart", OoSEntranceType.OneWay, lambda state: all([
            oos_can_use_ember_seeds(state, player, False),
            oos_can_kill_armored_enemy(state, player)
        ])],

        # 5 keys
        ["d4 final minecart", "d4 cracked floor room", OoSEntranceType.OneWay, lambda state: any([
            oos_has_small_keys(state, player, 4, 5),
            oos_self_locking_small_key(state, player, "d4 cracked floor room", 4)
        ])],
        ["d4 final minecart", "d4 dive spot", OoSEntranceType.OneWay, lambda state: all([
            any([  # hit distant levers
                oos_has_magic_boomerang(state, player),
                oos_has_slingshot(state, player)
            ]),
            oos_can_jump_2_wide_pit(state, player),
            any([
                oos_has_small_keys(state, player, 4, 5),
                oos_self_locking_small_key(state, player, "d4 dive spot", 4)
            ]),
            oos_has_flippers(state, player)
        ])],

        ["d4 final minecart", "d4 basement stairs", OoSEntranceType.OneWay, lambda state: all([
            oos_has_small_keys(state, player, 4, 5),
            any([
                oos_has_boomerang(state, player),
                oos_has_slingshot(state, player),
                oos_option_hard_logic(state, player)
            ])
        ])],

        ["d4 basement stairs", "gohma owl", OoSEntranceType.OneWay, lambda state: oos_can_use_mystery_seeds(state, player)],

        ["d4 basement stairs", "enter gohma", OoSEntranceType.OneWay, lambda state: all([
            oos_has_boss_key(state, player, 4),
            any([
                all([
                    oos_has_slingshot(state, player),
                    oos_can_use_ember_seeds(state, player, True)
                ]),
                oos_can_jump_3_wide_pit(state, player),
                all([  # throw seeds using satchel during a jump
                    oos_option_hard_logic(state, player),
                    oos_has_feather(state, player),
                    oos_can_use_ember_seeds(state, player, False)
                ])
            ])
        ])],

        ["enter gohma", "d4 boss", OoSEntranceType.OneWay, lambda state: any([
            all([
                # Kill Gohma without breaking its pincer
                oos_option_medium_logic(state, player),
                any([
                    oos_has_slingshot(state, player),
                    oos_option_hard_logic(state, player)  # You can kill Gohma with the satchel. Yup...
                ]),
                any([
                    oos_has_scent_seeds(state, player),
                    oos_has_ember_seeds(state, player)
                ])
            ]),
            all([
                # Kill Gohma with sword beams (Gohma's minions give enough hearts to justify it)
                oos_option_medium_logic(state, player),
                any([
                    oos_has_noble_sword(state, player),
                    all([
                        oos_has_sword(state, player),
                        state.has("Energy Ring", player)
                    ])
                ])
            ]),
            all([
                # Kill Gohma traditionally (break pincer, then spam seeds)
                any([
                    oos_has_sword(state, player),
                    oos_has_fools_ore(state, player)
                ]),
                any([
                    oos_can_use_ember_seeds(state, player, False),
                    oos_can_use_scent_seeds(state, player),
                    all([
                        oos_option_medium_logic(state, player),
                        oos_has_satchel(state, player, 2),  # It may require quite a bunch of mystery seeds...
                        oos_can_use_mystery_seeds(state, player)
                    ])
                ])
            ])
        ])],
    ]


def make_d5_logic(player: int):
    return [
        # 0 keys
        ["enter d5", "d5 left chest", OoSEntranceType.OneWay, lambda state: any([
            oos_has_magnet_gloves(state, player),
            oos_has_cape(state, player),
            oos_can_jump_4_wide_pit(state, player),
        ])],

        ["enter d5", "d5 spiral chest", OoSEntranceType.OneWay, lambda state: any([
            oos_can_kill_armored_enemy(state, player),
            oos_has_shield(state, player)
        ])],

        ["enter d5", "d5 terrace chest", OoSEntranceType.OneWay, lambda state: oos_has_magnet_gloves(state, player)],

        ["d5 terrace chest", "armos knights owl", OoSEntranceType.OneWay, lambda state: oos_can_use_mystery_seeds(state, player)],
        ["d5 terrace chest", "d5 armos chest", OoSEntranceType.OneWay, lambda state: oos_can_kill_armored_enemy(state, player)],

        ["enter d5", "d5 cart bay", OoSEntranceType.OneWay, lambda state: all([
            oos_has_flippers(state, player),
            oos_can_jump_2_wide_liquid(state, player)
        ])],

        ["d5 cart bay", "d5 terrace chest", OoSEntranceType.OneWay, lambda state: all([
            oos_has_feather(state, player),
            oos_has_bombs(state, player)
        ])],

        ["d5 cart bay", "d5 cart chest", OoSEntranceType.OneWay, lambda state: oos_can_trigger_lever_from_minecart(state, player)],

        ["d5 cart bay", "d5 spinner chest", OoSEntranceType.OneWay, lambda state: any([
            oos_has_magnet_gloves(state, player),
            oos_can_jump_5_wide_pit(state, player)
        ])],

        ["d5 cart bay", "d5 drop ball", OoSEntranceType.OneWay, lambda state: all([
            oos_can_trigger_lever_from_minecart(state, player),
            any([
                oos_can_kill_armored_enemy(state, player),
                all([
                    oos_option_medium_logic(state, player),
                    oos_has_shield(state, player)
                ])
            ])
        ])],

        ["enter d5", "d5 pot room", OoSEntranceType.OneWay, lambda state: all([
            oos_has_magnet_gloves(state, player),
            oos_has_bombs(state, player),
            oos_has_feather(state, player)
        ])],

        ["d5 cart bay", "d5 pot room", OoSEntranceType.OneWay, lambda state: any([
            oos_has_feather(state, player),
            all([
                oos_option_hard_logic(state, player),
                oos_can_use_pegasus_seeds(state, player)
            ])
        ])],

        ["d5 pot room", "d5 gibdo/zol chest", OoSEntranceType.OneWay, lambda state: oos_can_kill_normal_enemy(state, player)],

        ["d5 cart bay", "d5 syger lobby", OoSEntranceType.OneWay, lambda state: any([
            oos_has_magnet_gloves(state, player),
            oos_has_cape(state, player),
        ])],
        ["d5 pot room", "d5 syger lobby", OoSEntranceType.OneWay, lambda state: any([
            oos_has_magnet_gloves(state, player),
            oos_has_cape(state, player),
        ])],

        ["d5 syger lobby", "d5 stalfos room", OoSEntranceType.OneWay, None],

        # 5 keys
        ["d5 syger lobby", "d5 post syger", OoSEntranceType.OneWay, lambda state: all([
            oos_has_small_keys(state, player, 5, 3),
            oos_can_kill_armored_enemy(state, player)
        ])],

        ["d5 pot room", "d5 magnet ball chest", OoSEntranceType.OneWay, lambda state: all([
            any([
                oos_has_flippers(state, player),
                oos_can_jump_6_wide_liquid(state, player),
                all([
                    oos_option_medium_logic(state, player),
                    oos_can_jump_3_wide_liquid(state, player),
                ])
            ]),
            any([
                oos_has_small_keys(state, player, 5, 5),
                oos_self_locking_small_key(state, player, "d5 magnet ball chest", 5)
            ])
        ])],

        ["d5 post syger", "d5 basement", OoSEntranceType.OneWay, lambda state: all([
            any([
                oos_has_small_keys(state, player, 5, 5),
                oos_self_locking_small_key(state, player, "d5 basement", 5)
            ]),
            state.has("_dropped_d5_magnet_ball", player),
            oos_has_magnet_gloves(state, player),
            any([
                oos_can_kill_magunesu(state, player),
                all([
                    oos_option_medium_logic(state, player),
                    oos_has_feather(state, player)
                ])
            ])
        ])],

        ["d5 post syger", "d5 boss", OoSEntranceType.OneWay, lambda state: all([
            oos_has_small_keys(state, player, 5, 5),
            oos_has_magnet_gloves(state, player),
            oos_has_boss_key(state, player, 5),
            any([
                oos_option_medium_logic(state, player),
                oos_has_feather(state, player)
            ]),
        ])],
    ]


def make_d6_logic(player: int):
    return [
        # 0 keys
        ["enter d6", "d6 1F east", OoSEntranceType.OneWay, lambda state: any([
            oos_has_feather(state, player),
            oos_has_sword(state, player),
            oos_has_bombs(state, player),
            oos_option_hard_logic(state, player)
        ])],

        ["d6 1F east", "d6 rupee room", OoSEntranceType.OneWay, lambda state: oos_has_bombs(state, player)],

        ["d6 1F east", "d6 1F terrace", OoSEntranceType.OneWay, None],
        ["enter d6", "d6 1F terrace", OoSEntranceType.OneWay, lambda state: all([
            oos_has_small_keys(state, player, 6, 2),
            oos_has_magnet_gloves(state, player)
        ])],

        ["d6 1F terrace", "d6 magnet ball drop", OoSEntranceType.OneWay, lambda state: any([
            all([
                oos_has_feather(state, player),
                oos_has_magnet_gloves(state, player)
            ]),
            oos_can_jump_4_wide_pit(state, player),
        ])],
        ["d6 1F terrace", "d6 crystal trap room", OoSEntranceType.OneWay, None],
        ["d6 1F terrace", "d6 U-room", OoSEntranceType.OneWay, lambda state: all([
            oos_can_break_crystal(state, player),
            oos_has_magic_boomerang(state, player)
        ])],
        ["d6 U-room", "d6 torch stairs", OoSEntranceType.OneWay, lambda state: all([
            any([
                # In easy, logic expects slingshot, but medium+ can expect satchel
                # as well since the distance between platforms & torches is a half-tile
                oos_has_slingshot(state, player),
                oos_option_medium_logic(state, player)
            ]),
            oos_can_use_ember_seeds(state, player, False)
        ])],

        ["d6 torch stairs", "d6 escape room", OoSEntranceType.OneWay, lambda state: oos_has_feather(state, player)],
        ["d6 escape room", "d6 vire chest", OoSEntranceType.OneWay, lambda state: oos_can_kill_stalfos(state, player)],

        # 3 keys
        ["enter d6", "d6 beamos room", OoSEntranceType.OneWay, lambda state: oos_has_small_keys(state, player, 6, 3)],
        ["d6 beamos room", "d6 2F gibdo chest", OoSEntranceType.OneWay, None],
        ["d6 beamos room", "d6 2F armos chest", OoSEntranceType.OneWay, lambda state: oos_has_bombs(state, player)],
        ["d6 2F armos chest", "d6 armos hall", OoSEntranceType.OneWay, lambda state: oos_has_feather(state, player)],

        ["enter d6", "d6 spinner north", OoSEntranceType.OneWay, lambda state: all([
            oos_can_break_crystal(state, player),
            oos_has_magnet_gloves(state, player),
            any([
                oos_has_small_keys(state, player, 6, 3),
                all([
                    oos_has_small_keys(state, player, 6, 2),
                    oos_has_feather(state, player),
                    oos_has_bombs(state, player)
                ])
            ])
        ])],

        ["d6 vire chest", "enter vire", OoSEntranceType.OneWay, lambda state: oos_has_small_keys(state, player, 6, 3)],
        ["enter vire", "d6 pre-boss room", OoSEntranceType.OneWay, lambda state: all([
            any([
                # Kill Vire
                oos_has_sword(state, player, False),
                oos_has_fools_ore(state, player),
                # state.has("expert's ring", player)
            ]),
            any([
                # Kill hardhats
                oos_has_magnet_gloves(state, player),
                all([
                    oos_option_medium_logic(state, player),
                    oos_has_gale_seeds(state, player),
                    any([
                        oos_has_slingshot(state, player),
                        all([
                            oos_option_hard_logic(state, player),
                            oos_has_satchel(state, player)
                        ])
                    ])
                ])
            ]),
            oos_has_feather(state, player)  # jump on trampoline
            # Switches here are considered trivial since we'll need magic boomerang for
            # Manhandla anyway
        ])],

        ["d6 pre-boss room", "d6 boss", OoSEntranceType.OneWay, lambda state: all([
            oos_has_boss_key(state, player, 6),
            oos_has_magic_boomerang(state, player),
            any([
                oos_has_sword(state, player),
                oos_has_fools_ore(state, player),
                oos_has_slingshot(state, player),
                # state.has("expert's ring", player)
            ])
        ])],
    ]


def make_d7_logic(player: int):
    return [
        # 0 keys
        ["enter d7", "poe curse owl", OoSEntranceType.OneWay, lambda state: oos_can_use_mystery_seeds(state, player)],
        ["enter d7", "d7 wizzrobe chest", OoSEntranceType.OneWay, lambda state: oos_can_kill_normal_enemy(state, player)],
        ["enter d7", "d7 bombed wall chest", OoSEntranceType.OneWay, lambda state: oos_has_bombs(state, player)],
        ["enter d7", "d7 entrance wild embers", OoSEntranceType.OneWay, lambda state: oos_can_harvest_regrowing_bush(state, player)],

        # 1 key
        ["enter d7", "enter poe A", OoSEntranceType.OneWay, lambda state: all([
            oos_has_small_keys(state, player, 7, 1),
            oos_has_slingshot(state, player),
            oos_can_use_ember_seeds(state, player, False)
        ])],

        ["enter poe A", "d7 pot room", OoSEntranceType.OneWay, lambda state: all([
            any([
                # Kill poe sister
                oos_can_kill_armored_enemy(state, player),
                oos_has_rod(state, player),
                oos_can_use_ember_seeds(state, player, False)
            ]),
            oos_has_bracelet(state, player)
        ])],
        ["enter d7", "d7 pot room", OoSEntranceType.OneWay, lambda state: all([
            # Poe skip
            oos_option_hard_logic(state, player),
            oos_has_bombs(state, player),
            oos_can_use_pegasus_seeds(state, player),
            oos_has_feather(state, player),
            oos_has_bracelet(state, player),
        ])],

        ["d7 pot room", "d7 zol button", OoSEntranceType.OneWay, lambda state: oos_has_feather(state, player)],
        ["d7 pot room", "d7 armos puzzle", OoSEntranceType.OneWay, lambda state: any([
            oos_can_jump_3_wide_pit(state, player),
            oos_has_magnet_gloves(state, player)
        ])],

        ["d7 armos puzzle", "d7 magunesu chest", OoSEntranceType.OneWay, lambda state: all([
            oos_can_jump_3_wide_pit(state, player),
            oos_can_kill_magunesu(state, player),
            oos_has_magnet_gloves(state, player)
        ])],

        # 2 keys
        ["d7 pot room", "d7 quicksand chest", OoSEntranceType.OneWay, lambda state: all([
            oos_has_small_keys(state, player, 7, 2),
            oos_has_feather(state, player)
        ])],

        # 3 keys
        ["d7 pot room", "enter poe B", OoSEntranceType.OneWay, lambda state: all([
            oos_has_small_keys(state, player, 7, 3),
            oos_can_use_ember_seeds(state, player, False),
            any([
                oos_can_use_pegasus_seeds(state, player),
                # Hard logic can do it without pegasus, it's very tight but doable
                oos_option_hard_logic(state, player)
            ])
        ])],

        ["enter poe B", "d7 water stairs", OoSEntranceType.OneWay, lambda state: oos_has_flippers(state, player)],

        ["d7 water stairs", "d7 darknut bridge trampolines", OoSEntranceType.OneWay, lambda state: any([
            all([
                # Boomerang to activate the switch then magnet gloves to go to the trampolines
                oos_has_magnet_gloves(state, player),
                oos_has_magic_boomerang(state, player)
            ]),
            all([
                oos_option_hard_logic(state, player),
                oos_has_feather(state, player),
                oos_has_magnet_gloves(state, player)
            ]),
        ])],
        ["d7 water stairs", "d7 past darknut bridge", OoSEntranceType.OneWay, lambda state: any([
            # Just jump to the other side directly
            oos_can_jump_4_wide_pit(state, player),

            all([
                oos_has_slingshot(state, player),
                oos_has_scent_seeds(state, player)
            ]),
            all([
                # Kill one darknut then pull the others with the magnet glove
                oos_has_magnet_gloves(state, player),
                any([
                    oos_can_kill_armored_enemy(state, player),
                    oos_has_shield(state, player),  # To push the darknut, the rod not really working
                    oos_option_medium_logic(state, player)
                    # Pull the right darknut by just going and stalling in the hole
                ])
            ]),
            all([
                oos_has_sword(state, player, False),
                state.has("Energy Ring", player),
            ])
        ])],
        ["d7 past darknut bridge", "d7 darknut bridge trampolines", OoSEntranceType.OneWay, lambda state: any([
            # Reach trampolines directly
            oos_can_jump_3_wide_pit(state, player),

            all([
                any([
                    # Trigger the spinner switch
                    oos_has_sword(state, player),
                    oos_has_fools_ore(state, player),
                    oos_has_rod(state, player),
                    oos_has_bombs(state, player)
                ]),
                # Reach trampolines using the magnet gloves
                oos_has_feather(state, player),
                oos_has_magnet_gloves(state, player)
            ])
        ])],

        ["d7 darknut bridge trampolines", "d7 spike chest", OoSEntranceType.OneWay, lambda state: oos_can_kill_stalfos(state, player)],

        # 4 keys
        ["d7 water stairs", "d7 maze chest", OoSEntranceType.OneWay, lambda state: all([
            oos_has_small_keys(state, player, 7, 4),
            oos_can_kill_armored_enemy(state, player),  # Moldorms are more restrictive than Poe sisters to kill
            oos_can_jump_3_wide_liquid(state, player),  # Technically not a liquid but a diagonal pit
        ])],

        ["d7 maze chest", "d7 B2F drop", OoSEntranceType.OneWay, lambda state: any([
            oos_has_magnet_gloves(state, player),
            all([
                # The jumps in this room being pretty intricate, precise and counterintuitive,
                # we chose to put that in hard logic only.
                oos_option_hard_logic(state, player),
                oos_can_jump_6_wide_pit(state, player)
            ])
        ])],

        # 5 keys
        ["d7 maze chest", "d7 stalfos chest", OoSEntranceType.OneWay, lambda state: all([
            any([
                oos_has_small_keys(state, player, 7, 5),
                oos_self_locking_small_key(state, player, "d7 stalfos chest", 7)
            ]),
            any([
                oos_can_jump_5_wide_pit(state, player),
                all([
                    oos_option_hard_logic(state, player),
                    oos_can_jump_1_wide_pit(state, player, False)
                ])
            ]),
            oos_can_kill_stalfos(state, player),
        ])],

        ["d7 stalfos chest", "shining blue owl", OoSEntranceType.OneWay, lambda state: oos_can_use_mystery_seeds(state, player)],

        ["enter d7", "d7 right of entrance", OoSEntranceType.OneWay, lambda state: all([
            any([
                oos_has_small_keys(state, player, 7, 5),
                all([
                    oos_has_small_keys(state, player, 7, 1),
                    oos_self_locking_small_key(state, player, "d7 right of entrance", 7)
                ])
            ]),
            oos_can_kill_normal_enemy(state, player)
        ])],

        ["d7 maze chest", "d7 boss", OoSEntranceType.OneWay, lambda state: all([
            oos_has_boss_key(state, player, 7),
            any([
                oos_has_sword(state, player),
                oos_has_fools_ore(state, player),
                # oos_can_punch(state, player)
            ])
        ])]
    ]


def make_d8_logic(player: int):
    return [
        # 0 keys
        ["enter d8", "d8 eye drop", OoSEntranceType.OneWay, lambda state: all([
            oos_can_break_pot(state, player),
            any([
                oos_has_slingshot(state, player),
                all([
                    oos_option_medium_logic(state, player),
                    oos_has_feather(state, player),
                    any([
                        oos_can_use_ember_seeds(state, player, False),
                        oos_can_use_scent_seeds(state, player),
                        oos_can_use_mystery_seeds(state, player),
                    ])
                ])
            ])
        ])],

        ["enter d8", "d8 three eyes chest", OoSEntranceType.OneWay, lambda state: all([
            oos_has_feather(state, player),
            any([
                oos_has_hyper_slingshot(state, player),
                all([
                    oos_option_hard_logic(state, player),
                    any([
                        oos_can_use_ember_seeds(state, player, False),
                        oos_can_use_scent_seeds(state, player),
                        oos_can_use_mystery_seeds(state, player),
                    ])
                ])
            ])
        ])],

        ["enter d8", "d8 hardhat room", OoSEntranceType.OneWay, lambda state: oos_can_kill_magunesu(state, player)],

        ["d8 hardhat room", "d8 hardhat drop", OoSEntranceType.OneWay, lambda state: any([
            all([
                oos_has_bombs(state, player),
                oos_has_magnet_gloves(state, player)
            ]),
            oos_can_use_gale_seeds_offensively(state, player)
        ])],

        # 1 key
        ["d8 hardhat room", "d8 spike room", OoSEntranceType.OneWay, lambda state: all([
            oos_has_small_keys(state, player, 8, 1),
            any([
                oos_has_cape(state, player),
                all([  # Tight 2D section jump is hard mode without cape
                    oos_option_hard_logic(state, player),
                    oos_has_feather(state, player),
                    oos_can_use_pegasus_seeds(state, player)
                ])
            ])
        ])],

        # 2 keys
        ["d8 spike room", "d8 spinner", OoSEntranceType.OneWay, lambda state: oos_has_small_keys(state, player, 8, 2)],
        ["d8 spinner", "silent watch owl", OoSEntranceType.OneWay, lambda state: oos_can_use_mystery_seeds(state, player)],
        ["d8 spinner", "d8 magnet ball room", OoSEntranceType.OneWay, None],
        ["d8 spinner", "d8 armos chest", OoSEntranceType.OneWay, lambda state: oos_has_magnet_gloves(state, player)],
        ["d8 armos chest", "d8 spinner chest", OoSEntranceType.OneWay, None],
        ["d8 spinner chest", "frypolar entrance", OoSEntranceType.OneWay, lambda state: oos_has_magnet_gloves(state, player)],
        ["frypolar entrance", "frypolar owl", OoSEntranceType.OneWay, lambda state: oos_can_use_mystery_seeds(state, player)],
        ["frypolar entrance", "d8 darknut chest", OoSEntranceType.OneWay, lambda state: all([
            any([
                oos_has_hyper_slingshot(state, player),
                all([
                    oos_option_hard_logic(state, player),
                    any([
                        oos_can_use_ember_seeds(state, player, False),
                        oos_can_use_scent_seeds(state, player),
                        oos_can_use_mystery_seeds(state, player),
                    ])
                ])
            ]),
            # oos_can_kill_armored_enemy(state, player),
            oos_has_bombs(state, player),
        ])],
        ["frypolar entrance", "frypolar room", OoSEntranceType.OneWay, lambda state: oos_has_small_keys(state, player, 8, 3)],
        ["frypolar room", "frypolar room wild mystery", OoSEntranceType.OneWay, lambda state: \
            oos_can_harvest_regrowing_bush(state, player)],

        # 3 keys
        ["frypolar room", "d8 ice puzzle room", OoSEntranceType.OneWay, lambda state: all([
            # Hard-require HSS since we need it in the room right after Frypolar to hit the torches anyway
            oos_has_hyper_slingshot(state, player),

            # Requirements to kill Frypolar
            any([
                all([
                    # Casual logic: mystery seeds method is considered mandatory since it's the easiest one
                    oos_has_mystery_seeds(state, player),
                    oos_has_bracelet(state, player)
                ]),
                all([
                    # Medium logic: allow killing Frypolar with ember only, but with at least a Lv2 satchel
                    # (the miniboss require 15 embers to die, so 20 max is a bit tight)
                    oos_option_medium_logic(state, player),
                    oos_can_use_ember_seeds(state, player, False),
                    oos_has_satchel(state, player, 2),
                ]),
                all([
                    # Hard logic: yolo
                    oos_option_hard_logic(state, player),
                    oos_can_use_ember_seeds(state, player, False)
                ]),
            ]),

            # Requirements to pass the room after Frypolar
            oos_can_use_ember_seeds(state, player, False),
        ])],

        ["d8 ice puzzle room", "d8 pols voice chest", OoSEntranceType.OneWay, lambda state: any([
            oos_has_magic_boomerang(state, player),
            oos_can_jump_6_wide_pit(state, player)
        ])],

        # 4 keys
        ["d8 ice puzzle room", "d8 crystal room", OoSEntranceType.OneWay, lambda state: oos_has_small_keys(state, player, 8, 4)],
        ["d8 crystal room", "magical ice owl", OoSEntranceType.OneWay, lambda state: oos_can_use_mystery_seeds(state, player)],
        ["d8 crystal room", "d8 ghost armos drop", OoSEntranceType.OneWay, lambda state: oos_has_bombs(state, player)],
        ["d8 crystal room", "d8 NE crystal", OoSEntranceType.OneWay, lambda state: all([
            oos_has_bracelet(state, player),
            oos_can_trigger_lever(state, player)
        ])],
        ["d8 crystal room", "d8 SE crystal", OoSEntranceType.OneWay, lambda state: oos_has_bracelet(state, player)],
        ["d8 crystal room", "d8 SW lava chest", OoSEntranceType.OneWay, None],
        ["d8 SE crystal", "d8 SE lava chest", OoSEntranceType.OneWay, None],

        ["d8 ice puzzle room", "d8 spark chest", OoSEntranceType.OneWay, lambda state: all([
            oos_has_small_keys(state, player, 8, 4),
            all([
                state.has("_dropped_d8_NE_crystal", player),
                state.has("_dropped_d8_SE_crystal", player),
                oos_can_break_pot(state, player)
            ])
        ])],

        # 6 keys
        ["d8 crystal room", "d8 NW crystal", OoSEntranceType.OneWay, lambda state: all([
            oos_has_bracelet(state, player),
            oos_has_small_keys(state, player, 8, 6)
        ])],
        ["d8 crystal room", "d8 SW crystal", OoSEntranceType.OneWay, lambda state: all([
            oos_has_bracelet(state, player),
            oos_has_small_keys(state, player, 8, 6)
        ])],

        # 7 keys
        ["d8 NW crystal", "d8 boss", OoSEntranceType.OneWay, lambda state: all([
            oos_has_small_keys(state, player, 8, 7),
            oos_has_boss_key(state, player, 8),
            any([
                oos_has_sword(state, player),
                oos_has_fools_ore(state, player)
            ])
        ])],
    ]
