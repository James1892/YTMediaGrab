from defaultLocation import DefaultLocation
from clearScreen import ScreenCleaner
from pytube import YouTube, Playlist
from rich import print
import os



def downloadPlaylist(mainMenu):
    ScreenCleaner.clearScreen()

    print("""
▀██▀▀█▄  ▀██                    ▀██   ██           ▄   
 ██   ██  ██   ▄▄▄▄    ▄▄▄▄ ▄▄▄  ██  ▄▄▄   ▄▄▄▄  ▄██▄  
 ██▄▄▄█▀  ██  ▀▀ ▄██    ▀█▄  █   ██   ██  ██▄ ▀   ██   
 ██       ██  ▄█▀ ██     ▀█▄█    ██   ██  ▄ ▀█▄▄  ██   
▄██▄     ▄██▄ ▀█▄▄▀█▀     ▀█    ▄██▄ ▄██▄ █▀▄▄█▀  ▀█▄▀ 
                       ▄▄ █                            
                        ▀▀                             
          """)
    while True:
        try:
            # Get the URL of the playlist
            playListUrl = input("Enter URL of the playlist you want to download\n>> ")
            # Create an instance of the playlist class
            playlist = Playlist(playListUrl)
            # Get URLs of the videos in the playlist
            videoUrls = playlist.video_urls

            # Check if the entered URL is a playlist
            if not videoUrls:
                while True:
                    print("[bold red]Invalid: URL is not a playlist. Would you like to try again? (y/n)[/bold red]")
                    tryAgain = input(">> ")
                    if tryAgain.lower() == 'y':
                        # Retry by restarting the loop
                        break
                    elif tryAgain.lower() == 'n':
                        mainMenu()
                        return  # Exit the function
                    else:
                        print("[bold red]Invalid option[/bold red]")
                continue  # Restart the loop if URL is not a playlist

            break
        except Exception:
            print(f"[bold red]Invalid url[/bold red]")
            # Handle the exception and allow the user to try again

    while True:
        print("\nChoose a format")
        print("1) Audio")
        print("2) Video")
        option = input(">> ")
        if option == "1":
            audioFormat(videoUrls, mainMenu)
            break
        elif option == "2":
            videoFormat(videoUrls, mainMenu)
            break
        else:
            print("[bold red]Invalid option[/bold red]")



def audioFormat(urls, mainMenu):
    location = input(f"Save to directory [Default: {DefaultLocation.getDefaultSaveLocation()}]\n>> ")

    while True:
        if location == "":
            location = DefaultLocation.getDefaultSaveLocation()
        
        if not os.path.exists(location):
            print(f"[bold red]{location} does not exist[/bold red]\n")
            location = input("Enter a valid directory path\n>> ")
            continue
        else:
            break

    for url in urls:
        try:
            video = YouTube(url)
            print(f"[italic magenta]{video.title} [/italic magenta]")
            audio = video.streams.filter(only_audio=True).first()
        except:
            print(f"[bold red]{url} is an invalid URL[/bold red]\n")
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
                        newFileName = input("Enter a new name for the file\n>> ")
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

def videoFormat(urls, mainMenu):
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
