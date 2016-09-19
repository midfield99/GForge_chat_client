import requests
import json
import ast
import shlex
import stackexchange
from twilio.rest import TwilioRestClient
from time import sleep

usr = 'YOURUSERNAME'
pw = 'YOURPASSWORD'
base_url = "https://" + usr + ":" + pw + "@next.gforge.com"

def process_chat():
	last_message = 0
	while True:
		messages = get_chat_messages(last_message)

		for msg in messages:
			cmd = command(msg['body'])
			try:
				if (cmd):
					args = get_args(msg['body'])
					exectute(cmd, args)
				else:
					if msg['body'].split(' ')[0] == 'search':
						search_stackoverflow(' '.join(msg['body'].split(' ')[1:]))
					elif msg['body'].split(' ')[0] == 'text':
						s = shlex.split(msg['body'])
						twilioMessage(s[1], s[2])
					else:
						maps(msg['body'])
			except:
				continue
		
		last_message = get_last_id(messages, last_message)

		sleep(.2)

def maps(msg):
	gMapsOccasions = ["lunch", "dinner", "supper", "breakfast","brunch","go to"]
	for m in gMapsOccasions:
		if m in msg:
			zstr = str(msg)
			location = zstr.split(' at ')
			locationWords = location[1].split()
			urlWords =[]
			for x in locationWords:
				urlWords.append(x)
			payload = {'id':0, 'subject':'map', 'forumThread':7238}
			payload['body'] = 'http://maps.google.com/?q='+'+'.join(urlWords)

			chat(payload)

			return

def twilioMessage(phone, message):
	account_sid = "AC77f78f8c4d57d7ee2ce38e9ffd82c092"
	auth_token = "896ed08096cee90e016ce55179b0f86d"
	client = TwilioRestClient(account_sid, auth_token)

	sendMessage = client.messages.create(to=phone, from_="+18168443415",body=message)

def todo(payload):
	userURL = 'https://brendanoconnor:password@next.gforge.com/api/user/' + payload['for']
	userResponse = requests.get(userURL).json()
	userID = userResponse["id"]
	trackerItemsURL = 'https://brendanoconnor:password@next.gforge.com/api/user/'+str(userID)+'/trackeritems/?project=2269'
	trackerItemsResponse = requests.get(trackerItemsURL).json()

	tasks = []
	for i in trackerItemsResponse["items"]:
		tasks.append("Task #"+str(i["id"])+": "+ i["summary"] + " ")

	postForumURL = 'https://brendanoconnor:password@next.gforge.com/api/forummessage/?forumThread=7238'
	
	for t in tasks:
		postdata1 = '{"id":0,"forumThread":7238,"subject": "user tasks", "body": "'+ t +'"}'
		postrequest = requests.post(postForumURL,postdata1)

def search_stackoverflow(query):
	so = stackexchange.Site(stackexchange.StackOverflow, app_key='S3abU4WtBqUvzSlHg9)reA((', impose_throttling=True)
	qs = so.search(intitle=query)
	
	y=0
	maxval = 0
	count = 0

	for q in qs:
		if q.view_count>maxval:
			y=q.id
			maxval=q.view_count
		count+=1
		if count>1000:
			break

	url = 'http://stackoverflow.com/questions/' + str(y)
	postTrackeritemURL = 'https://USERNAME:PASSWORD@next.gforge.com/api/forummessage/?forumthread=7238'
	postdataMostViewedPosts = '{"id":0,"subject":"Most viewed posts on StackOverflow", "body":"http://stackoverflow.com/questions/tagged/' + query + '?sort=votes&pageSize=15","forumThread": 7238}'
	postrequest1 = requests.post(postTrackeritemURL, postdataMostViewedPosts)
	postdataMostPopularPosts = '{"id":0,"subject":"Most popular StackOverflow post", "body":"' + url + '","forumThread": 7238}'
	postrequest2 = requests.post(postTrackeritemURL, postdataMostPopularPosts)

def get_last_id(messages, old):
	try:
		return messages[-1]['id']
	except:
		return old

def get_chat_messages(id):
	try:
		last_message ='forumthread-7238-' + str(id) 
		payload={'rel':'chat','chat[]':last_message}
		url = 'http://next.gforge.com/api/poll'
		req = requests.get(url, params=payload, auth=('chris123', 'campion'))
		r = json.loads(req.content)

		return	r['items'][0]['items']
	except:
		return []

def exectute(func, payload):
	method = functions.get(func)
	method(payload)

def users(payload = {}):
	url = "http://next.gforge.com/api/project/gforge_chat/members"
	info = []
	req = requests.get(url, auth=('chatbot', 'chatchat'))

	r = json.loads(req.content)
	payload = {'id':0, 'subject':'user info', 'forumThread':7238}
	for user in r['items']:
		s = user['unixName'] + ": "
		s += user['firstname'] + " "
		s += user['lastname'] + " "
		s += user['email'] 
		payload['body'] = s

		chat(payload)

#/chat id:0 subject:'testing python post' body:'12345new post' forumThread:7238
def chat(payload):
	endpoint = "/api/forummessage/?forumthread=7238"
	post(base_url, endpoint, payload)

#/ticket summary:'gmail issue integration'
def ticket(payload):
	endpoint = "/api/trackeritem/trackerItemBasic"
	payload['tracker'] = 11548
	post(base_url, endpoint, payload)

def update(payload):
	endpoint = "/api/trackeritem/" + payload['id']
	payload['tracker'] = 11548
	post(base_url, endpoint, payload)

def post(base, endpoint, payload):
	url = base + endpoint
	req = requests.post(url,payload)

def command(body):
	w = body.split(' ')[0]
	if len(w) > 0 and w[0] == "/":
		cmd = w[1:]
		if cmd in functions.keys():
			return cmd

	return False 

def get_args(s):
	args = {}
	spl = shlex.split(s)
	for arg in spl[1:]:
		data = arg.split(':')
		args[data[0]] = data[1]

	return args


functions = globals().copy()
process_chat()
