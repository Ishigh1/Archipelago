import asyncio

import colorama

from worlds.LauncherComponents import Component, Type, components, launch

component_name = "Oracle of Seasons sprite editor"


def run_client() -> None:
    launch(launch_sprite_editor, name=component_name)


def launch_sprite_editor() -> None:
    from .client import main

    colorama.just_fix_windows_console()

    asyncio.run(main())
    colorama.deinit()


component = Component(component_name,
                      component_type=Type.TOOL, func=run_client,
                      description="An UI to extract and manipulates Link's sprite in Oracle of Seasons.")
components.append(component)
