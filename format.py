# calculando tempo e velocidade.

def calcular_tempo_viagem(distancia, velocidade_media):
    tempo = distancia / velocidade_media
    return tempo


# Exemplo de uso de Balneario a Gramado
distancia = 508  # em quilômetros
velocidade_media = 120  # em quilômetros por hora

tempo_viagem = calcular_tempo_viagem(distancia, velocidade_media)
print(f"O tempo estimado de viagem é de {tempo_viagem:.2f} horas.")
