class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1 # can also be Robot.self

    @staticmethod
    def RobotInstances():
        return Robot.__counter

print(Robot.RobotInstances())
x = Robot()
print(x.RobotInstances())
y = Robot()
print(x.RobotInstances())
print(Robot.RobotInstances())
