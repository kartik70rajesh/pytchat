import pytchat
import json
from datetime import datetime,timedelta


VIDEO_ID = "kV1b4rusqBc"
MESSAGE_STRING = "😂😂😂"
BASE_URL = "https://www.youtube.com/watch?v="
BUFFER_SECS = 5
def create_url(split_time):
    
    while len(split_time) < 3 :
        split_time.insert(0,0)
    h,m,s = map(int,split_time)
    dt = datetime(2021,1,1,h,m,s)
    if h>0 or m>0 or s>=20 :
        dt= dt-timedelta(seconds=20)
        
    return BASE_URL+VIDEO_ID+"&t="+str(dt.hour)+"h"+str(dt.minute)+"m"+str(dt.second)+"s"

chat = pytchat.create(video_id=VIDEO_ID)
chat_json=""
chats=[]
file = open("chat.txt", "w", encoding="utf-8")
print("--------------DOWNLOADING CHATS-------------")
#TO do - add ghumnewala progress bar
while chat.is_alive():
    chat_json=chat.get().json()
    chats = json.loads(chat_json)
    for msg in chats:
        if MESSAGE_STRING in msg["message"]:
            timed_url = create_url(msg["elapsedTime"].split(":"))
            file.write(msg["elapsedTime"]+" "+msg["message"]+" "+timed_url+"\n")
print("--------------CHATS DOWNLOADED-------------")
file.close()
