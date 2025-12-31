#1.
class Vehicle:
    pass
#2.
class Vehicle:
    def __init__(self, mileage, max_speed):
        self.max_speed = max_speed
        self.mileage = mileage

#5.
    def seating_capacity(self, capacity):
        self.capacity =capacity
        print(capacity)
#7.
    def fare(self):
        return self.capacity*100
#3.
class Bus (Vehicle):
    def __init__(self, mileage, max_speed):
        super().__init__(mileage, max_speed)
        print(max_speed)
        print(mileage)

 #6.
    def seating_capacity(self, capacity= 50):
        self.capacity =capacity
        return super().seating_capacity(capacity)

    def fare(self):
        return super().fare() + 50 



#4.
Vehicle.color="white"




