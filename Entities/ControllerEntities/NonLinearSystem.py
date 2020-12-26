import numpy as np

class SystemModel:
    def __init__(self):

        self.previous_system_state_1 = 0
        self.previous_system_state_2 = 0
        self.system_state_1_differential = 0
        self.system_state_2_differential = 0

        self.current_system_state_1 = self.previous_system_state_1 + self.system_state_1_differential
        self.current_system_state_2 = self.previous_system_state_2 + self.system_state_2_differential

        self.system_state = np.append(self.previous_system_state_1, self.previous_system_state_1)
        self.system_state_differential = np.append(self.system_state_1_differential, self.system_state_2_differential)

        self.current_control_signal = 0
        self.previous_control_signal = 0

        self.sampling_time = 0.1

        self.evaluation_equation = 1 / 2 * self.current_system_state_1 ** 2 + self.current_system_state_2 ** 2 + 1 / 4 * (
                (self.previous_system_state_1 ** 2 + self.previous_system_state_2 ** 2 + self.previous_control_signal ** 2) + (
                self.current_system_state_1 ** 2 + self.current_system_state_2 ** 2 + self.current_control_signal ** 2)) * self.sampling_time

    def system_model(self):
        pass


if __name__ == "__main__":
    nonlinear_optimal_model = SystemModel()
