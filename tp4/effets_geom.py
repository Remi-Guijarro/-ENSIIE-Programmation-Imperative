from PIL import Image

def effetFonteNB(img,  sx,  sy) :
    res = Image.new("L",img.size,"black")
    for x in range (0,sx) :
        for y in range (0,sy) :
            if(y == sy-1):
                col = img.getpixel ((x,y))
                res.putpixel((x,y),col) 
                break
            else:                
                col = img.getpixel ((x,y))
                nextPixel = img.getpixel((x,y+1))
                if nextPixel < col :
                    nextPixel = col
                    res.putpixel((x,y+1),nextPixel)
                    res.putpixel((x,y),col)
    return res

def quartImageNB(img,  sx,  sy) :
    print(img.size)
    newSize = (int(img.size[0]/2),int(img.size[1]/2))
    res = Image.new("L",newSize,"black")
    print(" VS ")
    print(res.size)
    v=0
    w=0
    for y in range (0,sy) :
        if((y % 2) == 0):
            w=0
            for x in range (0,sx) :
                if((x % 2) == 0):
                    col = img.getpixel((x,y))
                    print('v ' + str(v) + '  w ',str(w))
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
    print(res.size)
    return res