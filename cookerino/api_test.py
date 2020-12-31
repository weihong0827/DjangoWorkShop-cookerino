import requests
import json

data = {
    'usage':'product_img',
    'ingredients':'bread,bread,bread,bread',

}
info =json.dumps(data)

response = requests.post('http://127.0.0.1:8000/api/img',data = info)
print(response.content)