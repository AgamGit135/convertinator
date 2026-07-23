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
def main(points: list[tuple], images: list[tuple],heading, headingImage):

    # if rank of matrix is <= 1, all points must be proportional
    if np.linalg.matrix_rank(points) <= 1:
        raise ValueError("Fatal: points are on a straight line.")

    pointsNormalized = utils.normalizePoints(points)
    imagesNormalized = utils.normalizePoints(images)

    # convert to np array to use np utils
    pointsNormalized = np.array(pointsNormalized)
    imagesNormalized = np.array(imagesNormalized)
    
    # choose 2 points s.t. they are invertible
    invertiblePointMatrix = []
    imageMatrix = []

    # 3 = 3 choose 2 = 3 choose 1 -> checking what happens when removing eac row is
    # going over all options
    for i in range(3):
        tempPoints = np.delete(pointsNormalized, i, axis=0)
        tempIms = np.delete(imagesNormalized,i,axis=0)
        if utils.isIndependent(tempPoints):
            invertiblePointMatrix = tempPoints
            imageMatrix = tempIms
            break
    
    # use random horn thingy to get transformation matrix and translation vector
    pointMatrixInverse = np.linalg.inv(invertiblePointMatrix)
    transformationMatrix = np.matmul(pointMatrixInverse,imageMatrix)
    transformationMatrix = np.transpose(transformationMatrix)

    CoMPoints = np.array(utils.getCenterOfMass(points))
    CoMIms = np.array(utils.getCenterOfMass(images))

    t = CoMIms - np.matmul(transformationMatrix,CoMPoints)
    return transformationMatrix, t

if __name__ == "__main__":
    main()