import json
import os.path

from Fumetto.Classi.FumettoAcquistabile import FumettoAcquistabile

class GestoreFumettiA(FumettoAcquistabile):
    def __init__(self):
        super().__init__()


    def aggiungi_fumettoA(self,categoria,distributore, editore, collana, sottocollana , barcodeA, prezzo, quantita):
        
        self.setFumettoAcquistabile(categoria,distributore, editore, collana, sottocollana , barcodeA, prezzo, quantita)

        fumettiA = [self.getInfoFumettoA()]
        if os.path.isfile('Fumetto/Database/FumettiAcquistabili.json'):
            #with open('Fumetto/Database/FumettiAcquistabili.json', 'rt') as f:
            #    fumettiA = dict(json.load(f))
            #fumettiA[barcodeA] = self
            with open('Fumetto/Database/FumettiAcquistabili.json', 'at') as f:
                json.dump(fumettiA, f)


    def getInfoFumettoA(self):
        info = self.getFumettoAcquistabile()
        return info

    def ricercaFumettoA(self, barcodeA):
        if os.path.isfile('Fumetto/Database/FumettiAcquistabili.json'):
            with open('Fumetto/Database/FumettiAcquistabili.json', 'r') as f:
                fumettiA = dict(json.load(f))
                for fumettiA in fumettiA.values():
                    if fumettiA.barcodeA == barcodeA:
                        print("E' entrato qua:" + fumettiA)


                    return ("Finita la ricerca")
        else:
            return print("File non trovato")

    def rimuoviFumettoA(self):
        if os.path.isfile('Fumetto/Database/FumettiAcquistabili.json'):
            with open('Fumetto/Database/FumettiAcquistabili.json', 'r') as f:
                fumettiA = dict(json.load(f))
                del fumettiA[self.barcodeA]
            with open('Fumetto/Database/FumettiAcquistabili.json', 'w') as f:
                json.dump(fumettiA, f)
        self.rimossoFumettoA()
        del self


