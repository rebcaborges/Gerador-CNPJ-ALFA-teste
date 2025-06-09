import random
import string

# Conversão de caractere alfanumérico para valor numérico (A=10, B=11, ..., Z=35)
def char_to_int(c):
    if c.isdigit():
        return int(c)
    return ord(c.upper()) - 55  # A=65 → 10, ..., Z=90 → 35

# Geração aleatória de uma base alfanumérica de 8 caracteres (números + letras)
def generate_alphanumeric_base():
    chars = string.digits + string.ascii_uppercase
    return ''.join(random.choices(chars, k=8))

# Cálculo dos dígitos verificadores do CNPJ, adaptado para letras
def calculate_dv(base, filial='0001'):
    # Peso padrão para os 12 primeiros dígitos (base + filial)
    weights_first = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    weights_second = [6] + weights_first

    # Concatena base + filial (ambos como string)
    full = base + filial

    # Converte todos os caracteres para inteiros (letras são convertidas)
    values = [char_to_int(c) for c in full]

    # Primeiro DV
    sum1 = sum([a * b for a, b in zip(values, weights_first)])
    dv1 = 11 - (sum1 % 11)
    dv1 = dv1 if dv1 < 10 else 0

    # Segundo DV
    values.append(dv1)
    sum2 = sum([a * b for a, b in zip(values, weights_second)])
    dv2 = 11 - (sum2 % 11)
    dv2 = dv2 if dv2 < 10 else 0

    return f'{dv1}{dv2}'

# Formata CNPJ com pontuação padrão
def format_cnpj(base, filial, dv):
    return f'{base[:2]}.{base[2:5]}.{base[5:8]}/{filial}-{dv}'

# Função principal para gerar CNPJ alfanumérico válido
def generate_alphanumeric_cnpj():
    base = generate_alphanumeric_base()
    filial = '0001'
    dv = calculate_dv(base, filial)
    return format_cnpj(base, filial, dv)

# Gerar 10 CNPJs de teste
for i in range(10):
    print(generate_alphanumeric_cnpj())
