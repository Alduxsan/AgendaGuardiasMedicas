import requests
import json

class Notification:

    serverToken = 'AAAAQbP1oO8:APA91bGixEb8rSPnJqiha7VhLlgH8FthJAKn8z6BnOxJSd-Gl-01zadXCOR84-RwpQeENqfT9Ab6va9vt2NVt73Z4cmvqgAlJbT45i0VQLZlnMJyNZR38Sbbo69Qvj6Cm_w_0VL8V46o'
    
    def __init__(self, topic):
        self.topic = "/topics/" + str(topic)
        
        
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
                #"condition": "'deals' in topics || 'Colonia' in topics",
                'priority': 'high',

                }

        response = requests.post("https://fcm.googleapis.com/fcm/send", headers = headers, data=json.dumps(body))
        print(response.status_code)

        print(response.json())