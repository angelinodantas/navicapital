import math

def questao1():
    numbers = []
    for x in range(1,5000001):
        if x % 2 == 0 and x % 49 == 0 and x % 37 == 0: #verificando se o resto das divisoes e zero, ou seja, se e multiplo
            numbers.append(x)
        else:
            continue
    print("Questao 1)")
    print("Sao exatamente >"+ str(len(numbers)) +
          "< numeros que atendem as 3 condicoes dentro do intervalo")

def questao2():
    vector_X = []
    for i in range(10):
        if i % 2 == 0: #separando os pares identificando quem tem resto zero na divisao com 2
            factorial = 1 #menor fatorial e sempre 1
            n = i #criacao de um contador (regressivo)
            while n > 0:
                factorial = factorial * n #multiplicacao do numero pelo numero "anterior"
                n -= 1
                #tambem poderia ser calculado atraves do math.factorial(i), mas no intuito de demonstar o
                #racioncinio logico e dominio das ferramentas, deixei o calculo atraves do while

            evennumber = (3 ** i) + 7 * factorial
            vector_X.append(evennumber)
        else:
            ln = math.log(i)
            oddnumber = (2 ** i) + 4 * ln
            vector_X.append(oddnumber)

    larg = max(vector_X)
    larg_index = vector_X.index(larg) #usando max() e index() para identificar o maior numero e seu indice na lista
                                    # como o fatorial, o maior poderia facilmente ser encontrado utilizando um while
    print("Questao 2)")
    print("O maior elemento desse vetor esta na posicao >"+ str(larg_index) + "<, contando de 0 a 9.")

    mean = sum(vector_X)/len(vector_X) #encontrando a media atraves da divisao da soma dos valores pelo tamanho da lista
    mean2dec = "{:.2f}".format(mean)
    print("A media dos elementos contidos nesse vetor e: >"+ str(mean2dec) + "<")

def questao3():
    print("Questao 3)")
    print("Informe abaixo os nomes e notas de cada aluno, um de cada vez, no formato 'PrimeiroNome espaco Nota'")
    print("Exemplo: Felipe 9")
    grades = {}
    while len(grades) < 5: #loop para entrada de 5 alunos/notas
        try:
            student = input("Aluno(a) e nota:").split() #para Python 2.7 utilizar raw.input()
            grades.update({student[0]:int(student[1])}) #separacao do nome e nota, para add no dicionario
        except:
            print("Erro. Favor inserir no formato PrimeiroNome espaco Nota") #correcao de possivel erro
            continue

    maxkey = max(grades, key=grades.get)
    maxvalue = max(grades.values())
    print("O aluno de maior nota foi o(a) >"+str(maxkey)+"< com uma nota: "+str(maxvalue))

def main():
    print()
    questao1()
    questao2()
    questao3()

if __name__ == "__main__":
    main()






