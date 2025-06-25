import requests
import time
import os
import colorama
from colorama import Fore
r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
c = Fore.CYAN
re = Fore.RESET
def main():
    os.system('cls')
    BADGES = {
        1 << 0: "<:Badge_Discord_Staff:1365704725646807060>",
        1 << 1: "<:DiscordPartner:1365700977570742312>",
        1 << 2: "<:HypeSquadEvents:1365704359454834770>",
        1 << 3: "<:BugHunter1:1365701008184967278>",
        1 << 9: "<:86964earlysupporter:1345831325738995848>",
        1 << 14: "<:BugHunter2:1365701027830960259>",
        1 << 16: "<:developper:1365704272368500837>",
        1 << 17: "<:dev:1365704127103107112>",
        1 << 18: "<:ModeratorProgramsAlumni:1365701046256533525>",
    }

    print(f"""
{b} $$$$$$\                                      
$$  __$$\                                     
$$ /  $$ | $$$$$$\   $$$$$$\  $$$$$$$\        
$$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\       
$$ |  $$ |$$ /  $$ |$$$$$$$$ |$$ |  $$ |      
$$ |  $$ |$$ |  $$ |$$   ____|$$ |  $$ |      
 $$$$$$  |$$$$$$$  |\$$$$$$$\ $$ |  $$ |      
 \______/ $$  ____/  \_______|\__|  \__|      
          $$ |                                
          $$ |                                
          \__|             {c}By DATAOPEN        
                                     {r} ______                                                                       
                                     /      \                                                                      
                                    |  $$$$$$\  _______   ______   ______    ______    ______    ______    ______  
                                    | $$___\$$ /       \ /      \ |      \  /      \  /      \  /      \  /      \ 
                                     \$$    \ |  $$$$$$$|  $$$$$$\ \$$$$$$\|  $$$$$$\|  $$$$$$\|  $$$$$$\|  $$$$$$\\
                                     _\$$$$$$\| $$      | $$   \$$/      $$| $$  | $$| $$  | $$| $$    $$| $$   \$$
                                    |  \__| $$| $$_____ | $$     |  $$$$$$$| $$__/ $$| $$__/ $$| $$$$$$$$| $$      
                                     \$$    $$ \$$     \| $$      \$$    $$| $$    $$| $$    $$ \$$     \| $$      
                                      \$$$$$$   \$$$$$$$ \$$       \$$$$$$$| $$$$$$$ | $$$$$$$   \$$$$$$$ \$$      
                                                                           | $$      | $$                          
                                                                           | $$      | $$                          
                                                                            \$$       \$$                                     
""")

    channelid = input(f"{c}Channel ID: ")
    burl = f"https://discord.com/api/v9/channels/{channelid}/messages"
    token = input(f"{c}Token: ")
    webhook = input(f"{c}Webhook: ")

    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }

    seen = set()
    lmid = None
    ttc = 0

    while True:
        params = {"limit": 100}
        if lmid:
            params["before"] = lmid

        resp = requests.get(burl, headers=headers, params=params)
        if resp.status_code != 200:
            print("Error:", resp.status_code)
            print(resp.text)
            break

        messages = resp.json()
        if not messages:
            break  
        for msg in messages:
            author = msg["author"]
            user_id = author["id"]

            if user_id in seen:
                continue

            seen.add(user_id)
            username = author["username"]
            flags = author.get("public_flags", 0)
            badges = "".join([icon for bit, icon in BADGES.items() if flags & bit])

            if not badges:
                continue

            content = f"{username} ({user_id}) : {badges}"
            res = requests.post(webhook, data={"content": content,'username':"open scrapper",'avatar_url':"https://avatars.githubusercontent.com/u/198399128?v=4"})
            if res.status_code == 204:
                print(f"{g}{res.status_code}{re} - {content}")
                time.sleep(2) # dont change this value
            else:
                print(f"{r}{res.status_code}{re} - {content}")
                time.sleep(2) # dont change this value 

        lmid = messages[-1]["id"]
        ttc += len(messages)
main()