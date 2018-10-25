from PIL import Image

def effetFonteNB(img,  sx,  sy) :
    res = Image.new("L",img.size,"black")
    #
    return res

def quartImageNB(img,  sx,  sy) :
    res = Image.new("L",img.size,"black")
    #
    return res

def RotationNB(img,  sx,  sy) :
    (a,b)=img.size;
    res = Image.new("L",(b,a),"black")
    for y in range (0,sy) :
        for x in range (0,sx) :
            col = img.getpixel ((x,y))
            res.putpixel((y,(sx-1)-x),col)
    return res





