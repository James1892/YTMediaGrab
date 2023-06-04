#!/usr/bin/env python3

from pytube import YouTube
from rich import print
import os.path
import sys
import os

CONFIG_FILE = "config.txt"  # Path to the configuration file

def clearScreen():
    "Clears the terminal screen."
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and Mac
        os.system("clear")


def mainMenu():
    clearScreen()
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
            audioDownload()
        elif option == "2":
            videoDownload()
        elif option == "3":
            downloadMultiple()
        elif option == "4":
            setDefaultSaveLocation()
        elif option == "99":
            sys.exit()


def setDefaultSaveLocation():
    clearScreen()
    print("[blue]Set Default Save Location[/blue]")
    location = input("Enter the default save location or 'exit' to go back to main menu: ")
    if os.path.exists(location):
        with open(CONFIG_FILE, "w") as file:
            file.write(location)
        print(f"[bold green]Default save location set to {location}[/bold green]")
    elif location.lower() == "exit":
        mainMenu()
    else:
        print(f"[bold red]The specified location '{location}' does not exist.[/bold red]")
    input("Press Enter to continue...")
    mainMenu()


def getDefaultSaveLocation():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return file.read().strip()
    return ""


def audioDownload():
    clearScreen()
    print(""" [magenta]
 █████╗ ██╗   ██╗██████╗ ██╗ ██████╗ 
██╔══██╗██║   ██║██╔══██╗██║██╔═══██╗
███████║██║   ██║██║  ██║██║██║   ██║
██╔══██║██║   ██║██║  ██║██║██║   ██║
██║  ██║╚██████╔╝██████╔╝██║╚██████╔╝
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝ ╚═════╝ 

                  [/magenta] """)
    while True:
        try:
            url = input("Enter URL of the MP3 file you want to download\n>> ")  # YouTube URL input
            video = YouTube(url)
            print(video.title)  # Display the video title
            audio = video.streams.filter(only_audio=True).first()  # Grab only the audio
        except:
            print(f"[bold red]{url} invalid URL[/bold red]")
            continue
        else:
            while True:
                location = input(f"Save to directory [Default: {getDefaultSaveLocation()}]\n>> ")
                if location == "":
                    location = getDefaultSaveLocation()
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



def videoDownload():
    clearScreen()
    print(""" [yellow]
 __     __ __       __                   
|  \   |  \  \     |  \                  
| ▓▓   | ▓▓\▓▓ ____| ▓▓ ______   ______  
| ▓▓   | ▓▓  \/      ▓▓/      \ /      \ 
 \▓▓\ /  ▓▓ ▓▓  ▓▓▓▓▓▓▓  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\ 
  \▓▓\  ▓▓| ▓▓ ▓▓  | ▓▓ ▓▓    ▓▓ ▓▓  | ▓▓
   \▓▓ ▓▓ | ▓▓ ▓▓__| ▓▓ ▓▓▓▓▓▓▓▓ ▓▓__/ ▓▓
    \▓▓▓  | ▓▓\▓▓    ▓▓\▓▓     \\▓▓    ▓▓
     \▓    \▓▓ \▓▓▓▓▓▓▓ \▓▓▓▓▓▓▓ \▓▓▓▓▓▓ 
                                         
[/yellow]""")
    while True:
        try:
            url = input("Enter URL for the MOV file you want to download \n>> ")
            video = YouTube(url)
            print(video.title)
            stream = video.streams.get_highest_resolution()
        except:
            print(f"[bold red]{url} does not exist[/bold red]\n")
            continue

        while True:
            location = input(f"Save to directory [Default: {getDefaultSaveLocation()}]\n>> ")
            if location == "":
                location = getDefaultSaveLocation()
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


def downloadMultiple():
    clearScreen()
    print("""[cyan]

░░░░░░   ░░░░░  ░░░░░░░░  ░░░░░░ ░░   ░░     ░░░░░░   ░░░░░░  ░░     ░░ ░░░    ░░ ░░       ░░░░░░   ░░░░░  ░░░░░░  
▒▒   ▒▒ ▒▒   ▒▒    ▒▒    ▒▒      ▒▒   ▒▒     ▒▒   ▒▒ ▒▒    ▒▒ ▒▒     ▒▒ ▒▒▒▒   ▒▒ ▒▒      ▒▒    ▒▒ ▒▒   ▒▒ ▒▒   ▒▒ 
▒▒▒▒▒▒  ▒▒▒▒▒▒▒    ▒▒    ▒▒      ▒▒▒▒▒▒▒     ▒▒   ▒▒ ▒▒    ▒▒ ▒▒  ▒  ▒▒ ▒▒ ▒▒  ▒▒ ▒▒      ▒▒    ▒▒ ▒▒▒▒▒▒▒ ▒▒   ▒▒ 
▓▓   ▓▓ ▓▓   ▓▓    ▓▓    ▓▓      ▓▓   ▓▓     ▓▓   ▓▓ ▓▓    ▓▓ ▓▓ ▓▓▓ ▓▓ ▓▓  ▓▓ ▓▓ ▓▓      ▓▓    ▓▓ ▓▓   ▓▓ ▓▓   ▓▓ 
██████  ██   ██    ██     ██████ ██   ██     ██████   ██████   ███ ███  ██   ████ ███████  ██████  ██   ██ ██████  

                           
          [/cyan]""")
    urls = []
    while True:
        url = input("Enter URL of the file you want to download (or 'done' to finish):\n>> ")
        if url.lower() == "done":
            break
        urls.append(url)

    if not urls:
        print("[bold red]No URLs provided[/bold red]")
        input("Press Enter to continue...")
        mainMenu()

    while True:
        print("\nChoose a format")
        print("1) Audio")
        print("2) Video")
        option = input(">>  ")
        if option == "1":
            downloadMultipleAudio(urls)
        elif option == "2":
            downloadMultipleVideos(urls)
        else:
            print("[bold red]Invalid option[/bold red]")


def downloadMultipleAudio(urls):
    location = input(f"Save to directory [Default: {getDefaultSaveLocation()}]\n>> ")
    
    while True:
        if location == "":
            location = getDefaultSaveLocation()
        if not os.path.exists(location):
            print(f"[bold red]{location} does not exist[/bold red]\n")
            location = input("Enter a valid directory path:\n>> ")
            continue
        else:
            break
    
    for url in urls:
        try:
            video = YouTube(url)
            print(video.title)
            audio = video.streams.filter(only_audio=True).first()
        except:
            print(f"[bold red]{url} invalid URL[/bold red]\n")
            continue

        while True:
            saveFile = audio.download(output_path=location)
            base, ext = os.path.splitext(saveFile)
            newFile = f"{base}.mp3"

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


def downloadMultipleVideos(urls):
    location = input(f"Save to directory [Default: {getDefaultSaveLocation()}]\n>> ")
    
    while True:
        if location == "":
            location = getDefaultSaveLocation()
        if not os.path.exists(location):
            print(f"[bold red]{location} does not exist[/bold red]\n")
            location = input("Enter a valid directory path:\n>> ")
            continue
        else:
            break
    
    for url in urls:
        try:
            video = YouTube(url)
            print(video.title)
            download = video.streams.get_highest_resolution()
        except:
            print(f"[bold red]{url} does not exist[/bold red]\n")
            continue

        while True:
            saveFile = download.download(output_path=location)
            base, ext = os.path.splitext(saveFile)
            newFile = f"{base}.mov"

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
                        newFile = os.path.join(location, newFileName + ".mov")
                        if not os.path.exists(newFile):
                            os.rename(saveFile, newFile)  # Rename the file
                            print(f"[bold green]{video.title} renamed successfully to {newFileName}[/bold green]\n")
                            break
                    break
                else:
                    print("[bold red]Invalid input[/bold red]\n")
            else:
                os.rename(saveFile, newFile)
                print(f"[bold green]{video.title} saved successfully[/bold green]\n")
                break

    input("Press Enter to continue...")
    mainMenu()


if __name__ == "__main__":
    mainMenu()

