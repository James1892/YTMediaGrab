from defaultLocation import DefaultLocation
from clearScreen import ScreenCleaner
from pytube import YouTube
from rich import print
import os


def downloadMultiple(mainMenu):
    ScreenCleaner.clearScreen()
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
            downloadMultipleAudio(urls, mainMenu)
        elif option == "2":
            downloadMultipleVideos(urls, mainMenu)
        else:
            print("[bold red]Invalid option[/bold red]")


def downloadMultipleAudio(urls, mainMenu):
    location = input(f"Save to directory [Default: {DefaultLocation.getDefaultSaveLocation()}]\n>> ")
    
    while True:
        if location == "":
            location = DefaultLocation.getDefaultSaveLocation()
        if not os.path.exists(location):
            print(f"[bold red]{location} does not exist[/bold red]\n")
            location = input("Enter a valid directory path:\n>> ")
            continue
        else:
            break
    
    for url in urls:
        try:
            video = YouTube(url)
            print(f"[italic green]{video.title} [/italic green]")
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


def downloadMultipleVideos(urls, mainMenu):
    location = input(f"Save to directory [Default: {DefaultLocation.getDefaultSaveLocation()}]\n>> ")
    
    while True:
        if location == "":
            location = DefaultLocation.getDefaultSaveLocation()
        if not os.path.exists(location):
            print(f"[bold red]{location} does not exist[/bold red]\n")
            location = input("Enter a valid directory path:\n>> ")
            continue
        else:
            break
    
    for url in urls:
        try:
            video = YouTube(url)
            print(f"[italic green]{video.title} [/italic green]")
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
