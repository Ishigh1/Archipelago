from BaseClasses import Location

class MyGameLocation(Location):
    game = "Into The Breach"

    # override constructor to automatically mark event locations as such
    def __init__(self, player: int, name = "", code = None, parent = None):
        super(MyGameLocation, self).__init__(player, name, code, parent)
        self.event = code is None

itb_locations = {
    
}