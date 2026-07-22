from brain_games.engine import play_game
from brain_games.games.prime import generate_round

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    play_game(generate_round, DESCRIPTION)


if __name__ == '__main__':
    main()