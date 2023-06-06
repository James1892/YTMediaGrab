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
            url = input("Enter URL for the video you want to download \n>> ")
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

            file_name = video.title + ".mp4"
            file_path = os.path.join(location, file_name)

            if os.path.exists(file_path):
                print("[bold yellow]A file with the same name already exists. What do you want to do?[/bold yellow]")
                print("1) Replace the existing file")
                print("2) Rename the file")

                choice = input(">> ")
                if choice == "1":
                    os.remove(file_path)  # Delete the existing file
                    print(f"[bold green]{video.title} replaced successfully[/bold green]\n")
                    break
                elif choice == "2":
                    while True:
                        new_file_name = input("Enter a new name for the file: ")
                        new_file_path = os.path.join(location, new_file_name + ".mp4")
                        if not os.path.exists(new_file_path):
                            file_path = new_file_path
                            print(f"[bold green]{video.title} renamed successfully to {new_file_name}[/bold green]\n")
                            break
                    break
                else:
                    print("[bold red]Invalid choice[/bold red]\n")
            else:
                stream.download(output_path=location, filename=file_name)
                print(f"[bold green]{video.title} saved successfully[/bold green]\n")
                break


        input("Press Enter to continue...")
        mainMenu()

