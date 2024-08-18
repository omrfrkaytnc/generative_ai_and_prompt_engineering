#GGUF ile kuantizasyon örneği

def quantize_gguf(floating_point_parameter, number_of_bits, number_of_fraction_bits):
    # GGUF ile temsil edilecek uç noktaları belirle
    max_value = 2 ** (number_of_bits - 1) - 1
    min_value = -2 ** (number_of_bits - 1)

    # Ölçekleme faktörünü hesapla
    scale = 2 ** number_of_fraction_bits

    # Ondalıklı sayıyı GGUF ile kuantize et
    quantized_value = round(floating_point_parameter * scale)

    # Kuantize edilen değeri temsil edilebilir aralığa yansıt
    quantized_value = max(min(quantized_value, max_value), min_value)

    return quantized_value

# Örnek parametre | 8 bit ile
float_num = 0.434919
num_bits = 8
num_frac_bits = 4

quantized_num = quantize_gguf(float_num, num_bits, num_frac_bits)

print(f"Orijinal Parametre Değeri: {float_num}")
print(f"Kuantize Edilmiş Değer: {quantized_num}")