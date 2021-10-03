def equilateral(sides):
    equilateral = False
    if sides[0] > 0 and sides[1] > 0 and sides[2] > 0:
        if sides[0] == sides[1] and sides[0] == sides[2]:
            if max(sides) < (sum(sides)-max(sides)):
                equilateral = True
    return equilateral


def isosceles(sides):
    isosceles = False
    if sides[0] > 0 and sides[1] > 0 and sides[2] > 0:
        if sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
            if max(sides) < (sum(sides)-max(sides)):
                isosceles = True
    return isosceles


def scalene(sides):
    scalene = False
    if sides[0] > 0 and sides[1] > 0 and sides[2] > 0:
        if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]:
            if max(sides) < (sum(sides)-max(sides)):
                scalene = True
    return scalene
