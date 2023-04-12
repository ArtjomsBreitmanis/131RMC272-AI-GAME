import tkinter as tk
from tkinter import messagebox
import random

class AIGAME:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("2 vai 5 dalijuma spele")
        
        self.existing_numChar = 0
        self.move_P = 1
        
        self.number_label = tk.Label(self.root, text="Current Number: ")
        self.number_label.pack()
        
        self.showNumVal = tk.Label(self.root, text="0")
        self.showNumVal.pack()
        
        self.player_label = tk.Label(self.root, text="User's Turn: ")
        self.score_P = tk.StringVar(value="1")
        self.player_value_label = tk.Label(self.root, textvariable=self.score_P)
        self.player_label.pack()
        self.player_value_label.pack()
        
        
        self.playthisnnumber = tk.StringVar()
        self.playthisnnumber.set("Computer")
        
          
        self.starting_player_menu = tk.OptionMenu(self.root, self.playthisnnumber, "Player", "Computer")
        self.starting_player_menu.pack()

        self.user_input_label = tk.Label(self.root, text="Enter number 2 or 5: ")
        self.user_input_label.pack()
        self.user_input_entry = tk.Entry(self.root)
        self.user_input_entry.pack()
        
        self.submit_button = tk.Button(self.root, text="GO!", command=self.acceptstake)
        self.submit_button.pack()
        
        self.generate_button = tk.Button(self.root, text="Random number", command=self.randgenbutton)
        self.generate_button.pack()
        
        self.begindiv_button = tk.Button(self.root, text="Start", command=self.begindiv)
        self.begindiv_button.pack()
        
        self.starting_player_label = tk.Label(self.root, text="Starting Player: ")
        self.starting_player_label.pack()

        self.info_button = tk.Button(text="Game Instruction!!!!", height=5,width=20, command=self.FAQ_agree)
        self.info_button.pack()
        self.number_label = tk.Label(self.root, text="Instructions: ")
        self.number_label.pack()
        self.number_label = tk.Label(self.root, text="1. To start game choose the starting player. ")
        self.number_label.pack()
        self.number_label = tk.Label(self.root, text="2. Choose starting number, enter number by hand in window, or click 'Random number'")
        self.number_label.pack()
        self.number_label = tk.Label(self.root, text="3. If User is chosen to start then press 'GO!', if Computer - press 'Start' ")
        self.number_label.pack()
        self.number_label = tk.Label(self.root, text="4. If the generated number is not dividable with 2 or 5, you can proceed and and game instantly, or regenerate pressing 'Random Number'")
        self.number_label.pack()
        self.number_label = tk.Label(self.root, text="5. Due to limit if tree depth numbers over 6000 will cause the loop error (regenerate)")
        self.number_label.pack()

    def FAQ_agree(self):
        win=tk.Toplevel()
        win.title('Terms')
        message="To start game You should accept terms of agreement, press 'Accept', or close the game.\n\n\n\n\nJust kidding, no one cares!"
        tk.Label(win, text=message).pack()
        tk.Button(win,text='Accept',height=5,width=10, command=self.FAQ).pack()
        

        messagebox.showinfo(title="Lecince",message="To start game You should accept terms of agreement, press 'Accept', or close the game.", command=self.FAQ)    
        

    def FAQ(self):
         messagebox.showinfo(title="Game Instructions", message="1. To start game, firsh select who starts the game 'User' or 'Computer'"+"\n"+"2. Click 'Random Number' button to generate number in box"+"\n"+"3. If the User starts press'GO!' button, if Computer starts - 'Start'"+"\n"+"4. If the generated number is not dividable with 2 or 5, you can proceed and and game instantly, or regenerate pressing 'Random Number'"+"\n"+"5. Due to limit if tree depth numbers over 6000 will cause the loop error (regenerate)")   

    def randgenbutton(self, doComputerMove : bool = True):
        self.existing_numChar = random.randint(1000, 1995) *5
        self.showNumVal.config(text=str(self.existing_numChar))
        if(doComputerMove):
            self.makeAImove()
        
    def restart(self):
        self.randgenbutton(False)
        self.tree = move_koks(self.existing_numChar)
        self.move_P = 1
        self.score_P.set(self.move_P)
        self.user_input_entry.delete(0, tk.END)
    def begindiv(self):
        if(self.existing_numChar > 0):
            self.tree = move_koks(self.existing_numChar)
        else:
            messagebox.showinfo(title="Attention",message="Not valid move, You should enter YOUR number, Or press Random to generate number.")
        self.move_P = 1
        self.score_P.set(self.move_P)
        self.user_input_entry.delete(0, tk.END)
        self.makeAImove()        
    
        
    def acceptstake(self):
        num_gen_in = self.user_input_entry.get()
        if num_gen_in not in ["2", "5"]:
            messagebox.showinfo(title="Attention",message="Not valid move, only 2 or 5 are accepted")
            return
        num_gen_in = int(num_gen_in)
        
        if self.existing_numChar % num_gen_in != 0:
            messagebox.showerror(title="User-looser", message= "Cannot be divided, You loose!")
            self.restart()
            return
        
        self.existing_numChar //= num_gen_in
        self.showNumVal.config(text=str(self.existing_numChar))
        self.move_P = self.move_P + 1
        self.score_P.set(self.move_P)
        
        
        if self.existing_numChar == 1:
            messagebox.showinfo("Congratulations! Player {} wins!".format(self.move_P))
            self.restart()
        else:
            self.makeAImove()

    def makeAImove(self):
        if (self.move_P % 2 == 0 and self.playthisnnumber.get() == "Player")\
        or (self.move_P % 2 != 0 and self.playthisnnumber.get() == "Computer"):  
            
            optimal_divisor = self.algominimax()
            if(optimal_divisor == None):
                messagebox.showwarning(title="Victory",message="You beat primitive AI algorithm, \nNumber is not divisible nor by 5 nor by 2. \nYou win!")
                return self.restart()
            self.existing_numChar //= optimal_divisor
            self.showNumVal.config(text=str(self.existing_numChar))
            self.move_P = 3 - self.move_P
            self.score_P.set(self.move_P)
            self.player_value_label.config(text=str(self.move_P))
            
            if self.existing_numChar == 1:
                messagebox.showinfo("Player {} wins!".format(self.move_P))
                self.restart()
                
    def algominimax(self):
       
        
        def eval_big(number):
         
            if number == 1:
                return 0
            if number % 2 == 0:
                return 1 + eval_big(number // 2)
            else:
                return 1 + eval_big(number // 5)
        
        def eval_small(number):
            
            if number == 1:
                return 0
            if number %2 == 0:
                return 1 + eval_small(number // 2)
            else:
                return 1 + eval_small(number // 5)
        
        divisors = [2, 5]
        bestnum = None
        numhigh = float('-inf')
        
        for divisor in divisors:
            if self.existing_numChar % divisor == 0:
                eval = eval_small(self.existing_numChar // divisor)
                if eval > numhigh:
                    numhigh = eval
                    bestnum = divisor
        
        return bestnum


def move_koks(number):
    root = Node(number)
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.value > 1:
            for move in [2, 5]:
                if canItBeDivided(node.value // move):
                    child = Node(node.value // move)
                    node.children.append(child)
                    queue.append(child)
    return root
def canItBeDivided(number):
    return number % 2 == 0 or number % 5 == 0
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    def moveLeaf(self):
        return len(self.children) == 0
            
if __name__ == "__main__":
    AI_GAME = AIGAME()
    AI_GAME.root.mainloop()

