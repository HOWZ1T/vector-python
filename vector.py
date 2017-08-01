#Created by Dylan Randall
class Vector:
    def __init__(self, x_, y_, z_):
        self.x = x_
        self.y = y_
        self.z = z_

    def getMagnitude(self):
        return float(math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2)))

    def normalize(self):
        mag = getMagnitude()

        if(self.x != 0):
            self.x = self.x/mag

        if(self.y != 0):
            self.y = self.y/mag

        if(self.z != 0):
            self.z = self.z/mag

    def get2DAngle(self): #returns angle in degrees for 2 dimensions
        return float(math.degrees(math.atan2(self.y, self.x)))

    def get3DAngle(self): #value at index 0 is the rotation around the x axis, the value at index 1 is the rotation around the y axis.
        THETA = float(math.atan2(math.sqrt(math.pow(self.x, 2)+math.pow(self.y, 2)), self.z))
        PHI = float(math.atan2(self.y, self.x))
        vals = [math.degrees(THETA), math.degrees(PHI)]
        return vals

#TODO add Vector operations: multiply, divide, subtract, add, and scalar multiplication
