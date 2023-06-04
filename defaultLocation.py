import os
from rich import print
from clearScreen import ScreenCleaner

CONFIG_FILE = "config.txt"  # Path to the configuration file

class DefaultLocation:
    @staticmethod
    def setDefaultSaveLocation():
        ScreenCleaner().clearScreen()
        print("[blue]Set Default Save Location[/blue]")
        location = input("Enter the default save location or 'exit' to go back to the main menu:\n>> ")
        if os.path.exists(location):
            with open(CONFIG_FILE, "w") as file:
                file.write(location)
            print(f"[bold green]Default save location set to {location}[/bold green]")
        elif location.lower() == "exit":
            ScreenCleaner.clearScreen()
            return  # Return instead of calling mainMenu() directly
        else:
            print(f"[bold red]The specified location '{location}' does not exist.[/bold red]")
        input("Press Enter to continue...")

    @staticmethod
    def getDefaultSaveLocation():
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as file:
                return file.read().strip()
        return ""

