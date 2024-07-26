import asyncio
import json
import logging
import urllib.parse

from CommonClient import CommonContext, gui_enabled, get_base_parser, server_loop, ClientCommandProcessor
from Utils import open_filename

logger = logging.getLogger("Client")

ITEMS_HANDLING = 0b111


class ChillCommandProcessor(ClientCommandProcessor):
    def _cmd_sphere(self):
        """Print the current sphere"""
        logger.info("Current Sphere:")
        if len(self.ctx.sphere) == 0:
            logger.info("No sphere!")
            return
        for location in self.ctx.spheres[0]:
            logger.info(f"{location['name']} (Player {location['player']})")

    def _cmd_sphere_release(self):
        """Print the current sphere"""
        logger.info("Current Sphere:")
        if len(self.ctx.sphere) == 0:
            logger.info("No sphere!")
            return
        for location in self.ctx.spheres[0]:
            logger.info(f"/send_location {self.ctx.player_names[location['player']]} {location['name']}")


class ChillGameContext(CommonContext):
    game = ""
    tags = CommonContext.tags | {"Tracker"}
    command_processor = ChillCommandProcessor
    file_name = None
    spheres = None

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.items_handling = ITEMS_HANDLING
        self.locations_checked = []

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(ChillGameContext, self).server_auth(password_requested)

        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict):
        if cmd == 'Connected':
            self.update_spheres()
        elif cmd == 'RoomUpdate':
            self.update_spheres()

    def update_spheres(self):
        if self.slot:
            for sphere in self.spheres:
                locations_to_remove = []
                for location in sphere:
                    if location["player"] == self.slot:
                        if location["address"] in self.checked_locations:
                            locations_to_remove.append(location)
                for location in locations_to_remove:
                    sphere.remove(location)

            while len(self.spheres) > 0:
                if len(self.spheres[0]) > 0:
                    break
                del self.spheres[0]
            with open(self.file_name, "w") as f:
                json.dump(self.spheres, f, indent=4)

    def init_spheres(self):
        if self.file_name:
            self.spheres = json.load(open(self.file_name))


async def main(args):
    ctx = ChillGameContext(args.connect, args.password)
    ctx.file_name = open_filename("Select patch", (("Spheres file", [".apchill"]),))
    ctx.auth = args.name
    ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")

    ctx.init_spheres()

    if gui_enabled:
        ctx.run_gui()
    ctx.run_cli()

    await ctx.exit_event.wait()
    await ctx.shutdown()


def launch():
    parser = get_base_parser(description="Gameless Archipelago Client, for text interfacing.")
    parser.add_argument('--name', default=None, help="Slot Name to connect as.")
    parser.add_argument("url", nargs="?", help="Archipelago connection url")
    args = parser.parse_args()

    if args.url:
        url = urllib.parse.urlparse(args.url)
        args.connect = url.netloc
        if url.username:
            args.name = urllib.parse.unquote(url.username)
        if url.password:
            args.password = urllib.parse.unquote(url.password)

    asyncio.run(main(args))
