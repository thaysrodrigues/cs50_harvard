# ==================== Debugging e Tratamento de Erros ====================
distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
}


def main():
    spacecraft = input("Enter a spacecraft: ")
    try:
        au = float(distances[spacecraft])
    except KeyError:
        print(f"'{spacecraft}' is not a dictionary")
        return
    except ValueError:
        print(f"Can't convert {distances[spacecraft]} to a float")
        return

    m = convert(au)
    print(f"{m} m away")
