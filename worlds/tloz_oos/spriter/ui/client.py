# noinspection PyUnusedImports
import kvui
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonText

import shutil
from pathlib import Path
from PIL import Image as PILImage
import Utils
from CommonClient import gui_enabled
from settings import get_settings
from ...patching.RomData import RomData
from ..sprite import link_palette, bw_palette
from ..sprite.decoding import load_link_sprite, load_link_data
from ..sprite.encoding import remap_sprite, has_separator, encode_sprite


async def main() -> None:
    if not gui_enabled:
        raise RuntimeError("GUI not enabled.")

    Utils.init_logging(f"Oracle of Seasons Sprite Editor")
    ImageApp().run()


class ImageApp(MDApp):
    def build(self):
        self.sprite_folder = Path(Utils.cache_path("oos_ooa/sprites"))
        self.sprite_folder.mkdir(parents=True, exist_ok=True)

        layout = BoxLayout(orientation="vertical")

        self.img = Image(
            source="",
            fit_mode="contain"
        )
        layout.add_widget(self.img)

        bar = BoxLayout(
            orientation="horizontal",
            height=48
        )
        layout.add_widget(bar)

        bar.add_widget(MDButton(MDButtonText(
            text="Load Link"),
            on_release=self.load_link
        ))

        bar.add_widget(MDButton(MDButtonText(
            text="Load Sprite"),
            on_release=self.load_sprite
        ))

        bar.add_widget(MDButton(MDButtonText(
            text="Switch Palette"),
            on_release=self.switch_palette
        ))

        bar.add_widget(MDButton(MDButtonText(
            text="Switch Separator"),
            on_release=self.switch_separator
        ))

        bar.add_widget(MDButton(MDButtonText(
            text="Export Image"),
            on_release=self.export_image
        ))

        bar.add_widget(MDButton(MDButtonText(
            text="Export Binary"),
            on_release=self.export_binary
        ))

        bar2 = BoxLayout(
            orientation="horizontal",
            height=48
        )
        layout.add_widget(bar2)

        bar2.add_widget(MDButton(MDButtonText(
            text="Select sprite as default"),
            on_release=self.select_sprite
        ))
        return layout

    def load_link(self, *_) -> None:
        file_name = str(self.sprite_folder.joinpath(f"link.png"))

        rom_file = get_settings().tloz_oos_options.rom_file
        rom = RomData(bytes(open(rom_file, "rb").read()))
        sprite_data = load_link_data(rom)
        image = load_link_sprite(sprite_data)
        image.putpalette(link_palette, "RGBA")
        image.save(file_name)

        self.img.source = file_name
        self.img.reload()
        self.img.texture.mag_filter = 'nearest'  # prevents blur when scaling up
        self.img.texture.min_filter = 'nearest'  # prevents blur when scaling down

    def load_sprite(self, *_) -> None:
        file_name = Utils.open_filename("Select sprite file", (
            ("*", (".bin", ".png")),
            ("Binary", (".bin",)),
            ("Image", (".png",))
        ))
        if not file_name:
            return

        new_file_name = str(self.sprite_folder.joinpath(f"{Path(file_name).stem}.png"))
        if file_name.endswith(".bin"):
            image = load_link_sprite(Path(file_name).read_bytes())
            image.putpalette(link_palette, "RGBA")
            image.save(new_file_name)
        else:
            image = PILImage.open(file_name)
            image = remap_sprite(image)
            image.save(new_file_name)
        self.img.source = new_file_name
        self.img.reload()
        self.img.texture.mag_filter = 'nearest'  # prevents blur when scaling up
        self.img.texture.min_filter = 'nearest'  # prevents blur when scaling down

    def switch_palette(self, *_) -> None:
        if self.img.source == "":
            return

        image = PILImage.open(self.img.source)
        image = remap_sprite(image)
        if image.getpalette("RGBA")[3] == 255:
            image.putpalette(link_palette, "RGBA")
            image.save(self.img.source)
        else:
            image.putpalette(bw_palette, "RGBA")
            image.save(self.img.source)
        self.img.reload()
        self.img.texture.mag_filter = 'nearest'  # prevents blur when scaling up
        self.img.texture.min_filter = 'nearest'  # prevents blur when scaling down

    def switch_separator(self, *_) -> None:
        if self.img.source == "":
            return

        image = PILImage.open(self.img.source)
        image = remap_sprite(image)
        if image.getpalette("RGBA")[3] == 255:
            palette = bw_palette
        else:
            palette = link_palette

        encoded = encode_sprite(image)
        image = load_link_sprite(encoded, not has_separator(image))
        image.putpalette(palette, "RGBA")
        image.save(self.img.source)
        self.img.reload()
        self.img.texture.mag_filter = 'nearest'  # prevents blur when scaling up
        self.img.texture.min_filter = 'nearest'  # prevents blur when scaling down

    def export_image(self, *_) -> None:
        if self.img.source == "":
            return

        file_path = Utils.save_filename("Save sprite file", (("PNG", (".png",)),), "link.png")
        if not file_path:
            return
        shutil.copy(self.img.source, file_path)

    def export_binary(self, *_) -> None:
        if self.img.source == "":
            return

        file_path = Utils.save_filename("Save sprite binary", (("BIN", (".bin",)),), "link.bin")
        if not file_path:
            return

        image = PILImage.open(self.img.source)
        image = remap_sprite(image)
        encoded = encode_sprite(image)

        with open(file_path, "wb") as f:
            f.write(encoded)

    def select_sprite(self, *_) -> None:
        if self.img.source == "":
            return
        # todo
