import numpy as np
from scipy.signal import convolve2d

def eigencheck(l1,l2):
    print((l1*l2)-0.1*((l1+l2)**2))

def quadratic(a,b,c):
    # Solve the quadratic equation ax**2 + bx + c = 0

    # import complex math module
    import cmath

    # To take coefficient input from the users
    # a = float(input('Enter a: '))
    # b = float(input('Enter b: '))
    # c = float(input('Enter c: '))

    # calculate the discriminant
    d = (b**2) - (4*a*c)

    # find two solutions
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    print('The solution are {0} and {1}'.format(sol1,sol2))
    return sol1, sol2


def sobel_tranform(imgData):
    #x = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
    #y = np.array([[-1,-2,-1], [0,0,0], [1,2,1]])
    
    x = np.array([[1,0,-1], [2,0,-2], [1,0,-1]])
    y = np.array([[1,2,1], [0,0,0], [-1,-2,-1]])
    Gx = convolve2d(imgData, x, mode = 'same')
    Gy = convolve2d(imgData, y, mode = 'same')
    
    return Gx, Gy


G = [[0, 0.5, 0], [0.5, 1, 0.5], [0, 0.5, 0]]
window = [[10,9,10], [10,11, 9], [8,9,10]]
window2 =[[0,9,10], [0,10,8], [0,9,10]]
Ix, Iy = sobel_tranform(window2)
print('ekastote I:')
print (Ix)
print (Iy)
#print(np.sum(G * (Ix * Ix)) )



#G Ix^2
print ( (Ix[0][1]**2 + Ix[1][0]**2 + Ix[1][2]**2+Ix[2][1]**2)/2 +Ix[1][1]**2 )
#print ( (8**2 + 31**2 + 31**2 + 28**2)/2 +26**2 )
#G Iy^2
print ( (Iy[0][1]**2 + Iy[1][0]**2 + Iy[1][2]**2+Iy[2][1]**2)/2 +Iy[1][1]**2 )
#print ( (28**2 +11**2 + 31**2 + 28**2)/2 +32**2 )

#G Ix*Iy mallon auto einai to swsto!!
print ( (Ix[0][1]*Iy[0][1] + Ix[1][0]*Iy[1][0] + Ix[1][2]*Iy[1][2]+Ix[2][1]*Iy[2][1])/2 +Ix[1][1]*Iy[1][1] )
#print ( (8*28 +31*11 + 31*31 + 28*28)/2 +26*32 )

ei1,ei2 = quadratic(1,-3874,2923644)
#check
eigencheck(np.real(ei1), np.real(ei2))
