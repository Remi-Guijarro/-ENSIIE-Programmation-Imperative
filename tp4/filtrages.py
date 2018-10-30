
from PIL import Image

def filtrerMedianImageNB(src,  sy,  sx, tailleFiltre) :
    print('debut')
    res = Image.new("L",src.size,"black")
    i=tailleFiltre-2
    tab = []
    for k in range(0,src.size[0]):
        for m in range(0,src.size[1]):
            res.putpixel((k,m),src.getpixel((k,m)))
    positionrelativeligne= 0
    while (i<(src.size[0]-tailleFiltre-2)):
        j=tailleFiltre-2
        while (j<(src.size[1]-tailleFiltre-2)):
            positionrelativeligne=-(tailleFiltre-2)
            ip=0
            while(ip<tailleFiltre):
                jp=0
                positionrelativecol=-(tailleFiltre-2)
                while (jp<tailleFiltre):
                    tab.append(src.getpixel((i+positionrelativeligne,j+positionrelativecol)))
                    jp+=1
                    positionrelativecol = positionrelativecol +1
                positionrelativeligne=-(tailleFiltre-2)
                ip+=1
            tab.sort()
            median = tab[int((len(tab)+1)/2)]
            tab = []
            res.putpixel((i-(tailleFiltre-2),j-(tailleFiltre-2)),median)
            j+=1
        i+=1
    print('fin')
    return res

def filtrerMedianImageNBVAB(src,  sy,  sx, tailleFiltre) :
    print('debut')
    err =0
    res = Image.new("L",src.size,"black")
    i=tailleFiltre-2
    tab = []
    positionrelativeligne= 0
    while (i<(src.size[0])):
        j=tailleFiltre-2
        while (j<(src.size[1])):
            positionrelativeligne=-(tailleFiltre-2)
            ip=0
            while(ip<tailleFiltre):
                jp=0
                positionrelativecol=-(tailleFiltre-2)
                while (jp<tailleFiltre):
                    try:
                        tab.append(src.getpixel((i+positionrelativeligne,j+positionrelativecol)))
                    except Exception:
                        err+=1
                    jp+=1
                    positionrelativecol = positionrelativecol +1
                positionrelativeligne=-(tailleFiltre-2)
                ip+=1
            tab.sort()
            median = tab[int((len(tab)+1)/2)]
            tab = []
            res.putpixel((i-(tailleFiltre-2),j-(tailleFiltre-2)),median)
            j+=1
        i+=1
    print('fin')
    return res

def filtrerImageNB(src,  sy,  sx, tailleFiltre) :
    print('debut')
    res = Image.new("L",src.size,"black")
    i=tailleFiltre-2
    tab = []
    for k in range(0,src.size[0]):
        for m in range(0,src.size[1]):
            res.putpixel((k,m),src.getpixel((k,m)))
    positionrelativeligne= 0
    while (i<(src.size[0]-tailleFiltre-2)):
        j=tailleFiltre-2
        while (j<(src.size[1]-tailleFiltre-2)):
            positionrelativeligne=-(tailleFiltre-2)
            ip=0
            while(ip<tailleFiltre):
                jp=0
                positionrelativecol=-(tailleFiltre-2)
                while (jp<tailleFiltre):
                    tab.append(src.getpixel((i+positionrelativeligne,j+positionrelativecol)))
                    jp+=1
                    positionrelativecol = positionrelativecol +1
                positionrelativeligne=-(tailleFiltre-2)
                ip+=1
            tab.sort()
            moyenne = (sum(tab) / len(tab))
            tab = []
            res.putpixel((i-(tailleFiltre-2),j-(tailleFiltre-2)),int(moyenne))
            j+=1
        i+=1
    print('fin')
    return res



def filtrerImageNBVAB(src,  sy,  sx, tailleFiltre) :
    print('debut')
    res = Image.new("L",src.size,"black")
    i=tailleFiltre-2
    tab = []
    positionrelativeligne= 0
    while (i<(src.size[0])):
        j=tailleFiltre-2
        while (j<(src.size[1])):
            positionrelativeligne=-(tailleFiltre-2)
            ip=0
            while(ip<tailleFiltre):
                jp=0
                positionrelativecol=-(tailleFiltre-2)
                while (jp<tailleFiltre):
                    try:
                        tab.append(src.getpixel((i+positionrelativeligne,j+positionrelativecol)))
                    except Exception:
                        tab.append(255)
                    jp+=1
                    positionrelativecol = positionrelativecol +1
                positionrelativeligne=-(tailleFiltre-2)
                ip+=1
            tab.sort()
            moyenne = (sum(tab) / len(tab))
            tab = []
            res.putpixel((i-(tailleFiltre-2),j-(tailleFiltre-2)),int(moyenne))
            j+=1
        i+=1
    print('fin')
    return res
