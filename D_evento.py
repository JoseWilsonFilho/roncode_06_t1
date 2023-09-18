def tempo_dura(x):
    horas = x // 3600
    minutos = x % 3600 // 60
    segundos = x - (horas*3600 + minutos*60)
    return horas, minutos, segundos

x = int(input())
h, m, s = tempo_dura(x)
print(f'{h}:{m}:{s}')
