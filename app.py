import random
import time

pedra, papel, tesoura, lagarto, spock = list(range(1, 6))

emoji = {1: '✊', 2: '✋', 3: '✌️', 4: '🦎', 5: '🖖'}

user_victory_message = 'The player won!'
results = {
    (tesoura, papel): user_victory_message,
    (papel, pedra): user_victory_message,
    (pedra, lagarto): user_victory_message,
    (lagarto, spock): user_victory_message,
    (spock, tesoura): user_victory_message,
    (tesoura, lagarto): user_victory_message,
    (lagarto, papel): user_victory_message,
    (papel, spock): user_victory_message,
    (spock, pedra): user_victory_message,
    (pedra, tesoura): user_victory_message
}



while True:
    print(f'''
{32*'='}
Rock Paper Scissors Lizard Spock
{32*'='}

1) ✊
2) ✋
3) ✌️
4) 🦎
5) 🖖
''')
    try:
        cpu_choice = random.choice(list(range(1,6)))
        user_choice = int(input('Pick a number: '))
        valid_user_choice = 1 <= user_choice <= 5

        if not valid_user_choice:
            continue

        print('JO-KEN-PÔ!!!\n')
        time.sleep(1)

        print(f'You chose: {emoji[user_choice]}')
        print(f'CPU chose: {emoji[cpu_choice]}')

        if cpu_choice == user_choice:
            print('It\'s a tie')
        else:
            result_message = results.get((user_choice, cpu_choice), 'CPU Won!')
            print(result_message)
    except ValueError:
        print('ERROR: Try a number between 1 and 5!')

    second_chance = input('\nDo u wanna try again? 1) Yes | 2) No: \n')
    if second_chance == '1':
        print('Iniating a new game...\n')
        continue
    else:
        print('\nGoodbye!')
        break


