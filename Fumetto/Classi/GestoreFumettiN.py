import json
import os.path

from Fumetto.Classi.FumettoNoleggibile import FumettoNoleggiabile


class GestoreFumettiN(FumettoNoleggiabile):
    def __init__(self):
        super().__init__()

    def aggiungi_fumettoN(self, categoria, distributore, editore, collana, sotto_collana, barcodeN, prezzo, quantita):

        self.setFumettoNoleggiabile(categoria, distributore, editore, collana, sotto_collana, barcodeN, prezzo, quantita)

        fumettiN = [self.getInfoFumettoN()]
        if os.path.isfile('Fumetto/Database/FumettiNoleggiabile.json'):
            # with open('Fumetto/Database/FumettiAcquistabili.json', 'r') as f:
            #    fumettiA = json.load(f)
            # fumettiA[barcodeA] = self
            with open('Fumetto/Database/FumettiNoleggiabile.json', 'at') as f:
                json.dump(fumettiN, f)

    def getInfoFumettoN(self):
        info = self.getFumettiNoleggiabile()
        return info

    def ricercaFumettoN(self, barcodeN):
        if os.path.isfile('Fumetto/Database/FumettiNoleggiabile.json'):
            with open('Fumetto/Database/FumettiNoleggiabile.json', 'r') as f:
                fumettiN = dict(json.load(f))
                for fumettiN in fumettiN.values():
                    if fumettiN.barcodeN == barcodeN:
                        print("E' entrato qua:" + fumettiN)
                        print(fumettiN.get(barcodeN, None))
                        return fumettiN
                return ("Finita la ricerca")
        else:
            return print("File non trovato")

    def rimuoviFumettoN(self):
        if os.path.isfile('Fumetto/Database/FumettiNoleggiabile.json'):
            with open('Fumetto/Database/FumettiNoleggiabile.json', 'r') as f:
                fumettiN = dict(json.load(f))
                del fumettiN[self.barcodeN]
            with open('Fumetto/Database/FumettiNoleggiabile.json', 'w') as f:
                json.dump(fumettiN, f)
        self.rimossoFumettoN()
        del self

