import json
import os

from worlds.into_the_breach import IntoTheBreachWorld

if __name__ == "__main__":
    if not os.path.isdir("output"):
        os.mkdir("output")

    with open("output/mapping.json", "w+") as f:
        json.dump({
            "item_id_to_name": IntoTheBreachWorld.item_id_to_name,
            "location_id_to_name": IntoTheBreachWorld.location_id_to_name,
            "location_name_to_id": IntoTheBreachWorld.location_name_to_id
        }, f, indent=2)
