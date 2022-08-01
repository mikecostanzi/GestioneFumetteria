import json
from json import *
import os.path


from Fumetto.FumettoAcquistabile import FumettoAcquistabile


class GestoreFumettiA(FumettoAcquistabile):
    def __init__(self):
        super().__init__()


    def aggiungi_fumettoA(self,categoria,distributore, editore, collana, sottocollana , barcodeA, prezzo):
        
        self.setFumettoAcquistabile(categoria,distributore, editore, collana, sottocollana , barcodeA, prezzo)

        fumettiA = [self.getInfoFumettoA()]
        if os.path.isfile('DatabaseFumettiAcquistabili/FumettiAcquistabili.json'):
            #with open('DatabaseFumettiAcquistabili/FumettiAcquistabili.json', 'r') as f:
                #fumettiA = json.load(f)
            #fumettiA[barcodeA] = self
        #print(fumettiA)
            with open('DatabaseFumettiAcquistabili/FumettiAcquistabili.json', 'a') as f:
                json.dump(fumettiA, f)
        else:
            return print("Nicolaaaa pure qua")



    def getInfoFumettoA(self):

        info = self.getFumettoAcquistabile()
        return info

    def ricercaFumettoA(self, barcodeA):
        if os.path.isfile('DatabaseFumettiAcquistabili/FumettiAcquistabili.json'):
            with open('DatabaseFumettiAcquistabili/FumettiAcquistabili.json', 'r') as f:
                fumettiA = dict(json.load(f))
                for fumettiA in fumettiA.values():
                    if fumettiA.barcodeA == barcodeA:
                        print("E' entrato qua:" + fumettiA)
                        print(fumettiA.get(barcodeA, None))
                        return fumettiA
                return ("Finita la ricerca")
        else:
            return print("File non trovato")

    def rimuoviFumettoA(self):
        if os.path.isfile('DatabaseFumettiAcquistabili/FumettiAcquistabili.json'):
            with open('DatabaseFumettiAcquistabili/FumettiAcquistabili.json', 'r') as f:
                fumettiA = dict(json.load(f))
                del fumettiA[self.barcodeA]
            with open('DatabaseFumettiAcquistabili/FumettiAcquistabili.json', 'w') as f:
                json.dump(fumettiA, f)
        self.rimossoFumettoA()
        del self


