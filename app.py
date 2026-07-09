import random
import time

initial_message = f'''
{32*'='}
Rock Paper Scissors Lizard Spock
{32*'='}

1) ✊
2) ✋
3) ✌️
4) 🦎
5) 🖖
'''

pedra, papel, tesoura, lagarto, spock = 1, 2, 3, 4, 5

hands = {1: '✊', 2: '✋', 3: '✌️', 4: '🦎', 5: '🖖'}

while True:
    print(initial_message)
    cpu_choice = random.choice([1,2,3,4,5])
    try:
        user_choice = int(input('Pick a number: '))
        if user_choice in hands.keys():
            print('JO-KEN-PÔ!!!\n')
            time.sleep(1)

            print(f'You chose: {hands[user_choice]}')
            print(f'CPU chose: {hands[cpu_choice]}')

            if cpu_choice == user_choice:
                print('It\'s a tie')
            elif user_choice == tesoura and cpu_choice == papel or user_choice == papel and cpu_choice == pedra or user_choice == pedra and cpu_choice == lagarto or user_choice == lagarto and cpu_choice == spock or user_choice == spock and cpu_choice == tesoura or user_choice == tesoura and cpu_choice == lagarto or user_choice == lagarto and cpu_choice == papel or user_choice == papel and cpu_choice == spock or user_choice == spock and cpu_choice == pedra or user_choice == pedra and cpu_choice == tesoura:
                print('The player won!')
            else:
                print('The CPU won!')
        else:
            print('ERROR: INVALID OPTION!')
    except ValueError:
        print('OMG THERE\'S AN ERROR!!!')

    second_chance = input('\nDo u wanna try again? 1) Yes | 2) No: \n')
    if second_chance == '1':
        print('Iniating a new game...\n')
        continue
    else:
        print('\nGoodbye!')
        break


