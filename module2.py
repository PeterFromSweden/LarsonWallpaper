
#from html.parser import HTMLParser
import html.parser

class MyHTMLParser(html.parser.HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

myparser = MyHTMLParser()
myparser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')