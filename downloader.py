from pytube import YouTube

def download_youtube_video(url):
    # Create for the url an YouTube object
    try: 
        yt = YouTube(url)
    except: 
        print(f'{url} is not youtube video, try it again\n')
        main()
    
    # Pick a stream and download it
    stream = yt.streams.filter(progressive = True, res="720p")[0]

    try:
        stream.download(output_path='')
    except: 
        print(f'Error occured during downloading {yt.title}')
    

def main(): 
    url = input('URL of the Youtube video: ')

    while("www.youtube.com" not in url):
        print("No Youtube URL was entered - try again")
        url = input('URL of the Youtube video: ')
    
    download_youtube_video(url)
        

    
if __name__ == "__main__":
    main()