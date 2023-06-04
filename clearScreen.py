import os

class ScreenCleaner:
    @staticmethod
    def clearScreen():
        "Clears the terminal screen."
        if os.name == 'nt':  # For Windows
            os.system('cls')
        else:  # For Linux and Mac
            os.system("clear")
