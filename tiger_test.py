
from tower_of_hanio import print_towers, move_disk, get_tower_index, should_quit, is_invalid_input, is_invalid_move, has_won

class TestUI(object):
    def write(self, text):
        self.written = text
    def read(self):
        return self.test_input

class BetterTestUI(object):
    def write(self, text):
        self.test_output_list.append(text)
    def read(self):
        return self.test_input_list.pop(0)

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

def test_get_index():
    ui = TestUI()
    ui.test_input = '1'
    user_input = get_tower_index(ui)
    return user_input == '1'

def test_should_quit():
    user_input = 'q'
    result = should_quit(user_input)
    return result == True

def test_should_not_quit():
    user_input = '1'
    result = should_quit(user_input)
    return result == False

def test_is_invalid_input():
    user_input = 't'
    result = is_invalid_input(user_input)
    return result == True

def test_is_valid_input():
    user_input = '1'
    result = is_invalid_input(user_input)
    return result == False

def test_invalid_move():
    tower_list = [
        ['3', '2'],
        ['1'],
        [],
    ]
    from_index = 0
    to_index = 1
    result = is_invalid_move(tower_list, from_index, to_index)
    return result == True

def test_valid_move():
    tower_list = [
        ['3', '2'],
        ['1'],
        [],
    ]
    from_index = 0
    to_index = 2
    result = is_invalid_move(tower_list, from_index, to_index)
    return result == False

def test_win():
    tower_list = [
        [],
        [],
        ['1'],
    ]
    result = has_won(tower_list)
    return result == True

def test_not_win():
    tower_list = [
        [],
        ['1'],
        [],
    ]
    result = has_won(tower_list)
    return result == False

def main():

    print 'start test'

    if not test_print_tower():
        print 'Print towers did not print correctly.'

    if not test_move_disk():
        print 'Move disk did not move the disk properly.'

    if not test_get_index():
        print 'Get tower index did not get the index correctly.'

    if not test_should_quit():
        print 'should quit did not detect quit correctly.'

    if not test_should_not_quit():
        print 'should quit detected quit incorrectly.'

    if not test_is_invalid_input():
        print 'is invalid input was not detected.'

    if not test_is_valid_input():
        print 'is invalid input detected it was invalid when it was not.'

    if not test_invalid_move():
        print 'invalid move was not detected.'

    if not test_valid_move():
        print 'invalid move detected a invalid move when there was none.'

    if not test_win():
        print 'win case did not detect the win.'

    if not test_not_win():
        print 'win case detected a win when there was none.'

    print 'end test'

if __name__ == '__main__':
    main()

