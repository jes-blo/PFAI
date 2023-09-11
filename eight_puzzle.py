'''
'''
from copy import deepcopy


class EightPuzzle:

    def __init__(self, initial_state):
        self.state = initial_state
        self.goal = [['e', 1, 2], [3, 4, 5], [6, 7, 8]]
        self.action = ['right', 'down', 'left', 'up']

    def pretty_print(self):
        print('----------------------------')
        print(' Current frontier: ')
        for i in range(len(self.state)):
            curr = []
            for j in range(len(self.state)):
                curr.append(self.state[i][j])
            print(curr)
        print('----------------------------')

    def h_1(self):  # tiles out of place
        h_value = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != self.goal[i][j]:
                    h_value += 1
        return h_value

    def h_2(self):  # manhattan distance
        distance = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == self.goal[i][j]:
                    distance += abs(self.state[i] - self.goal[i]) + \
                        abs(self.state[j] - self.goal[j])
        return distance

    def check_goal(self):
        if self.state == self.goal:
            return True
        else:
            return False

    def get_e_position(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 'e':
                    return (i, j)

    def move(self, move):
        if move == 'right':
            dc = deepcopy(self)
            if dc.right():
                return dc
        elif move == 'down':
            dc = deepcopy(self)
            if dc.down():
                return dc
        elif move == 'left':
            dc = deepcopy(self)
            if dc.left():
                return dc
        elif move == 'up':
            dc = deepcopy(self)
            if dc.up():
                return dc

    def right(self):

        e_position = self.get_e_position()

        if self.state[e_position[0]][e_position[1]+1] != self.state[e_position[0]][2]:
            temp_value = self.state[e_position[0]][e_position[1]+1]
            self.state[e_position[0]][e_position[1+1]
                                      ] = self.state[e_position[0]][e_position[1]]
            self.state[e_position[0]][e_position[1]] = temp_value
            return True

    def down(self):

        e_position = self.get_e_position()

        if self.state[e_position[0]+1][e_position[1]] != self.state[2][e_position[1]]:
            temp_value = self.state[e_position[0]+1][e_position[1]]
            self.state[e_position[0]+1][e_position[1]
                                        ] = self.state[e_position[0]][e_position[1]]
            self.state[e_position[0]][e_position[1]] = temp_value
            return True

    def left(self):

        e_position = self.get_e_position()

        if self.state[e_position[0]][e_position[1]-1] != self.state[e_position[0]][0]:
            temp_value = self.state[e_position[0]][e_position[1]-1]
            self.state[e_position[0]][e_position[1-1]
                                      ] = self.state[e_position[0]][e_position[1]]
            self.state[e_position[0]][e_position[1]] = temp_value
            return True

    def up(self):

        e_position = self.get_e_position()

        if self.state[e_position[0]-1][e_position[1]] != self.state[0][e_position[1]]:
            temp_value = self.state[e_position[0]-1][e_position[1]]
            self.state[e_position[0]-1][e_position[1]
                                        ] = self.state[e_position[0]][e_position[1]]
            self.state[e_position[0]][e_position[1]] = temp_value
            return True
