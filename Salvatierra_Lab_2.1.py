from random import randint

who_beats_who = {
    'rock': ['lizard', 'scissors'],
    'paper': ['spock', 'rock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['paper', 'spock'],
    'spock': ['scissors', 'rock'],
}
number_option_to_named_option = {
    1: 'rock',
    2: 'paper',
    3: 'scissors',
    4: 'lizard',
    5: 'spock',
}

def play_rock_paper_scissors_lizard_spock() -> bool:
    """
    Play rock paper scissors lizard spock against the computer
    """
    # ask user to choose option and make sure is valid
    user_choose: int = input(
        'Choose one of the options: 1)Rock, 2)Paper, 3)Scissors, 4)Lizard, '
        '5)Spock: '
    )
    while user_choose not in ['1', '2', '3', '4', '5']:
        user_choose = input(
            'Please select the right option: 1)Rock, 2)Paper, 3)Scissors, '
            '4)Lizard, 5)Spock: '
        )

    user_choose = int(user_choose)
    machine_choose: int = randint(1, 5)
    
    # Parse number option to string (easy to map and read)
    user_choose = number_option_to_named_option[user_choose]
    machine_choose = number_option_to_named_option[machine_choose]
    print(f'You chose {user_choose} and the computer chose {machine_choose}')

    # if both choose the same end the function, and return true to repeat the
    # process ask again to choose an option
    if user_choose == machine_choose:
        print(
            'You need to choose again because the computer and you chose the '
            'same option'
        )
        return True

    # if we find the machine's option in the list of the options that the user
    # beats, it means that the user won, otherwise the macine won
    if machine_choose in who_beats_who[user_choose]:
        print(f'You win because {user_choose} beat {machine_choose}')
    else:
        print(f'You lose because {machine_choose} beat {user_choose}')

    keep_playing = input('Do you want to play again? 1)Yes 2)No :') or ''
    while keep_playing not in ['1', '2']:
        keep_playing = input(
            'Please select the right option. Do you want to play again? 1)Yes '
            '2)No: '
        )
    return True if keep_playing == '1' else False

print('Let\'s play Rock, Paper, Scissors, Lizard, Spock')

keep_playing: bool = True
while keep_playing == 1:
    keep_playing = play_rock_paper_scissors_lizard_spock()

print('Thanks for playing!')
