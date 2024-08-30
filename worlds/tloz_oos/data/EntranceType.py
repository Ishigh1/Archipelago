from enum import IntFlag


class OoSEntranceType(IntFlag):
    OneWay = 0b0
    TwoWay = 0b1
    DoorTransition = 0b10
    DoorTwoWayFlag = 0b100  # Flags that the entrance is two-way for ER purpose
    DoorOneWay = DoorTransition | OneWay
    DoorTwoWay = DoorTwoWayFlag | DoorTransition | TwoWay
    DoorComplexTwoWay = DoorTwoWayFlag | DoorTransition | OneWay  # The entrance is both way but the logic of each isn't None
