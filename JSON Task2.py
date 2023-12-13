import requests
def get_breweries_by_state(state):
    url = f"https://api.openbrewerydb.org/breweries?by_state={state}"
    response = requests.get(url)
    if response.status_code == 200:
        breweries = response.json()
        return breweries
    else:
        print(f"Failed to fetch breweries in {state}. Status code: {response.status_code}")
        return []
def count_brewery_types(breweries):
    types_count = {}
    for brewery in breweries:
        brewery_type = brewery['brewery_type']
        if brewery_type in types_count:
            types_count[brewery_type] += 1
        else:
            types_count[brewery_type] = 1
    return types_count

def count_breweries_with_websites(breweries):
    with_website = sum(1 for brewery in breweries if brewery['website_url'])
    return with_website

states_of_interest = ['Alaska', 'Maine', 'New York']
brewery_counts = {}
brewery_types_counts = {}
breweries_with_websites = {}
for state in states_of_interest:
    breweries = get_breweries_by_state(state)
    brewery_counts[state] = len(breweries)
    brewery_types_counts[state] = count_brewery_types(breweries)
    breweries_with_websites[state] = count_breweries_with_websites(breweries)

    print(f"\nNumber of breweries in {state}: {brewery_counts[state]}")
    print(f"Types of breweries in {state}: {brewery_types_counts[state]}")
    print(f"Breweries with websites in {state}: {breweries_with_websites[state]}")
for state in states_of_interest:
    print(f"\nBreweries in {state}:")
    breweries = get_breweries_by_state(state)
    for brewery in breweries:
        print(brewery['name'])
