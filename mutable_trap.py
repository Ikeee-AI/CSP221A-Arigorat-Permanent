"""Standalone demo of the mutable class-attribute trap.

This is deliberately kept OUT of the real Robot hierarchy in robot.py /
cleaning_robot.py / drone_robot.py. It exists only to demonstrate the bug
and its fix for grading purposes.
"""


class BuggyRobotLog:
    """BUG: tasks_done is a class attribute, so every instance shares
    the same list."""

    tasks_done = []

    def __init__(self, name):
        self.name = name

    def log_task(self, task):
        self.tasks_done.append(task)


class FixedRobotLog:
    """FIX: tasks_done is created fresh in __init__, so each instance
    gets its own list."""

    def __init__(self, name):
        self.name = name
        self.tasks_done = []

    def log_task(self, task):
        self.tasks_done.append(task)


def demonstrate_bug():
    print("--- Buggy version (shared list) ---")
    a = BuggyRobotLog("Log-A")
    b = BuggyRobotLog("Log-B")
    a.log_task("swept the garage")
    print("a.tasks_done:", a.tasks_done)
    print("b.tasks_done:", b.tasks_done, "<- bug: B picked up A's task")

    print("\n--- Fixed version (per-instance list) ---")
    x = FixedRobotLog("Log-X")
    y = FixedRobotLog("Log-Y")
    x.log_task("surveyed the yard")
    print("x.tasks_done:", x.tasks_done)
    print("y.tasks_done:", y.tasks_done, "<- correct: Y is untouched")


if __name__ == "__main__":
    demonstrate_bug()