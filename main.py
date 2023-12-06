from pytube import YouTube, Playlist

def download(ytObject, path='./vids/'):
    try:
        ytObject.download(output_path=path)
    except:
        print('An error has occured during download')
        return 'An error has occured during download'
    return 'success'

def downloadVidio(link, audioOnly=False, path='./vids/'):
    ytObject = YouTube(link)
    if audioOnly:
        ytObject = ytObject.streams.get_audio_only()
    else:
        ytObject = ytObject.streams.get_highest_resolution()
    result = download(ytObject, path)
    return result
    

def downloadAudio(link):
    ytObject = YouTube(link)
    ytObject = ytObject.streams.get_audio_only()
    result = download(ytObject)
    return result

def downloadPlaylist(link, audioOnly=False, path='./vids/'):
    playlistObj = Playlist(link)
    playlistName = playlistObj.title
    playlistPath = f'{path}{playlistName}'
    for video in playlistObj.video_urls:
        downloadVidio(video, audioOnly, playlistPath)
    
    return 'Done'

def main():
    print('What would you like to download?')
    print('1. Video')
    print('2. Audio')
    choice = ''
    validChoices = ['1', '2', 'quit']
    while choice == '':
        choice = input('Enter number of choice: ')
        if choice not in validChoices:
            print('Invalid choice')
            choice = ''
    if choice == '1':
        link = input('Insert youtube link: ')
        downloadVidio(link)
    elif choice == '2':
        link = input('Insert youtube link: ')
        downloadAudio(link)

print('test')
if __name__ == '__main__':
    main()