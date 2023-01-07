# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

download = float(input("Insira o tamando do arquivo que terá o download realizado, em MB: "))
velocidade = int(input("Agora insira a velocidade de download que está sendo utilizada: "))

download = download * 8
tempoDownload = download / velocidade 
tempoDownload = tempoDownload / 60

print (f"Para realizar o download do arquivo desejado levará {tempoDownload:,.2f} minutos")
