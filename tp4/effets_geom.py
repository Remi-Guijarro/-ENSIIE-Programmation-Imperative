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
                print(col,nextPixel)
                if nextPixel < col :
                    nextPixel = col
                    res.putpixel((x,y+1),nextPixel)
                    res.putpixel((x,y),col)
    return res

def quartImageNB(img,  sx,  sy) :
    print(img.size)
    newSize = (int(img.size[0]/2),int(img.size[1]/2))
    res = Image.new("L",newSize,"black")
    print(res.size)
    v=0
    w=0
    for y in range (0,sy-2,2) :
        v = v + 1
        w=0
        for x in range (0,sx-2,2) :
            w = w + 1
            col = img.getpixel((x,y))
            res.putpixel((w,v),col)
    return res

def RotationNB(img,  sx,  sy) :
    (a,b)=img.size;
    res = Image.new("L",(b,a),"black")
    for y in range (0,sy) :
        for x in range (0,sx) :
            col = img.getpixel ((x,y))
            res.putpixel((y,(sx-1)-x),col)
    return res
