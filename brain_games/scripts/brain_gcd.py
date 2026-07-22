from brain_games.engine import play_game
from brain_games.games.gcd import generate_round

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def main():
    play_game(generate_round, DESCRIPTION)


if __name__ == '__main__':
    main()