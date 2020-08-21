#!/usr/local/bin/python3.8
import urllib.request as urlreq
import json

api_base = "https://cloud.iexapis.com/stable"
api_key = "pk_611ba623ce1d4f25b44e64fc488a3f97"
symbol = "aapl"

def numtest(input):
    if isinstance(input, float) == True:
        input = input
    elif isinstance(input, int) == True:
        input = input
    else:
        input = 0
    return input

def tech_ind_range(base,sym,ind,key):
    api = f"{base}/stock/{sym}/indicator/{ind}?range=ytd&token={key}"
    response_data = json.loads(urlreq.urlopen(api).read().decode())
    response = {}
    response[0] = response_data['indicator'][0][-1]
    response[1] = response_data['indicator'][1][-1]
    response[2] = response_data['indicator'][2][-1]
    return response

print(numtest(tech_ind_range(api_base,symbol,"bbands",api_key)[2]))
