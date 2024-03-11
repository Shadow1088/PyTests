from tiktokapi import TikTokApi

def download_tiktok_video(url, output_path):
    api = TikTokApi()

    # Get the TikTok video information
    video_info = api.get_video_by_url(url)

    # Get the video URL
    video_url = video_info['item_info']['item_struct']['video']['download_addr']

    # Download the video
    response = api.session.get(video_url, stream=True)
    with open(output_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)

if __name__ == "__main__":
    tiktok_url = "https://www.tiktok.com/@beatamyslikova/video/7305025112040836384?_r=1&_t=8hgTV3m3uAD"  # Replace with the actual TikTok video URL
    output_path = "downloaded_video.mp4"  # Replace with the desired output path

    download_tiktok_video(tiktok_url, output_path)
