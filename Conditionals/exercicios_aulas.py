# ==================== Função de verificação de palpite ====================
def get_guess():
    guess = int(input("Enter a guess: "))
    return guess


def main():
    guess = get_guess()
    if guess == 50:
        print("Correct")
    else:
        print("Wrong")


main()


# ==================== Função de saudação com verificação de entrada ====================
def greet(user_input):
    if "hello" in user_input:
        return "hello, there"
    else:
        return "I'm not sure what you mean"


greeting = greet("hello, computer")
print(greeting + " Carter")


# ==================== Variável global e interação com função ====================
emoticon = "v.v"


def main():
    global emoticon
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, hi")


def say(phrase):
    print(phrase + " " + emoticon)


main()

# ==================== Exemplo condicional: Comparando dois números ====================
x = int(input("What's x? "))
y = int(input("What's y? "))

# Comparação básica
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x and y are equal")

# Verificação de igualdade usando operadores lógicos
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# ==================== Sistema de avaliação de notas ====================
score = int(input("Score: "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# ==================== Verifica se o número é par ou ímpar ====================
x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")


# ==================== Exemplo de função para verificar se o número é par ====================
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0


main()

# ==================== Exemplo de condições com match e case ====================
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
