import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO
    def mostra_strumenti(self, e):
        strumenti = self._model.get_strumenti()
        if strumenti is None:
            self._view.show_alert("Errore nel recupero strumenti")
            return
        #recupera gli strumenti dal Model e li passa alla View
        self._view.mostra_strumenti(strumenti)
        self._view.update()

    def cerca_per_tipo(self, e):
        tipo= self._view.input_tipo_strumento.value.strip()
        if tipo == "":
            self._view.show_alert("Errore! inserire un tipo di strumento")
            return
        #recupera gli strumenti per tipo dal Model e li passa alla View
        strumenti_per_tipo = self._model.cerca_strumenti_per_tipo(tipo)

        if strumenti_per_tipo is None:
            self._view.show_alert("Errore nel recupero strumenti")
            return
        self._view.mostra_strumenti_per_tipo(strumenti_per_tipo)
