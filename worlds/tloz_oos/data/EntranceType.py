from enum import auto, Flag


class OoSEntranceType(Flag):
    OneWay = 0
    TwoWay = auto()
    Asymmetric = auto()
    TwoWayAsymmetric = TwoWay | Asymmetric

    DoorTransition = auto()
    DoorTwoWayFlag = auto()  # Flags that the entrance is two-way for ER purpose
    DoorOneWay = DoorTransition | OneWay
    DoorTwoWaySymmetric = DoorTwoWayFlag | DoorTransition | TwoWay
    DoorTwoWay = DoorTwoWaySymmetric | Asymmetric
    DoorComplexTwoWay = DoorTwoWayFlag | DoorTransition | OneWay  # The entrance is both way but the logic of each isn't None

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

    DiveFlag = auto()
    DiveOneWay = DoorOneWay | DiveFlag
    DiveTwoWay = DoorTwoWaySymmetric | DiveFlag

    D0Alt = auto()
    D0Chimney = DoorOneWay | D0Alt
    D2Alt = auto()
    D2Stairs = DoorTwoWay | D2Alt