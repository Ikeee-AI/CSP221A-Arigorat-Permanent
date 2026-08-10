# Robot Fleet Management System

A small object-oriented fleet management system for robots, built for
Coding Assignment 2.

## Overview

- `robot.py` — abstract `Robot` base class, `InsufficientBatteryError`,
  and the `log_action` decorator.
- `cleaning_robot.py` — `CleaningRobot` subclass.
- `drone_robot.py` — `DroneRobot` subclass.
- `fleet.py` — `fleet_report()` and `run_task_safely()`.
- `mutable_trap.py` — standalone demonstration of the mutable class
  attribute bug, kept separate from the real Robot hierarchy.
- `main.py` — demo script that ties everything together.

## Running

python main.py
python mutable_trap.py