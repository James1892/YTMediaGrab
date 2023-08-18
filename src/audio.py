from defaultLocation import DefaultLocation
from clearScreen import ScreenCleaner
from pytube import YouTube
from rich import print
import subprocess
import os

def convertToMp3(input_file, output_file):
    subprocess.run(["ffmpeg", "-i", input_file, "-vn", "-acodec", "libmp3lame", "-y", "-loglevel", "error", output_file])

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
                convertedFile = base + ".mp3"  # Convert the file with the same base name and ".mp3" extension
                
                # Handling file already exists error
                if os.path.exists(convertedFile):
                    print("[bold yellow]A file with the same name already exists. What do you want to do?[/bold yellow]") 
                    print("1) Replace the existing file")
                    print("2) Rename the file")
                    choice = input(">> ")
                    if choice == "1":
                        os.remove(convertedFile)  # Delete the existing file
                        convertToMp3(saveFile, convertedFile)  # Convert and replace
                        print(f"[bold green]{video.title} replaced successfully[/bold green]\n")
                        break
                    elif choice == "2":
                        while True:
                            newFileName = input("Enter a new name for the file: ")
                            convertedFile = os.path.join(location, newFileName + ".mp3")
                            if not os.path.exists(convertedFile):
                                convertToMp3(saveFile, convertedFile)  # Convert and rename
                                print(f"[bold green]{video.title} renamed successfully to {newFileName}[/bold green]\n")
                                break
                        break
                    else:
                        print("[bold red]Invalid choice[/bold red]\n")
                else:
                    convertToMp3(saveFile, convertedFile)  # Convert and save
                    os.remove(saveFile)  # Remove the original MP4 file
                    print(f"[bold green]{video.title} saved successfully[/bold green]\n")
                    break

        input("Press Enter to continue...")
        mainMenu()

