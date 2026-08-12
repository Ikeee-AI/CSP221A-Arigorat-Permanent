"""DroneRobot: a Robot subclass specialized for aerial survey tasks."""

from robot import Robot


class DroneRobot(Robot):
    def __init__(self, name, battery=100, max_altitude=120):
        super().__init__(name, battery)
        self.max_altitude = max_altitude  # in meters

    def perform_task(self, **kwargs):
        """Fly an aerial survey. Costs 25% battery."""
        self.use_battery(25)
        return f"{self.name} completed an aerial survey at {self.max_altitude}m."