from pytube import YouTube, Playlist
from pathlib import Path
import os
import concurrent.futures

from pytube.exceptions import RegexMatchError

homedir = str(Path.home())
HOME = os.path.join(homedir, "YouTubeDownloads/")
DOWNLOAD_PATH = None
DEBUG = True

def downloadOne(link):
    try:
        pack = YouTube(link)
        pack.streams.filter(subtype='mp4').order_by('resolution').desc().first().download(DOWNLOAD_PATH)
        return str(pack.title) + " Downloaded"
    except RegexMatchError:
        print("Stream not Found")


def downloadAll(pl_link):
    pl = Playlist(pl_link)
    number_of_videos = len(pl)
    title = pl.title()
    makedirectory(title)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        try:
            results = [executor.submit(downloadOne, link) for link in pl]
            if DEBUG: print("Link List Generated")
            for f in concurrent.futures.as_completed(results):
                print(f.result())
        except AttributeError:
            print("No Results for search")


def makedirectory(user_input):
    os.mkdir(HOME + user_input)
    global DOWNLOAD_PATH
    DOWNLOAD_PATH = os.path.join(HOME, user_input)


playlistlink = input("Enter Playlist Link: ")
downloadAll(playlistlink)
