import math

def questao1():
    numbers = []
    for x in range(1,5000001):
        if x % 2 == 0 and x % 49 == 0 and x % 37 == 0: #verificando se o resto das divisões é zero, ou seja, se é múltiplo
            numbers.append(x)
        else:
            continue
    print("Questão 1) ""São exatamente >"+ str(len(numbers)) +
          "< números que atendem às 3 condições dentro do intervalo")

def questao2():
    vector_X = []
    for i in range(10):
        if i % 2 == 0: #separando os pares identificando quem tem resto zero na divisão com 2
            factorial = 1 #menor fatorial é sempre 1
            n = i #criação de um contador (regressivo)
            while n > 0:
                factorial = factorial * n #multiplicação do número pelo número "anterior"
                n -= 1
                #também poderia ser calculado através do math.factorial(i), mas no intuito de demonstar o
                #racioncínio lógico e domínio das ferramentas, deixei o calculo através do while

            evennumber = (3 ** i) + 7 * factorial
            vector_X.append(evennumber)
        else:
            ln = math.log(i)
            oddnumber = (2 ** i) + 4 * ln
            vector_X.append(oddnumber)

    larg = max(vector_X)
    larg_index = vector_X.index(larg) #usando max() e index() para identificar o maior número e seu índice na lista
                                    # como o fatorial, o maior poderia facilmente ser encontrado utilizando um while
    print("Questão 2)")
    print("O maior elemento desse vetor está na posição >"+ str(larg_index) + "<, contando de 0 a 9.")

    mean = sum(vector_X)/len(vector_X) #encontrando a média através da divisão da soma dos valores pelo tamanho da lista
    mean2dec = "{:.2f}".format(mean)
    print("A média dos elementos contidos nesse vetor é: >"+ str(mean2dec) + "<")

def questao3():
    print("Informe abaixo os nomes e notas de cada aluno, um de cada vez, no formato 'PrimeiroNome espaço Nota'")
    print("Exemplo: Felipe 9")
    grades = {}
    while len(grades) < 5: #loop para entrada de 5 alunos/notas
        try:
            student = input("Aluno(a) e nota:").split()
            grades.update({student[0]:int(student[1])}) #separacao do nome e nota, para add no dicionario
        except:
            print("Erro. Favor inserir no formato PrimeiroNome espaço Nota") #correção de possível erro
            continue

    maxkey = max(grades, key=grades.get)
    maxvalue = max(grades.values())
    print("O aluno de maior nota foi o(a) >"+str(maxkey)+"< com uma nota: "+str(maxvalue))







