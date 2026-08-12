"""Demo script: puts the whole fleet system through its paces."""

import logging

from robot import Robot
from cleaning_robot import CleaningRobot
from drone_robot import DroneRobot
from fleet import fleet_report, run_task_safely

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def main():
    roomba = CleaningRobot("Roomba", battery=100)
    aqua_drone = DroneRobot.from_config({"name": "Aqua-Drone", "battery": 15})

    print("=== Fleet report ===")
    fleet_report([roomba, aqua_drone])

    print(f"\nRobots built so far: {Robot.population}")
    print(f"Manufacturer: {Robot.manufacturer}")

    print("\n=== Running tasks safely ===")
    run_task_safely(roomba)          # plenty of battery, should succeed
    run_task_safely(aqua_drone)      # 15% battery, task costs 25% -> should log an error

    print("\n=== repr() check ===")
    print(repr(roomba))
    print(repr(aqua_drone))

    print("\n=== Decorator sanity check ===")
    print("perform_task.__name__ ->", CleaningRobot.perform_task.__name__)
    print("perform_task.__doc__  ->", CleaningRobot.perform_task.__doc__)


if __name__ == "__main__":
    main()