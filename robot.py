"""Core Robot base class shared by every robot in the fleet."""

import abc


class Robot(abc.ABC):
    """Abstract base class for all robots in the fleet.

    Subclasses must implement perform_task(). Robot itself can never be
    instantiated directly.
    """

    manufacturer = "RoboCorp Industries"
    population = 0  # plain int, bumped once per instance created

    def __init__(self, name, battery=100):
        self.name = name
        self._battery = 0
        self.battery = battery  # goes through the setter below for clamping
        Robot.population += 1

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, value):
        # Always clamp to the 0-100 range, no matter what's passed in.
        self._battery = max(0, min(100, value))

    def __str__(self):
        return f"{self.name} ({self.battery}% battery)"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, battery={self.battery})"

    @abc.abstractmethod
    def perform_task(self, **kwargs):
        """Every subclass must define what its task actually does."""
        raise NotImplementedError