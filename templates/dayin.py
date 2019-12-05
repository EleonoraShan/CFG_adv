import requests
import json
from flask import Flask, render_template, request

#app = Flask("MyApp")

amount = input("Enter amount in EUR:")
amount = int(amount)

#?q=USD_PHP&compact=ultra&apiKey=e6fc629a6bc70e9b7a1b
#
params = {
#    "q":"USD_PHP"
#    "compact":"ultr"

    "access_key": "0b58b2ffb9d75b6c3ca74063f36cbc57",
    "symbols": "GBP"

}


#response = resquests.get("https://free.currconv.com/api/v7/convert",params)

response = requests.get("http://data.fixer.io/api/latest",params)
response_dict = json.loads(response.text)
response_dict2 = response_dict["rates"]


out = amount * response_dict2["GBP"]
#for i in response_dict2:
#    print("key: ", i, "val: ", response_dict2[i])


print("response_dict2:",response_dict2)


#print("Response")
#print(response.content=="base")
