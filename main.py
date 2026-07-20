# outline:
# get points
# get p hat and q hat (ie, make center of mass 0)
# get matrices of 2 of the points
# use matrices to get linear transformation matrix
# use matrix to get translation
# return java function that multiplies matrix by input and applies the translation
# enjoy!
import ast
import utils
import numpy as np

print("usage: <(x1,y1) (x2,y2)>, where x2,y2 is the result of the tranformation.")
print("3 points needed, that don't lie on a straight line.")

points: list[tuple] = []
images: list[tuple] = []

for i in range(3):
    cur = input("point and image:")
    cur.split()

    # evaluate point and image as tuples
    curPoint = ast.literal_eval(cur[0]) 
    curIm = ast.literal_eval(cur[1])
    points.append(curPoint)
    images.append(curIm)

pointsNormalized = utils.normalizePoints(points)
imagesNormalized = utils.normalizePoints(images)

