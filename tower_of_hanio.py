
class ShellUI(object):
    def write(self, text):
        print text

def print_towers(tower_list, ui):
    first = 'O' + ''.join(tower_list[0])
    middle = 'O' + ''.join(tower_list[1])
    last = 'O' + ''.join(tower_list[2])
    output = '\n'.join([first, middle, last, '\n'])
    ui.write(output)

def move_disk(tower_list, from_index, to_index):
    disk = tower_list[from_index].pop()
    tower_list[to_index].append(disk)

def main():
    tower_list = [
        ['3', '2', '1'],
        [],
        [],
    ]
    ui = ShellUI()
    print_towers(tower_list, ui)
    move_disk(tower_list, 0, 2)
    print_towers(tower_list, ui)
    move_disk(tower_list, 0, 1)
    print_towers(tower_list, ui)
    move_disk(tower_list, 2, 1)
    print_towers(tower_list, ui)
    move_disk(tower_list, 0, 2)
    print_towers(tower_list, ui)
    move_disk(tower_list, 1, 0)
    print_towers(tower_list, ui)
    move_disk(tower_list, 1, 2)
    print_towers(tower_list, ui)
    move_disk(tower_list, 0, 2)
    print_towers(tower_list, ui)

if __name__ == '__main__':
    main()
