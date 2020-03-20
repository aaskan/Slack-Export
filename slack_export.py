import requests
import json
import os
import sys

OUTPUT = 'output/'

if not os.path.exists(OUTPUT):
    os.makedirs(OUTPUT)

f = open("token.txt", "r")
token = f.read()
available_types = ['im', 'mpim', 'private_channel', 'public_channel', 'all']
requested_type = sys.argv[1]
assert requested_type in available_types, 'Type is not right. Please choose one of the {}'.format(available_types)
if requested_type == 'all':
	types = [e for e in available_types if e != requested_type]
else:
	types = [requested_type]

url_main = 'https://slack.com/api/'
for t in types:

	url_convs = url_main+'conversations.list?token='+token+'&types='+t+'&pretty=1'
	r = requests.get(url_convs).json()
	if t == 'im':
		id_pairs = [(e['id'], e['user']) for e in r['channels']]
	else:
		id_pairs = [(e['id'], e['name']) for e in r['channels']]

	for conv_id, userid_or_name in id_pairs:
		if t == 'im':
			url_users = url_main+'users.info?token='+token+'&user='+userid_or_name+'&pretty=1'
			user = requests.get(url_users).json()
			file_name = user['user']['name']
		else:
			file_name = userid_or_name

		print(file_name + ' started!')
		url = url_main+'conversations.history?token='+token+'&channel='+conv_id+'&pretty=1&limit=200'
		data = requests.get(url).json()

		has_more = data['has_more']
		if has_more:
			cursor = data['response_metadata']['next_cursor']

		counter = 1
		data_dict = {counter : data}

		while has_more:
			counter += 1
			url = url_main+'conversations.history?token='+token+'&channel='+conv_id+'&pretty=1&limit=200&cursor='+cursor
			data = requests.get(url).json()
			data_dict[counter] = data

			has_more = data['has_more']
			if has_more:
				cursor = data['response_metadata']['next_cursor']
			
		with open(OUTPUT+file_name+'.json', 'w', encoding='utf-8') as f:
			json.dump(data_dict, f, ensure_ascii=False, indent=4)
		print(file_name + ' completed!')
