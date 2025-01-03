import json
import requests
import pprint
from datetime import datetime

cloudflare_api = "https://api.cloudflare.com/client/v4/"

api_token = "Bearer XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
headers = {'Authorization': api_token, 'Content-Type':'application/json'}

today = datetime.now()
datetimenow = today.strftime('%Y-%m-%d-%H%M%S')
export_filename = "./cloudflare_get_all_zones_records-export-"+datetimenow+".json"

cloudflare_dns = cloudflare_api + "zones?page=1&per_page=500"
cloudflare_dns_response = requests.get(cloudflare_dns, headers=headers, )

if cloudflare_dns_response.status_code == 200:
    dns_data = json.loads(cloudflare_dns_response.text)

    with open(export_filename, 'w') as json_file:
        json.dump(dns_data, json_file, indent=1)
#    pprint.pprint(dns_data["result"])

    for zones in dns_data["result"]:
        pprint.pprint(zones["id"]+" "+zones["name"])
else:
    print(cloudflare_dns_response.status_code)

