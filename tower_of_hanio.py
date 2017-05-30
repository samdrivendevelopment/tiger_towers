
class ShellUI(object):
    def write(self, text):
        print text

def print_towers(tower_list, ui):
    first = 'O' + ''.join(tower_list[0])
    middle = 'O' + ''.join(tower_list[1])
    last = 'O' + ''.join(tower_list[2])
    output = '\n'.join([first, middle, last])
    ui.write(output)

def main():
    ui = ShellUI()
    tower_list = [
        [],
        ['2', '1'],
        [],
    ]
    print_towers(tower_list, ui)

if __name__ == '__main__':
    main()
