import requests

class BuscaEndereco:
    
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP Inválido")
            
    def __str__(self):
        return self.format_cep()
    
    def cep_e_valido(self, cep):
        if len(cep)==8:
            return True
        else:
            return False
    
    def format_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:]) 
    
    #diferença entre text e json: text é uma str e json é um dicionário, então, é mais fácil de acessar os dados sendo um dict
    def acessa_via_cep(self):
        url = f'https://viacep.com.br/ws/{self.cep}/json'
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
            
        )         