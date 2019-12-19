import winreg
import ctypes
import requests
import html.parser
import shutil
import datetime

now = datetime.datetime.now();

response = requests.get(
    'https://www.thefarside.com/' + now.strftime('%Y/%m/%d'),
)

def Convert(lst):
    res_dct = {lst[i][0]:lst[i][1] for i in range(0, len(lst))}
    return res_dct


class MyHTMLParser(html.parser.HTMLParser):
    
    def __init__(self):
        self.img_url = ""
        self.comic = False
        super(MyHTMLParser,self).__init__()

    def handle_starttag(self, tag, attrs):
        if tag == 'div' and len(attrs) > 0 and attrs[0][1] == 'tfs-comic__image':
            self.comic = True
        
        if tag == "img" and self.comic and self.img_url == "":
            attr_dct = Convert(attrs)
            if 'data-src' in attr_dct:
                self.img_url = attr_dct['data-src']

    def get_url(self):
        return self.img_url

myParser = MyHTMLParser()
myParser.feed(response.text)
print(myParser.get_url())

resp = requests.get(myParser.get_url(), stream=True)
CSIDL_PERSONAL= 39
SHGFP_TYPE_CURRENT= 0
buf = ctypes.create_unicode_buffer(260)
ctypes.windll.shell32.SHGetFolderPathW(0, CSIDL_PERSONAL, 0, SHGFP_TYPE_CURRENT, buf)
filepath = buf.value + r'\daily_larson.jpg'
local_file = open(filepath, 'wb')

resp.raw.decode_content = True
shutil.copyfileobj(resp.raw, local_file)
local_file.close()
del resp

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Policies\System')
try:
    winreg.DeleteKey(key, "Wallpaper")
except:
    pass

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Control Panel\Desktop')
winreg.SetValue(key, 'TileWallpaper', winreg.REG_SZ, '0')
winreg.SetValue(key, 'WallpaperStyle', winreg.REG_SZ, '0')
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, filepath, 3)
#print(ctypes.GetLastError())
print(filepath)