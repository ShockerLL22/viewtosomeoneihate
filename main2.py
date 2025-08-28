import time
import requests
API_URL = "https://zefame-free.com/api_free.php?action=order"
VIDEO_ID = "7543647106356022535"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/116.0.0.0 Safari/537.36"
}
PROXY = "http://magcrfyp:zpny18760zw4@23.95.150.145:6114"
PROXIES = {
    "http": PROXY,
    "https": PROXY
}
def send_request(video_id):
    payload = {
        "action": "order",
        "service": "229",
        "link": f"https://www.tiktok.com/@eliya_y_amar/video/{video_id}",
        "uuid": "38dc8fb0-0d2b-4b4b-a506-17871835682b",
        "videoId": video_id
    }
    try:
        response = requests.post(API_URL, data=payload, headers=HEADERS, proxies=PROXIES, timeout=10)
        success = "Commande pass" in response.text
        print(f"Request for {video_id} sent. Success: {success}")
        return 300 if success else 0
    except Exception as e:
        print(f"Error sending request: {e}")
        return 0
def main():
    total_views = 0
    while True:
        added_views = send_request(VIDEO_ID)
        total_views += added_views
        print(f"Total views added: {total_views}")
        time.sleep(1)  
if __name__ == "__main__":
    main()
