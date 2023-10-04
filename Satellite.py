class Satellite:
    def __init__(self):
        self.orientation = "North"
        self.solar_panels = "Inactive"
        self.data_collected = 0

    def rotate(self, direction):
        if direction in ["North", "South", "East", "West"]:
            self.orientation = direction
        else:
            print("Invalid direction. Use North, South, East, or West.")

    def activatePanels(self):
        self.solar_panels = "Active"

    def deactivatePanels(self):
        self.solar_panels = "Inactive"

    def collectData(self):
        if self.solar_panels == "Active":
            self.data_collected += 10
        else:
            print("Solar panels are inactive. Cannot collect data.")

# Example usage
satellite = Satellite()
satellite.rotate(input("Direction : "))
Pannel = input("pannel status : ")
if Pannel == "Activate":
    satellite.activatePanels()
else:
    satellite.deactivatePanels()

satellite.collectData()

print(f"Orientation: {satellite.orientation}")
print(f"Solar Panels: {satellite.solar_panels}")
print(f"Data Collected: {satellite.data_collected}")
