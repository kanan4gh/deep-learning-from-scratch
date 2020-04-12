# Akiko Ishihara

import numpy as np

def perceptron(x1, x2, w1, w2, theta):
    x = np.array([x1, x2])
    w = np.array([w1, w2])
    b = theta
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def AND(x1, x2):
    return perceptron(x1, x2, 0.5, 0.5, -0.7)
    
def NAND(x1, x2):
    return perceptron(x1, x2, -0.5, -0.5, 0.7)

def OR(x1, x2):
    return perceptron(x1, x2, 0.5, 0.5, -0.2)

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    return AND(s1, s2)

ans = AND(0,0)
print('AND(0,0)={}'.format(ans))
ans = AND(0,1)
print('AND(0,1)={}'.format(ans))
ans = AND(1,0)
print('AND(1,0)={}'.format(ans))
ans = AND(1,1)
print('AND(1,1)={}'.format(ans))

ans = NAND(0,0)
print('NAND(0,0)={}'.format(ans))
ans = NAND(0,1)
print('NAND(0,1)={}'.format(ans))
ans = NAND(1,0)
print('NAND(1,0)={}'.format(ans))
ans = NAND(1,1)
print('NAND(1,1)={}'.format(ans))

ans = OR(0,0)
print('OR(0,0)={}'.format(ans))
ans = OR(0,1)
print('OR(0,1)={}'.format(ans))
ans = OR(1,0)
print('OR(1,0)={}'.format(ans))
ans = OR(1,1)
print('OR(1,1)={}'.format(ans))

ans = XOR(0,0)
print('XOR(0,0)={}'.format(ans))
ans = XOR(0,1)
print('XOR(0,1)={}'.format(ans))
ans = XOR(1,0)
print('XOR(1,0)={}'.format(ans))
ans = XOR(1,1)
print('XOR(1,1)={}'.format(ans))



