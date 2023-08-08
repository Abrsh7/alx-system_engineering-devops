import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Set a custom User-Agent to avoid "Too Many Requests" error
    headers = {"User-Agent": "Custom User Agent"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data["data"]["children"]
            
            if len(posts) == 0:
                print("No posts found.")
            else:
                for post in posts:
                    title = post["data"]["title"]
                    print(title)
        else:
            print("Invalid subreddit.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
