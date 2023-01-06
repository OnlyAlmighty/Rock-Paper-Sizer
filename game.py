from getpass import getpass as input
print("Rock,Paper,Scissors")
print("Select your move R, P or S")
player_1 = input("Player 1 > ").upper()
player_2 = input("Player 2 > ").upper()
if player_1 == player_2:
    print('Draw')
elif player_1 == 'R':
    if player_2 == 'S':
        print('Rock wins scissors')
    else:
        print('Rock loses to paper')
elif player_1 == 'P':
    if player_2 == 'R':
        print('Paper wins rock')
    else:
        print('Paper loses to scissors')
elif player_1 == 'S':
    if player_2 == 'P':
        print('Scissors wins paper')
    else:
        print('Scissors lose to rock')
