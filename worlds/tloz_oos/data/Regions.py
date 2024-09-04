from typing import Optional, Callable, Tuple, Any, Union

from BaseClasses import Region, CollectionState, MultiWorld, Entrance, EntranceType
from worlds.tloz_oos.data.Constants import SEASON_NAMES, SEASON_SPRING, SEASON_SUMMER, SEASON_WINTER, SEASON_CHAOTIC, SEASON_ITEMS

REGIONS = {
    "EYEGLASS_LAKE": [
        "impa",
        "d1 stump",
        "d1 island",
        "eyeglass lake portal",
        "d1 entrance",
        "d5 stump",
        "d5 entrance",
        "eyeglass lake, across bridge",
        "eyeglass lake",
        "impa gasha spot",
        "eyeglass lake gasha spot",

        "enter lon lon",
        "enter d1 old man",
        "enter red ring old man",
        "enter lake bomb cave",
        "enter lake boulder",
    ],
    "HOLODRUM_PLAIN": [
        "ghastly stump",
        "north horon",
        "underwater item below natzu bridge",
        "north horon tree",
        "holodrum plain gasha spot",
        "holodrum plain island gasha spot",
        "holodrum plain waters",

        "enter treehouse",
        "enter Mrs Ruul",
        "enter ruul old man",
        "enter Blaino",
        "enter old man near blaino",
        "enter ruul water cave",
        "enter autumn water cave",
    ],
    "EASTERN_SUBURBS": [
        "suburbs",
        "eastern suburbs portal",
        "suburbs fairy fountain",
        "top of suburbs",
        "suburbs NE",
        "woods of winter heart piece",
        "suburbs gasha spot",

        "enter guru guru",
        "enter winter guru guru",
        "top of guru guru",
        "enter suburb spring cave",
        "enter suburbs old man",
    ],
    "WOODS_OF_WINTER": [
        "moblin road",
        "central woods of winter",
        "woods of winter tree",
        "d2 entrance",
        "d2 stump",
        "d2 roof",
        "golden moblin",

        "enter peek cave near d2",
        "enter magnet cave near d2",
        "enter first woods of winter cave",
        "enter second woods of winter cave",
        "enter holly house",
        "enter holly chimney",
    ],
    "SUNKEN_CITY": [  # / Cucco Mountain
        "sunken city entrance",
        "sunken city",
        "sunken city tree",
        "sunken city stump",
        "sunken city dimitri",
        "sunken city gasha spot",

        "enter ingo",
        "enter syrup",
        "enter flooded house",
        "enter treasure hunter",
        "enter bomb house",
        "enter master diver house",
        "enter sunken city, summer cave",

        "mount cucco",
        "mt. cucco portal",
        "rightmost rooster ledge",
        "spring banana tree",
        "mt. cucco, talon's cave entrance",
        "mt. cucco heart piece",
        "dragon keyhole",
        "d4 entrance",
        "mt cucco gasha spot",
        "goron mountain right gasha spot",

        "enter mountain fairy cave",
        "enter talon cave",
        "enter winter cave in cucco mountain",
        "enter top of cucco mountain",
    ],
    "WESTERN_COAST": [
        "black beast's chest",
        "d0 entrance",
        "western coast after ship",
        "coast stump",
        "graveyard",
        "graveyard heart piece",
        "d7 entrance",
        "golden darknut",
        "western coast gasha spot",

        "enter old man near western coast house",
        "enter pirate ship",
        "enter beach fairy cave",
        "enter coast house",
        "enter coast house side",
        "enter graveyard cave",
        "outside graveyard chimney",
        "enter hidden graveyard stairs",
    ],
    "SPOOL_SWAMP": [
        "spool swamp north",
        "spool swamp middle",
        "spool swamp south",
        "spool swamp south near gasha spot",
        "spool swamp portal",
        "spool swamp digging spot",
        "spool swamp heart piece",
        "spool swamp tree",
        "floodgate keyhole",
        "spool stump",
        "dry swamp",
        "d3 entrance",
        "golden octorok",
        "spool swamp north gasha spot",
        "spool swamp south gasha spot",
        "open swamp bomb cave",

        "enter floodgate left",
        "enter floodgate right",
        "enter floodgate house",
        "enter swamp bomb cave",
    ],
    "TEMPLE_REMAINS": [
        "temple remains lower stump",
        "temple remains upper stump",
        "temple remains lower portal",
        "temple remains lower portal access",

        "enter d8 fairy room",
    ],
    "LOST_WOODS": [
        "tarm ruins",
        "lost woods plateau",
        "lost woods statue",
        "lost woods statues stump",
        "lost woods post statues stump",
        "lost woods stump",
        "golden lynel",

        "enter lost woods deku",
        "enter phonograph deku",
    ],
    "TARM_RUINS": [
        "d6 sector",
        "tarm ruins tree",
        "d6 entrance",
        "tarm ruins top",
        "tarm ruins gasha spot",

        "enter tarm ruins, under tree",
    ],
    "HORON_VILLAGE": [
        "horon village",
        "horon village tree",
        "horon village SE chest",
        "horon village SW chest",
        "horon heart piece",
        "horon gasha spot",

        "enter shop",
        "enter tick tock",
        "enter mayor's house",
        "enter vasu",
        "enter village portal room",
        "enter know-it-all birds",
        "enter bipin left",
        "enter bipin right",
        "enter advance shop",
        "enter dr left old man",
        "enter dr left",
        "enter dr left side",
        "enter hidden stairs behind clock shop",
    ],
    "NATZU": [
        "natzu west",
        "natzu river bank",
        "natzu west (ricky)",
        "natzu west (dimitri)",
        "natzu west (moosh)",
        "natzu east (ricky)",
        "natzu east (dimitri)",
        "natzu east (moosh)",
        "moblin keep bridge",
        "moblin keep",
        "natzu region, across water",

        "enter natzu north stairs",
    ],
    "SAMASA_DESERT": [
        "samasa desert",
        "samasa desert pit",
        "samasa desert chest",
        "samasa desert gasha spot",

        "enter desert fairy cave",
    ],
    "GORON_MOUNTAIN": [
        "biggoron trade",
        "goron mountain entrance",
        "goron blocked cave entrance",
        "goron mountain, across pits",
        "goron mountain left gasha spot",

        "enter goron mountain bottom",
        "enter goron mountain middle",
        "enter goron mountain top",
        "enter goron old man",
        "enter goron mountain bomb cave",
        "enter goron outside stairs",
    ],
    "SUBROSIA": [
        "volcanoes east portal",
        "subrosia temple sector",
        "subrosia market portal",
        "subrosia market sector",
        "strange brothers portal",
        "subrosia hide and seek sector",
        "house of pirates portal",
        "subrosia pirates sector",
        "great furnace portal",
        "subrosia furnace sector",
        "volcanoes west portal",
        "subrosia volcano sector",
        "d8 entrance portal",
        "d8 entrance",
        "subrosia east junction",
        "subrosia bridge sector",
        "subrosian buried bomb flower",
        "subrosia hide and seek",
        "subrosia seaside",
        "tower of spring",
        "subrosian wilds chest",
        "subrosian wilds digging spot",
        "subrosia village chest",
        "subrosian sign guy",
        "subrosia bath digging spot",
        "subrosia market digging spot",
        "subrosia temple digging spot",
        "subrosia bridge digging spot",

        # Temple area
        "enter open cave",
        "enter boomerang cave",
        "enter temple of seasons",
        "enter winter temple",
        "enter Rosa corridor left",
        "enter Summer tower",
        "enter Autumn tower",
        "enter Closed cave",
        "enter Useless subrosian house",
        "enter subrosian cook",
        "enter volcano cave",
        "enter dance hall",
        "enter tower of spring",
        "enter tower of spring staircase",

        # Market area
        "enter subrosian market",
        "enter Rosa corridor right",

        # Pirate area
        "enter house above hide and seek",
        "enter staircase to tower of spring",
        "enter strange brothers left",
        "enter strange brothers right",
        "enter pirate house",
        "enter pirate staircase",
    ],
    "CAVES": [
        "horon village portal",
        "advance shop",
        "dr. left reward",
        "old man trade",
        "malon trade",
        "talon trade",
        "syrup trade",
        "syrup shop",
        "mrs. ruul trade",
        "maple trade",
        "subrosian chef trade",
        "tick tock trade",
        "ingo trade",
        "guru-guru trade",
        "mayor's gift",
        "vasu's gift",
        "mayor's house secret room",
        "horon shop",
        "member's shop",
        "windmill heart piece",
        "holly's house",
        "cave outside D2",
        "woods of winter, 1st cave",
        "woods of winter, 2nd cave",
        "eastern suburbs spring cave",
        "spool swamp cave",
        "blaino prize",
        "old man in treehouse",
        "cave south of mrs. ruul",
        "cave north of D1",
        "floodgate keeper's house",
        "dry eyeglass lake, east cave",
        "dry eyeglass lake, west cave",
        "moblin keep chest",
        "master diver's challenge",
        "master diver's reward",
        "chest in master diver's cave",
        "sunken city, summer cave",
        "goron mountain",
        "goron's gift",
        "mt. cucco, platform cave",
        "diving spot outside D4",
        "chest in goron mountain",
        "lost woods deku",
        "phonograph deku",
        "tarm ruins, under tree",
        "temple remains heart piece",
        "temple remains upper portal",
        "maku seed",
        "pirate captain",
        "bomb temple remains",
        "subrosian dance hall",
        "subrosian smithy ore",
        "subrosian smithy bell",
        "subrosian house",
        "subrosian 2d cave",
        "temple of seasons",
        "tower of winter",
        "tower of summer",
        "tower of autumn",
        "subrosia market star ore",
        "subrosia market ore chunks",
        "subrosia, open cave",
        "subrosia, locked cave",
        "great furnace",
        "old man in horon",
        "old man near d1",
        "old man near blaino",
        "old man in goron mountain",
        "old man near western coast house",
        "old man near holly's house",
        "old man near mrs. ruul",
        "old man near d6",
        "golden beasts old man",

        # ER ################################################################
        # Horon Village
        "inside shop",
        "inside tick tock",
        "inside mayor's house",
        "inside vasu",
        "inside village portal room",
        "inside know-it-all birds",
        "inside bipin left",
        "inside bipin right",
        "inside advance shop",
        "inside dr left old man",
        "inside dr left",
        "inside dr left side",
        "inside hidden stairs behind clock shop",

        # Western Coast
        "inside old man near western coast house",
        "inside pirate ship",
        "inside beach fairy cave",
        "inside coast house",
        "inside coast house side",
        "inside graveyard cave",
        "inside graveyard chimney",
        "inside hidden graveyard stairs",

        # Eastern Suburbs
        "top guru guru staircase",
        "inside guru guru",
        "inside winter guru guru",
        "inside suburb spring cave",
        "inside suburbs old man",

        # Samasa Desert
        "inside desert fairy cave",

        # Woods of Winter
        "inside peek cave near d2",
        "inside magnet cave near d2",
        "inside first woods of winter cave",
        "inside second woods of winter cave",
        "inside holly house",
        "inside holly chimney",

        # Eyeglass Lake
        "inside lon lon",
        "inside d1 old man",
        "inside red ring old man",
        "inside lake bomb cave",
        "inside lake boulder",

        # Holodrum Plain
        "inside treehouse",
        "inside Mrs Ruul",
        "inside Blaino",
        "inside old man near blaino",
        "inside ruul old man",
        "inside ruul water cave",
        "inside autumn water cave",

        # Spool Swamp
        "inside floodgate left",
        "inside floodgate right",
        "inside floodgate house",
        "inside swamp bomb cave",

        # Natzu
        "inside natzu north stairs",

        # Sunken City
        "inside ingo",
        "inside syrup",
        "inside flooded house",
        "inside treasure hunter",
        "inside bomb house",
        "inside master diver",
        "inside sunken city, summer cave",

        # Cucco Mountain
        "inside mountain fairy cave",
        "inside talon cave",
        "inside winter cave in cucco mountain",
        "inside top of cucco mountain",

        # Goron Mountain
        "inside goron mountain bottom",
        "inside goron mountain middle",
        "inside goron mountain top",
        "inside goron old man",
        "inside goron mountain bomb cave",
        "inside goron outside stairs",

        # Lost Woods
        "inside lost woods deku",
        "inside phonograph deku",

        # Tarm Ruins
        "inside tarm ruins, under tree",

        # Temple Ruins
        "inside d8 fairy room",

        # Subrosia
        # Temple area
        "inside open cave",
        "inside boomerang cave",
        "inside temple of seasons",
        "inside winter temple",
        "inside Rosa corridor left",
        "inside Summer tower",
        "inside Autumn tower",
        "inside Closed cave",
        "inside Useless subrosian house",
        "inside subrosian cook",
        "inside volcano cave",
        "inside dance hall",
        "inside tower of spring",
        "inside tower of spring staircase",

        # Market area
        "inside subrosian market",
        "inside Rosa corridor right",

        # Pirate area
        "inside house above hide and seek",
        "inside staircase to tower of spring",
        "inside strange brothers left",
        "inside strange brothers right",
        "inside pirate house",
        "inside pirate staircase",
    ],
    "SPECIAL": [  # Seasons don't exist here
        "Menu",
        "maku tree",
        "maku tree, 3 essences",
        "maku tree, 5 essences",
        "maku tree, 7 essences",
        "d9 entrance",
        "onox beaten",
        "ganon beaten",
        "onox gasha spot",
        "lost woods",
        "warp to sunken city",
        "warp to d6 sector",

        "gasha tree 1",
        "gasha tree 2",
        "gasha tree 3",
        "gasha tree 4",
        "gasha tree 5",
        "gasha tree 6",
        "gasha tree 7",
        "gasha tree 8",
        "gasha tree 9",
        "gasha tree 10",
        "gasha tree 11",
        "gasha tree 12",
        "gasha tree 13",
        "gasha tree 14",
        "gasha tree 15",
        "gasha tree 16",
    ],
    "DUNGEONS": [
        "enter d0",
        "d0 key chest",
        "d0 rupee chest",
        "d0 hidden 2d section",
        "d0 sword chest",
        "enter d1",
        "d1 stalfos drop",
        "d1 floormaster room",
        "d1 boss",
        "d1 stalfos chest",
        "d1 goriya chest",
        "d1 lever room",
        "d1 block-pushing room",
        "d1 railway chest",
        "d1 button chest",
        "d1 basement",
        "enter d2",
        "d2 torch room",
        "d2 left from entrance",
        "d2 rope drop",
        "d2 arrow room",
        "d2 rupee room",
        "d2 rope chest",
        "d2 blade chest",
        "d2 alt entrances",
        "d2 roller chest",
        "d2 spiral chest",
        "d2 spinner",
        "dodongo owl",
        "d2 boss",
        "d2 hardhat room",
        "d2 pot chest",
        "d2 moblin chest",
        "d2 terrace chest",
        "enter d3",
        "spiked beetles owl",
        "d3 center",
        "d3 water room",
        "d3 mimic stairs",
        "trampoline owl",
        "d3 trampoline chest",
        "d3 zol chest",
        "d3 roller chest",
        "d3 quicksand terrace",
        "omuai owl",
        "d3 moldorm chest",
        "d3 bombed wall chest",
        "d3 mimic chest",
        "d3 omuai stairs",
        "d3 giant blade room",
        "d3 boss",
        "enter d4",
        "d4 north of entrance",
        "d4 pot puzzle",
        "d4 maze chest",
        "d4 dark room",
        "d4 water ring room",
        "d4 roller minecart",
        "d4 pool",
        "greater distance owl",
        "d4 stalfos stairs",
        "d4 terrace",
        "d4 miniboss room",
        "d4 final minecart",
        "d4 torch chest",
        "d4 cracked floor room",
        "d4 dive spot",
        "d4 basement stairs",
        "gohma owl",
        "enter gohma",
        "d4 boss",
        "enter d5",
        "d5 left chest",
        "d5 spiral chest",
        "d5 terrace chest",
        "armos knights owl",
        "d5 armos chest",
        "d5 cart bay",
        "d5 cart chest",
        "d5 pot room",
        "d5 spinner chest",
        "d5 drop ball",
        "d5 gibdo/zol chest",
        "d5 stalfos room",
        "d5 magnet ball chest",
        "d5 syger lobby",
        "d5 post syger",
        "d5 basement",
        "d5 boss",
        "enter d6",
        "d6 1F east",
        "d6 rupee room",
        "d6 1F terrace",
        "d6 magnet ball drop",
        "d6 crystal trap room",
        "d6 U-room",
        "d6 torch stairs",
        "d6 escape room",
        "d6 vire chest",
        "d6 beamos room",
        "d6 2F gibdo chest",
        "d6 2F armos chest",
        "d6 armos hall",
        "d6 spinner north",
        "enter vire",
        "d6 pre-boss room",
        "d6 boss",
        "enter d7",
        "poe curse owl",
        "d7 wizzrobe chest",
        "d7 bombed wall chest",
        "enter poe A",
        "d7 pot room",
        "d7 zol button",
        "d7 armos puzzle",
        "d7 magunesu chest",
        "d7 quicksand chest",
        "enter poe B",
        "d7 water stairs",
        "d7 darknut bridge trampolines",
        "d7 past darknut bridge",
        "d7 spike chest",
        "d7 maze chest",
        "d7 B2F drop",
        "d7 stalfos chest",
        "shining blue owl",
        "d7 right of entrance",
        "d7 boss",
        "enter d8",
        "d8 eye drop",
        "d8 three eyes chest",
        "d8 hardhat room",
        "d8 hardhat drop",
        "d8 spike room",
        "d8 spinner",
        "silent watch owl",
        "d8 magnet ball room",
        "d8 armos chest",
        "d8 spinner chest",
        "frypolar entrance",
        "frypolar room",
        "frypolar room wild mystery",
        "frypolar owl",
        "d8 darknut chest",
        "d8 ice puzzle room",
        "d8 pols voice chest",
        "d8 crystal room",
        "magical ice owl",
        "d8 ghost armos drop",
        "d8 NE crystal",
        "d8 SE crystal",
        "d8 SW lava chest",
        "d8 SE lava chest",
        "d8 spark chest",
        "d8 NW crystal",
        "d8 SW crystal",
        "d8 boss",

        "d4 miniboss room wild embers",
        "d7 entrance wild embers",
    ]
}

STUMP_REGIONS = {
    "horon village",
    "d1 stump",
    "suburbs",
    "suburbs fairy fountain",
    "moblin road",
    "enter suburbs old man",
    "d2 stump",
    "ghastly stump",
    "spool stump",
    "sunken city stump",
    "mount cucco",
    "mt. cucco, talon's cave entrance",
    "d5 stump",
    "tarm ruins",
    "lost woods statues stump",
    "lost woods post statues stump",
    "lost woods stump",
    "d6 sector",
    "coast stump",
    "temple remains lower stump",
    "temple remains upper stump",
}


class SeasonEntrance(Entrance):
    def __init__(self, player: int, name: str = "", parent: Region = None, randomization_group: int = 0,
                 randomization_type: EntranceType = EntranceType.ONE_WAY):
        super().__init__(player, name, parent, randomization_group, randomization_type)
        self.internal_entrance = False

    def can_reach(self, state: CollectionState) -> bool:
        if self.parent_region.can_reach(state):
            if self.internal_entrance:
                access, entrance, season = self.test_access_rule(state)
            else:
                access, season = self.test_access_rule(state)
                entrance = self
            if access:
                if not self.hide_path and self not in state.path:
                    if season == -1:
                        state.path[self] = (self.name, state.path.get(self.parent_region, (self.parent_region.name, None)))
                    else:
                        assert isinstance(entrance.parent_region, SeasonRegion)
                        state.path[self] = (self.name, state.path.get(entrance.parent_region.children_regions[season],
                                                                      (entrance.parent_region.children_regions[season].name, None)))
                return True
        return False

    def test_access_rule(self, state: CollectionState, season: int = -1) -> Union[Tuple[bool, int], Tuple[bool, Entrance, int]]:
        if self.internal_entrance:
            return self.access_rule(state)
        else:
            if self.access_rule.__code__.co_argcount == 1:
                return self.access_rule(state), -1
            else:
                if season == -1:
                    for season in range(4):
                        if isinstance(self.parent_region, SeasonRegion):
                            if (self.parent_region.children_regions[season].can_reach(state)
                                    and self.access_rule(state, season)):
                                return True, season
                    return False, -1
                else:
                    return self.access_rule(state, season), season

    def connect(self, region: Region, addresses: Any = None, target: Any = None) -> None:
        super().connect(region, addresses, target)
        parent: SeasonRegion = self.parent_region
        if parent is not None:
            if isinstance(region, SeasonRegion):
                for season in range(4):
                    parent.multiworld.register_indirect_condition(parent.children_regions[season], region)
                    for season2 in range(4):
                        parent.multiworld.register_indirect_condition(parent.children_regions[season], region.children_regions[season2])


class SeasonRegion(Region):
    entrance_type = SeasonEntrance

    def __init__(self, name: str, player: int, multiworld: MultiWorld, super_region_name: str, hint: Optional[str] = None):
        super().__init__(name, player, multiworld, hint)
        self.super_region_name = super_region_name
        self.children_regions = []
        world: "OracleOfSeasonsWorld" = multiworld.worlds[player]
        if super_region_name in world.default_seasons:
            default_season = world.default_seasons[super_region_name]
            force_season = False
        elif super_region_name == "NATZU":
            default_season = SEASON_SPRING
            force_season = True
        elif super_region_name == "SAMASA_DESERT":
            default_season = SEASON_SUMMER
            force_season = True
        elif super_region_name == "GORON_MOUNTAIN":
            default_season = SEASON_WINTER
            force_season = True
        else:
            default_season = -1
            force_season = False
        stump = self.name in STUMP_REGIONS
        for i in range(4):
            season = SEASON_NAMES[i]
            region = Region(f"{name} ({season})", player, multiworld)
            self.children_regions.append(region)
            multiworld.regions.append(region)

            if force_season:
                if default_season == i:
                    def rule(state: CollectionState) -> Tuple[bool, Entrance, int]:
                        return True, None, -1
                else:
                    def rule(state: CollectionState) -> Tuple[bool, Entrance, int]:
                        return False, None, -1
            elif default_season == -1:
                def rule(state: CollectionState, season: int = i) -> Tuple[bool, Entrance, int]:
                    for entrance in self.entrances:
                        assert isinstance(entrance, SeasonEntrance)
                        if isinstance(entrance.parent_region, SeasonRegion):
                            if entrance.parent_region.children_regions[season].can_reach(state):
                                if entrance.test_access_rule(state, season)[0]:
                                    return True, entrance, season
                    return False, None, -1
            elif default_season == i or default_season == SEASON_CHAOTIC:
                def rule(state: CollectionState, season: int = i) -> Tuple[bool, Entrance, int]:
                    if stump and state.has(SEASON_ITEMS[season], player):
                        return True, None, -1
                    for entrance in self.entrances:
                        assert isinstance(entrance, SeasonEntrance)
                        if isinstance(entrance.parent_region, SeasonRegion):
                            parent_super_region_name = entrance.parent_region.super_region_name
                            if parent_super_region_name == self.super_region_name or parent_super_region_name == "CAVES":
                                if entrance.parent_region.children_regions[season].can_reach(state):
                                    if entrance.test_access_rule(state, season)[0]:
                                        return True, entrance, season
                            else:
                                access, season = entrance.test_access_rule(state, -1)
                                if access:
                                    return True, entrance, season
                    return False, None, -1
            else:
                def rule(state: CollectionState, season: int = i) -> Tuple[bool, Entrance, int]:
                    if stump and state.has(SEASON_ITEMS[season], player):
                        return True, None, -1
                    for entrance in self.entrances:
                        assert isinstance(entrance, SeasonEntrance)
                        if isinstance(entrance.parent_region, SeasonRegion):
                            parent_super_region_name = entrance.parent_region.super_region_name
                            if parent_super_region_name == self.super_region_name or parent_super_region_name == "CAVES":
                                if entrance.parent_region.children_regions[season].can_reach(state):
                                    if entrance.test_access_rule(state, season)[0]:
                                        return True, entrance, season
                    return False, None, -1

            entrance: SeasonEntrance = self.connect(region, rule=rule)
            entrance.internal_entrance = True

    def connect(self, connecting_region: Region, name: Optional[str] = None, rule: Optional[Callable[[CollectionState], bool]] = None) -> entrance_type:
        entrance = super().connect(connecting_region, name, rule)
        if isinstance(connecting_region, SeasonRegion):
            for season in range(4):
                self.multiworld.register_indirect_condition(self.children_regions[season], connecting_region)
                for season2 in range(4):
                    self.multiworld.register_indirect_condition(self.children_regions[season], connecting_region.children_regions[season2])
        return entrance
