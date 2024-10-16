# Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.
# - calcular_volume_cilindro, que utiliza a função calcular_area_base para calcular o volume de um cilindro dado o raio e a altura.

def calcular_area_base(r):
    area_circulo = 3.14 * (r**2)
    return area_circulo


def calcular_volume_cilindro(raio, altura):
    valor_area = calcular_area_base(raio)
    volume_cilindro = valor_area * altura
    return volume_cilindro

raio_informado = int(input('digite o raio: '))
altura_informada = int(input('digite a altura: '))
resultado = calcular_volume_cilindro(raio_informado, altura_informada )
print(f'O volume do cilindro é {resultado}')