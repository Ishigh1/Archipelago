from enum import auto, Flag, IntEnum


class OoSEntranceType(Flag):
    OneWay = 0
    TwoWay = auto()
    Asymmetric = auto()
    TwoWayAsymmetric = TwoWay | Asymmetric

    DoorTransition = auto()
    DoorTwoWayFlag = auto()  # Flags that the entrance is two-way for ER purpose
    DoorOneWay = DoorTransition | OneWay
    DoorTwoWaySymmetric = DoorTwoWayFlag | DoorTransition | TwoWay  # Rule from right to left is the same
    DoorTwoWay = DoorTwoWaySymmetric | Asymmetric  # Rule from right to left is None
    DoorComplexTwoWay = DoorTwoWayFlag | DoorTransition | OneWay  # The entrance is both way but the logic of each isn't None

    Compact = auto()  # Second "region" is now considered the same as the first one, doesn't support any rule
    ReverseCompact = Compact | TwoWay  # First "region" is now considered the same as the second one, doesn't support any rule

    Ricky = auto()
    Moosh = auto()
    Dimitri = auto()
    CompanionEntrance = Ricky | Moosh | Dimitri

    OneWayRicky = OneWay | Ricky
    TwoWayRicky = TwoWay | Ricky

    TwoWayMoosh = TwoWay | Moosh

    OneWayDimitri = OneWay | Dimitri
    TwoWayDimitri = TwoWay | Dimitri
    TwoWayAsymmetricDimitri = TwoWay | Asymmetric | Dimitri

    DoorTwoWayRicky = DoorTwoWay | Ricky
    DoorTwoWayMoosh = DoorTwoWay | Moosh
    DoorTwoWayDimitri = DoorTwoWay | Dimitri

    WaterfallFlag = auto()
    Waterfall = DoorTwoWay | WaterfallFlag
    WaterfallDimitri = Waterfall | Dimitri

    D0Alt = auto()
    D0Chimney = DoorOneWay | D0Alt
    D2Alt = auto()
    D2Stairs = DoorTwoWay | D2Alt

    DungeonFlag = auto()
    DungeonEntrance = TwoWay | DoorTwoWayFlag | DungeonFlag

    PortalFlag = auto()
    Portal = TwoWay | DoorTwoWayFlag | PortalFlag

    DiveFlag = auto()
    DiveOneWay = DoorOneWay | DiveFlag
    DiveTwoWay = DoorTwoWay | DiveFlag


class OoSRandomizationGroup(IntEnum):
    Normal = auto()
    Waterfall = auto()
    Dive = auto()
    DungeonOutside = auto()
    DungeonInside = auto()
    PortalOverworld = auto()
    PortalSubrosia = auto()
