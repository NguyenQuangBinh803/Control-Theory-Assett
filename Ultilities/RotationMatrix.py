import numpy as np
import math


class Rotation:
    def __init__(self):
        pass

    def rotation_matrix_from_rpy(self, roll, pitch, yaw):
        rotation_matrix = np.zeros((3, 3))
        rotation_matrix[0][0] = math.cos(roll) * math.cos(pitch)
        rotation_matrix[1][0] = math.sin(roll) * math.cos(pitch)
        rotation_matrix[2][0] = -1 * math.sin(pitch)

        rotation_matrix[0][1] = math.cos(roll) * math.sin(pitch) * math.sin(yaw) - math.sin(roll) * math.cos(yaw)
        rotation_matrix[1][1] = math.sin(roll) * math.sin(pitch) * math.sin(yaw) + math.cos(roll) * math.cos(yaw)
        rotation_matrix[2][1] = math.cos(pitch) * math.sin(yaw)

        rotation_matrix[0][2] = math.cos(roll) * math.sin(pitch) * math.cos(yaw) + math.sin(roll) * math.sin(yaw)
        rotation_matrix[1][2] = math.sin(roll) * math.sin(pitch) * math.cos(yaw) - math.cos(roll) * math.sin(yaw)
        rotation_matrix[2][2] = math.cos(pitch) * math.cos(yaw)

        return rotation_matrix

    def rotation_axis_and_angle_from_matrix(self, rotation_matrix):
        rotation_axis = np.zeros((3, 1))
        rotation_axis[0][0] = rotation_matrix[2][1] - rotation_matrix[1][2]
        rotation_axis[1][0] = rotation_matrix[2][2] - rotation_matrix[2][0]
        rotation_axis[2][0] = rotation_matrix[2][0] - rotation_matrix[0][1]
        rotation_angle = math.acos((rotation_matrix[0][0] + rotation_matrix[1][1] + rotation_matrix[2][2] - 1) / 2)
        return rotation_angle, rotation_axis

    def rotation_matrix_from_quartenion(self, r, i, j, k):
        rotation_matrix = np.zeros((3, 3))
        rotation_matrix[0][0] = 1 - 2 * (j ** 2 + k ** 2)
        rotation_matrix[0][1] = 2 * (i * j - k * r)
        rotation_matrix[0][2] = 2 * (i * k + j * r)

        rotation_matrix[1][0] = 2 * (i * j + k * r)
        rotation_matrix[1][1] = 1 - 2 * (i ** 2 + k ** 2)
        rotation_matrix[1][2] = 2 * (j * k - i * r)

        rotation_matrix[2][0] = 2 * (i * k - j * r)
        rotation_matrix[2][1] = 2 * (j * k + i * r)
        rotation_matrix[2][2] = 1 - 2 * (i ** 2 + j ** 2)

        return rotation_matrix

    def rotation_axis_and_angle_from_quartenion(self, r, i, j, k):
        rotation_axis = np.zeros((3, 1))
        print(rotation_axis)
        s = math.sqrt(i ** 2 + j ** 2 + k ** 2)
        rotation_axis[0][0] = i / s
        rotation_axis[1][0] = j / s
        rotation_axis[2][0] = k / s

        rotation_angle = 2 * math.atan2(s, r)

        return rotation_angle, rotation_axis


if __name__ == "__main__":
    rotation = Rotation()
    print(rotation.rotation_axis_and_angle(rotation.rotation_matrix_from_rpy(0, 0, math.pi / 2)))
