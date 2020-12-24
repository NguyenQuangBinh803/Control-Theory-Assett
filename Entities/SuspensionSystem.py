import numpy as np
from Abstract.SystemAbstract import SystemAbstract


class SuspensionModel(SystemAbstract):
    def __init__(self, body_mass, suspension_mass, spring_const_supension, spring_const_body, damping_const_supension,
                 damping_const_body, *args):
        super().__init__(*args)
        self.body_mass = body_mass
        self.suspension_mass = suspension_mass
        self.spring_const_suspension = spring_const_supension
        self.spring_const_body = spring_const_body
        self.damping_const_suspension = damping_const_supension
        self.damping_const_body = damping_const_body
        self.state_vector = np.zeros((1, 4), dtype=float)
        self.control_vector = np.zeros((1, 4), dtype=float)

    def system_model(self):
        self.A = np.zeros((4, 4), dtype=float)
        self.A[0][1] = 1
        self.A[1][0] = -self.damping_const_body * self.damping_const_suspension / self.body_mass / self.suspension_mass
        self.A[1][2] = - self.damping_const_body / self.body_mass * (
                self.damping_const_body / self.body_mass + self.damping_const_body / self.suspension_mass + self.damping_const_suspension / self.suspension_mass) - self.spring_const_body / self.body_mass
        self.A[1][3] = -self.damping_const_body / self.body_mass
        self.A[2][0] = self.damping_const_suspension / self.suspension_mass
        self.A[2][2] = - (
                self.damping_const_body / self.body_mass + self.damping_const_body / self.suspension_mass + self.damping_const_suspension / self.suspension_mass)
        self.A[2][3] = 1
        self.A[3][0] = self.spring_const_suspension / self.suspension_mass
        self.A[3][2] = - (
                self.spring_const_body / self.body_mass + self.spring_const_body / self.suspension_mass + self.spring_const_suspension / self.suspension_mass)

        self.B = np.zeros((4, 2), dtype=float)
        self.B[1][0] = 1 / self.body_mass
        self.B[1][1] = self.damping_const_body * self.damping_const_suspension / self.body_mass / self.suspension_mass
        self.B[2][1] = -self.damping_const_suspension / self.suspension_mass
        self.B[3][0] = (1 / self.body_mass + 1 / self.suspension_mass)
        self.B[3][1] = -self.spring_const_suspension / self.suspension_mass

        self.C = np.zeros((1, 4), dtype=float)
        self.C[0][2] = 1
        self.D = np.zeros((1, 2), dtype=float)

    def display_system_model(self):
        print(self.A)
        print(self.B)


if __name__ == "__main__":
    suspension = SuspensionModel(10, 10, 10, 101, 10, 10)
    suspension.system_model()
    suspension.display_system_model()
