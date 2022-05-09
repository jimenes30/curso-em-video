# Pintando parede
l = float(input('Largura da parede (em metros): \n'))
a = float(input('Altura da parede (em metros): \n'))
print('Sua parede tem dimensão de {} x {} e sua área é de {}m².\n'
      'Para pintar essa parede, você precisará de {}l de tinta.'.format(l, a, l * a, (l * a) / 2))
# 2m² --> 1l de tinta