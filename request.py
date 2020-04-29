import requests

response = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=1a03d7e86615a1fc7d41d263bcd919e0c47ce1aa')
print(response.status_code)
print(response.content)