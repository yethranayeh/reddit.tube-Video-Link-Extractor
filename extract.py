import requests
import time
from bs4 import BeautifulSoup

subreddit = input("Subreddit name: ")
page = 1

video_exists = True 
while video_exists: 
    
    url = f"https://www.reddit.tube/category/{subreddit}/{page}"
    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")

    # Example video url: https://cdntube2.b-cdn.net/mp4/abcdefghijklmn.mp4
    video = soup.find("section", {"class":"container g-pb-40"}).find_all("a", {"class":"nav-link"})

    print("Checking:", url)

    if video: # Checks if there is content in the "video" variable. If not, it will return False and the loop will stop.
        with open(f"{subreddit}.txt", "a", encoding="utf-8") as file:
            for link in video:
                print("Found:", f"https://cdntube2.b-cdn.net/mp4/{link['href'][7:]}.mp4")
                file.write(f"https://cdntube2.b-cdn.net/mp4/{link['href'][7:]}.mp4\n")

        time.sleep(2) # Sleeps for 2 seconds to send too many requests quickly. Can be changed to make it faster or slower. Or you can completely remove it.
        page += 1 # After the links are found, changes the page number to go to next page in the next loop.
    else:
        print("No video found. Stopping search.")
        time.sleep(2) #Sleeps for 1 second after displaying message, then stops the loop.
        video_exists = False
