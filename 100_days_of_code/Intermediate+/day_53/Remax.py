import requests
import json
import os

USER_AGENT = os.getenv('USER_AGENT')
HEADERS = {"User-Agent": USER_AGENT, 'content-type': 'application/json'}

class FindRemaxListings:

    def __init__(self, region, price, method):
        self.region = region
        self.price = price
        self.method = '1' if (method == "comprar") else '2'

    def find_listings(self):
        all_listings = []
        page = 0
        results = [""]

        while len(results)>0:
            response = requests.post(f"https://www.remax.pt/Api/Listing/MultiMatchSearch?page={page}&searchValue=&size=20", headers=HEADERS, data=json.dumps(self.get_body()))
            response.raise_for_status()
            content = response.json()
            results = content['results']

            if content['isValid']:
                for item in content['results']:
                    if not item['isSold'] and "consulta" not in item['listingPriceText']:
                        price = self.get_price(item['listingPriceText'])
                        region = f"{item['regionName2']}, {item['regionName1']}"
                        desc = item['listingMetatagTitle'].split(' ')
                        typology = desc[1].strip()
                        description = item['listingMetatagDescription']
                        house_typology = desc[0].strip()
                        realtor = "REMAX"
                        link = self.get_link(page)
                    all_listings.append({"house":house_typology,"region":region,"price":price,"type":typology,"description":description,"realtor":realtor,"link":link})
                page +=1
        return [dict(t) for t in {tuple(d.items()) for d in all_listings}] #removes duplicate dictionaries in the list

    def get_link(self, page):
        if self.region == "Viana do Castelo":
            self.region = "Viana%20do%20Castelo"
        return f'https://www.remax.pt/{"comprar" if self.method==1 else "arrendar"}?searchQueryState={{"regionName":"{self.region}","businessType":{self.method},"page":{page+1},"sort":{{"fieldToSort":"ListingPrice","order":0}},"mapIsOpen":false,"listingClass":1,"listingTypes":["11","1"],"rooms":2,"hasMultimedia":false,"price":{{"min":10,"max":{self.price}}},"prn":"{self.region}","regionID":"{self.get_region_id(self.region)}","regionType":"Region1ID"}}'

    def get_price(self, price):
        if self.method == '1':
            return price.split('\xa0')[0]+"000"
        else:
            return price.split(' ')[0]
    
    def get_body(self):
        return {"filters":[
                    {"field":"BusinessTypeID","value":self.method,"type":0},
                    {"field":"NumberOfBedrooms","biggerThan":2,"type":4},
                    {"field":"ListingTypeID","shouldValues":["11","1"],"type":2},
                    {"field":"ListingPrice","biggerThan":10,"smallerThan":self.price,"type":4},
                    {"field":"Region1ID","value":self.get_region_id(self.region),"type":0},
            ],"sort":{"fieldToSort":"ListingPrice","order":0}
        }

    def get_region_id(self, region):
        values = {"Aveiro":"56","Braga":"58","Porto":"78","Viana do Castelo":"81"}
        return values.get(region)
