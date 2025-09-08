velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print(f'{'\033[31m'}MULTADO! Você excedeu o limite permitido que é de 80Km/h{'\033[m'}')
    multa = (velocidade - 80) * 7
    print(f'{'\033[31m'}Você deve pagar uma multa de{'\033[m'} {'\033[33m'}R${multa:.2f}!{'\033[m'}')
print(f'{'\033[32m'}Tenha um bom dia! Dirija com segurança!{'\033[m'}')