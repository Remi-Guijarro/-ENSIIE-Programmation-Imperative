#-*- coding: utf-8 -*-

######  #     #   ###     #       #     ######
#       ##    #  #   #                  #
#       # #   #   #      ##      ##     #
#####   #  #  #    #      #       #     #####
#       #   # #     #     #       #     #
#       #    ##  #   #    #       #     #
######  #     #   ###   #####   #####   ######

# 2018-2019
# ---------

import sys
import random
import PyQt5

from PIL import Image

from effets_photom import *
from effets_geom import *
from filtrages import *


# /*!
#  \file tpimage.py
#  \author Pierre Tellier
#  \date  16/10/2017
#  \brief programme principal : test des fonctionnalités de manipulation d'image
# */



def runImageTool():
    # argc=len(sys.argv)
    # if argc<3 :
    #     print ("usage : ", sys.argv[0], " fichier.png fichier.png")
    #     return
    random.seed()  #initialisation du générateur pseudo-aléatoire
    #print(sys.argv[1])
    #img1=Image.open(sys.argv[1])
    img1=Image.open(".\\test.pgm")
    (xsize,ysize) = img1.size
    print ("Lecture OK ( H =", ysize, " L =", xsize,")")
    img1.show()
    #inversion_videoNB(img1,xsize,ysize).show()
    #plusClairNB(img1,xsize,ysize).show()
    deriv1xNB(img1,xsize,ysize).show()
    #effetFonteNB(img1,xsize,ysize).show()
    quartImageNB(img1,xsize,ysize).show()
    # if argc==4 :
    #     img2=Image.open(sys.argv[2])
    #     img4 = mouvement(img1,img2)
    #     img4.show()
    #     img4.save(sys.argv[3])
    #     img4.close()
    #     return

    # img2 = RotationNB(img1, xsize, ysize)

    # img2.show()
    # img2.save(sys.argv[2])

    # img3 = traitV(256,500, 100, 300)
    # img3.show()



    # img1.close()
    # img2.close()
    # img3.close()

if __name__ == "__main__":
    runImageTool()





