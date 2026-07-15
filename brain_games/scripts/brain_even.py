from brain_games.engine import play_game
from brain_games.games.even import generate_round

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    play_game(generate_round, DESCRIPTION)


if __name__ == '__main__':
    main()