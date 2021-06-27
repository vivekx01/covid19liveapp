from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "27f13ef507mshe52f095046eb5c2p1066cdjsnce4235194fb0",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# Create your views here.
def responseview(request):
    mylist=[]
    noofresults= int(response['results'])
    for x in range(0,noofresults):
        mylist.append(response['response'][x]['country'])
    if request.method=="POST":
        selectedcountry=request.POST['selectedcountry']
        noofresults= int(response['results'])
        for x in range(0,noofresults):
            if selectedcountry==response['response'][x]['country']:
                new=response['response'][x]['cases']['new']
                active=response['response'][x]['cases']['active']
                critical=response['response'][x]['cases']['critical']
                recovered=response['response'][x]['cases']['recovered']
                total=response['response'][x]['cases']['total']
                deaths= int(total)-int(active)-int(recovered)
        context={'selectedcountry':selectedcountry,'mylist':mylist,'new':new,'active':active,'critical':critical,'recovered':recovered,'deaths':deaths,'total':total}
        return render (request,"CovidResponse.html",context)
    
   
    context={'mylist':mylist}
    return render (request,"covidresponse.html",context)
