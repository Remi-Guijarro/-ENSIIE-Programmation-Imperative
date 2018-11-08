from PIL import Image
from random import randrange

def effetFonteNB(img,  sx,  sy) :
    N = sx * sy
    res = img
    for _ in range(0,N):
        x = randrange(sx)
        y = randrange(sy)
        if(y < sy -1):
            if(res.getpixel((x,y)) < res.getpixel((x,y+1))):
                res.putpixel((x,y+1),res.getpixel((x,y)))
    return res

def quartImageNB(img,  sx,  sy) :
    newSize = (int(img.size[0]/2),int(img.size[1]/2))
    res = Image.new("L",newSize,"black")
    v=0
    w=0
    print(res.size)
    for y in range (0,sy) :
        if((y % 2) == 0):
            w=0
            for x in range (0,sx) :
                if((x % 2) == 0):
                    col = img.getpixel((x,y))
                    res.putpixel((w,v),col)
                    w = w + 1
            v += 1
    return res

def RotationNB(img,  sx,  sy) :
    (a,b)=img.size
    res = Image.new("L",(b,a),"black")
    for y in range (0,sy) :
        for x in range (0,sx) :
            col = img.getpixel ((x,y))
            res.putpixel((y,(sx-1)-x),col)
    return res


def ifRGBIMG(img):
    try:
        r,g,b = img.getpixel((0,0))
        rgb = ((r,g,b))
        img.putpixel((0,0),rgb) 
        return True
    except Exception:
        return False
        


def convertToGrayScale(img,  sx,  sy) :
    res = Image.new("L",img.size,"black")
    for x in range (0,sx) :
        for y in range (0,sy) :
            r,g,b = img.getpixel((x,y))
            grayScale = 0.707 * r + 0.202 * g + 0.071 * b
            res.putpixel((x,y),int(grayScale)) 
    return res