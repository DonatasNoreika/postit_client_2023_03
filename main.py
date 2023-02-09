import requests

# url = 'http://127.0.0.1:8000/posts/8/like'
# headers = {'Authorization': 'Token d7d1d18cf035da50380fd1ed372ff4d156a2a820'}
# r = requests.post(url, headers=headers)
#
# print(r.json())

url = 'http://127.0.0.1:8000/signup'
headers = {'Authorization': 'Token d7d1d18cf035da50380fd1ed372ff4d156a2a820'}
r = requests.delete(url, headers=headers)

print(r.json())

