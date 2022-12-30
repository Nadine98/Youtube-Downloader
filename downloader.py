from pytube import YouTube

def download_youtube_video(url):
  
    # Create for the url an YouTube object
    try: 
        yt = YouTube(url)
    except: 
        print(f'{url} is not youtube video, try it again\n')
        main()
    
    # pick a stream and download it
    stream = yt.streams.filter(progressive = True, res="720p")[0]

    try:
        stream.download()
    except: 
        print(f'Error occured during downloadign {yt.title}')
    
    

def main(): 
    url = str(input('URL of the Youtube video: '))

    while("www.youtube.com" not in url):
        print("No Youtube URL was entered - try again")
        url = str(input('URL of the Youtube video: '))
    
    download_youtube_video(url)
        

    
if __name__ == "__main__":
    main()