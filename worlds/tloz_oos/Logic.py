from BaseClasses import MultiWorld, EntranceType
from worlds.tloz_oos import LOCATIONS_DATA
from worlds.tloz_oos.data.logic.DungeonsLogic import *
from worlds.tloz_oos.data.logic.OverworldLogic import make_holodrum_logic
from worlds.tloz_oos.data.logic.SubrosiaLogic import make_subrosia_logic


def create_connections(multiworld: MultiWorld, player: int):
    oos_world = multiworld.worlds[player]

    dungeon_entrances = []
    for reg1, reg2 in oos_world.dungeon_entrances.items():
        dungeon_entrances.append([reg1, reg2, OoSEntranceType.TwoWay, None])

    portal_connections = []
    for reg1, reg2 in oos_world.portal_connections.items():
        portal_connections.append([reg1, reg2, OoSEntranceType.TwoWay, None])

    all_logic = [
        make_holodrum_logic(player),
        make_subrosia_logic(player),
        make_d0_logic(player),
        make_d1_logic(player),
        make_d2_logic(player),
        make_d3_logic(player),
        make_d4_logic(player),
        make_d5_logic(player),
        make_d6_logic(player),
        make_d7_logic(player),
        make_d8_logic(player),
        dungeon_entrances,
        portal_connections,
    ]

    # Create connections
    for logic_array in all_logic:
        for entrance_desc in logic_array:
            region_1 = multiworld.get_region(entrance_desc[0], player)
            region_2 = multiworld.get_region(entrance_desc[1], player)
            entrance_type = entrance_desc[2]
            if OoSEntranceType.CompanionEntrance & entrance_type != 0:
                if OoSEntranceType.Ricky in entrance_type and oos_world.options.animal_companion != "ricky" \
                        or OoSEntranceType.Moosh in entrance_type and oos_world.options.animal_companion != "moosh" \
                        or OoSEntranceType.Dimitri in entrance_type and oos_world.options.animal_companion != "dimitri":
                    continue
            if OoSEntranceType.D0Alt in entrance_type and oos_world.options.remove_d2_alt_entrance:
                continue

            rule = entrance_desc[3]
            if OoSEntranceType.DoorTransition in entrance_type and oos_world.options.randomize_entrances \
                    and not (OoSEntranceType.D2Stairs in entrance_type and oos_world.options.remove_d2_alt_entrance):
                entrance = region_1.connect(region_2, entrance_desc[0], rule)

                if OoSEntranceType.Waterfall in entrance_type:
                    randomization_group = 1
                elif OoSEntranceType.DiveFlag in entrance_type:
                    randomization_group = 2
                else:
                    randomization_group = 0
                entrance.randomization_group = randomization_group

                if OoSEntranceType.DoorTwoWayFlag in entrance_type:
                    entrance.randomization_type = EntranceType.TWO_WAY

                oos_world.entrances_to_randomize.append(entrance)

                if OoSEntranceType.TwoWay in entrance_type:
                    if OoSEntranceType.Asymmetric in entrance_type:
                        rule = None
                    entrance = region_2.connect(region_1, entrance_desc[1], rule)

                    entrance.randomization_group = randomization_group
                    entrance.randomization_type = EntranceType.TWO_WAY
                    oos_world.entrances_to_randomize.append(entrance)

                continue
            region_1.connect(region_2, rule=rule)
            if OoSEntranceType.TwoWay in entrance_type:
                if OoSEntranceType.Asymmetric in entrance_type:
                    rule = None
                region_2.connect(region_1, rule=rule)


def apply_self_locking_rules(multiworld: MultiWorld, player: int):
    if multiworld.worlds[player].options.accessibility == Accessibility.option_full:
        return

    # Process self-locking keys first
    MINIMAL_REQUIRED_KEYS_TO_REACH_KEYDOOR = {
        "Hero's Cave: Final Chest": 0,
        "Gnarled Root Dungeon: Item in Basement": 1,
        "Snake's Remains: Chest on Terrace": 2,
        "Poison Moth's Lair (1F): Chest in Mimics Room": 1,
        "Dancing Dragon Dungeon (1F): Crumbling Room Chest": 2,
        "Dancing Dragon Dungeon (1F): Eye Diving Spot Item": 2,
        "Unicorn's Cave: Magnet Gloves Chest": 1,
        "Unicorn's Cave: Treadmills Basement Item": 3,
        "Explorer's Crypt (B1F): Chest in Jumping Stalfos Room": 4,  # Not counting poe skip
        "Explorer's Crypt (1F): Chest Right of Entrance": 1
    }

    for location_name, key_count in MINIMAL_REQUIRED_KEYS_TO_REACH_KEYDOOR.items():
        location_data = LOCATIONS_DATA[location_name]
        dungeon = location_data["dungeon"]
        small_key_item_name = f"Small Key ({DUNGEON_NAMES[dungeon]})"
        location = multiworld.get_location(location_name, player)
        location.always_allow = make_self_locking_item_lambda(player, small_key_item_name, key_count)

    # Process other self-locking items
    OTHER_SELF_LOCKING_ITEMS = {
        "North Horon: Malon Trade": "Cuccodex",
        "Maple Trade": "Lon Lon Egg",
        "Holodrum Plain: Mrs. Ruul Trade": "Ghastly Doll",
        "Subrosia: Subrosian Chef Trade": "Iron Pot",
        "Goron Mountain: Biggoron Trade": "Lava Soup",
        "Sunken City: Ingo Trade": "Goron Vase",
        "North Horon: Yelling Old Man Trade": "Fish",
        "Horon Village: Tick Tock Trade": "Wooden Bird",
        "Eastern Suburbs: Guru-Guru Trade": "Engine Grease",
        "Subrosia: Smithy Hard Ore Reforge": "Hard Ore",
        "Subrosia: Smithy Rusty Bell Reforge": "Rusty Bell",
        "Sunken City: Master's Plaque Trade": "Master's Plaque",
        "Subrosia: Market #1": "Star Ore",
    }

    for loc_name, item_name in OTHER_SELF_LOCKING_ITEMS.items():
        location = multiworld.get_location(loc_name, player)
        location.always_allow = make_self_locking_item_lambda(player, item_name)

    # Great Furnace special case
    location = multiworld.get_location("Subrosia: Item Smelted in Great Furnace", player)
    location.always_allow = lambda state, item: (item.player == player and item.name in ["Red Ore", "Blue Ore"])


def make_self_locking_item_lambda(player: int, item_name: str, required_count: int = 0):
    if required_count == 0:
        return lambda state, item: (item.player == player and item.name == item_name)

    return lambda state, item: (item.player == player
                                and item.name == item_name
                                and state.has(item_name, player, required_count))
