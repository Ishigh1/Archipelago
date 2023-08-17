# List of tags :
# High Damage : can deal 4+ damage in an attack
# Triple Kill : Can kill 3 veks in an attack
# Forced Move : Can move veks once per round
# Triple Push : Can push 3 enemies with a single attack
# Deadly pull : ["Attraction Pulse", "Gravity Mirror", "Pull-Tank"] -> Can pull to self
# Charge : Can charge 4 tiles towards an enemy and kill it
# Fire : can make 5 fire in a mission
# Smoke : Can generate 5 smoke in a mission
# Electric Smoke : ["Storm Generator"]
# Laser : ["Burst Beam", "Prism Laser", "Refractor Laser", "Fire Beam", "Frost Beam"] extends LaserDefault in code
# Shield : Can create 4 shields in a mission
# Chain : can target 10+ tiles in a single attack
# Summon : Can create allies
# Teleport : "Teleporter" 3 cores
# Freeze : Can freeze 8 units in a mission
# Heal : Heal at least 5 damage in a mission
# ACID : Can give acid debuff
# Boost : Can boost once in a mission
# Fire Boost : Heat Engine
# Smoke Heal : Nanofilter Mending
# Hormones : Vek Hormones

def add_tag(tags: dict[str, int], tag: str, value: int):
    """
    Add a tag to the tags dictionary. If the tag already exists, take the minimum value.
    """
    if tag not in tags:
        tags[tag] = value
    else:
        tags[tag] = min(tags[tag], value)


def add_implied_tag(tags: dict[str, int], result: str, *requirements: str):
    """
    Add an implied tag to the tags dictionary if all the required tags exist.
    """
    max_value = 0
    for tag in requirements:
        if tag in tags:
            max_value = max(max_value, tags[tag])
        else:
            return
    add_tag(tags, result, max_value)


def expand_tags(tags: dict[str, int]):
    """
    Add implied tags based on existing tags in the dictionary.
    """
    add_implied_tag(tags, "Triple Kill", "Triple Push")
    add_implied_tag(tags, "Boost", "Fire Boost", "Fire")
    add_implied_tag(tags, "Heal", "Smoke Heal", "Smoke")


def add_tags(tags: dict[str, int], new_tags: dict[str, int]):
    for tag in new_tags:
        add_tag(tags, tag, new_tags[tag])
    expand_tags(tags)
