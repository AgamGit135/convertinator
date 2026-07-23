## About this project
This is a script that takes as input a few coordinates and the resulting coordinates after a change in the coordinate system, and outputs a Java function that can convert between those coordinate
systems. The Java function has the FTC (First Tech Challenge) SDK Pose2D class as input as well as output, as it is intended for use by FTC teams.

## All the math
This script assumes the transformation between every two coordinate systems is a linear transformation + translation.
###  Inputs and why these
The script takes:
- 3 points that don't lie on a straight line
- One angle and the resulting angle
- Units (for output as a function)

This way, the changes in angles are decoupled from the changes in position, so I could treat the position as a vector space (I probably didn't need that, but it made me worry less about the math :) ).
Let a given point be p and its output be q. Then, there exists a 2X2 matrix M and a vector t such that:

$$q = Mp + t$$

As $M \in M_{2}(\mathbb{R})$, it has 4 entries. T is a vector and therefore has two entries. Therefore, you can model each point and output pair as two 6 variable equations (one for x and one for
y). To have a single solution,you must have... 6 of them, or 3 points. If the points are collinear, those equations turn out to have more then one solution (trust).

### Getting M and t
Let $p_{1},p_{2},p_{3}$ be the input points and $q_{1},q_{2},q_{3}$ be their respective images. Let P be the center of mass of the points and Q be the center of mass of the images. From a theorem
my mum told me about, $T(P) = Q$, where T is the affine transformation. 
