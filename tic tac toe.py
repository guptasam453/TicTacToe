class TicTacToe:

    def make_board(self, dim):
        board = [];
        for i in range(dim):
            row = []
            for j in range(dim):
                row.append("-")
            board.append(row)    
        return board
    
    def __init__(self, dim):
        self.board = self.make_board(dim)
        self.dim = dim
    
    def display_board(self):
        for i in range(self.dim):
            for j in range(self.dim):
                print(self.board[i][j] + "  ", end="")
            print("\n")
    
    def play_game(self):
        self.display_board()
        
        check = input("Player1 Do You Want To Quit: ")
        
        if check=="Yes":
            self.board = self.make_board(self.dim)
            print("Player1 Loose")
            return
        
        
        x = int(input("Player1 Enter Row Value: "))
        y = int(input("Player1 Enter Col Value: "))
        val = input("Player1 Enter Value: ")
        
        while(self.handle_turn(x, y, val) == -1):
            x = int(input("Player1 Enter Row Value: "))
            y = int(input("Player1 Enter Col Value: "))
            val = input("Player1 Enter Value: ")
        
        
        status = self.check_status(x, y, val)
        
        if status == 0:
            self.board = self.make_board(self.dim)
            print("Deuce")
            return
        
        elif status == 1:
            self.board = self.make_board(self.dim)
            print("Player1 Win")
            return
        
        
        self.display_board()
        
        check = input("Player2 Do You Want To Quit: ")
        
        if check=="Yes":
            self.board = self.make_board(self.dim)
            print("Player2 Loose")
            return
        
        
        x = int(input("Player2 Enter Row Value: "))
        y = int(input("Player2 Enter Col Value: "))
        val = input("Player2 Enter Value: ")
        
        while(self.handle_turn(x, y, val) == -1):
            x = int(input("Player2 Enter Row Value: "))
            y = int(input("Player2 Enter Col Value: "))
            val = input("Player2 Enter Value: ")
        
        status = self.check_status(x, y, val)
        
        if status == 0:
            self.board = self.make_board(self.dim)
            print("Deuce")
            return
        
        elif status == 1:
            self.board = self.make_board(self.dim)
            print("Player2 Win")
            return
        
        return
        
    def handle_turn(self, x, y, val):
        if(self.board[x][y]!="-"):
            print("Invalid Entry")
            return -1
        
        self.board[x][y] = val
        return
    
    def check_status(self, x, y, val):

        count = 0
        for i in range(self.dim):
            if(self.board[i][y]==val):
                count+=1
        if count==self.dim:
            return 1
        
        count = 0;
        for j in range(self.dim):
            if(self.board[x][j]==val):
                count+=1
        if count==self.dim:
            return 1;
        
        count = 0
        if x==y:
            for i in range(self.dim):
                if self.board[i][i] == val:
                    count+=1
            if count==self.dim:
                return 1
            
        count = 0
        if x==2-y:
            for i in range(self.dim):
                if self.board[i][self.dim-1-i] == val:
                    count+=1
            if count==self.dim:
                return 1
        
        
        flag = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if(self.board[i][j]=="-"):
                    flag = 1
                    break
            if flag==1:
                break
        
        if(flag==0):
            return 0
        
        return