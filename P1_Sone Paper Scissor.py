import random


def compChoice():
    randNo = random.randint(1, 3)
    if randNo == 1:
        Comp = 'S'
    if randNo == 2:
        Comp = 'P'
    if randNo == 3:
        Comp = 'SC'
    return Comp


def game(Comp, Player):
    if Comp == Player:
        return None

    elif Comp == 'S':
        if Player == 'SC':
            return False
        elif Player == 'P':
            return True

    elif Comp == 'P':
        if Player == 'S':
            return False
        elif Player == 'SC':
            return True

    elif Comp == 'SC':
        if Player == 'P':
            return False
        elif Player == 'S':
            return True

    return -1


score = 0

while True:

    comp = compChoice()

    player = input(
        "Player : [Exit (Press [E]) , Restart (Press [R])] , [Stone (Press [S]) , Paper (Press [P]) , Scissor (Press [SC])] : ")

    if player == 'E':
        break
    elif player == 'R':
        print(f"\n\nTotal Score : {score}")
        score = 0

    A = game(comp, player)

    if A == None:
        print(F"\n\nComputer Chose '{comp}'")
        print(f"\n\nTie , Score : {score}")
    elif A == True:
        print(F"\n\nComputer Chose '{comp}'")
        score = score + 1
        print(f"\n\nVictory , Score : {score}")
    elif A == False:
        print(F"\n\nComputer Chose '{comp}'")
        score = score - 1
        print(f"\n\nDefeat , Score : {score}")
    elif A == -1:
        pass

    print("\n")

print(f"\n\nTotal Score : {score}")
print("\ngg")
