from typing import List
import string

class BaseUtil:
    def __init__(self):
        pass
    
    @staticmethod
    def distinct(list1):
        list_set = set(list1)
        unique_list = (list(list_set))
        return unique_list
    
    @staticmethod
    def containsNumericSequences(min: int, max: int, stexto: str):
        lista: List[str] = []
        sValorMin: str = ""
        vnum = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        for n in range(7):
            for qtd in range(min - 1, max+1):
                sValorMin = ""
                for i in range(n, (qtd + n)+1):
                    if i <= max:
                        sValorMin += str(vnum[i])
                lista.append(sValorMin)

        lista = BaseUtil.distinct(lista)
        return stexto in lista
    
    @staticmethod
    def containsConsecutiveIdenticalCharacters(min: int, max: int, stexto: str):
        lista: List[str] = []
        sAlfaMin: str = ""

        for c in list(string.ascii_lowercase):
            for qtd in range(min, max+1):
                sAlfaMin = ""
                for i in range(1, qtd+1):
                    sAlfaMin += str(c)
                lista.append(sAlfaMin)
                lista.append(sAlfaMin.upper())

        return stexto in lista


