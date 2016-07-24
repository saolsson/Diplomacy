#import Territory
#import Country
class Unit:
    def __init__(self,country="",territory=""):
        if(country != ""):
            self.country = country
        if(territory != ""):
            self.location = territory

    def move(self,territory):
        order = str(self.unitType + " " + self.location.name + " -> " + territory.name)
        moved = str("Illegal order " + order + " replaced with hold order.")
        for conn in self.location.connections:
            otherTerr = conn.otherTerritory(self.location)
            if (otherTerr == territory):
                if ((self.unitType == "Army" and conn.armyConn) or (self.unitType == "Navy" and conn.navyConn)):
                    unitThere = bool(otherTerr.unitInTerritory())
                    if (not unitThere):
                        moved = str("Successful move " + order)
                        self.location = territory
                        territory.country = self.country
                    else:
                        if(self.country == territory.unit.country):
                            moved = str("Cannot displace your own unit in " + territory.name + "; " + order + " unsuccessful.")
                        else:
                            moved = str("Unable to displace unit in " + territory.name + "; " + order + " unsuccessful.")
                else:
                    if (self.unitType == "Army"):
                        moved = str("Cannot move " + self.unitType + " into sea; " + order + " unsuccessful.")
                    else:
                        moved = str("Cannot move " + self.unitType + " farther inland than the coast; " + order + " unsuccessful.")
        return moved

    def unitValue(self):
        return self.location.value()