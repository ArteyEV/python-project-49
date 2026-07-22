from brain_games.engine import play_game
from brain_games.games.progression import generate_round

DESCRIPTION = 'What number is missing in the progression?'


def main():
    play_game(generate_round, DESCRIPTION)


if __name__ == '__main__':
    main()