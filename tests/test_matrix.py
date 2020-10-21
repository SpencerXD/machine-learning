import sys
sys.path.append('src')
from matrix import Matrix


print("Testing method 'copy'...")
A = Matrix([[1,3], [2,4]])
assert A.elements == [[1,3], [2,4]], 'Test Failed'
print('PASSED')

print('')
B = A.copy()
A = 'resetting A to a string'
assert B.elements == [[1,3], [2,4]], 'Test Failed'
print('PASSED')

print('Testing method "add"...')
C = Matrix([[1,0], [2,-1]])
D = B.add(C)
assert D.elements == [[2,3], [4,3]], 'Test Failed'
print('PASSED')

print('Testing method "subtract"...')
E = B.subtract(C)
assert E.elements == [[0,3], [0,5]], 'Test Failed'
print('PASSED')

print('Testing method "scalar_multiply"...')
F = B.scalar_multiply(2)
assert F.elements == [[2,6], [4,8]], 'Test Failed'
print('PASSED')

print('Testing method "matrix_multiply"...')
G = B.matrix_multiply(C)
assert G.elements == [[7,-3], [10,-4]], 'Test Failed'
print('PASSED')


A = Matrix([[1,0,2,0,3], [0,4,0,5,0], [6,0,7,0,8], [-1,-2,-3,-4,-5]])
assert (A.num_rows, A.num_cols) == (4, 5), 'Test Failed'
print('PASSED')

A_t = A.transpose()
assert A_t.elements == [[ 1,  0,  6, -1], [ 0,  4,  0, -2], [ 2,  0,  7, -3], [ 0,  5,  0, -4], [ 3,  0,  8, -5]], 'Test Failed'
print('PASSED')

B = A_t.matrix_multiply(A)
assert B.elements == [[38,  2, 47,  4, 56], [ 2, 20,  6, 28, 10], [47,  6, 62, 12, 77], [ 4, 28, 12, 41, 20], [56, 10, 77, 20, 98]], 'Test Failed'
print('PASSED')

C = B.scalar_multiply(0.1)
print(C.elements)
assert C.elements == [[3.8,  .2, 4.7,  .4, 5.6], [ .2, 2.0,  .6, 2.8, 1.0], [4.7,  .6, 6.2, 1.2, 7.7], [ .4, 2.8, 1.2, 4.1, 2.0], [5.6, 1.0, 7.7, 2.0, 9.8]]
print('PASSED')

D = B.subtract(C)
assert D.elements == [[34.2,  1.8, 42.3,  3.6, 50.4], [ 1.8, 18. ,  5.4, 25.2,  9. ], [42.3,  5.4, 55.8, 10.8, 69.3], [ 3.6, 25.2, 10.8, 36.9, 18. ], [50.4,  9. , 69.3, 18. , 88.2]], 'test Failed'
print('PASSED')

E = D.add(C)
assert E.elements == [[38,  2, 47,  4, 56],
 [ 2, 20,  6, 28, 10],
 [47,  6, 62, 12, 77],
 [ 4, 28, 12, 41, 20],
 [56, 10, 77, 20, 98]], 'test failed'
print('PASSED')

assert (E.is_equal(B), E.is_equal(C)) == (True, False), 'test failed'
print('PASSED')

print('')
print('rref assignment')
A = Matrix([[0, 1, 2],[3, 6, 9], [2, 6, 8]])

assert A.rref().elements == ([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 'test failed'
print('PASSED 1st test') 

B = Matrix([[0, 0, -4, 0], [0, 0, 0.3, 0], [0, 2, 1, 0]])

assert B.rref().elements == ([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]), 'test failed'
print('PASSED 2nd test')

A = Matrix([
    [1, 2,   3,  4],
    [5, 6,   7,  8],
    [9, 10, 11, 12]
])

B = Matrix([
    [13, 14],
    [15, 16],
    [17, 18]
])
A_augmented = A.augment(B)

assert A_augmented.elements == [[1, 2,   3,  4, 13, 14], [5, 6,   7,  8, 15, 16], [9, 10, 11, 12, 17, 18]], 'test failed'

print('Augment 1 PASSED')

A_augmented = Matrix([[1, 2,   3,  4, 13, 14],
[5, 6,   7,  8, 15, 16],[9, 10, 11, 12, 17, 18]])

rows_02 = A_augmented.get_rows([0, 2])

assert rows_02.elements == [[1, 2,   3,  4, 13, 14], [9, 10, 11, 12, 17, 18]], 'test failed'
print('Augment 2 PASSED')