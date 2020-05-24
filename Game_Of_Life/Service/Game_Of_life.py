import numpy as np
import random


class Game_Of_life:
    def __init__(self, num_cells, rule_1, rule_2, rule_3):
        self.num_cells = num_cells
        self.game_arr = np.zeros((num_cells, num_cells))
        self.cell_neighbours = dict()
        self.rule_1 = rule_1
        self.rule_2 = rule_2
        self.rule_3 = rule_3

    def start_game(self):
        for _ in range(20):
            coordinates = [random.randint(0, self.num_cells - 1), random.randint(0, self.num_cells - 1)]
            self.game_arr[coordinates[0]][coordinates[1]] = 1
            self.neighbours(coordinates)

            random_iteration = random.randint(4, 10)
            for i in range(0, random_iteration):
                self.resurrect_neighbour((coordinates[0], coordinates[1]))
        self.play_game()

    def resurrect_neighbour(self, coordinates: tuple):
        neighbour_cell = self.cell_neighbours.get(coordinates)
        for neighbour in neighbour_cell:
            self.game_arr[neighbour[0], neighbour[1]] = np.random.randint(2, size=1)

    def neighbours(self, coordinates):
        create_list = [[coordinates[0] - 1, coordinates[1] + 1],
                       [coordinates[0], coordinates[1] + 1],
                       [coordinates[0] + 1, coordinates[1] + 1],
                       [coordinates[0] - 1, coordinates[1]],
                       [coordinates[0] + 1, coordinates[1]],
                       [coordinates[0] - 1, coordinates[1] - 1],
                       [coordinates[0], coordinates[1] - 1],
                       [coordinates[0] + 1, coordinates[1] - 1]]

        for coordinate in create_list:
            # Corners
            if coordinate[0] == coordinate[1] == -1:
                coordinate[0] = coordinate[1] = self.num_cells - 1

            elif coordinate[0] == coordinate[1] == self.num_cells:
                coordinate[0] = coordinate[1] = 0

            elif coordinate[0] == self.num_cells and coordinate[1] == -1:
                coordinate[0] = 0
                coordinate[1] = self.num_cells - 1

            elif coordinate[0] == -1 and coordinate[1] == self.num_cells:
                coordinate[0] = self.num_cells - 1
                coordinate[1] = 0

            # Sides
            # # check X
            if coordinate[0] < 0:
                coordinate[0] = self.num_cells - 1

            elif coordinate[0] > self.num_cells - 1:
                coordinate[0] = 0

            # # check Y
            if coordinate[1] < 0:
                coordinate[1] = self.num_cells - 1

            elif coordinate[1] > self.num_cells - 1:
                coordinate[1] = 0
        self.cell_neighbours[(coordinates[0], coordinates[1])] = create_list

    def play_game(self, i: int = None, j: int = None):

        if i is None and j is None:
            for i in range(self.num_cells):
                for j in range(self.num_cells):
                    self.apply_logic(i, j)
        else:
            self.apply_logic(i, j)

    def apply_logic(self, i, j):
        live_neighbour_for_cell = 0
        if (i, j) not in self.cell_neighbours:
            self.neighbours((i, j))
        neighbours = self.cell_neighbours.get((i, j))

        for neighbour in neighbours:
            if self.game_arr[neighbour[0]][neighbour[1]] == 1:
                live_neighbour_for_cell += 1
        self.critical_choice(live_neighbour_for_cell, i, j)

    def critical_choice(self, number_of_neighbours, i, j):
        if self.game_arr[i][j] == 1:
            if number_of_neighbours < self.rule_1 or number_of_neighbours > self.rule_2:
                self.game_arr[i][j] = 0
        else:
            if number_of_neighbours == self.rule_3:
                self.game_arr[i][j] = 1