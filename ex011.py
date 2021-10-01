width = float(input('Digite a largura da parede: '))
height = float(input('Digite o comprimento da parede: '))
area = width*height

if(area % 2 == 0.0):
    tinta = int(area/2)
else:
    tinta = int(area/2 + 1)

print('A parede possui {} m², portanto serão necessárias {} latas de tinta.'.format(area, tinta))