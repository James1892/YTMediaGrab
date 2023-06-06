
from defaultLocation import DefaultLocation
from clearScreen import ScreenCleaner
from pytube import YouTube
from rich import print
import os

def audioDownload(mainMenu):
    ScreenCleaner.clearScreen()
    print(""" [dark_magenta]
 █████╗ ██╗   ██╗██████╗ ██╗ ██████╗ 
██╔══██╗██║   ██║██╔══██╗██║██╔═══██╗
███████║██║   ██║██║  ██║██║██║   ██║
██╔══██║██║   ██║██║  ██║██║██║   ██║
██║  ██║╚██████╔╝██████╔╝██║╚██████╔╝
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝ ╚═════╝ 

                  [/dark_magenta] """)
    while True:
        try:
            url = input("Enter URL of the MP3 file you want to download\n>> ")  # YouTube URL input
            video = YouTube(url)
            print(f"[italic orange3]{video.title} [/italic orange3]")  # Display the video title
            audio = video.streams.filter(only_audio=True).first()  # Grab only the audio
        except:
            print(f"[bold red]{url} invalid URL[/bold red]")
            continue
        else:
            while True:
                location = input(f"Save to directory [Default: {DefaultLocation.getDefaultSaveLocation()}]\n>> ")
                if location == "":
                    location = DefaultLocation.getDefaultSaveLocation()
                if not os.path.exists(location):
                    print(f"[bold red]{location} does not exist[/bold red]\n")
                    continue

                saveFile = audio.download(output_path=location)  # Get the location then download the audio
                base, ext = os.path.splitext(saveFile)
                newFile = base + ".mp3"  # Change the extension of the file
                
                # Handling file already exists error
                if os.path.exists(newFile):
                    print("[bold yellow]A file with the same name already exists. What do you want to do?[/bold yellow]")
                
                    print("1) Replace the existing file")
                    print("2) Rename the file")
                    choice = input(">> ")
                    if choice == "1":
                        os.remove(newFile)  # Delete the existing file
                        os.rename(saveFile, newFile)  # Rename the file
                        print(f"[bold green]{video.title} replaced successfully[/bold green]\n")
                        break
                    elif choice == "2":
                        while True:
                            newFileName = input("Enter a new name for the file: ")
                            newFile = os.path.join(location, newFileName + ".mp3")
                            if not os.path.exists(newFile):
                                os.rename(saveFile, newFile)  # Rename the file
                                print(f"[bold green]{video.title} renamed successfully to {newFileName}[/bold green]\n")
                                break
                        break
                    else:
                        print("[bold red]Invalid choice[/bold red]\n")
                else:
                    os.rename(saveFile, newFile)
                    print(f"[bold green]{video.title} saved successfully[/bold green]\n")
                    break

        input("Press Enter to continue...")
        mainMenu()

