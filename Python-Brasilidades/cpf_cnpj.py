from validate_docbr import CPF
from validate_docbr import CNPJ

class CpfCnpj:
    
    def __init__(self, documento, tipo_documento):
        
        self.tipo_documento = tipo_documento
        documento = str(documento)
        if tipo_documento == "cpf":
            if self.cpf_eh_valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF Inválido")
        elif tipo_documento == "cnpj":
            if self.cnpj_eh_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ Inválido")
        else:
            raise ValueError("Documento Inválido!!")
               
    
    def  __str__(self):
        return self.format_cpf()
    
    def cnpj_eh_valido(self,cnpj):
        if(len(cnpj)==14):
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("Quantidade de dígitos inválida!!") 
        
    def cpf_eh_valido(self, documento):
        if(len(documento)==11):
            validador = CPF()
            return validador.validate(documento)
        else:
            raise ValueError("Quantidade de digitos inválida!!")
        
    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
        