# http://docs.python-requests.org/en/master/
import requests
response = requests.post('http://localhost:5000/api/add_data', json={'some_value_1':123, 'some_value_2':234})
print('Poster data')
print(response.status_code, response.text)
print()

print('Henter data')
response = requests.get('http://localhost:5000/api/dht11')
data = response.json() # Konverterer json data til en dict
print(response.status_code)
for k in data:
    print(k,data[k])

