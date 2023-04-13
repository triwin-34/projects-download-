from pytube import YouTube
video_url = 'https://www.youtube.com/watch?v=LyhQ3uMBoq4'
yt = YouTube(video_url)
stream = yt.streams.filter(res='144p').first()

stream.download()