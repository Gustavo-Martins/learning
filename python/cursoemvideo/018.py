# Reads angle and prints sine, cosine and tangent
from math import cos, radians, sin, tan


angle = float(input("Digite um ângulo: "))
angle_rad = radians(angle)
angle_sin = sin(angle_rad)
angle_cos = cos(angle_rad)
angle_tan = tan(angle_rad)

print(
    f"Do ângulo {angle:.2f}, o seno é {angle_sin:.2f}, o cosseno {angle_cos:.2f} e a tangente é {angle_tan:.2f}."
)
