import math
from rich import print
def progressBar(progress, total):
    percent = 100 *(progress / float(total))
    bar = "█" * int(percent) + '-' * (100 - int(percent))
    print(f"[green]\r|{bar}| {percent:.2f}%[/green]", end="\r")
