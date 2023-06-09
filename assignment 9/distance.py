class Distance:
    def get_distance(self):
        distance=int(input("Enter the distance in km: "))
        self.distance=distance
    
    def print_distance(self):
        print("Distance in meteres: ",self.distance*1000)

d=Distance()
d.get_distance()
d.print_distance()
