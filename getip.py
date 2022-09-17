import subprocess
import re

response = subprocess.run('arp -a', stdout=subprocess.PIPE).stdout.decode("utf-8")
response_interfaces = response.splitlines()
response = re.sub(' +', ' ', response).split('\r\n\r\n')

def stripper(data):
	data = data[0: 0:] + data[data.find("Type")+3 + 1::]
	data = data.replace("\r\n", "")
	data = data.split(" ")
	data = list(filter(None, data))
	return data

ip_list = []
for interface in range(len(response)):
	ip_list.append(stripper(response[interface])[::3])
ip_list = sum(ip_list, [])