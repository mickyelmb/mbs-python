import os, shutil
import CONFIG_PROD
#fo = open("GUPSImageUpload", "a")

path = r"C:\Users\mboyd\Desktop\GUPSImageUpload\\"
#moveto = "\\gdot-go-prd3\GUPS_upload\DrawingUploads"
moveto = r"C:\Users\mboyd\Desktop\Test\\" 
files = os.listdir(path)
files.sort()
for f in files:
    src = path+f
    newdir = os.makedirs(moveto+'\\'+ f[:7])
    #moveto = newdir
    dst = r"C:\Users\mboyd\Desktop\Test\\" + f[:7] + "\\"+ f 
    shutil.move(src,dst)
        
    
