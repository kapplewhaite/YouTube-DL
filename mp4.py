from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

while True:

    link = input("Enter the YouTube video URL: ")
    Download(link)

    rerun = input("Would you like to download another video? (y/n): ")
    if rerun == "n":
        break