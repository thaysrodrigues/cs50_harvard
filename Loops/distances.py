# ==================== Conversão de Distâncias Astronômicas para Metros ====================

distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pionner 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44,
}

# def main():
#     for name in distances.keys():
#         print(f"{name} is {distances[name]} AU from Earth")


def main():
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} m")


def convert(au):
    return au * 149597870700


main()
