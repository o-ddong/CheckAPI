import requests

<<<<<<< HEAD
URL = 'http://211.169.35.155:5580/api/whitelist/'
=======
URL = 'http://[IP주소:Port]/api/whitelist/'
>>>>>>> f53b5c69519c74b9d2bb1a9ea8e87e2650db77ba
params = {'cert_sha1_hash': 'B8D9AEDF4AFF2E8392649028D5F56AD8DFA1EF39'}
response = requests.get(URL, params)
print(response.status_code)
print(response.text)
