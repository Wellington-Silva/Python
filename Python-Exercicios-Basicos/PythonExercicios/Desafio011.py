larg = float(input('Largura da parede:'))
alt = float(input('Altura da parede:'))
área = larg * alt
tinta = área / 2
print('Sua parede tem dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, área))
print('Para pintar essa parede, você precisará de {}L de tinta.'.format(tinta))

