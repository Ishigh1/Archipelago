import os

import kvui  # noqa: F401 isort: skip

import shutil
from pathlib import Path

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivymd.uix.button import MDButton, MDButtonText

import Utils
from CommonClient import gui_enabled
from settings import get_settings

from ...patching.RomData import RomData
from ..microbmp import MicroBMP
from ..sprite import bw_palette, link_palette
from ..sprite.decoding import load_link_data, load_link_sprite
from ..sprite.encoding import encode_sprite, has_separator, remap_sprite


async def main() -> None:
    if not gui_enabled:
        raise RuntimeError("GUI not enabled.")

    Utils.init_logging("Oracle of Seasons Sprite Editor")
    ImageApp().run()


class ImageApp(MDApp):
    def build(self):
        self.sprite_folder = Path(Utils.cache_path("oos_ooa/sprites"))
        self.sprite_folder.mkdir(parents=True, exist_ok=True)

        layout = BoxLayout(orientation="vertical")

        self.img = Image(source="", fit_mode="contain", size_hint_y=1)
        layout.add_widget(self.img)

        bar = BoxLayout(orientation="horizontal", size_hint_y=None, height=48)
        bar.add_widget(MDButton(MDButtonText(text="Load Link"), on_release=self.load_link))
        bar.add_widget(MDButton(MDButtonText(text="Load Sprite"), on_release=self.load_sprite))
        bar.add_widget(MDButton(MDButtonText(text="Switch Palette"), on_release=self.switch_palette))
        bar.add_widget(MDButton(MDButtonText(text="Switch Separator"), on_release=self.switch_separator))
        bar.add_widget(MDButton(MDButtonText(text="Export Image"), on_release=self.export_image))
        bar.add_widget(MDButton(MDButtonText(text="Export Binary"), on_release=self.export_binary))
        layout.add_widget(bar)

        bar2 = BoxLayout(orientation="horizontal", size_hint_y=None, height=48)
        bar2.add_widget(MDButton(MDButtonText(text="Select sprite as default"), on_release=self.select_sprite))
        layout.add_widget(bar2)
        return layout

    def load_link(self, *_) -> None:
        file_name = str(self.sprite_folder.joinpath("link.png"))

        rom_file = get_settings().tloz_oos_options.rom_file
        rom = RomData(bytes(open(rom_file, "rb").read()))
        sprite_data = load_link_data(rom)
        image = load_link_sprite(sprite_data)
        image.palette = link_palette
        image.save(file_name)

        self.img.source = file_name
        self.img.reload()
        self.img.texture.mag_filter = "nearest"  # prevents blur when scaling up
        self.img.texture.min_filter = "nearest"  # prevents blur when scaling down

    def load_sprite(self, *_) -> None:
        file_name = Utils.open_filename(
            "Select sprite file", (("*", (".bin", ".png")), ("Binary", (".bin",)), ("Image", (".png",)))
        )
        if not file_name:
            return

        new_file_name = str(self.sprite_folder.joinpath(f"{Path(file_name).stem}.png"))
        if file_name.endswith(".bin"):
            image = load_link_sprite(Path(file_name).read_bytes())
            image.palette = link_palette
            image.save(new_file_name)
        else:
            image = MicroBMP().load(file_name)
            remap_sprite(image)
            image.save(new_file_name)
        self.img.source = new_file_name
        self.img.reload()
        self.img.texture.mag_filter = "nearest"  # prevents blur when scaling up
        self.img.texture.min_filter = "nearest"  # prevents blur when scaling down

    def switch_palette(self, *_) -> None:
        if self.img.source == "":
            return

        image = MicroBMP().load(self.img.source)
        remap_sprite(image)
        if image.palette == bw_palette:
            image.palette = link_palette
        else:
            image.palette = bw_palette
        image.save(self.img.source)
        self.img.reload()
        self.img.texture.mag_filter = "nearest"  # prevents blur when scaling up
        self.img.texture.min_filter = "nearest"  # prevents blur when scaling down

    def switch_separator(self, *_) -> None:
        if self.img.source == "":
            return

        image = MicroBMP().load(self.img.source)
        remap_sprite(image)
        if image.palette == bw_palette:
            palette = bw_palette
        else:
            palette = link_palette

        encoded = encode_sprite(image)
        image = load_link_sprite(encoded, not has_separator(image))
        image.palette = palette
        image.save(self.img.source)
        self.img.reload()
        self.img.texture.mag_filter = "nearest"  # prevents blur when scaling up
        self.img.texture.min_filter = "nearest"  # prevents blur when scaling down

    def export_image(self, *_) -> None:
        if self.img.source == "":
            return

        image_name = Path(self.img.source).stem
        file_path = Utils.save_filename("Save sprite file", (("PNG", (".png",)),), f"{image_name}.png")
        if not file_path:
            return
        shutil.copy(self.img.source, file_path)

    def export_binary(self, *_) -> None:
        if self.img.source == "":
            return

        image_name = Path(self.img.source).stem
        file_path = Utils.save_filename("Save sprite binary", (("BIN", (".bin",)),), f"{image_name}.bin")
        if not file_path:
            return

        image = MicroBMP().load(self.img.source)
        remap_sprite(image)
        encoded = encode_sprite(image)

        with open(file_path, "wb") as f:
            f.write(encoded)

    def select_sprite(self, *_) -> None:
        if self.img.source == "":
            return
        image = MicroBMP().load(self.img.source)
        remap_sprite(image)
        encoded = encode_sprite(image)

        image_name = Path(self.img.source).stem
        if image_name == "link":
            image_name = "custom sprite"
        sprite_folder = Utils.local_path(os.path.join("data", "sprites", "oos_ooa"))
        if not os.path.exists(sprite_folder):
            os.makedirs(sprite_folder)
        file_path = Path(sprite_folder, f"{image_name}.bin")
        with open(file_path, "wb") as f:
            f.write(encoded)

        settings = get_settings()
        settings.tloz_oos_options.character_sprite = image_name
        settings.tloz_oos_options._changed = True
