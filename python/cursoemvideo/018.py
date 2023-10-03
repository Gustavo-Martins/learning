# Reads angle and prints sine, cosine and tangent
from math import cos, radians, sin, tan


angle = float(input("Digite um ângulo: "))
angle_rad = radians(angle)
angle_sin = sin(angle_rad)
angle_cos = cos(angle_rad)
angle_tan = tan(angle_rad)

print(
    "Do ângulo {:.2f}, o seno é {:.2f}, o cosseno {:.2f} e a tangente é {:.2f}.".format(
        angle, angle_sin, angle_cos, angle_tan
    )
)
