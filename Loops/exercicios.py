# ==================== Monitoramento de Umidade ====================
from soil import sample


def main():
    # Coleta inicial da umidade
    moisture = sample()
    days = 0  # Inicializa os dias
    print(f"Dia {days}: Umidade é {moisture}%")

    # Verifica a umidade diariamente e rega quando necessário
    while moisture > 20:
        days += 1
        moisture = sample()
        print(f"Dia {days}: Umidade é {moisture}%")

    print("Hora de regar!")


main()

# ==================== Manipulação de Resultados ====================
results = [
    "Mario",
    "Luigi",
    "Princess Peach",
    "Yoshi",
    "Koopa Troopa",
    "Toad",
    "Bowser",
    "Donkey Kong Jr",
]

# Modificação da lista
to_add = ["Princess Peach", "Yoshi", "Koopa Troopa", "Toad"]
results.extend(to_add)  # Adiciona personagens

# Adiciona lista aninhada e corrige/remove duplicatas
nested_characters = ["Bowser", "Donkey Kong Jr"]
results.remove("Bowser")  # Remove Bowser e adiciona no início
results.insert(0, "Bowser")
results.extend(nested_characters)

# Inverte a lista
results.reverse()
print(results)


# ==================== Cartas de Convite ====================
def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    Prezado(a) {receiver},

    Você está cordialmente convidado(a) para um baile no
    Castelo da Peach hoje à noite, às 19:00.

    Atenciosamente,
    {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """


def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi", "Bowser"]
    for name in names:
        print(write_letter(name, "Princess Peach"))


main()


# ==================== Relatório da Nave Espacial ====================
def create_report(spacecraft):
    return f"""
    ======== RELATÓRIO ========

    Nome: {spacecraft.get("name", "desconhecido")}
    Distância: {spacecraft.get("distance", "desconhecido")} AU
    Órbita: {spacecraft.get("orbit", "desconhecido")}

    ========================
    """


def main():
    spacecraft = {"name": "Telescópio Espacial James Webb"}
    spacecraft.update({"distance": 0.01, "orbit": "Sol"})
    print(create_report(spacecraft))


main()

# ==================== Distâncias da Terra ====================
distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44,
}


def main():
    # Imprime as distâncias das naves espaciais em relação à Terra
    for name, distance in distances.items():
        print(f"{name} está a {distance} AU da Terra")

    # Converte as distâncias para metros
    for distance in distances.values():
        print(f"{distance} AU são {convert_to_meters(distance)} metros")


def convert_to_meters(au):
    AU_TO_METERS = 149_597_870_700  # 1 AU em metros
    return au * AU_TO_METERS


main()
