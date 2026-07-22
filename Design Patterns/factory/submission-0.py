from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def getType(self):
        pass


class Car(Vehicle):
    def getType(self):
        return "Car"


class Truck(Vehicle):
    def getType(self):
        return "Truck"


class Bike(Vehicle):
    def getType(self):
        return "Bike"


class VehicleFactory(ABC):
    @abstractmethod
    def createVehicle(self):
        pass


class CarFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Car()


class TruckFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Truck()


class BikeFactory(VehicleFactory):
    def createVehicle(self) -> Vehicle:
        return Bike()
