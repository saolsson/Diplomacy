class Country:
    def __init__(self,name,parentList=[],startingUnits=[]):
        self.name = name
        parentList.append(self)
        self.units = []
        self.homeCenters = []
        self.centers = []
        self.startingValue = 0
        self.value = 0
        for startingUnit in startingUnits:
            unit = startingUnit.unit
            territory = startingUnit.territory
            territory.setCountry(self,unit)
            unit.location = territory
            unit.country = self
            self.units.append(unit)
            self.homeCenters.append(territory)
            self.centers.append(territory)
            self.startingValue += unit.unitValue()
        self.value = self.startingValue
    
    def move(self, embark, terminus):
        import Territory
        for unit in self.units:
            if (unit.location == embark):
                theUnit = unit
   
        if(theUnit):
            #moved = theUnit.move(terminus)
            print(theUnit.move(terminus))
            #if (moved):
            #    print(theUnit.unitType + " " + embark.name + " moved to " + terminus.name)
            #else:
            #    print("Illegal move " + theUnit.unitType + " " + embark.name + " - " + terminus.name + " replaced with hold.")
        
        self.updateValues()

    def updateValues(self):
        self.value = 0
        for unit in self.units:
            self.value += unit.unitValue()

    def printValue(self):
        print(self.name + " currently has value " + str(round(self.value,2)))

    def printHomeCenters(self):
        print(self.name + " Home Centers: ")
        for center in self.homeCenters:
            print("    " + center.name)

    def printCenters(self):
        print(self.name + " Current Centers: ")
        for center in self.centers:
            print("    " + center.name)

    def printUnits(self,printVals=False):
        print(self.name + " Current Units: ")
        for unit in self.units:
            displayString = "    " +  unit.unitType + " " + unit.location.name
            if(printVals):
                displayString += " with value " + str(round(unit.unitValue(),2))
            print(displayString)

    def printUnitValues(self):
        self.printUnits(True)
