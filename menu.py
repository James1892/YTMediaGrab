
from multiple import downloadMultiple, downloadMultipleAudio, downloadMultipleVideos
from defaultLocation import DefaultLocation
from clearScreen import ScreenCleaner
from audio import audioDownload
from video import videoDownload
from rich import print
import sys

CONFIG_FILE = "config.txt"  # Path to the configuration file

def mainMenu():
    ScreenCleaner.clearScreen()
    while True:
        print("""[red]
██╗   ██╗████████╗███╗   ███╗███████╗██████╗ ██╗ █████╗  ██████╗ ██████╗  █████╗ ██████╗ 
╚██╗ ██╔╝╚══██╔══╝████╗ ████║██╔════╝██╔══██╗██║██╔══██╗██╔════╝ ██╔══██╗██╔══██╗██╔══██╗
 ╚████╔╝    ██║   ██╔████╔██║█████╗  ██║  ██║██║███████║██║  ███╗██████╔╝███████║██████╔╝
  ╚██╔╝     ██║   ██║╚██╔╝██║██╔══╝  ██║  ██║██║██╔══██║██║   ██║██╔══██╗██╔══██║██╔══██╗
   ██║      ██║   ██║ ╚═╝ ██║███████╗██████╔╝██║██║  ██║╚██████╔╝██║  ██║██║  ██║██████╔╝
   ╚═╝      ╚═╝   ╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
       
   [/red][white]v1.3                                                       By James[/white]""")

        print("""======================================================================
        options:
                    1) Audio
                    2) Video
                    3) Download Multiple URLs
                    4) Set Default Save Location
                    99) Exit
======================================================================""")

        option = input(">> ")
        if option == "1":
            audioDownload(mainMenu)  # Pass mainMenu function as an argument
        elif option == "2":
            videoDownload(mainMenu)
        elif option == "3":
            downloadMultiple(mainMenu)
        elif option == "4":
            DefaultLocation.setDefaultSaveLocation()
        elif option == "99":
            sys.exit()

