from .Options import itb_options
from .Items import itb_items
from .Locations import itb_locations
from worlds.AutoWorld import World
from .Squads import shuffle_teams
from jinja2 import Environment, FileSystemLoader
import os

class IntoTheBreachWorld(World):
    """A strategy turn based game"""
    game = "Into The Breach"
    option_definitions = itb_options
    topology_present = True

    base_id = 6777699702823011 #thanks random.org

    item_name_to_id = {name: id for
                       id, name in enumerate(itb_items, base_id)}
    location_name_to_id = {name: id for
                           id, name in enumerate(itb_locations, base_id)}
    
    item_name_groups = {
    }

    def generate_early(self):
        self.randomized_squads = shuffle_teams(self.multiworld.random)

    def generate_output(self, output_directory: str):

        # Create the Jinja environment
        jinja_template_env = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'mod_template')))

        # Load the template
        template = jinja_template_env.get_template('squads.lua')

        squad_lua = template.render(squads_list= self.randomized_squads)

        with open(os.path.join(output_directory, "squad.lua"), "w") as file:
            file.write(squad_lua)
