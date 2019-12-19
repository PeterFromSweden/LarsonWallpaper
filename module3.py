import winreg
import ctypes

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Policies\System')
try:
    winreg.DeleteKey(key, "Wallpaper")
except:
    pass
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, r'C:\Users\pliedholm\Pictures\Volvo Ocean Race\m6813_telefonica2-1920x1200.jpg', 0)