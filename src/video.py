from defaultLocation import DefaultLocation
from clearScreen import ScreenCleaner
from pytube import YouTube
from rich import print
import os

def videoDownload(mainMenu):
    ScreenCleaner.clearScreen()
    print(""" [green_yellow]
 __     __ __       __                   
|  \   |  \  \     |  \                  
| ▓▓   | ▓▓\▓▓ ____| ▓▓ ______   ______  
| ▓▓   | ▓▓  \/      ▓▓/      \ /      \ 
 \▓▓\ /  ▓▓ ▓▓  ▓▓▓▓▓▓▓  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\ 
  \▓▓\  ▓▓| ▓▓ ▓▓  | ▓▓ ▓▓    ▓▓ ▓▓  | ▓▓
   \▓▓ ▓▓ | ▓▓ ▓▓__| ▓▓ ▓▓▓▓▓▓▓▓ ▓▓__/ ▓▓
    \▓▓▓  | ▓▓\▓▓    ▓▓\▓▓    \ \▓▓    ▓▓
     \▓    \▓▓ \▓▓▓▓▓▓▓ \▓▓▓▓▓▓  \▓▓▓▓▓▓ 
                                         
[/green_yellow]""")
    while True:
        try:
            url = input("Enter URL for the MOV file you want to download \n>> ")
            video = YouTube(url)
            print(f"[italic orange3]{video.title} [/italic orange3]")
            stream = video.streams.get_highest_resolution()
        except:
            print(f"[bold red]{url} does not exist[/bold red]\n")
            continue

        while True:
            location = input(f"Save to directory [Default: {DefaultLocation.getDefaultSaveLocation()}]\n>> ")
            if location == "":
                location = DefaultLocation.getDefaultSaveLocation()
            if not os.path.exists(location):
                print(f"[bold red]{location} does not exist[/bold red]\n")
                continue

            file_path = stream.download(output_path=location)
            base, ext = os.path.splitext(file_path)
            new_file = f"{base}.mov"

            if os.path.exists(new_file):
                print("[bold yellow]A file with the same name already exists. What do you want to do?[/bold yellow]")
                print("1) Replace the existing file")
                print("2) Rename the file")

                choice = input(">> ")
                if choice == "1":
                    os.remove(new_file)  # Delete the existing file
                    os.rename(file_path, new_file)  # Rename the file
                    print(f"[bold green]{video.title} replaced successfully[/bold green]\n")
                    break
                elif choice == "2":
                    while True:
                        new_file_name = input("Enter a new name for the file: ")
                        new_file = os.path.join(location, new_file_name + ".mov")
                        if not os.path.exists(new_file):
                            os.rename(file_path, new_file)  # Rename the file
                            print(f"[bold green]{video.title} renamed successfully to {new_file_name}[/bold green]\n")
                            break
                    break
                else:
                    print("[bold red]Invalid choice[/bold red]\n")
            else:
                os.rename(file_path, new_file)
                print(f"[bold green]{video.title} saved successfully[/bold green]\n")
                break

        input("Press Enter to continue...")
        mainMenu()

