from pytube import YouTube

def downloader(url, output_directory):
    
    yt = YouTube(url)
    highest_quality_stream = yt.streams.filter(
        progressive=True
    ).order_by(
        'resolution'
    ).desc().first().download(output_directory)

    return highest_quality_stream