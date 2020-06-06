from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from App import worldData,indiaData
from django.http import JsonResponse
import requests,json


def index(request):
	return HttpResponseRedirect('/map/india')

def map(request,m):
	covidCases = worldData.data()
	newCases = covidCases[215]['new_cases']
	newDeaths = covidCases[215]['new_deaths']
	worldList = ['country_name','cases','deaths','total_recovered']
	worldCases = []
	for j in covidCases[0:215]:
		k = [j[i] for i in worldList if i in j]
		worldCases.append(k)
		# print(len(cases))
	
	if m == 'india':
		indiaList = ['state','confirmed','active','recovered','deaths']
		cases1 = []
		indCases =indiaData.data()
		for p in indCases:
			r = [p[q] for q in indiaList if q in p]
			cases1.append(r)

		totalCases = cases1[0]
		totalConfirmed = totalCases[1]
		totalActive = totalCases[2]
		totalRecovered = totalCases[3]
		totalDead = totalCases[4]
		stateCases = cases1[1:]
	    # print(indiaCases)
		params = {"cases":worldCases,"total":covidCases[215]['total_cases'],"dead":covidCases[215]['total_deaths'],
	    "recover":covidCases[215]['total_recovered'],"stateCases":stateCases,"totalCases":totalCases,
	    "totalConfirmed":totalConfirmed,"totalActive":totalActive,"totalRecovered":totalRecovered,
	    "totalDead":totalDead,"newCases":newCases,"newDeaths":newDeaths}
		return render(request,'india.html',params)
	
	elif m == 'world':
		indCases =indiaData.data()
		
		params = {"cases":worldCases,"total":covidCases[215]['total_cases'],"dead":covidCases[215]['total_deaths'],
	    "recover":covidCases[215]['total_recovered'],"newCases":newCases,"newDeaths":newDeaths}

		return render(request,'worldmap.html',params)
	else:
		return HttpResponseRedirect('/')
	# return render(request,"map.html")

def worlddata(request):
	covidCases = worldData.data()
	response = JsonResponse(covidCases)
	return HttpResponse(response)

# def graphOne(request):
# 	DataWorld = worldData.data()
# 	data = DataWorld[0:215]
# 	worldList = ['country_name','cases','deaths','total_recovered','total_tests']
# 	countries = []; cases = []; deaths = []; total_recovered = []; total_tests = []
# 	for i in data:
# 		countries.append(i['country_name'])
# 		cases.append(i['cases'].replace(",",""))
# 		deaths.append(i['deaths'])
# 		total_recovered.append(i['total_recovered'])
# 		total_tests.append(i['total_tests'])
# 	params = {"countries":countries,"cases":cases}
# 	result = json.dumps(params)
# 	td = [int(b) for b in cases]
# 	result = {"countries": countries[:10],"cases":td[:10]}
# 	return HttpResponse(json.dumps(result))

def allgraphs(request):
	url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"
	headers = {
	    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
	    'x-rapidapi-key': "Your API Key"
	    }

	response = requests.request("GET", url, headers=headers)
	x = response.json()
	y = x['state_wise']
	state = []; confirmed = []; active = []; recovered = []; dead = []; stateCode = []
	for i in y.values():
		code = i['statecode']
		stateName = i['state']
		confirmedCases = i['confirmed']
		activeCases = i['active']
		recoveredCases = i['recovered']
		deathCases = i['deaths']
		stateCode.append(code)
		state.append(stateName)
		confirmed.append(confirmedCases)
		active.append(activeCases)
		recovered.append(recoveredCases)
		dead.append(deathCases)
	td1 = [int(b) for b in confirmed]
	td2 = [int(b) for b in active]
	td3 = [int(b) for b in recovered]
	td4 = [int(b) for b in dead]
	params = {"stateCode":stateCode,"states":state,"confirmedCases":td1,"activeCases":td2,"recoveredCases":td3,"deathCases":td4}
	result = json.dumps(params)
	return HttpResponse(result)

def Sort(allData): 
    allData.sort(key = lambda i: i["country_name"]) 
    return allData 

def globe_data(request):
	covidCases = worldData.data()
	#response = JsonResponse(covidCases)
	worlddata = covidCases[215]
	worldCases = covidCases[215]['total_cases']
	worldActive = covidCases[215]['active_cases'][1:]
	worldRecovered = covidCases[215]['total_recovered']
	worldDeaths = covidCases[215]['total_deaths']
	cases = covidCases[0:215]

	countrywiseSort = Sort(cases)
	confirmed = []; active = []; recovered = []; dead = []; country = []
	for k in countrywiseSort:
		countryName = k['country_name']
		confirmedCases = k['cases'].replace(",","")
		activeCases = k['serious_critical'].replace(",","")
		recoveredCases = k['total_recovered'].replace(",","")
		deathCases = k['deaths'].replace(",","")
		if recoveredCases == "" or recoveredCases == "N/A":
			recoveredCases = "0"
		else:
			pass

		if activeCases == "" or activeCases == "N/A":
			activeCases = "0"
		else:
			pass

		if deathCases == " ":
			deathCases = "0"
		else:
			pass
		country.append(countryName)
		confirmed.append(confirmedCases)
		active.append(activeCases)
		recovered.append(recoveredCases)
		dead.append(deathCases)
	con = [int(p) for p in confirmed]
	act = [int(q) for q in active]
	rec = [int(r) for r in recovered]
	dea = [int(s) for s in dead]
	countries_iso = ["AF","AL","DZ","AD","AO","AI","AG","AR","AM","AW","AU","AT","AZ","BS","BH","BD","BB","BY","BE","BZ","BJ","BM","BT","BO","BA","BW","BR","VG","BN","BG","BF","BI","CF","CV","KH","CM","CA","BQ","KY","TD","GB","CL","CN","CO","CG","CR","HR","CU","CW","CY","CZ","CD","DK","DJ","DM","DO","EC","EG","SV","GQ","ER","EE","SZ","ET","FO","FK","FJ","FI","FR","GF","PF","TF","GA","GM","GE","DE","GH","GI","GR","GL","GD","GP","GT","GN","GW","GY","HT","HN","HK","HU","IS","IN","ID","IR","IQ","IE","IM","IL","IT","CI","JM","JP","JO","KZ","KE","KW","KG","LA","LV","LB","LR","LY","LI","LT","LU","","MO","MG","MW","MY","MV","ML","MT","MQ","MR","MU","YT","MX","MD","MC","MN","ME","MS","MA","MZ","MM","NA","NP","NL","NC","NZ","NI","NE","NG","MK","NO","OM","PK","PS","PA","PG","PY","PE","PH","PL","PT","QA","RO","RU","RW","RE","KR","KN","LC","MF","PM","SM","ST","SA","SN","RS","SC","SL","SG","SX","SK","SI","SO","ZA","SS","ES","LK","BL","VC","SD","SR","SE","CH","SY","TW","TZ","TH","TL","TG","TT","TN","TR","TC","AE","GB","US","UG","UA","UY","UZ","VA","VE","VN","EH","YE","ZM","ZW"]
	confirmedList = []; activeList = []; recoveredList = []; deadList = []
	for i in range(0,len(countries_iso)):
		confirmedList.append({""+countries_iso[i]+"" : con[i]})
	for i in range(0,len(countries_iso)):
		activeList.append({""+countries_iso[i]+"" : act[i]})
	for i in range(0,len(countries_iso)):
		recoveredList.append({""+countries_iso[i]+"" : rec[i]})
	for i in range(0,len(countries_iso)):
		deadList.append({""+countries_iso[i]+"" : dea[i]})
	mergedConfirmed={}; mergeActive = {}; mergeRecovered = {}; mergeDead = {}
	for x1 in confirmedList:
		mergedConfirmed.update(x1)
	for x2 in activeList:
		mergeActive.update(x2)
	for x3 in recoveredList:
		mergeRecovered.update(x3)
	for x4 in deadList:
		mergeDead.update(x4)
	params = {"confirmed":mergedConfirmed,"active":mergeActive,"recovered":mergeRecovered,"deaths":mergeDead,"countries":country,"cases":con,"worldCases":worldCases,"worldActive":worldActive,"worldRecovered":worldRecovered,"worldDeaths":worldDeaths}
	result = json.dumps(params)
	return HttpResponse(result)

def Indiadistrict(request,m):
	state = m
	url = 'https://api.covid19india.org/state_district_wise.json'
	response = requests.request("GET",url)
	data = response.text
	d2={}
	d2=json.loads(data)
	countryData = {}
	for i in d2:
		if(i==state):
			for j in (d2[i]["districtData"]):
				key = "cases"
				countryData.setdefault(key,[])
				countryData[key].append({"district":j,"confirmed":int(d2[i]["districtData"][j]["confirmed"]),
					"active":int(d2[i]["districtData"][j]["active"]),
					"deaths":int(d2[i]["districtData"][j]["deceased"]),
					"recovered":int(d2[i]["districtData"][j]["recovered"])})
	newData = countryData["cases"]
	worldList = ['district','confirmed','active','deaths','recovered']
	cases = []
	for j in newData:
		k = [j[i] for i in worldList if i in j]
		cases.append(k)
	params = {"districtData":cases,"district":m}
	return render(request,'Indiadistrict.html',params)