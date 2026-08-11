"""CleaningRobot: a Robot subclass specialized for vacuuming tasks."""

from robot import Robot, log_action


class CleaningRobot(Robot):
    def __init__(self, name, battery=100, dust_capacity=500):
        super().__init__(name, battery)
        self.dust_capacity = dust_capacity  # in milliliters

    @log_action
    def perform_task(self, **kwargs):
        """Vacuum a room. Costs 10% battery."""
        self.use_battery(10)
        return f"{self.name} vacuumed the living room."