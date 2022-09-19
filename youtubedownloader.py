from pytube import YouTube, StreamQuery
from pytube.exceptions import PytubeError


def ask_action(streams: StreamQuery):
    while True:
        print("Available actions:")
        print("1. Download video")
        print("2. Download audio")
        print("3. Input another link")
        print("4. Exit")
        action = input("Enter action: ")
        
        video = None
        
        match action:
            case "1":
                print("Downloading video...")
                video = streams.get_highest_resolution()
            case "2":
                print("Downloading audio...")
                video = streams.get_audio_only(subtype="webm")
            case "3":
                ask_youtube_link()
            case "4":
                print("Bye bye!")
                break
            case _:
                print("\n Invalid action! \n")
                continue
        
        video.download()
        print("\n Finished! \n")
    

def ask_youtube_link():
    try:
        link = input("Enter link: ")
        yt = YouTube(url=link)
        ask_action(yt.streams)
    except PytubeError:
        print("\n Invalid Youtube Link! \n")
        ask_youtube_link()
    except KeyboardInterrupt:
        print("\nBye bye!")

def main():
    ask_youtube_link()

if __name__ == "__main__":
    main()