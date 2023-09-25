import bs4
import requests
import pandas as pd 
import json 

def data_scrap(cities_url):
    """Scrapes the cities data from the given URL and saves it to a CSV file.

    Args:
        cities_url: The URL of the cities data.

    Returns:
        A string indicating whether the operation was successful or not.
    """
    # Try to scrape the data from the given URL.
    try:
         # Get the body of the HTML document.
        body = requests.get(cities_url).text

         # Create a BeautifulSoup object to parse the HTML document.
        ob = bs4.BeautifulSoup(body,'html.parser')
        # Select the table rows that contain the cities data.
        cities = ob.select("td b")

        # Create a list to store the cities data.
        cities_list = []

        # Keep track of the current state.
        state = ""
        # Iterate over the table rows and extract the cities data.
        for city in cities:
            # If the table row is a state heading, update the current state.
            if city.find(class_="success") != None:
                state = city.text
            # Otherwise, add the city data to the list.
            else:
                cities_list.append({
                    'City': city.text,
                    'State': state
                })

        # Create a Pandas DataFrame from the list of cities data.
        cities_df = pd.DataFrame.from_dict(cities_list)

        # Save the DataFrame to a CSV file.
        cities_df.to_csv("Cities_list.txt", index=False)

    # If an error occurs, return an error message.
    except Exception as e:
        return "Something Has Happened. Check the scraping.py file " + str(e)
    # Otherwise, return a success message.
    else:
        return "Operation is Succesful"



if __name__ == "__main__" :
    #Opening and loading the url to config from config.json
    with open("config.json") as f :
        config = json.load(f)
    cities_url = config['web_url']
    # Calling the method
    response = data_scrap(cities_url=cities_url)
    print(response)




