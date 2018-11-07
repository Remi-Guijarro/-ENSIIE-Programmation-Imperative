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
import time
import random

from PIL import Image


from effect_source.effets_geom import *
from effect_source.effets_photom import *
from effect_source.filtrages import *


# /*!
#  \file tpimage.py
#  \author Pierre Tellier
#  \date  16/10/2017
#  \brief programme principal : test des fonctionnalités de manipulation d'image
# */

def getValidCommands():
    switcher = {
        1: "help",
        2: "rotate",
        3: "divide",
        4: "relief",
        5: "fonte",
        6: "lighter",
        7: "noise",
        8: "blur",
        9: "inversion",
        10: "quit"
    }
    for i in range(1,11):
        print( ' :> ' + switcher.get(i) + '\n')
        time.sleep(0.2)



def launchMenu(fichierDep,fichierDest):
    switcher = {
        1: "help",
        2: "rotate",
        3: "divide",
        4: "relief",
        5: "fonte",
        6: "lighter",
        7: "noise",
        8: "blur",
        9: "inversion",
        10: "quit"
    }

    print('What do you want to do ? type help to get the availables commands :>')
    user = input()
    user = user.strip().lower()
    img1 = Image.open(fichierDep)
    (xsize,ysize) = img1.size
    while user != switcher.get(10):
        if(user == switcher.get(1)):
            getValidCommands()
        elif(user == switcher.get(2)):
            if(ifRGBIMG(img1)):
                img1 = convertToGrayScale(img1,xsize,ysize)     
            img1 = RotationNB(img1,xsize,ysize) 
        elif(user == switcher.get(3)):
            if(ifRGBIMG(img1)):
                img1 = convertToGrayScale(img1,xsize,ysize)     
            img1 = quartImageNB(img1,xsize,ysize)
        elif(user == switcher.get(4)):
            if(ifRGBIMG(img1)):
                img1 = convertToGrayScale(img1,xsize,ysize)     
            img1 = deriv1xNB(img1,xsize,ysize)
        elif(user == switcher.get(5)):
            if(ifRGBIMG(img1)):
                img1 = convertToGrayScale(img1,xsize,ysize)     
            img1 = effetFonteNB(img1,xsize,ysize)
        elif(user == switcher.get(6)):
            if(ifRGBIMG(img1)):
                img1 = convertToGrayScale(img1,xsize,ysize)     
            img1 = plusClairNB(img1,xsize,ysize)
        elif(user == switcher.get(7)):
            if(ifRGBIMG(img1)):
                img1 = convertToGrayScale(img1,xsize,ysize)         
            img1 = filtrerMedianImageNB(img1,xsize,ysize,3)
        elif(user == switcher.get(8)):
            if(ifRGBIMG(img1)):
                img1 = convertToGrayScale(img1,xsize,ysize)     
            img1 = filtrerImageNB(img1,xsize,ysize,3)
        elif(user == switcher.get(9)):
            if(ifRGBIMG(img1)):
                img1 = convertToGrayScale(img1,xsize,ysize)          
            img1 = inversion_videoNB(img1,xsize,ysize) 
        else:   
            print('Invalid Command type help to get some help :) ')
        img1.show()
        user = input()
        user =  user.strip().lower()
    print('result file will be save with the name :> ' + fichierDest)
    img1.save(fichierDest)
    print('Good Bye !')

def runImageTool():
    argc=len(sys.argv)
    if argc<3 :
        print ("usage : ", sys.argv[0], " image_en_entrée       nom_du_fichier_pour_sauvegarde.extension_souhaité")
        return 
    imgSource =  sys.argv[1]
    savedImageName = sys.argv[2]
    launchMenu(imgSource,savedImageName)
    
if __name__ == "__main__":
    runImageTool()





