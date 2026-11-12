import secrets
import string


def gerar_senha(tamanho, usar_maiusculas, usar_numeros, usar_simbolos):
    caracteres = string.ascii_lowercase
    obrigatorios = [secrets.choice(string.ascii_lowercase)]

    if usar_maiusculas:
        caracteres += string.ascii_uppercase
        obrigatorios.append(secrets.choice(string.ascii_uppercase))
    if usar_numeros:
        caracteres += string.digits
        obrigatorios.append(secrets.choice(string.digits))
    if usar_simbolos:
        simbolos = "!@#$%&*?"
        caracteres += simbolos
        obrigatorios.append(secrets.choice(simbolos))

    restante = [secrets.choice(caracteres) for _ in range(tamanho - len(obrigatorios))]
    senha = obrigatorios + restante
    secrets.SystemRandom().shuffle(senha)
    return "".join(senha)


def perguntar_sim_nao(pergunta):
    return input(pergunta + " (s/n): ").strip().lower() == "s"


def main():
    print("=== Gerador de Senhas ===")
    while True:
        try:
            tamanho = int(input("Tamanho da senha (mínimo 6): "))
        except ValueError:
            print("Digite um número inteiro.\n")
            continue

        if tamanho < 6:
            print("A senha precisa ter pelo menos 6 caracteres.\n")
            continue

        maiusculas = perguntar_sim_nao("Incluir letras maiúsculas?")
        numeros = perguntar_sim_nao("Incluir números?")
        simbolos = perguntar_sim_nao("Incluir símbolos?")

        print("\nSenha gerada:", gerar_senha(tamanho, maiusculas, numeros, simbolos))

        if not perguntar_sim_nao("\nGerar outra?"):
            print("Até mais!")
            break


main()