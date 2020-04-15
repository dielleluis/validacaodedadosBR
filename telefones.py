import re

class Telefones:

    def __init__(self, telefone):
        if self.valida_tel(telefone):
            self.numero = telefone
        
        else:
            raise ValueError('Número incorreto!')

    def __str__(self):
        return self.format_num()


    def valida_tel(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True

        else:
            return False


    def format_num(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.numero)
        numero_format = '+{}({}){}-{}'.format(
            resposta.group(1),
            resposta.group(2),
            resposta.group(3),
            resposta.group(4)
        )
        return numero_format