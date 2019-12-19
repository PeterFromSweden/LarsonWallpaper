
import ctypes
CSIDL_PERSONAL= 39
SHGFP_TYPE_CURRENT= 0
buf = ctypes.create_unicode_buffer(260)
ctypes.windll.shell32.SHGetFolderPathW(0, CSIDL_PERSONAL, 0, SHGFP_TYPE_CURRENT, buf)
#print(buf.value)
filepath = buf.value + r'\filename.ext'
print(filepath)
