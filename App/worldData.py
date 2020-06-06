def data():
	import requests
	url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
	headers = {
	    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
	    'x-rapidapi-key': "Your API Key"
	    }
	response = requests.request("GET", url, headers=headers)
	x = response.json()
	countryData = x['countries_stat']
	allData = x['world_total']
	countryData.append(allData) 
	return countryData
	# print(countryData)

	# file = open('countriesSorted.json','w')
	# json.dump(countries, file)

data()