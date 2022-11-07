from PIL import Image
from PIL.ExifTags import TAGS

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret
def gps():
    imagename=input("Enter the filepath : " )
    exif=get_exif(imagename)
    for key,value in exif.items():
        print("%s : %s" %(key,value))

if __name__ == "__main__":
    gps()