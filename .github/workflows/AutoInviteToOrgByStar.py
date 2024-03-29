# Max Base
# 2021-06-19
# https://github.com/BaseMax/AutoInviteToOrgByStar

import os
import sys
import json
import requests

print("Hello, World")

if os.getenv('CI'):
    print('Looks like GitHub!')
else:
    print('Maybe running locally?')

print("Environ:")
print(os.environ)
print("Prefix:")
print(sys.prefix)

MY_GITHUB_KEY = os.environ['MY_GITHUB_KEY']
COMMUNITY_TEAM_ID = os.environ['COMMUNITY_TEAM_ID']

file = open(os.environ['GITHUB_EVENT_PATH'])
data = json.load(file)

print("Data: ")
print(data)

USERNAME = data['sender']['login']

print('Send invite for the @'+USERNAME)

# TODO: check user already joined or no....
url = 'https://api.github.com/teams/'+COMMUNITY_TEAM_ID+'/memberships/' + USERNAME
#url = "https://api.github.com/orgs/ITESO-Ulab/teams/community/memberships/"+USERNAME

payload = json.dumps({
  "role": "member"
})
headers = {
  'Accept': 'application/vnd.github.v3+json',
  'Authorization': 'token '+MY_GITHUB_KEY,
  'Content-Type': 'application/json',
  'Cookie': '_octo=GH1.1.1312574687.1613761866; logged_in=no',
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)
