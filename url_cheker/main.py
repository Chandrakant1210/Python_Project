import requests
from datetime import datetime
from config import API_KEY


url = input("enter website link : ")

#  endpoint 

endpoint=f"https://safebrowsing.googleapis.com/v4/threatMatches:find?key={API_KEY}"

# json body request

data = {
    "client": {
        "clientId": "python-threat-analyzer",
        "clientVersion": "1.0"
    },
    "threatInfo": {
        "threatTypes": [
            "MALWARE",
            "SOCIAL_ENGINEERING",
            "UNWANTED_SOFTWARE"
        ],
        "platformTypes": [
            "ANY_PLATFORM"
        ],
        "threatEntryTypes": [
            "URL"
        ],
        "threatEntries": [
            {
                "url": url
            }
        ]
    }
}

# post

try:
    response=requests.post(endpoint, json=data)
    print(f"\n statuscode : ",response.status_code)
    if(response.status_code==200):
        result=response.json()
        if "matches" in result:
            print("\n====================================")
            print("⚠️  UNSAFE WEBSITE")
            print("Threats Found:")
            print("====================================")
            for threat in result["matches"]:
                 print("Threat Type :", threat["threatType"])
                 print("Platform    :", threat["platformType"])
                 print("------------------------------------")
            status = "UNSAFE"

        else:
            print("\n====================================")
            print("✅  SAFE WEBSITE")
            print("Threats NOT Found:")
            print("====================================")
            status = "SAFE"
        with open("report.txt",'a')as file:
            file.write(f"{datetime.now()}\n")
            file.write(f"urlL: {url}\n")
            file.write(f"status {status}\n")
            file.write("_"*50+"\n")
            print("report.txt saved")
    else:
        print("API Error ")
        print(response.text)


            
except Exception as e:
    print("connection failed \n",e)