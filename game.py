from getpass import getpass as input
print("Select your move R, P or S")
player_1, player_2 = input("Player 1 > ").upper(), input("Player 2 > ").upper()
mydict = {'R':{'R':'Draw', 'P':'Paper wins rock', 'S':'Rock wins scissors'}, 'P':{'R':'Paper wins rock', 'P':'Draw', 'S':'Scissors cut paper'}, 'S':{'R':'Rock wins scissors', 'P':'Scissors cut paper', 'S':'Draw'}}
try:
    print(mydict[player_1][player_2])
except:
    print('Non-valid inputs')
