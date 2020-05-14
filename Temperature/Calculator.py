import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def check_dictionary_put_value(value, index_i, index_j, row_number):
    index_of_unknown = unknown_dictionary.get((index_i, index_j))
    answer_array[row_number][index_of_unknown] = value


class Calculator:

    def __init__(self):
        self.index = 0

    def initialize_dictionary(self, index_x, index_y):
        unknown_dictionary[(index_x, index_y)] = self.index
        self.index += 1


temperatures = [150, 100, 200, 50]

rows = 6
columns = 7
answer = 0

wooden_block_temperature = np.zeros((rows, columns))
counter = 0

calc = Calculator()
unknown_dictionary = dict()

for i in range(0, rows):
    if i % (rows - 1) == 0:
        wooden_block_temperature[i][range(1, columns - 1)] = temperatures[counter]
        counter = 2
    else:
        wooden_block_temperature[i][0] = temperatures[1]
        wooden_block_temperature[i][columns - 1] = temperatures[3]

        for k in range(1, columns - 1):
            calc.initialize_dictionary(i, k)

sns.heatmap(wooden_block_temperature, cmap="YlOrRd")
#annot=True, fmt=".2f",z
plt.xlabel("", size=columns)
plt.ylabel("", size=rows)
plt.tight_layout()
plt.show()

number_of_unknowns = (rows - 2) * (columns - 2)

answer_array = np.zeros((number_of_unknowns, number_of_unknowns))
answers = []

row_number_count = 0

# array x, y, z, n, s
# formula t(i-1, j) - 4 t(i, j) + t()
for i in range(1, rows - 1):
    for j in range(1, columns - 1):

        t_i_j = wooden_block_temperature[i][j]
        t_i_plus = wooden_block_temperature[i + 1][j]
        t_i_minus = wooden_block_temperature[i - 1][j]
        t_j_minus = wooden_block_temperature[i][j - 1]
        t_j_plus = wooden_block_temperature[i][j + 1]

        answer = 0

        if t_i_j == 0:
            check_dictionary_put_value(-4, i, j, row_number_count)
        else:
            answer += 4 * t_i_j

        if t_i_plus == 0:
            check_dictionary_put_value(1, i + 1, j, row_number_count)
        else:
            answer += t_i_plus

        if t_i_minus == 0:
            check_dictionary_put_value(1, i - 1, j, row_number_count)
        else:
            answer += t_i_minus

        if t_j_plus == 0:
            check_dictionary_put_value(1, i, j + 1, row_number_count)
        else:
            answer += t_j_plus

        if t_j_minus == 0:
            check_dictionary_put_value(1, i, j - 1, row_number_count)
        else:
            answer += t_j_minus

        row_number_count += 1
        answers.append(-1 * answer)

print(answer_array, answers)

X = np.linalg.inv(answer_array).dot(answers)
index = 0



print(X)

for i in range(1, rows - 1):
    for j in range(1, columns - 1):
        wooden_block_temperature[i][j] = X[index]
        index += 1
        
sns.heatmap(wooden_block_temperature, cmap="YlOrRd")
# annot=True, fmt=".2f"
plt.xlabel("", size=columns)
plt.ylabel("", size=rows)
plt.tight_layout()
plt.show()
