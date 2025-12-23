import os

from settings import get_settings
from worlds.tloz_oos.patching.RomData import RomData
from worlds.tloz_oos.spriter.sprite import bw_palette, link_palette
from worlds.tloz_oos.spriter.sprite.decoding import load_link_data, load_link_sprite
from worlds.tloz_oos.spriter.sprite.encoding import encode_sprite

if __name__ == "__main__":
    if not os.path.isdir("output"):
        os.mkdir("output")
    file_name = get_settings().tloz_oos_options.rom_file
    rom = RomData(bytes(open(file_name, "rb").read()))
    sprite_data = load_link_data(rom)
    image = load_link_sprite(sprite_data, True)
    image.putpalette(bw_palette, "RGBA")
    image.save("output/link_bw.png")
    image.putpalette(link_palette, "RGBA")
    image.save("output/link_g.png")

    # Test encoder
    encoded = encode_sprite(image)
    image = load_link_sprite(encoded, True)
    image.putpalette(bw_palette, "RGBA")
    image.save("output/link_bw_2.png")

