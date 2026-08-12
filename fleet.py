"""Fleet-wide helpers that operate polymorphically on any Robot."""

import logging

from robot import InsufficientBatteryError


def fleet_report(robots):
    """Print a status line for every robot, regardless of its subclass."""
    for robot in robots:
        print(str(robot))


def run_task_safely(robot, **kwargs):
    """Run robot.perform_task() with full try/except/else/finally handling."""
    try:
        result = robot.perform_task(**kwargs)
    except InsufficientBatteryError as e:
        logging.error(str(e))
    else:
        print(f"Task result: {result}")
    finally:
        print(f"{robot.name} battery is now at {robot.battery}%")