class House:
    def __init__(self, number_of_floors):
        self.numberOfFloors = 0


    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)


h = House(3)
h.setNewNumberOfFloors(14)

