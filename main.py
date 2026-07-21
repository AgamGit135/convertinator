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
def main():
    print("usage: <(x1,y1) (x2,y2)>, where x2,y2 is the result of the tranformation.")
    print("3 points that don't lie on a straight line are needed. newlines in between.")
    print("after that, input a heading and the resulting heading, and the output units")

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

    heading = int(input("heading:"))
    headingImage = int(input("heading image:"))
    distUnit = input("distance unit:")
    angleUnit = input("angle unit:")

    pointsNormalized = utils.normalizePoints(points)
    imagesNormalized = utils.normalizePoints(images)

    # convert to np array to use np utils
    pointsNormalized = np.array(pointsNormalized)
    imagesNormalized = np.array(imagesNormalized)

    # if rank of matrix is <= 1, all points must be proportional
    if np.linalg.matrix_rank(pointsNormalized) <= 1:
        raise ValueError("Fatal: points are on a straight line.")
    
    # choose 2 points s.t. they are invertible
    invertiblePointMatrix = []
    imageMatrix = []

    # 3 = 3 choose 2 = 3 choose 1 -> checking what happens when removing eac row is
    # going over all options
    for i in range(3):
        tempPoints = np.delete(points, i, axis=0)
        tempIms = np.delete(images,i,axis=0)
        if utils.isIndependent(tempPoints):
            invertiblePointMatrix = tempPoints
            imageMatrix = tempIms
            break
    
    # use random horn thingy to get transformation matrix and translation vector
    pointMatrixInverse = np.linalg.inv(invertiblePointMatrix)
    transformationMatrix = np.matmul(pointMatrixInverse,imageMatrix)

    CoMPoints = np.array(utils.getCenterOfMass(points))
    CoMIms = np.array(utils.getCenterOfMass(images))

    t = CoMIms - np.matmul(transformationMatrix,CoMPoints)

    # ugly string manipulation
    print("public Pose2D convert(Pose2D pose){")   
    print("    double x = pose.getX();")
    print("    double y = pose.getY();")
    print("    double heading = pose.getHeading();")
    print(f"    double newHead = heading + {headingImage - heading};")
    print("    if (newHead < -180) newHead += 360;")
    # kill me now why isnt there built in matrix multiplication
    print("    // no built in matrix multiplication :(")
    print(f"    double newX = x*{transformationMatrix[0][0]} + y*{transformationMatrix[0][1]};")
    print(f"    double newY = x*{transformationMatrix[1][0]} + y*{transformationMatrix[1][1]};")
    print(f"    return new Pose2D(DistanceUnit.{distUnit}, newX,newY,AngleUnit.{angleUnit},newHead);")
    print("}")




if __name__ == "__main__":
    main()