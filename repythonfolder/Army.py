import Territory
import Unit
class Army(Unit.Unit):  
    
    unitType = "Army"
    
    def move(self,territory):
        return Unit.Unit.move(self,territory)

    def unitValue(self):
        return self.location.armyVal()