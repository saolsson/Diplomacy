import Territory
import Unit
class Navy(Unit.Unit): 
    
    unitType = "Navy"
       
    def move(self,territory):
        return Unit.Unit.move(self,territory)

    def unitValue(self):
        return self.location.navyVal()