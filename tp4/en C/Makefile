# ########################################## #

######  #     #   ###     #       #     ######                                  
#       ##    #  #   #                  #                                       
#       # #   #   #      ##      ##     #                                       
#####   #  #  #    #      #       #     #####                                   
#       #   # #     #     #       #     #                                       
#       #    ##  #   #    #       #     #                                       
######  #     #   ###   #####   #####   ######      

# ########################################## #

# Makefile minimaliste pour le TP IPI sur la manipulation d’images
# Pierre Tellier, ENSiiE, octobre 2017

APPLI=tp_image
CSRC= tpimage.c effets_photom.c pnm.c effets_geom.c filtrages.c
CC = gcc

CFLAGS = -Wall -Wextra -ansi -I. 

COBJ=$(CSRC:.c=.o)

.c.o:
	$(CC) $(CFLAGS) -c $*.c

$(APPLI):	$(COBJ)
	$(CC) -o $(APPLI) $(COBJ) -lm

clean:
	-rm *.o *[~%] core *.bak

