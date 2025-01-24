# List of tags :
# High Damage : can deal 4+ damage in an attack
# Triple Kill : Can kill 3 veks in an attack
# Forced Move : Can move veks once per round
# Triple Push : Can push 3 enemies with a single attack
# Quadruple Move : Can move 4 units with it
# Deadly pull : Can pull to self
# Charge : Can charge 4 tiles towards an enemy and kill it
# Fire : can make 5 fire in a mission
# Triple Fire : Can light 3 units on fire at once
# Smoke : Can generate 5 smoke in a mission
# Electric Smoke : ["Storm Generator"]
# Electric Smoke 2 : upgraded storm generator
# Laser : ["Burst Beam", "Prism Laser", "Refractor Laser", "Fire Beam", "Frost Beam"] extends LaserDefault in code
# Shield : Can create 4 shields in a mission
# Chain : can target 10+ tiles in a single attack
# Summon : Can add pawns
# Many Summons : Can summon something at least thrice per mission
# Hoard Summons : Can summon something at least thrice per mission then kill them at once
# Teleport : "Teleporter" 3 cores
# Freeze : Can freeze 8 units in a mission
# Heal : Heal at least 5 damage in a mission
# ACID : Can give acid debuff
# Boost : Can boost 5 times in a mission
# Crack : Can crack 10 tiles in one mission
# Fire Boost : Heat Engine
# Smoke Heal : Nanofilter Mending
# Hormones : Vek Hormones
from typing import Iterable

tag_implications = {
    "Triple Push": ("Quadruple Move",),
    "Triple Kill": ("Triple Push",),
    "Triple Fire": ("Fire", "Triple Push",),
    "Summon": ("Many Summons",),
    "Many Summons": ("Hoard Summons",),
    "Boost": ("Fire Boost", "Fire",),
    "Heal": (("Smoke Heal", "Boost"), ("Smoke", "Boost"),),
}


def add_implied_tag(tags: dict[str, int], result: str, requirements: Iterable[str]):
    """
    Add an implied tag to the tags dictionary if all the required tags exist.
    """
    total_core_requirement = 0
    for tag in requirements:
        if tag not in tags:
            return
        core_requirement = tags[tag]
        if core_requirement > total_core_requirement:
            total_core_requirement = core_requirement
    if result not in tags or total_core_requirement < tags[result]:
        tags[result] = total_core_requirement


def expand_tags(tags: dict[str, int]):
    """
    Add implied tags based on existing tags in the dictionary.
    """
    for result in tag_implications:
        add_implied_tag(tags, result, tag_implications[result])


def add_tags(tags: dict[str, int], new_tags: dict[str, int]):
    for tag in new_tags:
        cores = new_tags[tag]
        if tag not in tags or cores < tags[tag]:
            tags[tag] = cores
    expand_tags(tags)
