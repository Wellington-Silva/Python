nome = str(input("Nome: "))
idade = int(input("Idade: "))
cargo = str(input("Cargo: "))
#líquido = float(input("Salário Líquido: R$ ")) Só para teste
bruto = float(input("Salário Bruto: R$ "))
reajuste = bruto - (38/100)
gratificação = bruto + (20/100)
total = (reajuste + gratificação)
desconto = (total - (0.15 * total))
print("O funcionário", nome, ",de ", idade, "anos de idade, trabalha no cargo de ", cargo)
print("Recebe ", desconto, "de salário bruto")
print("O seu salário líquido é: R$ ", bruto - (0.10 * bruto))

                   
