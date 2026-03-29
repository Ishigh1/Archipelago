import os

from ..common.patching.Util import simple_hex
from ..common.patching.z80asm.Assembler import GameboyAddress, Z80Assembler


def make_sym(assembler: Z80Assembler):
    if not os.path.isdir("output"):
        os.mkdir("output")

    with open("output/seasons.sym", "w+", encoding="utf-8") as f:
        for label in assembler.global_labels:
            address: GameboyAddress = assembler.global_labels[label]
            f.write(f"{simple_hex(address.bank)}:{address.to_word()[1:]} {label}\n")