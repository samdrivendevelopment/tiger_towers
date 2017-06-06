
from tower_of_hanio import TowerofHanioGame

class BetterTestUI(object):
    def write(self, text):
        self.test_output_list.append(text)
    def read(self):
        return self.test_input_list.pop(0)

def test_turn_norm():
    game = TowerofHanioGame()
    game.ui = BetterTestUI()
    game.ui.test_input_list = ['0', '1']
    game.ui.test_output_list = []
    game.tower_list = [
        ['3', '2', '1'],
        [],
        [],
    ]
    should_quit = game.turn()
    tower_good = game.tower_list == [
        ['3', '2'],
        ['1'],
        [],
    ]
    output_good = game.ui.test_output_list == [
        'O321\nO\nO\n\n', 'O32\nO1\nO\n\n']
    return output_good and tower_good and (should_quit == False)

def test_turn_st_quit():
    game = TowerofHanioGame()
    game.ui = BetterTestUI()
    game.ui.test_input_list = ['q']
    game.ui.test_output_list = []
    game.tower_list = [
        ['3', '2', '1'],
        [],
        [],
    ]
    should_quit = game.turn()
    tower_good = game.tower_list == [
        ['3', '2', '1'],
        [],
        [],
    ]
    output_good = game.ui.test_output_list == [
        'O321\nO\nO\n\n']
    return output_good and tower_good and (should_quit == True)


def test_turn_nd_quit():
    game = TowerofHanioGame()
    game.ui = BetterTestUI()
    game.ui.test_input_list = ['0', 'q']
    game.ui.test_output_list = []
    game.tower_list = [
        ['3', '2', '1'],
        [],
        [],
    ]
    should_quit = game.turn()
    tower_good = game.tower_list == [
        ['3', '2', '1'],
        [],
        [],
    ]
    output_good = game.ui.test_output_list == [
        'O321\nO\nO\n\n']
    return output_good and tower_good and (should_quit == True)

def test_turn_st_invalid_input():
    game = TowerofHanioGame()
    game.ui = BetterTestUI()
    game.ui.test_input_list = ['t']
    game.ui.test_output_list = []
    game.tower_list = [
        ['3', '2', '1'],
        [],
        [],
    ]
    should_quit = game.turn()
    tower_good = game.tower_list == [
        ['3', '2', '1'],
        [],
        [],
    ]
    output_good = game.ui.test_output_list == [
        'O321\nO\nO\n\n']
    return output_good and tower_good and (should_quit == False)


def test_turn_nd_invalid_input():
    game = TowerofHanioGame()
    game.ui = BetterTestUI()
    game.ui.test_input_list = ['0', 't']
    game.ui.test_output_list = []
    game.tower_list = [
        ['3', '2', '1'],
        [],
        [],
    ]
    should_quit = game.turn()
    tower_good = game.tower_list == [
        ['3', '2', '1'],
        [],
        [],
    ]
    output_good = game.ui.test_output_list == [
        'O321\nO\nO\n\n']
    return output_good and tower_good and (should_quit == False)

def test_turn_valid_move():
    game = TowerofHanioGame()
    game.ui = BetterTestUI()
    game.ui.test_input_list = ['0', '1']
    game.ui.test_output_list = []
    game.tower_list = [
        ['3', '2', '1'],
        [],
        [],
    ]
    should_quit = game.turn()
    tower_good = game.tower_list == [
        ['3', '2'],
        ['1'],
        [],
    ]
    output_good = game.ui.test_output_list == [
        'O321\nO\nO\n\n', 'O32\nO1\nO\n\n']
    return output_good and tower_good and (should_quit == False)

def test_turn_invalid_move():
    game = TowerofHanioGame()
    game.ui = BetterTestUI()
    game.ui.test_input_list = ['0', '1']
    game.ui.test_output_list = []
    game.tower_list = [
        ['3', '2'],
        ['1'],
        [],
    ]
    should_quit = game.turn()
    tower_good = game.tower_list == [
        ['3', '2'],
        ['1'],
        [],
    ]
    output_good = game.ui.test_output_list == [
        'O32\nO1\nO\n\n']
    return output_good and tower_good and (should_quit == False)

def test_turn_win():
    game = TowerofHanioGame()
    game.ui = BetterTestUI()
    game.ui.test_input_list = ['0', '2']
    game.ui.test_output_list = []
    game.tower_list = [
        ['1'],
        [],
        [],
    ]
    should_quit = game.turn()
    tower_good = game.tower_list == [
        [],
        [],
        ['1'],
    ]
    output_good = game.ui.test_output_list == [
        'O1\nO\nO\n\n', 'O\nO\nO1\n\n']
    return output_good and tower_good and (should_quit == True)


def test_turn_not_win():
    game = TowerofHanioGame()
    game.ui = BetterTestUI()
    game.ui.test_input_list = ['0', '1']
    game.ui.test_output_list = []
    game.tower_list = [
        ['1'],
        [],
        [],
    ]
    should_quit = game.turn()
    tower_good = game.tower_list == [
        [],
        ['1'],
        [],
    ]
    output_good = game.ui.test_output_list == [
        'O1\nO\nO\n\n', 'O\nO1\nO\n\n']
    return output_good and tower_good and (should_quit == False)


def main():

    print 'start test'

    if not test_turn_norm():
        print 'turn messed up on normal inputs.'

    if not test_turn_st_quit():
        print 'turn did not detect the first quit.'

    if not test_turn_nd_quit():
        print 'turn did not detect the second quit.'

    if not test_turn_st_invalid_input():
        print 'turn did not detect the first invalid input.'

    if not test_turn_nd_invalid_input():
        print 'turn did not detect the second invalid input.'

    if not test_turn_valid_move():
        print 'turn detected a invalid move when there was none.'

    if not test_turn_invalid_move():
        print 'turn did not detect the invalid move.'

    if not test_turn_win():
        print 'turn did not detected the win.'

    if not test_turn_not_win():
        print 'turn detected a win when there was none.'

    print 'end test'

if __name__ == '__main__':
    main()

