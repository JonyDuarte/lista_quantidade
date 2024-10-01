# lista
cidades = ["Cubatão", "João Pessoa","Recife", "Duque de Caxias", "Aracaju","Araçuaí","São João de Meriti","Belford Roxo", "Guaíba", "Contagem","Ananindeua","Mesquita", "Itaquequecetuba", "Carapicuíba", "Valparaíso", "Contagem","Perdigão","João Pessoa","Aracruz", "Araçu", "Araçuaí"]

# usuario informa o nome que deseja procurar
cidade = input("Informe o nome da cidade que deseja procurar: ")

# informa a quantidade de vezes que o termo foi achado
quantidade = cidades.count(cidade)

# exibe o resultado na tela
if cidade in cidades:
    print(f"{cidade} foi encontrado na lista {quantidade} vezes.")
else:
    print(f"{cidade} não foi encontrado")
