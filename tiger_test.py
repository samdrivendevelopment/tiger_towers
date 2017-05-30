
from tower_of_hanio import print_towers

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
    return ui.written == 'O\nO21\nO'


def main():

    print 'start test'

    if not test_print_tower():
        print 'Print towers did not print correctly.'

    print 'end test'

if __name__ == '__main__':
    main()
