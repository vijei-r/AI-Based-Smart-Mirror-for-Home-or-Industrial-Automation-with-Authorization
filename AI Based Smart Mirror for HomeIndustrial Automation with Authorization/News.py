import requests
URL="url with apiKey"
response = requests.get(URL).json()


def main():
    count = 0
    data = []
    for i in range(15):
        count += 1
        datas=response["articles"][i]["title"]
        data.append("NEWS : "+ str(count)  + datas) #### + str(count) +
        #print("NEWS_"+ str(count)+": "+datas)
    #print(data[0])
    return data

