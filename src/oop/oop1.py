"""
Write classes for the following class hierarchy:

 [Vehicle]->[FlightVehicle]->[Starship]
     |                |
     v                v
[GroundVehicle]      [Airplane]
  |       |
  v       v
[Car]  [Motorcycle]

Each class can simply "pass" for its body. The exercise is about setting up
the hierarchy.

e.g.

class Whatever:
    pass

Put a comment noting which class is the base class
"""

class Vehicle:
    pass
"""
Base Class for all type vehicles
Types: Ground Vehicle, Flight Vehicle
"""

class FlightVehicle(Vehicle):
    pass
"""
Base Class for all flying type vehicles
"""

class GroundVehicle(Vehicle):
    pass
"""
Base Class for all ground type vehicles
"""

class Starship(FlightVehicle):
    pass
"""
Base class is flightvehicles
"""

class Airplane(FlightVehicle):
    pass
"""
Base Class is Flightvechiles
"""
class Car(GroundVehicle):
    pass
"""
Base Class is Ground Vehicle
""" 
class Motorcycle(GroundVehicle):
    pass
"""
Base Class is Ground Vehicle
"""
