import re
from base.util.BaseUtil import BaseUtil

class ChangePasswordService:
    def __init__(self):
        pass

    """
    As minimum requirements for user passwords, the following should be considered:
    Minimum length of 8 characters;
    Presence of at least 3 of the 4 character classes below:
        uppercase characters;
        lowercase characters;
        numbers;
        special characters;
        Absence of strings (eg: 1234) or consecutive identical characters (yyyy);
        Absence of any username identifier, such as: John Silva - user: john.silva - password cannot contain "john" or "silva".
    """
    def validatePassword(self, login: str, senha: str):
        if len(senha) >= 8:
            letterUppercase = "[A-Z]"
            letterLowercase = "[a-z]"
            digit = "[0-9]"
            special = "[!@#$%&*()_+=|<>?{}\\[\\]~-]"
    
            hasLetterUppercase = re.search(letterUppercase, senha)
            hasLetterLowercase = re.search(letterLowercase, senha)
            hasDigit = re.search(digit, senha)
            hasSpecial = re.search(special, senha)
                        
            U: bool = hasLetterUppercase!=None
            L: bool = hasLetterLowercase!=None
            D: bool = hasDigit!=None
            S: bool = hasSpecial!=None
            
            hasChars: bool = (U and L and D) or (S and U and L) or (D and S and U) or (L and D and S)
            
            return hasChars \
                    and not(BaseUtil.containsNumericSequences(4,9, senha)) \
                    and not(BaseUtil.containsConsecutiveIdenticalCharacters(4,9, senha)) \
                    and not(senha in login)
        else:
            return False
