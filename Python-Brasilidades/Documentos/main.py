from cpf_cnpj import Documento

exemplo_cnpj = "80100033000142"
exemplo_cpf = "43790325074"

documento_cnpj = Documento.cria_documento(exemplo_cnpj)
documento_cpf = Documento.cria_documento(exemplo_cpf)

print(documento_cnpj)
print(documento_cpf)
