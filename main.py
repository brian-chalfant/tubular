from pytube import Playlist, YouTube


yt = Playlist("https://www.youtube.com/playlist?list=PLMRqhzcHGw1ZkH8RuznGMS0NZs0jWQQ5a")
print(yt)
for video in yt:
    thisV = YouTube(video)
    stream = thisV.streams.first()
    stream.download()