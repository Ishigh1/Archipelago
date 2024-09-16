from ..data.Constants import *

EOB_ADDR = [
    0x3ec8,  # 00
    0x3e89,  # 01
    0x35bb,  # 02
    0x3dd7,  # 03
    0x3e12,  # 04
    0x3e2d,  # 05
    0x3864,  # 06 - 128 bytes reserved for sprite expansion w/ web patcher
    0x3900,  # 07
    0x3fc0,  # 08
    0x3f4e,  # 09
    0x3bf9,  # 0a
    0x3f6d,  # 0b
    0x3ea1,  # 0c
    0x3b82,  # 0d
    0x3ef3,  # 0e
    0x3f9d,  # 0f
    0x3bee,  # 10
    0x3eb0,  # 11
    0x3c8f,  # 12
    0x3bd2,  # 13
    0x2fc9,  # 14 - ton of free space here
    0x392d,  # 15
    0x3a07,  # 16
    0x3f3a,  # 17
    0x3e6d,  # 18
    0x36e1,  # 19
    0x30f0,  # 1a - here too
    0x3c40,  # 1b
    0x4000,  # 1c
    0x4000,  # 1d
    0x4000,  # 1e
    0x4000,  # 1f
    0x4000,  # 20
    0x4000,  # 21
    0x4000,  # 22
    0x4000,  # 23
    0x4000,  # 24
    0x4000,  # 25
    0x4000,  # 26
    0x4000,  # 27
    0x4000,  # 28
    0x4000,  # 29
    0x4000,  # 2a
    0x4000,  # 2b
    0x4000,  # 2c
    0x4000,  # 2d
    0x4000,  # 2e
    0x4000,  # 2f
    0x4000,  # 30
    0x4000,  # 31
    0x4000,  # 32
    0x4000,  # 33
    0x4000,  # 34
    0x4000,  # 35
    0x4000,  # 36
    0x4000,  # 37
    0x3df0,  # 38
    0x4000,  # 39
    0x4000,  # 3a
    0x4000,  # 3b
    0x4000,  # 3c
    0x4000,  # 3d
    0x4000,  # 3e
    0x314b,  # 3f - also here

    # New banks
    0x0750,  # 40 - rounded up to leave room for more warps, subject to change
]

DEFINES = {
    # WRAM addresses
    "wSubscreen1CurrentSlotIndex": "$c085",
    "wOriginalMinimapGroup": "$c09d",  # Custom address
    "wOriginalDungeonIndex": "$c09e",  # Custom address
    "wMinimapCycleToNextMode": "$c09f",  # Custom address
    "wKeysPressed": "$c481",
    "wKeysJustPressed": "$c482",
    "wPaletteThread_mode": "$c4ab",
    "wCustomBuffer": "$c4bf",  # Custom address
    "wAnimalRegion": "$c610",
    "wRingsObtained": "$c616",
    "wTotalSignsDestroyed": "$c626",
    "wDeathRespawnBuffer": "$c62b",
    "wMinimapGroup": "$c63a",
    "wBoughtShopItems2": "$c640",
    "wBoughtSubrosianItems": "$c642",
    "wDimitriState": "$c644",
    "wAnimalTutorialFlags": "$c646",
    "wGashaSpotFlags": "$c649",
    "wDungeonCompasses": "$c67c",
    "wDungeonMaps": "$c67e",
    "wObtainedTreasureFlags": "$c692",
    "wNetCountIn": "$c6a0",
    "wLinkMaxHealth": "$c6a3",
    "wCurrentBombs": "$c6aa",
    "wMaxBombs": "$c6ab",
    "wSeedSatchelLevel": "$c6ae",
    "wFluteIcon": "$c6af",
    "wFeatherLevel": "$c6b4",
    "wNumEmberSeeds": "$c6b5",
    "wEssencesObtained": "$c6bb",
    "wSatchelSelectedSeeds": "$c6be",
    "wActiveRing": "$c6c5",
    "wRingBoxLevel": "$c6c6",
    "wInsertedJewels": "$c6e1",
    "wTextIndexL": "$cba2",
    "wTextIndexH": "$cba3",
    "wTextNumberSubstitution": "$cba8",
    "wDungeonMapScroll": "$cbb4",
    "wMapMenuMode": "$cbb3",
    "wMapMenuCursorIndex": "$cbb6",
    "wMenuLoadState": "$cbcc",
    "wMenuActiveState": "$cbcd",
    "wDungeonMapScrollState": "$cbce",
    "wInventorySubmenu1CursorPos": "$cbd1",
    "wRingMenu_mode": "$cbd3",
    "wStatusBarNeedsRefresh": "$cbea",
    "wNetTreasureIn": "$cbfb",  # Custom address
    "wFrameCounter": "$cc00",
    "wIsLinkedGame": "$cc01",
    "wMenuDisabled": "$cc02",
    "wLinkDeathTrigger": "$cc34",
    "wRememberedCompanionRoom": "$cc42",
    "wRememberedCompanionY": "$cc43",
    "wLinkObjectIndex": "$cc48",
    "wActiveGroup": "$cc49",
    "wActiveRoom": "$cc4c",
    "wActiveRoomPack": "$cc4d",
    "wRoomStateModifier": "$cc4e",
    "wLostWoodsTransitionCounter1": "$cc53",
    "wLostWoodsTransitionCounter2": "$cc54",
    "wDungeonIndex": "$cc55",
    "wDungeonFloor": "$cc57",
    "wWarpDestGroup": "$cc63",
    "wWarpDestRoom": "$cc64",
    "wWarpTransition": "$cc65",
    "wWarpDestPos": "$cc66",
    "wWarpTransition2": "$cc67",
    "wLinkGrabState": "$cc75",
    "wLinkSwimmingState": "$cc78",
    "wLinkImmobilized": "$cc7c",
    "wDisabledObjects": "$cca4",
    "wDisableWarpTiles": "$ccaa",
    "wScreenTransitionDirection": "$cd02",
    "wScreenOffsetY": "$cd08",

    "w1Link.yh": "$d00b",
    "w7ActiveBank": "$d0d4",

    # High RAM offsets (FF00 + offset)
    "hRomBank": "$97",

    # Bank 0 functions
    "addAToDe": "$0068",
    "interBankCall": "$008a",
    "getNumSetBits": "$0176",
    "checkFlag": "$0205",
    "setFlag": "$020e",
    "decHlRef16WithCap": "$0237",
    "disableLcd": "$02c1",
    "getRandomNumber": "$041a",
    "queueDmaTransfer": "$0566",
    "loadUncompressedGfxHeader": "$05b6",
    "forceEnableIntroInputs": "$0862",
    "saveFile": "$09b4",
    "playSound": "$0c74",
    "setMusicVolume": "$0c89",
    "giveTreasure": "$16eb",
    "loseTreasure": "$1702",
    "checkTreasureObtained": "$1717",
    "refillSeedSatchel": "$17e5",
    "showTextNonExitable": "$1847",
    "showText": "$184b",
    "getThisRoomFlags": "$1956",
    "getRoomFlags": "$1963",
    "openMenu": "$1a76",
    "linkInteractWithAButtonSensitiveObjects": "$1b23",
    "lookupKey": "$1dc4",
    "lookupCollisionTable": "$1ddd",
    "objectSetVisiblec2": "$1e03",
    "objectSetInvisible": "$1e39",
    "convertShortToLongPosition": "$2089",
    "objectCopyPosition": "$21fd",
    "objectCopyPosition_rawAddress": "$2202",
    "interactionIncState": "$239b",
    "interactionSetScript": "$24fe",
    "createTreasure": "$271b",
    "setLinkIdOverride": "$2a16",
    "clearStaticObjects": "$3076",
    "checkGlobalFlag": "$30c7",
    "setGlobalFlag": "$30cd",
    "fastFadeoutToWhite": "$313b",
    "loadScreenMusicAndSetRoomPack": "$32dc",
    "setTile": "$3a52",
    "getFreeInteractionSlot": "$3ac6",
    "interactionDelete": "$3ad9",
    "getFreePartSlot": "$3ea7",

    # Byte constants
    "STARTING_TREE_MAP_INDEX": "$f8",
    "INTERACID_TREASURE": "$60",
    "BTN_A": "$01",
    "BTN_B": "$02",
    "BTN_START": "$08",
    "BTN_RIGHT": "$10",
    "BTN_LEFT": "$20",
    "BTN_UP": "$40",
    "BTN_DOWN": "$80",
    "COLLECT_PICKUP": "$0a",
    "COLLECT_PICKUP_NOFLAG": "$02",
    "COLLECT_CHEST": "$38",
    "COLLECT_CHEST_NOFLAG": "$30",
    # "COLLECT_CHEST_MAP_OR_COMPASS": "$68",
    "COLLECT_FALL": "$29",
    "COLLECT_FALL_KEY": "$28",

    "SND_SOLVEPUZZLE_2": "$5b",
    "SND_GETSEED": "$5e",
    "SND_TELEPORT": "$8d",
    "SND_COMPASS": "$a2",

    "SEASON_SPRING": "$00",
    "SEASON_SUMMER": "$01",
    "SEASON_AUTUMN": "$02",
    "SEASON_WINTER": "$03",

    "TREASURE_SHIELD": "$01",
    "TREASURE_PUNCH": "$02",
    "TREASURE_BOMBS": "$03",
    "TREASURE_SWORD": "$05",
    "TREASURE_BOOMERANG": "$06",
    "TREASURE_ROD_OF_SEASONS": "$07",
    "TREASURE_MAGNET_GLOVES": "$08",
    "TREASURE_FLUTE": "$0e",
    "TREASURE_SLINGSHOT": "$13",
    "TREASURE_BRACELET": "$16",
    "TREASURE_FEATHER": "$17",
    "TREASURE_SEED_SATCHEL": "$19",
    "TREASURE_FOOLS_ORE": "$1e",
    "TREASURE_EMBER_SEEDS": "$20",
    "TREASURE_SCENT_SEEDS": "$21",
    "TREASURE_PEGASUS_SEEDS": "$22",
    "TREASURE_GALE_SEEDS": "$23",
    "TREASURE_MYSTERY_SEEDS": "$24",
    "TREASURE_PIRATES_BELL": "$25",  # Rando specific ID
    "TREASURE_RUPEES": "$28",
    "TREASURE_HEART_REFILL": "$29",
    "TREASURE_HEART_CONTAINER": "$2a",
    "TREASURE_RING": "$2d",
    "TREASURE_FLIPPERS": "$2e",
    "TREASURE_POTION": "$2f",
    "TREASURE_SMALL_KEY": "$30",
    "TREASURE_BOSS_KEY": "$31",
    "TREASURE_COMPASS": "$32",
    "TREASURE_MAP": "$33",
    "TREASURE_GASHA_SEED": "$34",
    "TREASURE_MAKU_SEED": "$36",
    "TREASURE_ORE_CHUNKS": "$37",
    "TREASURE_ESSENCE": "$40",
    "TREASURE_GNARLED_KEY": "$42",
    "TREASURE_FLOODGATE_KEY": "$43",
    "TREASURE_DRAGON_KEY": "$44",
    "TREASURE_STAR_ORE": "$45",
    "TREASURE_RIBBON": "$46",
    "TREASURE_SPRING_BANANA": "$47",
    "TREASURE_RICKY_GLOVES": "$48",
    "TREASURE_BOMB_FLOWER": "$49",
    "TREASURE_RUSTY_BELL": "$4a",
    "TREASURE_TREASURE_MAP": "$4b",
    "TREASURE_ROUND_JEWEL": "$4c",
    "TREASURE_PYRAMID_JEWEL": "$4d",
    "TREASURE_SQUARE_JEWEL": "$4e",
    "TREASURE_X_SHAPED_JEWEL": "$4f",
    "TREASURE_RED_ORE": "$50",
    "TREASURE_BLUE_ORE": "$51",
    "TREASURE_HARD_ORE": "$52",
    "TREASURE_MEMBERS_CARD": "$53",
    "TREASURE_MASTERS_PLAQUE": "$54",
    "TREASURE_BOMB_FLOWER_LOWER_HALF": "$58",
    "TREASURE_CUCCODEX": "$55",  # Rando specific ID
    "TREASURE_LON_LON_EGG": "$56",  # Rando specific ID
    "TREASURE_GHASTLY_DOLL": "$57",  # Rando specific ID
    "TREASURE_IRON_POT": "$35",  # Rando specific ID
    "TREASURE_LAVA_SOUP": "$38",  # Rando specific ID
    "TREASURE_GORON_VASE": "$39",  # Rando specific ID
    "TREASURE_FISH": "$3a",  # Rando specific ID
    "TREASURE_MEGAPHONE": "$3b",  # Rando specific ID
    "TREASURE_MUSHROOM": "$3c",  # Rando specific ID
    "TREASURE_WOODEN_BIRD": "$3d",  # Rando specific ID
    "TREASURE_ENGINE_GREASE": "$3e",  # Rando specific ID
    "TREASURE_PHONOGRAPH": "$3f",  # Rando specific ID

    # Scripting
    "scriptend": "$00",
    "loadscript": "$83",
    "jumptable_memoryaddress": "$87",
    "setcollisionradii": "$8d",
    "setanimation": "$8f",
    "writememory": "$91",
    "ormemory": "$92",
    "rungenericnpc": "$97",
    "showtext": "$98",
    "checkabutton": "$9e",
    "checkcfc0_bit0": "$a0",
    "jumpifroomflagset": "$b0",
    "orroomflag": "$b1",
    "jumpifc6xxset": "$b3",
    "writec6xx": "$b4",
    "setglobalflag": "$b6",
    "setdisabledobjectsto00": "$b9",
    "setdisabledobjectsto11": "$ba",
    "disableinput": "$bd",
    "enableinput": "$be",
    "callscript": "$c0",
    "retscript": "$c1",
    "jumpalways": "$c4",
    "jumpifmemoryset": "$c7",
    "jumpifmemoryeq": "$cb",
    "checkcollidedwithlink_onground": "$d0",
    "setcounter1": "$d7",
    "loseitem": "$dc",
    "spawnitem": "$dd",
    "giveitem": "$de",
    "jumpifitemobtained": "$df",
    "asm15": "$e0",
    "initcollisions": "$eb",
    "movedown": "$ee",
    "delay1frame": "$f0",
    "delay30frames": "$f6",
    "setdisabledobjectsto91": "$b8",
    "showtextlowindex": "$98",
    "writeobjectbyte": "$8e",
    "setspeed": "$8b",
    "moveup": "$ec",
}

ASM_FILES = [
    "asm/animals.yaml",
    "asm/boss_items.yaml",
    "asm/collect.yaml",
    "asm/combat_difficulty.yaml",
    "asm/compass_chimes.yaml",
    "asm/cutscenes.yaml",
    "asm/file_select_custom_string.yaml",
    "asm/gasha_loot.yaml",
    "asm/get_item_behavior.yaml",
    "asm/gfx.yaml",
    "asm/impa_refill.yaml",
    "asm/item_events.yaml",
    "asm/layouts.yaml",
    "asm/locations.yaml",
    "asm/map_menu.yaml",
    "asm/maku_tree.yaml",
    "asm/misc.yaml",
    "asm/multi.yaml",
    "asm/new_game.yaml",
    "asm/new_treasures.yaml",
    "asm/permanent_subrosia_pirate_ship.yaml",
    "asm/progressives.yaml",
    "asm/remove_items_on_use.yaml",
    "asm/rings.yaml",
    "asm/samasa_combination.yaml",
    "asm/seasons_handling.yaml",
    "asm/shops_handling.yaml",
    "asm/subscreen_1_improvement.yaml",
    "asm/static_items.yaml",
    "asm/tarm_gate_requirement.yaml",
    "asm/text.yaml",
    "asm/triggers.yaml",
    "asm/util.yaml",
    "asm/vars.yaml",
    "asm/warp_to_start.yaml",
]

RUPEE_VALUES = {
    0: 0x00,
    1: 0x01,
    2: 0x02,
    5: 0x03,
    10: 0x04,
    20: 0x05,
    40: 0x06,
    30: 0x07,
    60: 0x08,
    70: 0x09,
    25: 0x0a,
    50: 0x0b,
    100: 0x0c,
    200: 0x0d,
    400: 0x0e,
    150: 0x0f,
    300: 0x10,
    500: 0x11,
    900: 0x12,
    80: 0x13,
    999: 0x14,
}

DUNGEON_ENTRANCES = {
    "d0": {
        "addr": 0x13651,
        "map_tile": 0xd4,
        "room": 0xd4,
        "group": 0x00,
        "position": 0x54
    },
    "d1": {
        "addr": 0x1346d,
        "map_tile": 0x96,
        "room": 0x96,
        "group": 0x00,
        "position": 0x44
    },
    "d2": {
        "addr": 0x13659,
        "map_tile": 0x8d,
        "room": 0x8d,
        "group": 0x00,
        "position": 0x24
    },
    "d3": {
        "addr": 0x13671,
        "map_tile": 0x60,
        "room": 0x60,
        "group": 0x00,
        "position": 0x25
    },
    "d4": {
        "addr": 0x13479,
        "map_tile": 0x1d,
        "room": 0x1d,
        "group": 0x00,
        "position": 0x13
    },
    "d5": {
        "addr": 0x1347d,
        "map_tile": 0x8a,
        "room": 0x8a,
        "group": 0x00,
        "position": 0x25
    },
    "d6": {
        "addr": 0x13481,
        "map_tile": 0x00,
        "room": 0x00,
        "group": 0x00,
        "position": 0x34
    },
    "d7": {
        "addr": 0x13485,
        "map_tile": 0xd0,
        "room": 0xd0,
        "group": 0x00,
        "position": 0x34
    },
    "d8": {
        "addr": 0x1369d,
        "map_tile": 0x04,
        "room": 0x00,
        "group": 0x01,
        "position": 0x23
    },
}

DUNGEON_EXITS = {
    "d0": 0x13909,
    "d1": 0x1390d,
    "d2": 0x13911,
    "d3": 0x13915,
    "d4": 0x13919,
    "d5": 0x1391d,
    "d6": 0x13921,
    "d7": 0x13a89,
    "d8": 0x13a8d,
}

WARP_DEST_ADDR = [
    0x100000,
    0x100180,
    0x100200,
    0x1002C0,
    0x1003B0,
    0x1004D0,
    0x1006F0,
    0x100720
]

# Format = name: (transition_address, opposite entrance name)
NORMAL_EXITS = {
    # Group 0 / Overworld ################################################################
    # Horon Village
    "enter shop": (0x134D9, "inside shop"),
    "enter tick tock": (0x135E5, "inside tick tock"),
    "enter mayor's house": (0x134A5, "inside mayor's house"),
    "enter vasu": (0x134AD, "inside vasu"),
    "enter village portal room": (0x134E1, "inside village portal room"),
    "enter know-it-all birds": (0x13605, "inside know-it-all birds"),
    "enter bipin left": (0x13625, "inside bipin left"),
    "enter bipin right": (0x13629, "inside bipin right"),
    "enter advance shop": (0x13609, "inside advance shop"),
    "enter dr left old man": (0x1362D, "inside dr left old man"),
    "enter dr left": (0x13631, "inside dr left"),
    "enter dr left side": (0x13635, "inside dr left side"),
    "enter hidden stairs behind clock shop": (0x135E9, "inside hidden stairs behind clock shop"),

    # Western Coast
    "enter beach fairy cave": (0x1359D, "inside beach fairy cave"),
    "enter d0 chimney": (0x1364D, "inside d0 chimney"),
    "enter pirate ship": (0x135A1, "inside pirate ship"),
    "enter old man near western coast house": (0x13641, "inside old man near western coast house"),
    "enter coast house": (0x13645, "inside coast house"),
    "enter coast house side": (0x13649, "inside coast house side"),
    "enter graveyard cave": (0x13575, "inside graveyard cave"),
    "outside graveyard chimney": (None, "inside graveyard chimney"),
    "enter hidden graveyard stairs": (0x135D9, "inside hidden graveyard stairs"),

    # Eyeglass Lake
    "enter lon lon": (0x13495, "inside lon lon"),
    "enter d1 old man": (0x135B1, "inside d1 old man"),
    "enter red ring old man": (0x135D5, "inside red ring old man"),
    "enter lake bomb cave": (0x13591, "inside lake bomb cave"),
    "enter lake boulder": (0x13545, "inside lake boulder"),

    # Easter Suburbs
    "enter guru guru": (0x13675, "inside guru guru"),
    "top of guru guru": (0x13525, "top guru guru staircase"),
    "enter winter guru guru": (0x13679, "inside winter guru guru"),
    "enter suburb spring cave": (0x13585, "inside suburb spring cave"),
    "enter suburbs old man": (0x135B9, "inside suburbs old man"),

    # Samasa Desert
    "enter desert fairy cave": (0x13619, "inside desert fairy cave"),
    "enter desert cave": (0x135A9, "inside desert cave"),
    "enter stairs near desert chest": (0x1357D, "inside stairs near desert chest"),
    "enter desert ship": (0x135A5, "inside desert ship"),

    # Woods of Winter
    "enter peek cave near d2": (0x13665, "inside peek cave near d2"),
    "enter magnet cave near d2": (0x13669, "inside magnet cave near d2"),
    "enter first woods of winter cave": (0x1351D, "inside first woods of winter cave"),
    "enter second woods of winter cave": (0x135DD, "inside second woods of winter cave"),
    "enter d2 side entrance left": (0x1365D, "inside d2 side entrance left"),
    "enter d2 side entrance right": (0x13661, "inside d2 side entrance right"),
    "enter holly house": (0x13639, "inside holly house"),
    "enter holly chimney": (0x1363D, None),

    # Holodrum Plain
    "enter treehouse": (0x134B5, "inside treehouse"),
    "enter Mrs Ruul": (0x134E5, "inside Mrs Ruul"),
    "enter ruul old man": (0x135BD, "inside ruul old man"),
    "enter Blaino": (0x134E9, "inside Blaino"),
    "enter old man near blaino": (0x135AD, "inside old man near blaino"),
    "enter ruul water cave": (0x13595, "inside ruul water cave"),
    "enter autumn water cave": (0x13599, "inside autumn water cave"),

    # Spool Swamp
    "enter floodgate left": (0x1366D, "inside floodgate left"),
    "enter floodgate right": (0x1361D, "inside floodgate right"),
    "enter floodgate house": (0x13621, "inside floodgate house"),
    "enter swamp bomb cave": (0x1358D, "inside swamp bomb cave"),

    # Natzu
    "enter natzu north stairs": (0x135D1, "inside natzu north stairs"),
    "enter moblin keep left": (0x1360D, "inside moblin keep left"),
    "enter moblin keep right": (0x13611, "inside moblin keep right"),
    "enter ricky fairy": (0x135ED, "inside ricky fairy"),
    "enter moosh fairy": (0x135F1, "inside moosh fairy"),
    "enter dimitri fairy": (0x135C5, "inside dimitri fairy"),
    "enter ricky deku": (0x135C9, "inside ricky deku"),
    "enter moosh deku": (0x135CD, "inside moosh deku"),

    # Sunken City
    "enter ingo": (0x134B9, "inside ingo"),
    "enter syrup": (0x134C1, "inside syrup"),
    "enter flooded house": (0x134C5, "inside flooded house"),
    "enter treasure hunter": (0x134C9, "inside treasure hunter"),
    "enter bomb house": (0x134CD, "inside bomb house"),
    "enter master diver house": (0x134F1, "inside master diver house"),
    "enter sunken city, summer cave": (0x1352D, "inside sunken city, summer cave"),

    # Cucco Mountain
    "enter mountain fairy cave": (0x135FD, "inside mountain fairy cave"),
    "enter talon cave": (0x13531, "inside talon cave"),
    "enter winter cave in cucco mountain": (0x13539, "inside winter cave in cucco mountain"),
    "enter top of cucco mountain": (0x13535, "inside top of cucco mountain"),
    "enter banana stairs": (0x13685, "inside banana stairs"),
    "enter banana cave": (0x13689, "inside banana cave"),
    "enter fast platform cave": (0x13541, "inside fast platform cave"),

    # Goron Mountain
    "enter goron mountain bottom": (0x13561, "inside goron mountain bottom"),
    "enter goron mountain middle": (0x135F5, "inside goron mountain middle"),
    "enter goron mountain top": (0x13559, "inside goron mountain top"),
    "enter goron old man": (0x135F9, "inside goron old man"),
    "enter goron mountain bomb cave": (0x1356D, "inside goron mountain bomb cave"),
    "enter goron outside stairs": (0x13699, "inside goron outside stairs"),
    "enter left cave to lynel in goron mountain": (0x1368D, "inside left cave to lynel in goron mountain"),
    "enter right cave to lynel in goron mountain": (0x13691, "inside right cave to lynel in goron mountain"),
    "enter lynel stairs in goron mountain": (0x13565, "inside lynel stairs in goron mountain"),
    "enter goron ring cave": (0x13695, "inside goron ring cave"),

    # Lost Woods
    "enter lost woods deku": (0x134F5, "inside lost woods deku"),
    "enter phonograph deku": (0x13589, "inside phonograph deku"),
    "enter lost woods bomb cave": (0x13571, "inside lost woods bomb cave"),

    # Tarm Ruins
    "enter tarm ruins, under tree": (0x134BD, "inside tarm ruins, under tree"),
    "enter tarm old man": (0x135B5, "inside tarm old man"),

    # Temple Ruins
    "enter d8 fairy room": (0x134DD, "inside d8 fairy room"),
    "enter temple remains cave": (0x13549, "inside temple remains cave"),
    "enter right stairs in top of temple remains": (0x13551, "inside right stairs in top of temple remains"),
    "enter middle stairs in top of temple remains": (0x13681, "inside middle stairs in top of temple remains"),
    "enter left stairs in top of temple remains": (0x1367D, "inside left stairs in top of temple remains"),
    "enter temple remains bomb cave": (0x13555, "inside temple remains bomb cave"),

    # Group 1 / Subrosia ################################################################
    # Temple area
    "enter open cave": (0x13711, "inside open cave"),
    "enter boomerang cave": (0x1370D, "inside boomerang cave"),
    "enter Closed cave": (0x136CD, "inside Closed cave"),
    "enter temple of seasons": (0x136A1, "inside temple of seasons"),
    "enter winter temple": (0x136B1, "inside winter temple"),
    "enter Summer tower": (0x136A9, "inside Summer tower"),
    "enter Autumn tower": (0x136AD, "inside Autumn tower"),
    "enter Rosa corridor left": (0x1373D, "inside Rosa corridor left"),
    "enter subrosian cook": (0x136D9, "inside subrosian cook"),
    "enter Useless subrosian house": (0x136E1, "inside Useless subrosian house"),
    "enter tower of spring staircase": (0x13739, "inside tower of spring staircase"),
    "enter volcano cave": (0x13709, "inside volcano cave"),
    "enter tower of spring": (0x13735, "inside tower of spring"),
    "enter dance hall": (0x136DD, "inside dance hall"),
    "enter smithy": (0x136E5, "inside smithy"),

    # Market area
    "enter Rosa corridor right": (0x13741, "inside Rosa corridor right"),
    "enter subrosian market": (0x136ED, "inside subrosian market"),

    # Furnace area
    "enter red ore cave": (0x13725, "inside red ore cave"),
    "enter red ore stairs": (0x13721, "inside red ore stairs"),
    "enter furnace": (0x136E9, "inside furnace"),
    "enter sign guy": (0x136F9, "inside sign guy"),

    # Pirate area
    "enter staircase to tower of spring": (0x13705, "inside staircase to tower of spring"),
    "enter house above hide and seek": (0x136F1, "inside house above hide and seek"),
    "enter strange brothers left": (0x136FD, "inside strange brothers left"),
    "enter strange brothers right": (0x13701, "inside strange brothers right"),
    "enter pirate house": (0x13731, "inside pirate house"),
    "enter pirate staircase": (0x1372D, "inside pirate staircase"),
    "enter subrosia ship": (0x13719, "inside subrosia ship"),

    # Group 3, 4, 5 / Caves ################################################################
    # Horon Village
    "inside shop": (0x1387D, "enter shop"),
    "inside tick tock": (0x13805, "enter tick tock"),
    "inside mayor's house": (0x1380D, "enter mayor's house"),
    "inside vasu": (0x13829, "enter vasu"),
    "inside village portal room": (0x13901, "enter village portal room"),
    "inside know-it-all birds": (0x13809, "enter know-it-all birds"),
    "inside bipin left": (0x1382D, "enter bipin left"),
    "inside bipin right": (0x13831, "enter bipin right"),
    "inside advance shop": (0x1389D, "enter advance shop"),
    "inside dr left old man": (0x13C25, "enter dr left old man"),
    "inside dr left": (0x13875, "enter dr left"),
    "inside dr left side": (0x13879, "enter dr left side"),
    "inside hidden stairs behind clock shop": (0x13C49, "enter hidden stairs behind clock shop"),

    # Western Coast
    "inside old man near western coast house": (0x13C21, "enter old man near western coast house"),
    "inside d0 chimney": (None, "enter d0 chimney"),
    "inside pirate ship": (0x13BFD, "enter pirate ship"),
    "inside beach fairy cave": (0x13A59, "enter beach fairy cave"),
    "inside coast house": (0x13811, "enter coast house"),
    "inside coast house side": (0x13815, "enter coast house side"),
    "inside graveyard cave": (0x13A29, "enter graveyard cave"),
    "inside graveyard chimney": (0x13A2D, None),
    "inside hidden graveyard stairs": (0x138D5, "enter hidden graveyard stairs"),

    # Eastern Suburbs
    "inside guru guru": (0x13B61, "enter guru guru"),
    "top guru guru staircase": (0x13CB1, "top of guru guru"),
    "inside winter guru guru": (0x13B6D, "enter winter guru guru"),
    "inside suburb spring cave": (0x13A41, "enter suburb spring cave"),
    "inside suburbs old man": (0x13C2D, "enter suburbs old man"),

    # Samasa Desert
    "inside desert fairy cave": (0x13A3D, "enter desert fairy cave"),
    "inside desert cave": (0x13C11, "enter desert cave"),
    "inside stairs near desert chest": (0x13A35, "enter stairs near desert chest"),
    "inside desert ship": (0x13C9D, "enter desert ship"),

    # Woods of Winter
    "inside peek cave near d2": (0x13B75, "enter peek cave near d2"),
    "inside magnet cave near d2": (0x13B79, "enter magnet cave near d2"),
    "inside first woods of winter cave": (0x13B7D, "enter first woods of winter cave"),
    "inside second woods of winter cave": (0x13C55, "enter second woods of winter cave"),
    "inside d2 side entrance left": (0x13935, "enter d2 side entrance left"),
    "inside d2 side entrance right": (0x13939, "enter d2 side entrance right"),
    "inside holly house": (0x13871, "enter holly house"),
    "inside holly chimney": (None, "enter holly chimney"),

    # Eyeglass Lake
    "inside lon lon": (0x137F9, "enter lon lon"),
    "inside d1 old man": (0x13C1D, "enter d1 old man"),
    "inside red ring old man": (0x13C51, "enter red ring old man"),
    "inside lake bomb cave": (0x13A55, "enter lake bomb cave"),
    "inside lake boulder": (0x13D79, "enter lake boulder"),

    # Holodrum Plain
    "inside treehouse": (0x13835, "enter treehouse"),
    "inside Blaino": (0x138B1, "enter Blaino"),
    "inside old man near blaino": (0x13C19, "enter old man near blaino"),
    "inside Mrs Ruul": (0x138AD, "enter Mrs Ruul"),
    "inside ruul old man": (0x13C31, "enter ruul old man"),
    "inside ruul water cave": (0x139DD, "enter ruul water cave"),
    "inside autumn water cave": (0x139E1, "enter autumn water cave"),

    # Spool Swamp
    "inside floodgate left": (0x13A79, "enter floodgate left"),
    "inside floodgate right": (0x139F1, "enter floodgate right"),
    "inside floodgate house": (0x138B5, "enter floodgate house"),
    "inside swamp bomb cave": (0x13A51, "enter swamp bomb cave"),

    # Natzu
    "inside natzu north stairs": (0x13C45, "enter natzu north stairs"),
    "inside moblin keep left": (0x138C5, "enter moblin keep left"),
    "inside moblin keep right": (0x138C9, "enter moblin keep right"),
    "inside ricky fairy": (0x13C35, "enter ricky fairy"),
    "inside moosh fairy": (0x13C4D, "enter moosh fairy"),
    "inside dimitri fairy": (0x13C39, "enter dimitri fairy"),
    "inside ricky deku": (0x13C3D, "enter ricky deku"),
    "inside moosh deku": (0x13C41, "enter moosh deku"),

    # Sunken City
    "inside sunken city, summer cave": (0x13B81, "enter sunken city, summer cave"),
    "inside ingo": (0x13849, "enter ingo"),
    "inside syrup": (0x13855, "enter syrup"),
    "inside flooded house": (0x13859, "enter flooded house"),
    "inside treasure hunter": (0x13861, "enter treasure hunter"),
    "inside bomb house": (0x13895, "enter bomb house"),
    "inside master diver house": (0x138B9, "enter master diver house"),

    # Cucco Mountain
    "inside mountain fairy cave": (0x13A09, "enter mountain fairy cave"),
    "inside talon cave": (0x13B85, "enter talon cave"),
    "inside winter cave in cucco mountain": (0x13B91, "enter winter cave in cucco mountain"),
    "inside top of cucco mountain": (0x13D71, "enter top of cucco mountain"),
    "inside banana stairs": (0x13B95, "enter banana stairs"),
    "inside banana cave": (0x13B99, "enter banana cave"),
    "inside fast platform cave": (0x13B9D, "enter fast platform cave"),
    "inside gem dive spot": (0x13DF1, "enter gem dive spot"),
    "inside mount cucco dive spot": (0x13DE1, "enter mount cucco dive spot"),
    "inside north sunken city dive spot": (0x13DE5, "enter north sunken city dive spot"),

    # Goron Mountain
    "inside goron mountain bottom": (0x13BD1, "enter goron mountain bottom"),
    "inside goron mountain middle": (0x13BCD, "enter goron mountain middle"),
    "inside goron mountain top": (0x13BC9, "enter goron mountain top"),
    "inside goron old man": (0x13C15, "enter goron old man"),
    "inside goron mountain bomb cave": (0x13BED, "enter goron mountain bomb cave"),
    "inside goron outside stairs": (0x13BF1, "enter goron outside stairs"),
    "inside left cave to lynel in goron mountain": (0x13BE1, "enter left cave to lynel in goron mountain"),
    "inside right cave to lynel in goron mountain": (0x13BE5, "enter right cave to lynel in goron mountain"),
    "inside lynel stairs in goron mountain": (0x13BE9, "enter lynel stairs in goron mountain"),
    "inside goron ring cave": (0x13BF5, "enter goron ring cave"),

    # Lost Woods
    "inside lost woods deku": (0x138C1, "enter lost woods deku"),
    "inside lost woods bomb cave": (0x13A0D, "enter lost woods bomb cave"),
    "inside phonograph deku": (0x13A45, "enter phonograph deku"),

    # Tarm Ruins
    "inside tarm ruins, under tree": (0x13851, "enter tarm ruins, under tree"),
    "inside tarm old man": (0x13C29, "enter tarm old man"),

    # Temple Ruins
    "inside d8 fairy room": (0x13889, "enter d8 fairy room"),
    "inside temple remains cave": (0x13BAD, "enter temple remains cave"),
    "inside right stairs in top of temple remains": (0x13D85, "enter right stairs in top of temple remains"),
    "inside middle stairs in top of temple remains": (0x13BBD, "enter middle stairs in top of temple remains"),
    "inside left stairs in top of temple remains": (0x13BB9, "enter left stairs in top of temple remains"),
    "inside temple remains bomb cave": (0x13BC5, "enter temple remains bomb cave"),

    # Subrosia
    # Temple area
    "inside boomerang cave": (0x13A19, "enter boomerang cave"),
    "inside temple of seasons": (0x138E9, "enter temple of seasons"),
    "inside winter temple": (0x13C65, "enter winter temple"),
    "inside Rosa corridor left": (0x13A49, "enter Rosa corridor left"),
    "inside Summer tower": (0x13C5D, "enter Summer tower"),
    "inside Autumn tower": (0x13C61, "enter Autumn tower"),
    "inside open cave": (0x13A1D, "enter open cave"),
    "inside Closed cave": (0x13BC1, "enter Closed cave"),
    "inside Useless subrosian house": (0x1383D, "enter Useless subrosian house"),
    "inside subrosian cook": (0x13825, "enter subrosian cook"),
    "inside volcano cave": (0x13A15, "enter volcano cave"),
    "inside dance hall": (0x13839, "enter dance hall"),
    "inside tower of spring": (0x13C59, "enter tower of spring"),
    "inside tower of spring staircase": (0x13DED, "enter tower of spring staircase"),
    "inside smithy": (0x13841, "enter smithy"),

    # Market area
    "inside subrosian market": (0x13865, "enter subrosian market"),
    "inside Rosa corridor right": (0x13A4D, "enter Rosa corridor right"),

    # Furnace area
    "inside red ore cave": (0x13A25, "enter red ore cave"),
    "inside red ore stairs": (0x13A21, "enter red ore stairs"),
    "inside furnace": (0x1385D, "enter furnace"),
    "inside sign guy": (0x13891, "enter sign guy"),

    # Pirate area
    "inside house above hide and seek": (0x13869, "enter house above hide and seek"),
    "inside staircase to tower of spring": (0x13DE9, "enter staircase to tower of spring"),
    "inside strange brothers left": (0x138A5, "enter strange brothers left"),
    "inside strange brothers right": (0x138A9, "enter strange brothers right"),
    "inside pirate house": (0x13819, "enter pirate house"),
    "inside pirate staircase": (0x138FD, "enter pirate staircase"),
    "inside subrosia ship": (0x13CA1, "enter subrosia ship"),
}

WATERFALL_WARPS = {
    "enter sunken left waterfall": (0x211E5, "inside sunken left waterfall"),
    "enter sunken right waterfall": (0x211E9, "inside sunken right waterfall"),
    "enter natzu waterfall": (0x211ED, "inside natzu waterfall"),

    "inside sunken left waterfall": (0x211F1, "enter sunken left waterfall"),
    "inside sunken right waterfall": (0x211F5, "enter sunken right waterfall"),
    "inside natzu waterfall": (0x211F9, "enter natzu waterfall"),
}

DIRECT_WARPS = {
    "enter like like quicksand": (0x24C81, "inside like like quicksand"),
    "enter deku quicksand": (0x24C85, "inside deku quicksand"),
    "enter bell quicksand": (0x24C89, "inside bell quicksand"),
    "enter treasure quicksand": (0x24C8D, "inside treasure quicksand"),

    "enter gem dive spot": (0x212A8, "inside gem dive spot"),
    "enter mount cucco dive spot": (0x212A0, "inside mount cucco dive spot"),
    "enter north sunken city dive spot": (0x212A4, "inside north sunken city dive spot"),
    "enter south sunken city dive spot": (0x212B4, "inside south sunken city dive spot"),
}

SPECIAL_WARPS = {
    "inside like like quicksand": (0xB1, 0x5, "enter like like quicksand"),
    "inside deku quicksand": (0xB2, 0x5, "enter deku quicksand"),
    "inside bell quicksand": (0xB3, 0x5, "enter bell quicksand"),
    "inside treasure quicksand": (0x5D, 0x4, "enter treasure quicksand"),

    "inside gem dive spot": (0x08, 0x7, "enter gem dive spot"),
    "inside mount cucco dive spot": (0x04, 0x7, "enter mount cucco dive spot"),
    "inside north sunken city dive spot": (0x05, 0x7, "enter north sunken city dive spot"),
    "inside south sunken city dive spot": (0xB0, 0x5, "enter south sunken city dive spot"),
}

SOFTLOCK_WARPS = {
    "enter d1 old man": 0x11,
    "enter red ring old man": -0x14,
    "enter lake bomb cave": 0x10,
    "enter lake boulder": -0x06,

    "enter dr left old man": -0x10,

    "enter pirate ship": -0x20,
    "enter old man near western coast house": 0x10,

    "enter desert fairy cave": 0x10,

    "enter suburbs old man": 0x10,

    "enter peek cave near d2": 0x20,
    "enter first woods of winter cave": 0x30,
    "enter holly house": 0x10,

    "enter old man near blaino": 0x10,
    "enter ruul old man": -0x01,
    "inside autumn water cave": -0x50,
    "inside ruul water cave": -0x58,

    "enter floodgate right": 0x20,
    "enter swamp bomb cave": 0x10,

    "enter flooded house": -0x02,

    "enter goron old man": -0x10,
    "enter goron mountain bomb cave": 0x10,

    "enter lost woods bomb cave": 0x10,
    "enter phonograph deku": -0x10,

    "enter tarm ruins, under tree": 0x01,

    "enter temple remains bomb cave": 0x10,

    "enter Closed cave": 0x10,
    "enter Summer tower": 0x10,
    "enter Autumn tower": 0x30,
    "enter Rosa corridor left": 0x10,
    "enter Rosa corridor right": 0x10,
    "inside Rosa corridor left": -0x60,
}

SEASON_WARP = {
    "enter goron mountain bottom",
    "enter goron mountain middle",
    "enter goron mountain top",
    "enter goron old man",
    "enter goron mountain bomb cave",
    "enter goron outside stairs",
    "enter left cave to lynel in goron mountain",
    "enter right cave to lynel in goron mountain",
    "enter lynel stairs in goron mountain",
    "enter goron ring cave",

    "enter natzu north stairs",
    "enter moblin keep left",
    "enter moblin keep right",
    "enter ricky fairy",
    "enter moosh fairy",
    "enter dimitri fairy",
    "enter ricky deku",
    "enter moosh deku",

    "enter desert fairy cave",
    "enter desert ship",
    "enter desert cave",
    "enter stairs near desert chest",
}

PORTAL_WARPS = {
    "eastern suburbs portal": {
        "addr": 0x134fd,
        "map_tile": 0x9a,
        "in_subrosia": False,
        "text_index": 0x0,
    },
    "spool swamp portal": {
        "addr": 0x13501,
        "map_tile": 0xb0,
        "in_subrosia": False,
        "text_index": 0x1,
    },
    "mt. cucco portal": {
        "addr": 0x13601,
        "map_tile": 0x1e,
        "in_subrosia": False,
        "text_index": 0x2,
    },
    "eyeglass lake portal": {
        "addr": 0x13509,
        "map_tile": 0xb9,
        "in_subrosia": False,
        "text_index": 0x3,
    },
    "horon village portal": {
        "addr": 0x13905,
        "map_tile": 0xf7,
        "in_subrosia": False,
        "text_index": 0x4,
    },
    "temple remains lower portal": {
        "addr": 0x1350d,
        "map_tile": 0x25,
        "in_subrosia": False,
        "text_index": 0x5,
    },
    "temple remains upper portal": {
        "addr": 0x1388d,
        "map_tile": 0x04,
        "in_subrosia": False,
        "text_index": 0x6,
    },

    "volcanoes east portal": {
        "addr": 0x136b5,
        "map_tile": 0x05,
        "in_subrosia": True,
        "text_index": 0x7,
    },
    "subrosia market portal": {
        "addr": 0x136b9,
        "map_tile": 0x3e,
        "in_subrosia": True,
        "text_index": 0x8,
    },
    "strange brothers portal": {
        "addr": 0x136bd,
        "map_tile": 0x3a,
        "in_subrosia": True,
        "text_index": 0x9,
    },
    "great furnace portal": {
        "addr": 0x136c1,
        "map_tile": 0x36,
        "in_subrosia": True,
        "text_index": 0xa,
    },
    "house of pirates portal": {
        "addr": 0x13729,
        "map_tile": 0x4f,
        "in_subrosia": True,
        "text_index": 0xb,
    },
    "volcanoes west portal": {
        "addr": 0x136c5,
        "map_tile": 0x0e,
        "in_subrosia": True,
        "text_index": 0xc,
    },
    "d8 entrance portal": {
        "addr": 0x136c9,
        "map_tile": 0x16,
        "in_subrosia": True,
        "text_index": 0xd,
    }
}

PALETTE_BYTES = {
    "green": 0x00,
    "blue": 0x01,
    "red": 0x02,
    "orange": 0x03,
}

# Scripting constants
DELAY_6 = 0xf6
CALL_SCRIPT = 0xc0
MOVE_UP = 0xec
MOVE_DOWN = 0xee
MOVE_LEFT = 0xef
MOVE_RIGHT = 0xed
WRITE_OBJECT_BYTE = 0x8e
SHOW_TEXT_LOW_INDEX = 0x98
ENABLE_ALL_OBJECTS = 0xb9

DIRECTION_STRINGS = {
    DIRECTION_UP: [0x15, 0x20],
    DIRECTION_DOWN: [0x16, 0x20],
    DIRECTION_LEFT: [0x17, 0x20],
    DIRECTION_RIGHT: [0x18, 0x20],
}

SEASON_STRINGS = {
    SEASON_SPRING: [0x02, 0xde],
    SEASON_SUMMER: ['S'.encode()[0], 0x04, 0xbc],
    SEASON_AUTUMN: ['A'.encode()[0], 0x05, 0x25],
    SEASON_WINTER: [0x03, 0x7e]
}
