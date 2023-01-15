from os import system
board=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]


def display_board():

    x=(5*"***")

    print(f"          {x}") 

    for liste in board:

        print(f"          * {liste[0]}  | {liste[1]}  |{liste[2]}  *")

        print(f"          * ---|--- |---*")
    
    print(f"          {x}") 

display_board()



def player_input(player):

    print(f"\nPlayer {player}'s turn...")

    l=int(input("\nEnter row :"))

    while l<1 or l>3:

        l=int(input("\nEnter row between 1 and 3:"))

    c=int(input("\nEnter column :"))

    while c<1 or c>3:
        c=int(input("\nEnter column between 1 and 3:"))

    if board[l-1][c-1]==" ":

        board[l-1][c-1]=player

        display_board()

    else:
        print(f"The cell is busy! ")

        player_input(player)
    
def check_win():

    if board[0][0]!=" " and (board[0][0]==board[0][1] and board[0][0]==board[0][2]):

        return 1

    elif board[1][0]!=" " and (board[1][0]==board[1][1] and board[1][0]==board[1][2]):

        return 1
        
    elif board[2][0]!=" " and(board[2][0]==board[2][1] and board[2][0]==board[2][2]):
        return 1
    elif board[0][0]!=" " and (board[0][0]==board[1][0] and board[0][0]==board[2][0]):
        return 1
    elif board[0][1]!=" " and (board[0][1]==board[1][1] and board[0][1]==board[2][1]):
        return 1
    elif board[0][2]!=" " and (board[0][2]==board[1][2] and board[0][2]==board[2][2]):
        return 1
    elif board[0][0]!=" " and (board[0][0]==board[1][1] and board[0][0]==board[2][2]):
        return 1
    elif board[0][2]!=" " and (board[0][2]==board[1][2] and board[0][2]==board[2][0]):
        return 1
    else:
        return 0
    
def play():
    for i in range(4):
        player_input('X')
        if check_win():
            print("Player X win!")
            break
        player_input('O')
        if check_win():
            print("Player O win!")
            break
    else:
        print("Match nul!")
        
            
play()