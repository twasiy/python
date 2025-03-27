import requests

def fetch_youtube_playlist_freeapi():
    url = "https://api.freeapi.app/api/v1/public/youtube/playlists?page=1&limit=5"
    response = requests.get(url)
    main_data = response.json()

    if main_data['success'] and main_data['data']:
        playlist = main_data['data']['data']

        if not playlist:
            raise Exception("No playlists found")

        # Assuming we want the first playlist
        items = playlist[0]
        name = items['kind']
        user_id = items['id']
        playlist_thumbnail = items['snippet']['thumbnails']['default']['url']
        channel_name = items['snippet']['channelTitle']

        return name, user_id, playlist_thumbnail, channel_name
    
    else:
        raise Exception("Failed to fetch playlist data")
    
def main():
    try:
        name, user_id, playlist_thumbnail, channel_name = fetch_youtube_playlist_freeapi()
        print(f"Playlist Name: {name} \nUser_ID: {user_id} \nPlaylist Thumbnail: {playlist_thumbnail} \nChannel Name: {channel_name}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
