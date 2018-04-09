class triangle:
    tri_sides = [];
    tri_angles = [];
    is_tri = False;
    def __init__(self, _name):
        self.name = _name;
    def setSides(self, length, base, height):
        h = [length, base, height]
        self.tri_sides.extend(h);
    def getSides(self):
        return(self.tri_sides);
    def setAngles(self, a1, a2, a3):
        o = [a1, a2, a3];
        self.tri_angles.extend(o);
        if(sum(i for i in self.tri_angles) == 180):
            is_tri = True;
        else:
            is_tri = False;
    def getAngles(self):
        return(self.tri_angles);
    def Area(self):
        return(.5*self.tri_sides[1]*self.tri_sides[2]);
    def Perimeter(self):
        return(sum(i for i in self.tri_angles));
    def __repr__(self):
        return('The name of the triangle is: '+self.name);

me = triangle("Myself");
me.setSides(6, 4, 5);
me.setAngles(45, 45, 90);
print('Area is %d'%me.Area(), '\nPerimeter is %d'%me.Perimeter());
    
