class Flight:

    counter = 1

    def __init__(self, origin, destination, duration):
        self.id = Flight.counter
        Flight.counter += 1
        self.passengers = []
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")
        print()
        for item in self.passengers:
            print(f"{item.name}")

    def delay(self, amount):
        self.duration += amount

    def add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id

class Passenger:
    def __init__(self, name):
        self.name = name

def main():
    f = Flight(origin="New York", destination="Paris", duration=540)
    f.delay(10)
    f.print_info()

    print("----------------------------")

    f2 = Flight("Chennai", "Bangalore", 512)
    p = Passenger("Kaushik")
    f2.add_passenger(p)
    f2.print_info()

if __name__ == "__main__":
    main()
