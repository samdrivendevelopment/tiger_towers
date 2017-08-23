#!/usr/bin/python

import json
import sys

class ShellUI(object):
    def write(self, text):
        print text
    def read(self):
        return raw_input('->')

def print_towers(tower_list, ui):
    first = 'O' + ''.join(tower_list[0])
    middle = 'O' + ''.join(tower_list[1])
    last = 'O' + ''.join(tower_list[2])
    output = '\n'.join([first, middle, last, '\n'])
    ui.write(output)

def move_disk(tower_list, from_index, to_index):
    disk = tower_list[from_index].pop()
    tower_list[to_index].append(disk)


def get_tower_index(ui):
    user_input = ui.read()
    return user_input

def should_quit(user_input):
    if user_input in ['q', 'quit']:
        return True
    return False

def is_invalid_input(user_input):
    if user_input not in ['0', '1', '2']:
        return True
    return False

def is_invalid_move(tower_list, from_index, to_index):
    if len(tower_list[from_index]) < 1:
        return True
    if len(tower_list[to_index]) < 1:
        return False
    if tower_list[from_index][-1] > tower_list[to_index][-1]:
        return True
    return False
    
def has_won(tower_list):
    if len(tower_list[0]) == 0 and len(tower_list[1]) == 0:
        return True
    return False

class TowerofHanioGame(object):
    def turn(self):
        get = self.state
        print_towers(get['tower_list'], self.ui)
        from_index = get_tower_index(self.ui)
        if should_quit(from_index):
            return True
        if is_invalid_input(from_index):
            return False
        to_index = get_tower_index(self.ui)
        if should_quit(to_index):
            return True
        if is_invalid_input(to_index):
            return False
        if is_invalid_move(get['tower_list'], int(from_index), int(to_index)):
            return False
        move_disk(get['tower_list'], int(from_index), int(to_index))
        if has_won(get['tower_list']):
            print_towers(get['tower_list'], self.ui)
            return True
        print_towers(get['tower_list'], self.ui)
        return False

def main():
    filename = sys.argv[1]
    f = open(filename)
    state = json.load(f)
    f.close()
    game = TowerofHanioGame()
    game.ui = ShellUI()
    game.state = state

    for i in range(999):
        if game.turn():
            break

if __name__ == '__main__':
    main()
