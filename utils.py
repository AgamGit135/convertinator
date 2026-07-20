
def normalizePoints(points: list[tuple]):
    CoM: tuple = getCenterOfMass(points)
    out: list[tuple] = []

    for point in points:
        pointNormalized = pointMinus(point, CoM)
        out.append(pointNormalized)
    
    return out

def getCenterOfMass(points: list[tuple]) -> tuple:
    x: float = 0
    y: float = 0

    for point in points:
        x += point[0]
        y += point[1]

    return (x/len(points), y/len(points))


def pointMinus(a: tuple, b: tuple):
    out: list = []

    # possible to assume tuple size as they're points
    # however, that limits to 2 dim and i'd rather it would be more general
    for i in range(len(a)):
        out.append(a[i] - b[i])
    
    return tuple(out)