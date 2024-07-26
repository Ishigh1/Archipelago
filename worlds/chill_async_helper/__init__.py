import json
import os
from typing import Any

from BaseClasses import Location
from worlds import AutoWorld
from worlds.LauncherComponents import Component, components, Type, launch_subprocess


def launch_client():
    from .Client import launch as ChillMain
    launch_subprocess(ChillMain, name="Chill Client")


class TrackerWorld:
    pass


old_call_stage = AutoWorld.call_stage


def call_stage(multiworld: "MultiWorld", method_name: str, *args: Any) -> None:
    old_call_stage(multiworld, method_name, *args)
    if method_name == "generate_output":
        spheres = multiworld.get_spheres()
        save_path = os.path.join(args[0], f"AP_{multiworld.seed_name}.apchill")

        json_spheres = []
        for sphere in spheres:
            json_sphere = []
            for location in sphere:
                location: Location
                if location.address:
                    json_sphere.append({
                        "name": location.name,
                        "address": location.address,
                        "player": location.player,
                    })
            if len(json_sphere) == 0:
                break
            json_spheres.append(json_sphere)

        with open(save_path, "w") as f:
            json.dump(json_spheres, f, indent=4)


AutoWorld.call_stage = call_stage

components.append(Component("Chill Helper", None, func=launch_client, component_type=Type.CLIENT))
