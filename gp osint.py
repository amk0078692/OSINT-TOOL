from pdfanalysis import pdfinfo
from exif import gps
from Instagraminfo import instainfo

def reconinput():
    inp=(input("gp osint >> "))
    if(inp == '1'):
        gps()
    elif(inp=='2'):
        instainfo()
    elif (inp=='3'):
        pdfinfo()
    elif(inp=='exit'):
        exit()


        
if __name__=="__main__":
    print(
            """ 
   _____   _____       ____     _____   _____   _   _   _______   
  / ____| |  __ \     / __ \   / ____| |_   _| | \ | | |__   __|  
 | |  __  | |__) |   | |  | | | (___     | |   |  \| |    | |     
 | | |_ | |  ___/    | |  | |  \___ \    | |   | . ` |    | |     
 | |__| | | |        | |__| |  ____) |  _| |_  | |\  |    | |     
  \_____| |_|         \____/  |_____/  |_____| |_| \_|    |_|     
                                                                  
                                                                  
  __  __              _____    ______     ____   __     __    _______   ______              __  __     __    ___  
 |  \/  |     /\     |  __ \  |  ____|   |  _ \  \ \   / /   |__   __| |  ____|     /\     |  \/  |   /_ |  / _ \ 
 | \  / |    /  \    | |  | | | |__      | |_) |  \ \_/ /       | |    | |__       /  \    | \  / |    | | | (_) |
 | |\/| |   / /\ \   | |  | | |  __|     |  _ <    \   /        | |    |  __|     / /\ \   | |\/| |    | |  > _ < 
 | |  | |  / ____ \  | |__| | | |____    | |_) |    | |         | |    | |____   / ____ \  | |  | |    | | | (_) |
 |_|  |_| /_/    \_\ |_____/  |______|   |____/     |_|         |_|    |______| /_/    \_\ |_|  |_|    |_|  \___/ 
                                                                                                                  
                       Authors  -  Asif Mohammad Khan, Yash___HackZ,  Aksh puri, MD Tajdar Alam Ansari                                                                             
                                                                                  
"""
        )

    language = 'en'
    print('')
    print("""Tools available 
    
            1.Image Meta data extraction
            2.Instagram Info lookup
            3.PDF meta data analysis
            usage : type exit to stop
            """)
    print('')
    
    
    while True:
        reconinput()
