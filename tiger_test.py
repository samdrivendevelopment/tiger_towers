
from tower_of_hanio import print_towers, move_disk

class TestUI(object):
    def write(self, text):
        self.written = text

def test_print_tower():
    ui = TestUI()
    ui.written = None
    tower_list = [
        [],
        ['2', '1'],
        [],
    ]
    print_towers(tower_list, ui)
    return ui.written == 'O\nO21\nO\n\n'

def test_move_disk():
    tower_list = [
        [],
        ['2', '1'],
        [], 
    ]   
    from_index = 1
    to_index = 2
    move_disk(tower_list, from_index, to_index)
    return tower_list == [
        [],
        ['2'],
        ['1'],
    ]

def main():

    print 'start test'

    if not test_print_tower():
        print 'Print towers did not print correctly.'

    if not test_move_disk():
        print 'Move disk did not move the disk properly.'

    print 'end test'

if __name__ == '__main__':
    main()
