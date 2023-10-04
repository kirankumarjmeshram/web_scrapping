import requests

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "https://10.10.1.10:1080",
}

r = requests.get("https://api64.ipify.org?format=json")

print(r.json()) #{'ip': '2409:40c2:1165:1fc2:b13d:fdb5:b10e:9a3'}