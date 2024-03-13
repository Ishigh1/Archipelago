from worlds.tloz_oos.data.logic.LogicPredicates import *


def make_d0_logic(player: int):
    return [
        ["d0 entrance", "enter d0", True, None],

        # 0 keys
        ["enter d0", "d0 key chest", False, None],
        ["enter d0", "d0 rupee chest", False, lambda state: oos_can_break_bush(state, player, True)],
        ["enter d0", "d0 hidden 2d section", False, lambda state: any([
            oos_can_kill_normal_enemy(state, player),
            all([
                # Keese can be killed using boomerang as well, but that's kind of obscure so not in casual logic
                oos_option_medium_logic(state, player),
                oos_has_boomerang(state, player),
            ])
        ])],

        # 1 key
        ["enter d0", "d0 sword chest", False, lambda state: oos_has_small_keys(state, player, 0, 1)],
    ]


def make_d1_logic(player: int):
    return [
        # 0 keys
        ["enter d1", "d1 stalfos drop", False, lambda state: any([
            oos_can_kill_stalfos(state, player),
            all([
                # Medium logic expects the player to be able to use bushes
                oos_option_medium_logic(state, player),
                oos_has_bracelet(state, player)
            ])
        ])],

        ["enter d1", "d1 floormaster room", False, lambda state: oos_can_use_ember_seeds(state, player, True)],

        ["d1 floormaster room", "d1 boss", False, lambda state: all([
            oos_has_boss_key(state, player, 1),
            oos_can_kill_armored_enemy(state, player)
        ])],

        # 1 key
        ["enter d1", "d1 stalfos chest", False, lambda state: all([
            oos_has_small_keys(state, player, 1, 1),
            oos_can_kill_stalfos(state, player)
        ])],

        ["d1 stalfos chest", "d1 goriya chest", False, lambda state: any([
            oos_can_use_ember_seeds(state, player, True),
            oos_can_kill_normal_enemy(state, player, True)
        ])],

        ["d1 stalfos chest", "d1 lever room", False, None],

        ["d1 stalfos chest", "d1 block-pushing room", False, lambda state: any([
            oos_can_kill_normal_enemy(state, player),
            all([
                oos_option_hard_logic(state, player),
                oos_has_bracelet(state, player)
            ])
        ])],

        ["d1 stalfos chest", "d1 railway chest", False, lambda state: any([
            oos_can_trigger_lever(state, player),
            all([
                oos_option_hard_logic(state, player),
                oos_has_bracelet(state, player)
            ])
        ])],

        ["d1 railway chest", "d1 button chest", False, None],

        # 2 keys
        ["d1 railway chest", "d1 basement", False, lambda state: all([
            oos_has_bombs(state, player),
            oos_has_small_keys(state, player, 1, 2),
            oos_can_kill_armored_enemy(state, player)
        ])],
    ]


def make_d2_logic(player: int):
    return [
        # 0 keys
        ["enter d2", "d2 torch room", False, None],
        ["d2 torch room", "d2 left from entrance", False, None],
        ["d2 torch room", "d2 rope drop", False, lambda state: oos_can_kill_normal_enemy(state, player)],
        ["d2 torch room", "d2 arrow room", False, lambda state: oos_can_use_ember_seeds(state, player, True)],

        ["d2 arrow room", "d2 torch room", False, None],  # Backwards path
        ["d2 arrow room", "d2 rupee room", False, lambda state: oos_has_bombs(state, player)],
        ["d2 arrow room", "d2 rope chest", False, lambda state: oos_can_kill_normal_enemy(state, player)],
        ["d2 arrow room", "d2 blade chest", False, lambda state: oos_can_kill_normal_enemy(state, player)],

        ["d2 blade chest", "d2 arrow room", False, None],  # Backwards path
        ["d2 blade chest", "d2 alt entrances", True, lambda state: oos_has_bracelet(state, player)],
        ["d2 blade chest", "d2 roller chest", False, lambda state: all([
            oos_has_bombs(state, player),
            oos_has_bracelet(state, player),
        ])],
        ["d2 alt entrances", "d2 spiral chest", False, lambda state: all([
            oos_can_break_bush(state, player, False),
            oos_has_bombs(state, player),
        ])],

        # 2 keys
        ["d2 roller chest", "d2 spinner", False, lambda state: oos_has_small_keys(state, player, 2, 2)],
        ["d2 spinner", "dodongo owl", False, lambda state: oos_can_use_mystery_seeds(state, player)],
        ["d2 spinner", "d2 boss", False, lambda state: all([
            oos_has_boss_key(state, player, 2),
            oos_has_bombs(state, player),
            oos_has_bracelet(state, player)
        ])],

        # 3 keys
        ["d2 arrow room", "d2 hardhat room", False, lambda state: oos_has_small_keys(state, player, 2, 3)],
        ["d2 hardhat room", "d2 pot chest", False, lambda state: oos_can_break_pot(state, player)],
        ["d2 hardhat room", "d2 moblin chest", False, lambda state: any([
            all([
                oos_can_kill_d2_hardhat(state, player),
                oos_can_kill_d2_far_moblin(state, player)
            ])
        ])],
        ["d2 spinner", "d2 terrace chest", False, lambda state: oos_has_small_keys(state, player, 2, 3)],
    ]


def make_d3_logic(player: int):
    return [
        # 0 keys
        ["enter d3", "spiked beetles owl", False, lambda state: oos_can_use_mystery_seeds(state, player)],
        ["enter d3", "d3 center", False, lambda state: any([
            oos_can_kill_spiked_beetle(state, player),
            all([
                oos_option_medium_logic(state, player),
                oos_can_flip_spiked_beetle(state, player),
                oos_has_bracelet(state, player)
            ])
        ])],

        ["d3 center", "d3 water room", False, lambda state: oos_has_feather(state, player)],
        ["d3 center", "d3 mimic stairs", False, lambda state: oos_has_bracelet(state, player)],
        ["d3 center", "trampoline owl", False, lambda state: all([
            oos_has_feather(state, player),
            oos_can_use_mystery_seeds(state, player)
        ])],
        ["d3 center", "d3 trampoline chest", False, lambda state: oos_has_feather(state, player)],
        ["d3 center", "d3 zol chest", False, lambda state: oos_has_feather(state, player)],

        ["d3 mimic stairs", "d3 water room", True, None],
        ["d3 mimic stairs", "d3 roller chest", False, lambda state: oos_has_bracelet(state, player)],
        ["d3 mimic stairs", "d3 quicksand terrace", False, lambda state: oos_has_feather(state, player)],
        ["d3 mimic stairs", "omuai owl", False, lambda state: all([
            oos_has_feather(state, player),
            oos_can_use_mystery_seeds(state, player)
        ])],
        ["d3 mimic stairs", "d3 moldorm chest", False, lambda state: oos_can_kill_armored_enemy(state, player)],
        ["d3 mimic stairs", "d3 bombed wall chest", False, lambda state: oos_has_bombs(state, player)],

        # 2 keys
        ["d3 water room", "d3 mimic chest", False, lambda state: all([
            oos_has_small_keys(state, player, 3, 2),
            oos_can_kill_normal_enemy(state, player)
        ])],
        ["d3 mimic stairs", "d3 omuai stairs", False, lambda state: all([
            oos_has_feather(state, player),
            oos_has_small_keys(state, player, 3, 2),
            oos_has_bracelet(state, player),
            oos_can_kill_armored_enemy(state, player)
        ])],
        ["d3 omuai stairs", "d3 giant blade room", False, None],
        ["d3 omuai stairs", "d3 boss", False, lambda state: oos_has_boss_key(state, player, 3)],
    ]


def make_d4_logic(player: int):
    return [
        # 0 keys
        ["enter d4", "d4 north of entrance", False, lambda state: any([
            oos_has_flippers(state, player),
            oos_has_cape(state, player)
        ])],
        ["d4 north of entrance", "d4 pot puzzle", False, lambda state: all([
            oos_has_bombs(state, player),
            oos_has_bracelet(state, player)
        ])],
        ["d4 north of entrance", "d4 maze chest", False, lambda state: any([
            oos_can_trigger_lever_from_minecart(state, player),
            all([
                oos_option_hard_logic(state, player),
                oos_has_bracelet(state, player)
            ])
        ])],
        ["d4 maze chest", "d4 dark room", False, lambda state: oos_has_feather(state, player)],

        # 1 key
        ["enter d4", "d4 water ring room", False, lambda state: all([
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
                    oos_has_boomerang(state, player)  # TODO: oos_can_push_enemy?
                ])
            ])
        ])],

        ["enter d4", "d4 roller minecart", False, lambda state: all([
            oos_has_flippers(state, player),  # TODO: Medium logic, cape + pegasus => 6-wide liquid?
            oos_has_small_keys(state, player, 4, 1),
            oos_has_feather(state, player)
        ])],

        ["d4 roller minecart", "d4 pool", False, lambda state: all([
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
        ["d4 roller minecart", "greater distance owl", False, lambda state: all([
            oos_has_small_keys(state, player, 4, 2),
            oos_can_use_mystery_seeds(state, player)
        ])],

        ["d4 roller minecart", "d4 stalfos stairs", False, lambda state: all([
            oos_has_small_keys(state, player, 4, 2),
            any([
                oos_can_kill_stalfos(state, player),
                all([
                    oos_option_medium_logic(state, player),
                    oos_has_bracelet(state, player)
                ])
            ])
        ])],

        ["d4 stalfos stairs", "d4 terrace", False, None],

        ["d4 stalfos stairs", "d4 final minecart", False, lambda state: all([
            oos_can_use_ember_seeds(state, player, False),
            oos_can_kill_armored_enemy(state, player)
        ])],

        ["d4 stalfos stairs", "d4 torch chest", False, lambda state: all([
            oos_has_slingshot(state, player),
            oos_has_ember_seeds(state, player)
        ])],

        # 5 keys
        ["d4 final minecart", "d4 cracked floor room", False, lambda state: oos_has_small_keys(state, player, 4, 5)],
        ["d4 final minecart", "d4 dive spot", False, lambda state: all([
            any([  # hit distant levers
                oos_has_magic_boomerang(state, player),
                oos_has_slingshot(state, player)
            ]),
            oos_can_jump_2_wide_pit(state, player),
            oos_has_small_keys(state, player, 4, 5),
            oos_has_flippers(state, player)
        ])],

        ["d4 cracked floor room", "d4 basement stairs", False, lambda state: any([
            oos_has_boomerang(state, player),
            oos_has_slingshot(state, player),
            oos_option_hard_logic(state, player)
        ])],

        ["d4 basement stairs", "gohma owl", False, lambda state: oos_can_use_mystery_seeds(state, player)],

        ["d4 basement stairs", "enter gohma", False, lambda state: all([
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
                    oos_can_use_ember_seeds(state, player, True)
                ])
            ])
        ])],

        ["enter gohma", "d4 boss", False, lambda state: any([
            all([
                # kill with pincer
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
            # kill after destroying pincer
            all([
                # With a sword's laser
                oos_option_medium_logic(state, player),
                any([
                    oos_has_noble_sword(state, player), # Gohma's minions give enough hearts to justify it
                    all([
                        oos_has_sword(state, player),
                        state.has("Energy Ring", player)
                    ])
                ])
            ]),
            all([
                any([
                    oos_has_sword(state, player),
                    oos_has_fools_ore(state, player)
                ]),
                any([
                    oos_can_use_ember_seeds(state, player, False),
                    oos_can_use_scent_seeds(state, player),
                    all([
                        oos_option_medium_logic(state, player),
                        oos_can_use_mystery_seeds(state, player)
                    ])
                ])
            ])
        ])],
    ]


def make_d5_logic(player: int):
    return [
        # 0 keys
        ["enter d5", "d5 left chest", False, lambda state: any([
            oos_has_magnet_gloves(state, player),
            oos_has_cape(state, player),
            oos_can_jump_4_wide_pit(state, player),
            all([
                oos_option_medium_logic(state, player),
                oos_can_jump_3_wide_liquid(state, player),
                # Not a liquid, but technically equivalent
            ])
        ])],

        ["enter d5", "d5 spiral chest", False, lambda state: any([
            oos_can_kill_armored_enemy(state, player),
            oos_has_shield(state, player)
        ])],

        ["enter d5", "d5 terrace chest", False, lambda state: oos_has_magnet_gloves(state, player)],

        ["d5 terrace chest", "armos knights owl", False, lambda state: oos_can_use_mystery_seeds(state, player)],
        ["d5 terrace chest", "d5 armos chest", False, lambda state: oos_can_kill_armored_enemy(state, player)],

        ["enter d5", "d5 cart bay", False, lambda state: all([
            oos_has_flippers(state, player),
            oos_can_jump_2_wide_liquid(state, player)
        ])],

        ["d5 cart bay", "d5 terrace chest", False, lambda state: all([
            oos_has_feather(state, player),
            oos_has_bombs(state, player)
        ])],

        ["d5 cart bay", "d5 cart chest", False, lambda state: oos_can_trigger_lever_from_minecart(state, player)],

        ["enter d5", "d5 pot room", False, lambda state: all([
            oos_has_magnet_gloves(state, player),
            oos_has_bombs(state, player),
            oos_has_feather(state, player)
        ])],

        ["d5 cart bay", "d5 spinner chest", False, lambda state: any([
            oos_has_magnet_gloves(state, player),
            oos_can_jump_5_wide_pit(state, player)
        ])],

        ["d5 cart bay", "d5 drop ball", False, lambda state: all([
            oos_can_trigger_lever_from_minecart(state, player),
            any([
                oos_can_kill_armored_enemy(state, player),
                all([
                    oos_option_medium_logic(state, player),
                    oos_has_shield(state, player)
                ])
            ])
        ])],

        ["d5 cart bay", "d5 pot room", False, lambda state: any([
            oos_has_feather(state, player),
            all([
                oos_option_hard_logic(state, player),
                oos_can_use_pegasus_seeds(state, player)
            ])
        ])],

        ["d5 pot room", "d5 gibdo/zol chest", False, lambda state: oos_can_kill_normal_enemy(state, player)],

        ["d5 cart bay", "d5 stalfos room", False, lambda state: any([
            oos_has_magnet_gloves(state, player),
            oos_has_cape(state, player),
        ])],

        ["d5 pot room", "d5 stalfos room", False, lambda state: any([
            oos_has_magnet_gloves(state, player),
            oos_has_cape(state, player),
        ])],

        # 5 keys
        ["d5 pot room", "d5 magnet ball chest", False, lambda state: all([
            any([
                oos_has_flippers(state, player),
                oos_can_jump_6_wide_liquid(state, player),
                all([
                    oos_option_medium_logic(state, player),
                    oos_can_jump_3_wide_liquid(state, player),
                ])
            ]),
            oos_has_small_keys(state, player, 5, 5),
        ])],

        ["d5 pot room", "d5 post syger", False, lambda state: all([
            oos_has_small_keys(state, player, 5, 5),
            oos_can_kill_armored_enemy(state, player)
        ])],

        ["d5 post syger", "d5 basement", False, lambda state: all([
            oos_has_small_keys(state, player, 5, 5),
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

        ["d5 post syger", "d5 boss", False, lambda state: all([
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
        ["enter d6", "d6 1F east", False, lambda state: any([
            oos_has_feather(state, player),
            oos_has_sword(state, player),
            oos_has_bombs(state, player),
            oos_option_hard_logic(state, player)
        ])],

        ["d6 1F east", "d6 rupee room", False, lambda state: oos_has_bombs(state, player)],

        ["d6 1F east", "d6 1F terrace", False, None],
        ["enter d6", "d6 1F terrace", False, lambda state: all([
            oos_has_small_keys(state, player, 6, 2),
            oos_has_magnet_gloves(state, player)
        ])],

        ["d6 1F terrace", "d6 magnet ball drop", False, lambda state: any([
            all([
                oos_has_feather(state, player),
                oos_has_magnet_gloves(state, player)
            ]),
            oos_can_jump_4_wide_pit(state, player),
        ])],
        ["d6 1F terrace", "d6 crystal trap room", False, None],
        ["d6 1F terrace", "d6 U-room", False, lambda state: all([
            oos_can_break_crystal(state, player),
            oos_has_magic_boomerang(state, player)
        ])],
        ["d6 U-room", "d6 torch stairs", False, lambda state: all([
            any([
                # In easy, logic expects slingshot, but medium+ can expect satchel
                # as well since the distance between platforms & torches is a half-tile
                oos_has_slingshot(state, player),
                oos_option_medium_logic(state, player)
            ]),
            oos_can_use_ember_seeds(state, player, True)
        ])],

        ["d6 torch stairs", "d6 escape room", False, lambda state: oos_has_feather(state, player)],
        ["d6 escape room", "d6 vire chest", False, lambda state: oos_can_kill_stalfos(state, player)],

        # 3 keys
        ["enter d6", "d6 beamos room", False, lambda state: oos_has_small_keys(state, player, 6, 3)],
        ["d6 beamos room", "d6 2F gibdo chest", False, None],
        ["d6 beamos room", "d6 2F armos chest", False, lambda state: oos_has_bombs(state, player)],
        ["d6 2F armos chest", "d6 armos hall", False, lambda state: oos_has_feather(state, player)],

        ["enter d6", "d6 spinner north", False, lambda state: all([
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

        ["d6 vire chest", "enter vire", False, lambda state: oos_has_small_keys(state, player, 6, 3)],
        ["enter vire", "d6 pre-boss room", False, lambda state: all([
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

        ["d6 pre-boss room", "d6 boss", False, lambda state: all([
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
        ["enter d7", "poe curse owl", False, lambda state: oos_can_use_mystery_seeds(state, player)],
        ["enter d7", "d7 wizzrobe chest", False, lambda state: oos_can_kill_normal_enemy(state, player)],
        ["enter d7", "d7 bombed wall chest", False, lambda state: oos_has_bombs(state, player)],

        # 1 key
        ["enter d7", "enter poe A", False, lambda state: all([
            oos_has_small_keys(state, player, 7, 1),
            oos_has_slingshot(state, player),
            oos_can_use_ember_seeds(state, player, True)
        ])],

        ["enter poe A", "d7 pot room", False, lambda state: all([
            any([
                # Kill poe sister
                oos_can_kill_armored_enemy(state, player),
                oos_has_rod(state, player),
                oos_can_use_ember_seeds(state, player, False)
            ]),
            oos_has_bracelet(state, player)
        ])],
        ["enter d7", "d7 pot room", False, lambda state: all([
            # Poe skip
            oos_option_hard_logic(state, player),
            oos_has_bombs(state, player),
            oos_can_use_pegasus_seeds(state, player),
            oos_has_feather(state, player),
            oos_has_bracelet(state, player),
        ])],

        ["d7 pot room", "d7 zol button", False, lambda state: oos_has_feather(state, player)],
        ["d7 pot room", "d7 armos puzzle", False, lambda state: any([
            oos_can_jump_3_wide_pit(state, player),
            oos_has_magnet_gloves(state, player)
        ])],

        ["d7 armos puzzle", "d7 magunesu chest", False, lambda state: all([
            oos_can_jump_3_wide_pit(state, player),
            oos_can_kill_magunesu(state, player),
            oos_has_magnet_gloves(state, player)
        ])],

        # 2 keys
        ["d7 pot room", "d7 quicksand chest", False, lambda state: all([
            oos_has_small_keys(state, player, 7, 2),
            oos_has_feather(state, player)
        ])],

        # 3 keys
        ["d7 pot room", "enter poe B", False, lambda state: all([
            oos_has_small_keys(state, player, 7, 3),
            oos_can_use_ember_seeds(state, player, False),
            any([
                oos_can_use_pegasus_seeds(state, player),
                oos_has_hyper_slingshot(state, player),
                oos_option_hard_logic(state, player)
            ])
        ])],

        ["enter poe B", "d7 water stairs", False, lambda state: oos_has_flippers(state, player)],

        ["d7 water stairs", "d7 darknut bridge trampolines", False, lambda state: any([
            oos_has_cape(state, player),
            all([
                oos_option_hard_logic(state, player),
                oos_has_feather(state, player),
                oos_has_magnet_gloves(state, player)
            ]),
        ])],
        ["d7 water stairs", "d7 past darknut bridge", False, lambda state: any([
            all([
                oos_has_slingshot(state, player),
                oos_has_scent_seeds(state, player)
            ]),
            oos_has_magnet_gloves(state, player),
            all([
                oos_has_sword(state, player, False),
                state.has("Energy Ring", player),
            ])
        ])],
        ["d7 past darknut bridge", "d7 darknut bridge trampolines", False, lambda state: any([
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

        ["d7 darknut bridge trampolines", "d7 spike chest", False, lambda state: oos_can_kill_stalfos(state, player)],

        # 4 keys
        ["d7 water stairs", "d7 maze chest", False, lambda state: all([
            oos_has_small_keys(state, player, 7, 4),
            oos_can_kill_armored_enemy(state, player),  # Moldorms are more restrictive than Poe sisters to kill
            oos_can_jump_3_wide_liquid(state, player),  # Technically not a liquid but a diagonal pit
        ])],

        ["d7 maze chest", "d7 B2F drop", False, lambda state: any([
            oos_has_magnet_gloves(state, player),
            all([
                oos_option_medium_logic(state, player),
                oos_can_jump_6_wide_pit(state, player)
            ])
        ])],

        # 5 keys
        ["d7 maze chest", "d7 stalfos chest", False, lambda state: all([
            oos_has_small_keys(state, player, 7, 5),
            any([
                oos_can_jump_5_wide_pit(state, player),
                all([
                    oos_option_hard_logic(state, player),
                    oos_can_jump_1_wide_pit(state, player, False)
                ])
            ]),
            oos_can_kill_stalfos(state, player),
        ])],

        ["d7 stalfos chest", "shining blue owl", False, lambda state: oos_can_use_mystery_seeds(state, player)],

        ["enter d7", "d7 right of entrance", False, lambda state: oos_has_small_keys(state, player, 7, 5)],

        ["d7 maze chest", "d7 boss", False, lambda state: all([
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
        ["enter d8", "d8 eye drop", False, lambda state: all([
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

        ["enter d8", "d8 three eyes chest", False, lambda state: all([
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

        ["enter d8", "d8 hardhat room", False, lambda state: oos_can_kill_magunesu(state, player)],

        ["d8 hardhat room", "d8 hardhat drop", False, lambda state: any([
            all([
                oos_has_bombs(state, player),
                oos_has_magnet_gloves(state, player)
            ]),
            oos_can_use_gale_seeds_offensively(state, player)
        ])],

        # 1 key
        ["d8 hardhat room", "d8 spike room", False, lambda state: all([
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
        ["d8 spike room", "d8 spinner", False, lambda state: oos_has_small_keys(state, player, 8, 2)],
        ["d8 spinner", "silent watch owl", False, lambda state: oos_can_use_mystery_seeds(state, player)],
        ["d8 spinner", "d8 magnet ball room", False, None],
        ["d8 spinner", "d8 armos chest", False, lambda state: oos_has_magnet_gloves(state, player)],
        ["d8 armos chest", "d8 spinner chest", False, None],
        ["d8 spinner chest", "frypolar entrance", False, lambda state: oos_has_magnet_gloves(state, player)],
        ["frypolar entrance", "frypolar owl", False, lambda state: oos_can_use_mystery_seeds(state, player)],
        ["frypolar entrance", "d8 darknut chest", False, lambda state: all([
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

        # 3 keys
        ["frypolar entrance", "d8 ice puzzle room", False, lambda state: all([
            oos_has_small_keys(state, player, 8, 3),
            # Frypolar can be killed many ways, but we need HSS + ember seeds in the room
            # right after anyway...
            oos_has_hyper_slingshot(state, player),
            oos_can_use_ember_seeds(state, player, False)
        ])],

        ["d8 ice puzzle room", "d8 pols voice chest", False, lambda state: any([
            oos_has_magic_boomerang(state, player),
            oos_can_jump_6_wide_pit(state, player)
        ])],

        # 4 keys
        ["d8 ice puzzle room", "d8 crystal room", False, lambda state: oos_has_small_keys(state, player, 8, 4)],
        ["d8 crystal room", "magical ice owl", False, lambda state: oos_can_use_mystery_seeds(state, player)],
        ["d8 crystal room", "d8 ghost armos drop", False, lambda state: oos_has_bombs(state, player)],
        ["d8 crystal room", "d8 NE crystal", False, lambda state: all([
            oos_has_bracelet(state, player),
            oos_can_trigger_lever(state, player)
        ])],
        ["d8 crystal room", "d8 SE crystal", False, lambda state: oos_has_bracelet(state, player)],
        ["d8 crystal room", "d8 SW lava chest", False, None],
        ["d8 SE crystal", "d8 SE lava chest", False, None],

        ["d8 ice puzzle room", "d8 spark chest", False, lambda state: all([
            oos_has_small_keys(state, player, 8, 4),
            all([
                state.has("_dropped_d8_NE_crystal", player),
                state.has("_dropped_d8_SE_crystal", player),
                oos_can_break_pot(state, player)
            ])
        ])],

        # 6 keys
        ["d8 crystal room", "d8 NW crystal", False, lambda state: all([
            oos_has_bracelet(state, player),
            oos_has_small_keys(state, player, 8, 6)
        ])],
        ["d8 crystal room", "d8 SW crystal", False, lambda state: all([
            oos_has_bracelet(state, player),
            oos_has_small_keys(state, player, 8, 6)
        ])],

        # 7 keys
        ["d8 NW crystal", "d8 boss", False, lambda state: all([
            oos_has_small_keys(state, player, 8, 7),
            oos_has_boss_key(state, player, 8),
            any([
                oos_has_sword(state, player),
                oos_has_fools_ore(state, player)
            ])
        ])],
    ]
