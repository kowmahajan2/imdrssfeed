import feedparser
import requests
import time

while(1):
    NewsFeed = feedparser.parse("https://mosdac.gov.in/3drimager.xml")
    entry = NewsFeed.entries[0]



    for i in range(0, len(NewsFeed.entries)):
        if (NewsFeed.entries[i].title == "3RIMG_L1C_ASIA_MER"):
            downloadlink = NewsFeed.entries[i].link
            imgname = NewsFeed.entries[i].datacasting_productname
            print(imgname)
            break

    if downloadlink != "":
        image_url = downloadlink
        r = requests.get(image_url)
        if r.status_code == 200:
            file = open("latest/latestimd.jpg", "wb")
            file.write(r.content)
            file.close()
            saveloc = "all/" + imgname + ".jpg"
            file = open(saveloc, "wb")
            file.write(r.content)
            file.close()
    time.sleep(1800)