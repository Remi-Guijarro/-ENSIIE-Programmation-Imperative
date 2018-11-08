
from PIL import Image

def filtrerMedianImageNB(src,  sy,  sx, tailleFiltre) :
    res = Image.new("L",src.size,"black")
    print(res.size)
    #calcul des coordonnees (relatives a x et y : coordonnees du pixel traite) du pixel en haut a gauche dans la
    # fenetre de voisinage de taille tailleFiltre
    xv = -1 * (tailleFiltre // 2)
    yv = -1 * (tailleFiltre // 2)
    for y in range(0, sy):
        for x in range(0, sx):
            pixel_value = src.getpixel((x,y))
            #condition bords image
            if x+xv < 0 or y+yv < 0 or x-xv > sx-1 or y-yv > sy-1:
                res.putpixel((x, y), pixel_value)
            else:
                # nombre de pixels dans le voisinage : (taille du filtre ^ 2) - 1
                voisinage = []
                for i in range(0, tailleFiltre*tailleFiltre):
                    pixel_value = src.getpixel((x+xv, y+yv))
                    voisinage.append(pixel_value)
                    # pixel suivant dans la fenetre
                    if xv == tailleFiltre // 2:
                        xv = -1 * (tailleFiltre // 2)
                        yv += 1
                    else:
                        xv += 1
                    if i == tailleFiltre * tailleFiltre - 1:
                        xv = -1 * (tailleFiltre // 2)
                        yv = -1 * (tailleFiltre // 2)
                #trier le tableau
                voisinage.sort()
                #recuperer la mediane
                pixel_value = voisinage[len(voisinage)//2]
                res.putpixel((x,y), pixel_value)
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
    res = Image.new("L",src.size,"black")

    # calcul des coordonnees (relatives a x et y : coordonnees du pixel traite) du pixel en haut a gauche dans la
    # fenetre de voisinage de taille tailleFiltre
    xv = -1 * (tailleFiltre // 2)
    yv = -1 * (tailleFiltre // 2)

    for y in range(0, sy):
        for x in range(0, sx):
            pixel_value = src.getpixel((x, y))

            # condition bords image
            if x + xv < 0 or y + yv < 0 or x - xv > sx - 1 or y - yv > sy - 1:
                res.putpixel((x, y), pixel_value)
            else:
                # nombre de pixels dans le voisinage : (taille du filtre ^ 2) - 1
                voisinage = []
                for i in range(0, tailleFiltre * tailleFiltre):
                    pixel_value = src.getpixel((x + xv, y + yv))
                    voisinage.append(pixel_value)

                    # pixel suivant dans la fenetre
                    if xv == tailleFiltre // 2:
                        xv = -1 * (tailleFiltre // 2)
                        yv += 1
                    else:
                        xv += 1
                    if i == tailleFiltre * tailleFiltre - 1:
                        xv = -1 * (tailleFiltre // 2)
                        yv = -1 * (tailleFiltre // 2)

                # calculer la moyenne
                pixel_value = sum(voisinage)//len(voisinage)
                res.putpixel((x, y), pixel_value)
    return res