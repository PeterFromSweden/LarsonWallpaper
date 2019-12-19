
import requests
import html.parser
import shutil

response = requests.get(
    'https://www.thefarside.com/2019/12/18',
)

def Convert(lst):
    res_dct = {lst[i][0]:lst[i][1] for i in range(0, len(lst))}
    return res_dct


class MyHTMLParser(html.parser.HTMLParser):
    
    def __init__(self):
        self.img_url = ""
        super(MyHTMLParser,self).__init__()

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            attr_dct = Convert(attrs)
            if 'data-src' in attr_dct:
                if 'alt' in attr_dct:
                    if attr_dct['alt'] == '':
                        self.img_url = attr_dct['data-src']
    def get_url(self):
        return self.img_url

myParser = MyHTMLParser()
myParser.feed(response.text)
print(myParser.get_url())

resp = requests.get(myParser.get_url(), stream=True)
local_file = open('daily_larson.jpg', 'wb')

resp.raw.decode_content = True
shutil.copyfileobj(resp.raw, local_file)

del resp
