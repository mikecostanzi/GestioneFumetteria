import json
import os

from Fumetto.FumettoNoleggibile import FumettoNoleggiabile

class GestoreFumettiN(FumettoNoleggiabile):

    def __int__(self,):
        super().__init__()


    def creaFumettoN(self, Fumetto, barcodeN, prezzo):
        self.creaFumettoN(Fumetto, barcodeN, prezzo)

        fumettiN = []
        if os.path.isfile('DatabaseFumettiNoleggiabili/FumettiNoleggiabili.json'):
            with open('DatabaseFumettiNoleggiabili/FumettiNoleggiabili.json', 'r') as f:
                fumettiN = json.load(f)
        fumettiN[barcodeN] = self
        print(fumettiN)
        with open('DatabaseFumettiNoleggiabili/FumettiNoleggiabili.json', 'w') as f:
            json.dump(fumettiN,f)

    def getInfoFumettoN(self):
        info = self.getFumettoNoleggibile()
        return info

    def ricercaFumettoN(self, barcodeN):
        if os.path.isfile('DatabaseFumettiNoleggiabili/FumettiNoleggiabili.json'):
            with open('DatabaseFumettiNoleggiabili/FumettiNoleggiabili.json', 'r') as f:
                fumettiN = dict(json.load(f))
                for fumettiN in fumettiN.values():
                    if fumettiN.barcodeN == barcodeN:
                        print("E' entrato qua:"+ fumettiN)
                        print(fumettiN.get(barcodeN,None))
                        return fumettiN
                return ("Finita la ricerca")
        else:
            return print("File non trovato")


    def rimuoviFumettoN(self):
        if os.path.isfile('DatabaseFumettiNoleggiabili/FumettiNoleggiabili.json'):
            with open('DatabaseFumettiNoleggiabili/FumettiNoleggiabili.json','r') as f:
                fumettiN = dict(json.load(f))
                del fumettiN[self.barcodeN]
            with open('DatabaseFumettiNoleggiabili/FumettiNoleggiabili.json', 'w') as f:
                json.dump(fumettiN,f)
        self.rimossoFumettoN()
        del self

