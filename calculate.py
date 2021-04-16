import numpy as np

class Calculate:
    def __init__(self, number_list):
        self.matrix = np.reshape(np.array(number_list), (3,3))
        self.number_list = number_list

    # Mean
    def calc_matrix_mean(self, dimension):
        return np.mean(self.matrix, axis=dimension).tolist()

    def calc_flat_mean(self):
        return np.mean(self.number_list).tolist()

    def calc_mean_values(self):
        return [
            self.calc_matrix_mean(0),
            self.calc_matrix_mean(1),
            self.calc_flat_mean()
        ]

    # Variance
    def calc_matrix_var(self, dimension):
        return np.var(self.matrix, axis=dimension).tolist()

    def calc_flat_var(self):
        return np.var(self.number_list).tolist()

    def calc_var_values(self):
        return [
            self.calc_matrix_var(0),
            self.calc_matrix_var(1),
            self.calc_flat_var()
        ]

    # Standard Deviation
    def calc_matrix_std(self, dimension):
        return np.std(self.matrix, axis=dimension).tolist()

    def calc_flat_std(self):
        return np.std(self.number_list).tolist()

    def calc_std_values(self):
        return [
            self.calc_matrix_std(0),
            self.calc_matrix_std(1),
            self.calc_flat_std()
        ]
    
    # Max
    def calc_matrix_max(self, dimension):
        return np.max(self.matrix, axis=dimension).tolist()

    def calc_flat_max(self):
        return np.max(self.number_list).tolist()

    def calc_max_values(self):
        return [
            self.calc_matrix_max(0),
            self.calc_matrix_max(1),
            self.calc_flat_max()
        ]

    # Min
    def calc_matrix_min(self, dimension):
        return np.min(self.matrix, axis=dimension).tolist()

    def calc_flat_min(self):
        return np.min(self.number_list).tolist()

    def calc_min_values(self):
        return [
            self.calc_matrix_min(0),
            self.calc_matrix_min(1),
            self.calc_flat_min()
        ]

    # Sum
    def calc_matrix_sum(self, dimension):
        return np.sum(self.matrix, axis=dimension).tolist()

    def calc_flat_sum(self):
        return np.sum(self.number_list).tolist()

    def calc_sum_values(self):
        return [
            self.calc_matrix_sum(0),
            self.calc_matrix_sum(1),
            self.calc_flat_sum()
        ]

    def get_calculations(self):
        return {
            'mean': self.calc_mean_values(),
            'variance': self.calc_var_values(),
            'standard deviation': self.calc_std_values(),
            'max': self.calc_max_values(),
            'min': self.calc_min_values(),
            'sum': self.calc_sum_values()
        }
