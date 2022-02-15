import requests
import os

headers = {
  "content-type": "application/json",
  "accept": "application/json",
  "Authorization": os.environ["DEMISTO_API_KEY"]
}

data = {
  "filter": {
    "query": "-status:closed -category:job",
    "period": {"by":"day","fromValue":7}
  }
}

res = requests.post(f"{os.environ['DEMISTO_BASE_URL']}/incidents/search", headers=headers, json=data, verify=False)
print(res.text)
