import string
import random


letters = string.ascii_letters
digitss = string.digits
punctuations = string.punctuation

NormalCharactersNUMALPH = letters + digitss
AllCharacters = letters + digitss + punctuations
#print (NormalCharactersNUMALPH)

#print(letters, digitss, punctuations)

def super_strong_PGv0 (length):
    iSPG = ""
    while len(iSPG) < length:
        temporary = ''
        iSPG = iSPG + str(random.choice(AllCharacters))
        temporary = ''.join(iSPG)
    return temporary

#print (super_strong_PGv0(6))    

def super_strong_PGv1 (length, howmuch):
    count = 0
    while count < howmuch:
        iSPG = ""
        while len(iSPG) < length:
            temporary = ''
            iSPG += str(random.choice(AllCharacters))
            temporary = ''.join(iSPG)
        print (temporary)
        count = count + 1

#super_strong_PGv1(8, 10)

def super_strong_PGv2 (length, howmuch, Clists):
    count = 0
    while count < howmuch:
        iSPG = ""
        while len(iSPG) < length:
            lista = globals().get(Clists) #esto hace q se pueda usar los nombres de listas como inputs del usuario, sino tomara lo q el usuario puso para generar el pw
            temporary = ''
            iSPG += str(random.choice(lista))
            temporary = ''.join(iSPG)
        print (temporary)
        count = count + 1

super_strong_PGv2(int(input('How many characters do you want for your password? ')), int(input('How many passwords do you want to generate ')), input('What charactrers do you want in your password? \n Letras y numeros \n Letras, numeros y caracteres especiiales ?'))

