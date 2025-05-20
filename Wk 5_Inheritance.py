# Base class: ElectronicDevice
class ElectronicDevice:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life  # in hours

    def power_on(self):
        print(f"{self.brand} {self.model} is now ON.")

    def power_off(self):
        print(f"{self.brand} {self.model} is now OFF.")


# Derived class: Smartphone inherits from ElectronicDevice
class Smartphone(ElectronicDevice):
    def __init__(self, brand, model, battery_life, os, camera_megapixels):
        super().__init__(brand, model, battery_life)  # initialize base class attributes
        self.os = os
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"Taking a photo with {self.camera_megapixels}MP camera on {self.brand} {self.model}.")

    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.os} smartphone.")


# Create objects
phone1 = Smartphone("Apple", "iPhone 14", 20, "iOS", 12)
phone2 = Smartphone("Samsung", "Galaxy S22", 24, "Android", 108)

# Use methods
phone1.power_on()
phone1.take_photo()
phone1.install_app("Instagram")
phone1.power_off()

print("---")

phone2.power_on()
phone2.take_photo()
phone2.install_app("WhatsApp")
phone2.power_off()
