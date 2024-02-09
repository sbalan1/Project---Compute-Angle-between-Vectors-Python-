#Using Python To Determine The Angle Between Two Vectors

#importing required math module
import math
import numpy as np

#calculating the magnitude of the vectors
def mag(u, N):
 
    # Stores the final magnitude
    vec_magnitude = 0
 
    # Traverse the array
    for i in range(N):
        vec_magnitude += u[i] * u[i]
 
    # Return the square root of magnitude
    return math.sqrt(vec_magnitude)
 
# Function to find the dot product of the vectors
def dotProd(u, v, N):
 
    # Stores the dot product of the vectors
    vec_prod = 0
 
    # Traverse the array
    for i in range(N):
        vec_prod = vec_prod + u[i] * v[i]
 
    # Return the product
    return vec_prod

# Find the angle between vectors
def angleVector(u, v, N):
 
    # Find the dot product of vectors
    dotProduct_Vectors = dotProd(u, v, N)
 
    # magnitude of vector u
    mag_u = mag(u, N)
 
    #magnitude of vector v
    mag_v = mag(v, N)
 
    # angle between given vectors
    angle = (dotProduct_Vectors
            / (mag_u * mag_v))
 
    #display the angle
    print('%.5f'%angle)
    return angle

#pre defined vectors
u = [2, -1, 3]
v = [2, 0, 1]
# Size of the vectors
N = len(u)
#display the angle
print("The angle between the two vectors is:")
 
#function call to calculate the angle between the vectors
a = angleVector(u, v, N)

x = np.array(a)

#compute angle in radians
z = np.emath.arccos(x) #OR use np.arccos(x)

#compute angle in degrees
print(math. degrees(z))
