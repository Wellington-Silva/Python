matrícula = int(input("informe o número da matrícula do(a) aluno(a): "))
nome = str(input("Nome do(a) aluno(a): "))
sexo = str(input("Sexo: "))
n1 = float(input("Digite a primeira nota do(a) aluno(a): "))
n2 = float(input("Digite a segunda nota do(a) aluno(a): "))
n3 = float(input("Digite a terceira nota do(a) aluno(a): "))
faltas = int(input("Informe o número de faltas: "))
média = (n1 + n2 + n3)/3 
print("A média de", nome, "é: ", média, "e possui", faltas, "faltas.")
