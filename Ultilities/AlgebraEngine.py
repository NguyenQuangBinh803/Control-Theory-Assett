'''
Author: Edward J. C. Ashenbert
'''
import numpy as np
import math
from scipy import linalg
from string import Template

class AlgebraEngine:
    def __init__(self):
        pass

    @staticmethod
    def transpose(input_matrix):
        try:
            assert (isinstance(input_matrix, np.ndarray))
            return input_matrix.transpose()
        except:
            print("Input is not a numpy array!")

    @staticmethod
    def get_singular_value(input_matrix):
        try:
            assert (isinstance(input_matrix, np.ndarray))
            singular_values = []
            if input_matrix.shape[0] == input_matrix.shape[1]:
                for eigen_value in np.linalg.eigvals(input_matrix):
                    if eigen_value != 0:
                        singular_values.append(math.sqrt(eigen_value))
            else:
                for eigen_value in np.linalg.eigvals(input_matrix.dot(input_matrix.transpose())):
                    if eigen_value != 0:
                        singular_values.append(math.sqrt(eigen_value))
            return singular_values
        except:
            print("Input is not a numpy array!")

    @staticmethod
    def solve_ricatti(A, B, Q, R):
        return linalg.solve_discrete_are(A, B, Q, R)

    @staticmethod
    def solve_lyapunov_equation(A, Q):
        return linalg.solve_lyapunov(A, Q)

    @staticmethod
    def solve_sylvester_equation(A, B, C):
        '''
        Bartels–Stewart algorithm
        :param A:
        :param Q:
        :return:
        '''
        return linalg.solve_sylvester(A, B, C)

    @staticmethod
    def kronecker_product(A, B):
        return np.kron(A,B)

    @staticmethod
    def schur_decomposition(A):
        # return
        return np.kron(A, B)

    def __repr__(self):

        print("This engine is to implement transparently algebra notation require for control theory")


if __name__ == "__main__":
    al = AlgebraEngine()

    a = np.zeros((2, 3))
    a[0][0] = 1
    a[0][1] = 2
    a[0][2] = 3
    a[1][0] = 4
    a[1][1] = 5
    a[1][2] = 6

    print(AlgebraEngine.get_singular_value(a))

    a = np.array([[0, 1], [0, -1]])
    b = np.array([[1, 0], [2, 1]])
    print(AlgebraEngine.kronecker_product(a,b))
    q = np.array([[-4, -4], [-4, 7]])
    r = np.array([[9, 3], [3, 1]])

    print(AlgebraEngine.solve_ricatti(a, b, q, r))
import control

control.care()

# print(a.shape)
# print(AlgebraEngine.transpose(a))
# print(type(a))
