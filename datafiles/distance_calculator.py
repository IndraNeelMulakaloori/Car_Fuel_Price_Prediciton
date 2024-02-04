import requests
import pandas as pd 
import json 
import random 



def distance_calculator(api_key,base_url,src,dest):
    try:
        request_url = base_url + f"wp.1={src[0],src[1]},India&wp.2={dest[0],dest[1]},India&output=json&key={api_key}"
        response = requests.get(request_url)

        if response.status_code != 200:
            print(f"Error : fetching data{requests.get(request_url).status_code}")
        # else :
        #     print("Good to go")

        response_data = json.loads(response.content)
        details = response_data['resourceSets'][0]['resources'][0]['routeLegs'][0]
        # print(details['startLocation']['address']['formattedAddress'].split(",")[0],details['endLocation']['address']['formattedAddress'].split(",")[0])
        # print(details['travelDistance'])
        return details['travelDistance']
        
    except Exception as e:
        print("Something went wrong. Check distance_calculator.py" + str(e))
    # else : 
    #     print("Good to go")
    

def populate_data(cities_list,api_key,base_url,fuel_cost = 106.31):
    dup_list = []
    data_list = []
    for _ in range(300):
        cities = random.sample(cities_list,2)
        if cities not in dup_list:
            distance = distance_calculator(api_key,base_url,cities[0],cities[1])
            data_list.append({
                'Source' : cities[0][0],
                'Destination' : cities[1][0],
                'Distance' : distance,
                'Cost' : distance * fuel_cost if distance != None else None
            })
            dup_list.append(cities)
        else : 
            continue
        # src = cities[0]
        # dest = cities[1]
        # print(type(src[0]),src[1],dest[0],dest[1])
        cities_df = pd.DataFrame.from_dict(data_list)
        cities_df.to_csv("Data.csv",index=False)

if __name__ == "__main__" :
    #Opening and loading the url to config from config.json
    with open("config.json") as f :
        config = json.load(f)
        
    api_key,base_url = config['api']['access_key'],config['api']['endpoint']
    cities_list = []

    with open("Cities_list.txt", "r") as f:
        f.readline()
        for line in f:
           line = line.replace("\n", "").replace("\t", "").replace("\"", "").split(",")           
           cities_list.append(line)
    populate_data(cities_list,api_key,base_url)
    
    
