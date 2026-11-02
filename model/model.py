from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        # TODO
        cnx = get_connection()

        if cnx is None:
            return None

        query="SELECT * FROM strumento"
        cursor = cnx.cursor()
        cursor.execute(query)

        strumenti=[]
        for riga in cursor:
            strumento=Strumento(*riga) #crea un oggetto per ogni riga restituita dal database
            strumenti.append(strumento)

        cursor.close()
        cnx.close()
        return strumenti


    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO
        cnx = get_connection()
        if cnx is None:
            return None

        query="SELECT * FROM strumento WHERE tipo = %s" #%s parametro che verrà sostituito con il tipo scelto dall'utente
        cursor = cnx.cursor()
        cursor.execute(query, (tipo,))

        strumenti_per_tipo=[]
        for riga in cursor:
            strumenti_per_tipo.append(Strumento(*riga))

        cursor.close()
        cnx.close()
        return strumenti_per_tipo
