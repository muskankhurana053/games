import sys
print("""hey player yu can enter your input by choosing a number from 1-9 
            1|2|3
            -----
            4|5|6
            -----
            7|8|9
      
      """)

board=[" "," "," "," "," "," "," "," "," "]
def disp():
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("_____")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("_____")
    print(f"{board[6]}|{board[7]}|{board[8]}")
def onepl():
    posi=int(input("player1 enter the position you want to choose"))
    if board[posi-1]==" ":
        board[posi-1]="X"
    else:
        print("That position is occupied, kindly pick another")
        onepl()
        
def twopl():
    posi=int(input("player2 enter the position you want to choose"))
    if board[posi-1]==" ":
        board[posi-1]="0"
    else:
        print("That position is occupied, kindly pick another")
        twopl()
    
def statuscheck():
    
    
    if(board[0]==board[1]==board[2]=="X"or board[3]==board[4]==board[5]=="X" or board[6]==board[7]==board[8]=="X" or board[1]==board[4]==board[7]=="X" or board[0]==board[3]==board[6]=="X" or board[2]==board[5]==board[8]=="X" or board[0]==board[4]==board[7]=="X" or board[2]==board[4]==board[6]=="X"):
        print('congratulation!!player1 is the winner')
        sys.exit()
    elif(board[0]==board[1]==board[2]=="0"or board[3]==board[4]==board[5]=="0" or board[6]==board[7]==board[8]=="0" 
        or board[1]==board[4]==board[7]=="0" or board[0]==board[3]==board[6]=="0" or board[2]==board[5]==board[8]=="0" 
        or board[0]==board[4]==board[7]=="0" or board[2]==board[4]==board[6]=="0"):
        print('congratulation!!player2 is the winner')
        sys.exit()
            
    elif(board[0]!=" "and board[1]!=" " and board[2]!=" " and board[3]!=" " and board[4]!=" " and board[5]!=" " and board[6]!=" " and board[7]!=" " and board[8]!=" "):

        print('its a tie')
        sys.exit()
            

        
        
    
        
        
    
        
def runcode():
    i=1
    while i<=5:
        onepl()
        disp()
        statuscheck()
        twopl()
        disp()
        statuscheck()
        i+=1
    
    
runcode()        
        

    
