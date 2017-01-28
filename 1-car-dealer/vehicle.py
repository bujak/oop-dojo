class Vehicle:
    def __init__(self):
        self.ccm = 1
        self.top_speed = 1

if __name__ == '__main__':

    vehicle = Vehicle(12, 200)
    print(vehicle.__dict__)
