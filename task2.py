import string

class alphabet:
    def __init__(self,lang,letters):
        self.lang=lang
        self.letters=list(set(letters))
        pass
    def print(self):
        print(self.letters)
    def letters_num(self):
        return len(self.letters)

#===============================================================
class EngAlphabet(alphabet):
    __letters_num=0
    def __init__(self,lang,letters):
        super().__init__(lang,letters)
        __letters_num=len(self.letters)
    def is_en_letter(self,letter):
        if ord(letter.upper())>=65 and ord(letter.upper()) <= 90:
            return "Это английский символ"
        else:
            return "Это не английский символ"

    def __letrers_num(self):
        pass
    @staticmethod
    def exemple(self):
        print("The quick brown fox jumps over the lazy dog")


Latin=alphabet("English","asdfgkl")
Latin.print()
print(Latin.letters_num())


Eng=EngAlphabet("English","asdfgkl")
Eng.print()
print(Eng.is_en_letter('F'))

