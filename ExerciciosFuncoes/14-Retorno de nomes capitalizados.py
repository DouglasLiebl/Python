def nomes():
    listanomes = []
    x = 0
    while x != "0":
        x = input("Insira um nome: \"0\" para encerrar]: ")
        if x == "0":
            break
        else:
            listanomes.append(x)
    listanomes.sort(key = len)
    return print(listanomes[0].capitalize())

nomes()