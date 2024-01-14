from pytube import YouTube, Playlist

def cleanTitle(title):
    title = title.replace(' ', '_')
    title = title.replace('/', '_')
    title = title.replace('\\', '_')
    title = title.replace(':', '_')
    title = title.replace('*', '_')
    title = title.replace('?', '_')
    title = title.replace('"', '_')
    title = title.replace('<', '_')
    title = title.replace('>', '_')
    title = title.replace('|', '_')
    return title

def download(ytObject, path='./vids/'):
    try:
        ytObject.download(output_path=path)
    except:
        print('An error has occured during download')
        return 'An error has occured during download'
    return 'success'

def downloadVidio(link, audioOnly=False, path='./vids/'):
    ytObject = YouTube(link)
    fileTitle = cleanTitle(ytObject.title)
    if audioOnly:
        ytObject = ytObject.streams.get_audio_only()
    else:
        ytStreams = ytObject.streams.filter(adaptive=True)
        videoStreams = ytStreams.filter(type='video')
        audioStreams = ytStreams.filter(type='audio')
        print('Video Streams:')
        for index, stream in enumerate(videoStreams):
            print(f"{index}. Resolution: {stream.resolution}, FPS: {stream.fps}, Type: {stream.mime_type.split('/')[1]}")
        videoChoice = input('Enter number of choice: ')
        videoStream = ytObject.streams.get_by_itag(videoStreams[int(videoChoice)].itag)
        print('Audio Streams:')
        for index, stream in enumerate(audioStreams):
            print(f"{index}. Bitrate: {stream.abr}, Type: {stream.mime_type.split('/')[1]}") 
        audioChoice = input('Enter number of choice: ')
        audioStream = ytObject.streams.get_by_itag(audioStreams[int(audioChoice)].itag)
        print('Downloading video...')
        videoStream.download(output_path=f"{path}{fileTitle}/", filename_prefix='video_')
        print('Downloading audio...')
        audioStream.download(output_path=f"{path}{fileTitle}/", filename_prefix='audio_')
        print('Done!')

    # result = download(ytObject, path)
    # return result
    

def downloadAudio(link, path='./audio/'):
    ytObject = YouTube(link)
    fileTitle = cleanTitle(ytObject.title)
    ytObject = ytObject.streams.get_audio_only()
    result = download(ytObject, path=f"{path}{fileTitle}/")
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
    path = input('Enter path to download to: ')
    if path == '':
        path = './vids/'
    path = path.replace('\\', '/')
    if path[-1] != '/':
        path += '/'
    
    if choice == '1':
        link = input('Insert youtube link: ')
        downloadVidio(link, path=path)
    elif choice == '2':
        link = input('Insert youtube link: ')
        downloadAudio(link, path=path)

print('test')
if __name__ == '__main__':
    main()