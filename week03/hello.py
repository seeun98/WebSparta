import requests

my_url = 'http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99'
response = requests.get(my_url)
my_data = response.json()
my_list = my_data['RealtimeCityAir']['row']

for data in my_list:
    print(data['MSRSTE_NM'],data['PM10'])