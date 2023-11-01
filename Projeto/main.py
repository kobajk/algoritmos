import math as m
import matplotlib.pyplot as plt

def dil(a,L,T):
  d = a * L * T
  return d
matm = 0
matp = 0


print('---------------------------------------------------------------------------------------'
      '\n Bem-vindo ao programa especializado em TERMODINÂMICA: DILATAÇÃO TÉRMICA DE CORPOS')

print('\n Por favor, escolha qual método você quer utilizar nosso programa: '
      '\n (1) Calcular a expansão térmica de um objeto.'
      '\n (2) Definir material a partir de uma necessidade de temperatura específica.')
met = int(input())
while met != 1 and met != 2:
  print(' Opção inválida: Escolha uma das alternativas do menu.')
  print('\n Por favor, escolha qual método você quer utilizar nosso programa: '
      '\n (1) Calcular a expansão térmica de um objeto.'
      '\n (2) Definir material a partir de uma necessidade de temperatura específica.')
  met = int(input())

if met == 1:
  print(' Você escolheu a opção de calcular a expansão térmica de um objeto!')
  print('\n Qual grupo de materiais seu objeto pertence? '
      '\n (1) Metais'
      '\n (2) Plásticos'
      '\n (3) Outros')
  tmat = int(input())
  while tmat != 1 and tmat != 2:
    print(' Opção inválida: Escolha uma das alternativas do menu.')
    print('\n Qual grupo de materiais seu objeto pertence? '
        '\n (1) Metais'
        '\n (2) Plásticos'
        '\n (3) Outros')
    tmat = int(input())

  if tmat == 1:
    print(' Você escolheu a classe dos metais! ')
    print(' Qual plástico o objeto é feito? '
          '\n (1) Alumínio'
          '\n (2) Cobre'
          '\n (3) Ouro'
          '\n (4) Prata'
          '\n (5) Titânio'
          '\n (6) Outro')
    matp = int(input( ))
    while matp < 1 or matp > 6:
      print(' Opção inválida: Escolha uma das alternativas do menu.')
      print(' Qual plástico o objeto é feito? '
            '\n (1) Alumínio'
            '\n (2) Cobre'
            '\n (3) Ouro'
            '\n (4) Prata'
            '\n (5) Titânio'
            '\n (6) Outro')
      matp = int(input( ))

    if matp == 1:
      a = 23.6 * 10**-6
    elif matp == 2:
      a = 17.6 * 10**-6
    elif matp == 3:
      a = 14.2 * 10**-6
    elif matp == 4:
      a = 19.8 * 10**-6
    elif matp == 5:
      a = 8.64 * 10**-6
    else:
      a = float(input(' Qual o coeficiente de dilatação térmica linear do material utlizado? (°C))'))
      while a <= 0:
        print(' Valor inválido: Menor ou igual a zero!')
        a = float(input(' Qual o coeficiente de dilatação térmica linear do material utlizado? (°C))'))
      tesp = float(input(' Qual a temperatura máxima que o material especificado se mantém sólido? (°C))'))
      while tesp <= 0:
        print(' Valor inválido: Menor ou igual a zero!')
        tesp = float(input(' Qual a temperatura máxima que o material especificado se mantém sólido? (°C))'))

  elif tmat == 2:
    print(' Você escolheu a classe dos plásticos! ')
    print(' Qual plástico o objeto é feito? '
          '\n (1) ABS'
          '\n (2) PP'
          '\n (3) PA'
          '\n (4) PS'
          '\n (5) PC'
          '\n (6) Outro')
    matm = int(input( ))
    while matm < 1 or matm > 6:
      print(' Opção inválida: Escolha uma das alternativas do menu.')
      print(' Qual plástico o objeto é feito? '
            '\n (1) ABS'
            '\n (2) PP'
            '\n (3) PA'
            '\n (4) PS'
            '\n (5) PC'
            '\n (6) Outro')
      matm = int(input( ))
    if matm == 1:
      a = 90 * 10**-6
    elif matm == 2:
      a = 140 * 10**-6
    elif matm == 3:
      a = 110 * 10**-6
    elif matm == 4:
      a = 65 * 10**-6
    elif matm == 5:
      a = 67.5 * 10**-6
    else:
      a = float(input(' Qual o coeficiente de dilatação térmica linear do material utlizado? (°C))'))
      while a <= 0:
        print(' Valor inválido: Menor ou igual a zero!')
        a = float(input(' Qual o coeficiente de dilatação térmica linear do material utlizado? (°C))'))
      tesp = float(input(' Qual a temperatura máxima que o material especificado se mantém sólido? (°C))'))
      while tesp <= 0:
        print(' Valor inválido: Menor ou igual a zero!')
        tesp = float(input(' Qual a temperatura máxima que o material especificado se mantém sólido? (°C))'))


  else:
    print(' Você escolheu a classe dos materiais personalizados! ')
    a = float(input(' Qual o coeficiente de dilatação térmica linear do material utlizado? (°C))'))
    while a <= 0:
        print(' Valor inválido: Menor ou igual a zero!')
        a = float(input(' Qual o coeficiente de dilatação térmica linear do material utlizado? (°C))'))

  print('\n Material do objeto definido com sucesso! ')

  print(' Qual o formato do objeto? '
        '\n (1) Polígono'
        '\n (2) Cilindrico')
  format = int(input())
  while format != 1 and format != 2:
    print(' Opção inválida: Escolha uma das alternativas do menu.')
    print(' Qual o formato do objeto? '
          '\n (1) Polígono'
          '\n (2) Cilindrico')
    format = int(input())

  if format == 1:
    print('\n Quais são as dimensões desse polígono? Em metros: ')
    # desenho do polígono
    fig, ax = plt.subplots()
    ax.plot([1, 2, 2, 1, 1], [1, 1, 2, 2, 1])
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('Comprimento (x)')
    plt.ylabel('Largura (y)')

    plt.show()

    compx = float(input('\n Qual o comprimento(x) do polígono? Em metros: '))
    largy = float(input('\n Qual a largura(y) do polígono? Em metros: '))
    altz = float(input('\n Qual a altura/espessura (z) do polígono? Em metros: '))

    diam = 1

  else:
    print('\n Quais são as dimensões desse cilindro? Em metros: ')
    # desenho do cilindro
    circle1 = plt.Circle((0.5, 0.5), 0.2, fill = False)
    circle2 = plt.Circle((0.5, 1.5), 0.2, fill = False)
    fig, ax = plt.subplots()
    ax.add_artist(circle1)
    ax.add_artist(circle2)
    plt.plot([0.3, 0.3], [0.5, 1.5], 'k-')
    plt.plot([0.7, 0.7], [0.5, 1.5], 'k-')
    plt.xlim(0, 1)
    plt.ylim(0, 2)
    plt.xticks([])
    plt.yticks([])
    plt.xlabel('Diâmetro (Ø)')
    plt.ylabel('Altura (z)')

    plt.show()

    diam = float(input('\n Qual o diâmetro do cilindro? Em metros: '))
    altz = float(input('\n Qual a altura(z) do cilindro? Em metros: '))

  print('\n Obrigado por fornecer as dimensões do seu objeto! ')

  print('\n Agora é a ultima etapa! O range de temperatura que o objeto será exposto. ')

  t1 = float(input('\n Qual a temperatura inicial que o objeto será exposto? °C: '))
  while (matp == 1 and t1 >= 100) or (matp == 2 and t1 >= 160) or (matp == 3 and t1 >= 160) or (matp == 4 and t1 >= 100) or (matp == 5 and t1 >= 150) or ((matp == 6 or matm == 6) and t1 >= tesp) or (matm == 1 and t1 >= 660) or (matm == 2 and t1 >= 1084) or (matm == 3 and t1 >= 1064) or (matm == 4 and t1 >= 961.78) or (matm == 5 and t1 >= 1668):
    print(' Temperatura inválida para o material especificado! A temperatura deve manter o material sólido')
    t1 = float(input('\n Qual a temperatura inicial que o objeto será exposto? °C: '))

  t2 = float(input(' Qual a temperatura final que o objeto será exposto? °C: '))
  while (matp == 1 and t2 >= 100) or (matp == 2 and t2 >= 160) or (matp == 3 and t2 >= 160) or (matp == 4 and t2 >= 100) or (matp == 5 and t2 >= 150) or ((matp == 6 or matm == 6) and t2 >= tesp) or (matm == 1 and t2 >= 660) or (matm == 2 and t2 >= 1084) or (matm == 3 and t2 >= 1064) or (matm == 4 and t2 >= 961.78) or (matm == 5 and t2 >= 1668):
    print(' Temperatura inválida para o material especificado! A temperatura deve manter o material sólido')
    t2 = float(input(' Qual a temperatura final que o objeto será exposto? °C: '))

  dildiam = dil(a,t2-t1,diam)
  dilalt = dil(a,t2-t1,altz)
  dilcomp = dil(a,t2-t1,compx)
  dillarg = dil(a,t2-t1,largy)

  if format == 1:
    print('\n\n\n A dilatação do seu objeto será: '
          '\n No eixo X: %.4f m (comprimento final de %.4f m)'
          '\n No eixo Y: %.4f m (comprimento final de %.4f m)'
          '\n No eixo Z: %.4f m (comprimento final de %.4f m)' %(dilcomp , dilcomp+compx, dillarg , dillarg+largy, dilalt , dilalt+altz))
  else:
    print('\n\n\n A dilatação do seu objeto será: '
          '\n No diâmetro: %.4f m (comprimento final de %.4f m)'
          '\n No eixo Z: %.4f m (comprimento final de %.4f m)' %(dildiam , dildiam+diam, dilalt , dilalt+altz))

else:
  print(' Você escolheu a opção de definir o material a partir de uma temperatura!')


