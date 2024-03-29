from colorama import Style, Fore, Back
from castle import Castle
from player import Player
import random
# from utilities import *
import time

class Game:
    def __init__(self):
        self.players = []
        self.current_player = 0 # index

        self.current_sector = "A1" # coordinates
        self.board = [[Castle(), Castle(), Castle(), Castle(), Castle()],
                      [Castle(), Castle(), Castle(), Castle(), Castle()],
                      [Castle(), Castle(), Castle(), Castle(), Castle()],
                      [Castle(), Castle(), Castle(), Castle(), Castle()],
                      [Castle(), Castle(), Castle(), Castle(), Castle()]]

        self.prompt = ""
        self.invalid_prompt = ""
        self.confirm_message = ""
        self.LINE_UP = '\033[1A'

        self.round = 0
        self.gpa_setting = ""

    def print_gpa(self):
        """Prints the 13-line gameplay area. Moves cursor down 13 lines."""
        if self.gpa_setting == "":
            print("\n" * 13, end="")
        elif self.gpa_setting == "board":
            self.print_board(coordinates=False)
        elif self.gpa_setting == "board coords":
            self.print_board(coordinates=True)
        # TODO prob add more

    def print_board(self, coordinates=True, highlight=False):
        """Requires that the cursor be placed at the top of 
        the gameplay area.
        -If coordinates is True, then ABCDE and 12345 are displayed
        on the sides of the board
        -highlight specifies a sector or list of sectors to highlight.
        
        Moves the cursor down 13 lines."""
        # print first 3 empty lines
        print("\n\n\n", end="")

        # print top border of board
        if coordinates:
            print(" " * 8 + "╭─A─B─C─D─E─╮")
        else:
            print(" " * 8 + "╭───────────╮")

        # print 5 middle lines of board
        for row_idx,row in enumerate(self.board):
            print(" " * 8, end="")
            if coordinates:
                print(row_idx + 1, end=" ")
            else:
                print("│", end=" ")
            for col_idx,castle in enumerate(row):
                print(castle, end=" ")
            print("│")

        # print bottom border of board and then last 3 lines
        print(" " * 8 + "╰───────────╯")
        print("\n\n\n", end="")

    def print_screen(self):
        """If reload is True, then this function returns the cursor to 
        where it started."""
        
        # Print HUD
        current_money = "1000" # delete this later
        self.current_player = "RED" # delete this later
        print(f" {self.current_player} │ {self.current_sector} │ $ {current_money} │")
        print("─────┴────┴────────╯")

        self.print_gpa() # prints 13 lines

        # Print top of prompt box, leave cursor on prompt line
        print("─" * 70 + "\n\n", end="", flush=True)
        self.print_prompt_box() # prints 3 lines

    def clear_screen(self):
        """Moves cursor from bottom line to top line, clearing all text onscreen"""
        print((self.LINE_UP + " "*70 + "\r") * 19)

    def reload_screen(self):
        self.clear_screen()
        self.print_screen()

    def print_prompt_box(self, prompt_input=False, valid_inputs="",
                         invalid_inputs="", confirm=False, 
                         case_sensitive_input=False):
        """Assumes:
        -the cursor is located on the prompt line
        -self.prompt is set
        -if prompt_input == True:
            -valid_inputs is a non-empty string or list of strings
        -if confirm == True:
            -self.confirm_message is set
        -if invalid_inputs is nonempty:
            -invalid_inputs is a non-empty string or list of strings
            -self.invalid_prompt is set
        This function returns the cursor to the prompt line when it is done."""
        # Used to reset the cursor after input has been submitted,
        # meaning the cursor is located below the line where input takes place.
        reset_string = "\n\n" + (self.LINE_UP + " "*70 + "\r") * 4
        
        # Move cursor to bottom line to clear previous prompt,
        # then return cursor to prompt line
        print("\n\n" + reset_string, end="", flush=True)

        self.print_by_char(self.prompt)

        if prompt_input:
            if valid_inputs == "":
                print("ERROR in print_prompt_box()")

            inp = input(">>> ")
            print(reset_string, end="", flush=True)

            if not case_sensitive_input:
                valid_inputs = [i.lower() for i in valid_inputs]
                invalid_inputs = [i.lower() for i in invalid_inputs]

            while (inp not in valid_inputs and valid_inputs != "any") or (inp == ""):
                if not case_sensitive_input:
                    inp = inp.lower()
                if inp in invalid_inputs:
                    self.print_by_char(self.invalid_prompt)
                else:
                    self.print_by_char("Try again. " + self.prompt)
                inp = input(">>> ").lower()
                print(reset_string, end="", flush=True)

            # Get rid of >>>
            print("\n\n" + reset_string, end="", flush=True)

            if confirm:
                cm = self.confirm_message.replace("INP", inp)
                self.print_by_char(cm)
                conf_inp = input(">>> ").lower()
                print(reset_string, end="", flush=True)

                while conf_inp not in "yn":
                    self.print_by_char("Try again. " + cm)
                    conf_inp = input(">>> ").lower()
                    print(reset_string, end="", flush=True)

                # Get rid of >>>
                print("\n\n" + reset_string, end="", flush=True)

                if conf_inp == "y":
                    return inp
                elif conf_inp == "n":
                    return self.print_prompt_box(prompt_input, valid_inputs, invalid_inputs,
                                                 confirm, case_sensitive_input)
            else:
                return inp
        else:
            # cursor is on input line, no input necessary in this branch of code
            print(self.LINE_UP, end="")

    def add_players(self):
        max_players = 4
        available_colors = ["RED", "BLUE", "GREEN", "PINK"]

        # Input number of players
        self.prompt = "How many human players?"
        self.confirm_message = "Play with INP human players? (y/n)"
        self.invalid_prompt = "Choose between 1 and 4 human players."
        num_humans = int(self.print_prompt_box(True, "1234", "056789", True))

        num_cpus = max_players - num_humans
        for i in range(num_humans):
            p = Player()
            p.cpu = False

            # Input name for each player
            self.prompt = f"Enter a name for Player {i + 1}"
            self.confirm_message = "Confirm name for this player: INP (y/n)"
            p.name = self.print_prompt_box(True, "any", "", True, True)

            self.prompt = f"Name set to {p.name}."
            self.print_prompt_box()
            time.sleep(1.5)

            # Input color for each player
            color_string = ", ".join(available_colors)
            self.prompt = f"{p.name}, choose a color: {color_string}"
            self.confirm_message = "Confirm color for this player: INP (y/n)"
            p.color = self.print_prompt_box(True, available_colors, "", True).upper()
            available_colors.remove(p.color.upper())

            self.prompt = f"{p.name}'s color has been set to {p.color}."
            self.print_prompt_box()
            time.sleep(1.5)

            self.players.append(p)

        for i in range(num_cpus):
            p = Player()
            p.cpu = True

            # Name each CPU
            p.name = "CPU_" + str(i)

            # Assign a color to each CPU
            p.color = random.choice(available_colors)
            available_colors.remove(p.color.upper())

            self.prompt = f"{p.name} will play as {p.color}."
            self.print_prompt_box()
            time.sleep(1)

            self.players.append(p)

        # Recite all players
        self.prompt = "All players have been set. Reciting players..."
        self.print_prompt_box()
        time.sleep(1.5)
        for i,p in enumerate(self.players):
            self.prompt = f"Player {i + 1}: " + str(p)
            self.print_prompt_box()
            time.sleep(2)
        
    def get_sector(self, sector_coords):
        """Takes sector_coords like b3 and returns the castle object
        located in that sector in the board."""
        letters = "ABCDE"
        col = letters.index(sector_coords[0].upper())
        row = int(sector_coords[1]) - 1
        return self.board[row][col]
            
    def print_by_char(self, s, speed=0.01, end="\n"):
        for char in s:
            print(char, end="", flush=True)
            time.sleep(speed)
        print(end=end)

    def run_round(self):
        self.round += 1
        self.gpa_setting = "board coords"
        self.reload_screen()
        for idx, p in enumerate(self.players):
            valid_inputs = []
            invalid_inputs = []
            for col in "ABCDE":
                for row in "12345":
                    coords = col + row
                    if self.get_sector(coords).owner == "":
                        valid_inputs.append(coords)
                    else:
                        invalid_inputs.append(coords)

            self.prompt = f"{p}, choose a Sector to build a Sandcastle."
            self.confirm_message = f"Build a sandcastle in Sector INP? (y/n)"
            self.invalid_prompt = "There is already a Sandcastle in that Sector. Try again."
            sector_coords = self.print_prompt_box(True, valid_inputs, invalid_inputs, True)

            castle = self.get_sector(sector_coords)
            castle.owner = p.name
            # castle.color = get_color_code(p.color) #TODO input is color name, output is color code
            castle.hp = 100
            castle.level = 1
            castle.state = "1"
            p.castles.append(castle)

            self.reload_screen()

#####################################################################
    
g = Game()
g.prompt = "Welcome to the game!"
g.print_screen()
time.sleep(3)
g.add_players()

g.run_round()