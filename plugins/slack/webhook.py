import http.client as client
import urllib.parse as parse
import json

class Robot(object):
    def __init__(self, name, hook_url=None, icon=None, channel=None):
        self.name = name
        self.icon = icon
        self.channel = channel
        self.hook_url = hook_url

    def send(self, msg):
        if self.hook_url is None:
            raise NameError
        
        headers = {'content-type': "application/json"}
        body = self.message(msg)

        conn = client.HTTPSConnection("hooks.slack.com")
        conn.request('POST', self.hook_url, body, headers)
        res = conn.getresponse()
        
        return res.read().decode('utf-8')

    def message(self, text):
        context = {"text": text, "username": self.name}

        if self.icon is not None:
            if parse.urlparse(self.icon).scheme != '':
                context["icon_url"] = self.icon
            else:
                context["icon_emoji"] = self.icon
        
        if self.channel is not None:
            context["channel"] = '#' + self.channel
        
        return json.dumps(context)
