import requests
import json
from api.server_token import serverToken

class Notification:

    serverToken = serverToken

    def __init__(self, topic):
        self.topic = "/topics/" + topic
        
        
    def sendPush(self, title, body):
        self.title = title
        self.body = body

        headers = {
                'Content-Type': 'application/json',
                'Authorization': 'key=' + self.serverToken,
            }

        body = {
                'notification': {'title': self.title,
                                    'body': self.body
                                    },
                'to':
                    self.topic,
                'priority': 'high',
                }

        response = requests.post("https://fcm.googleapis.com/fcm/send", headers = headers, data=json.dumps(body))
        print(response.status_code)

        print(response.json())

