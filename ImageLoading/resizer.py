import cv2
from os import  listdir
from  os.path import isfile, join


file_ext = "100by100.jpg"

def resize_images():
    onlyfiles = [f for f in listdir("sample-images") if isfile(join("sample-images", f))]
    print(onlyfiles)
    for f in onlyfiles:
        with open("sample-images//" + f, 'r') as img:
            img = cv2.imread(f , 0)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("100by100" + f,resized_image )

"""
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


print(img)
print(img.shape)
print(img.ndim)

resized_imag=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Galaxy",resized_imag)
cv2.imwrite("Galaxy_resized.jpg", resized_imag)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
resize_images()