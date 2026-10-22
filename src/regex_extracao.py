
import re


def extrair_dados(mensagem):
    dados = {}

    quantidade = re.search(
        r'(\d+(?:[.,]\d+)?)\s*(kg|quilos|caixas|unidades)',
        mensagem.lower()
    )

    if quantidade:
        dados["quantidade"] = float(
            quantidade.group(1).replace(",", ".")
        )
        dados["unidade"] = quantidade.group(2)

    alimentos = [
        "arroz", "feijão", "feijao", "leite",
        "pão", "pao", "macarrão", "macarrao",
        "carne", "frutas", "legumes"
    ]

    for alimento in alimentos:
        if alimento in mensagem.lower():
            dados["alimento"] = alimento
            break

    validade = re.search(
        r'\b(hoje|amanhã|amanha)\b',
        mensagem.lower()
    )

    if validade:
        dados["validade"] = validade.group(1)

    horario = re.search(
        r'\b(\d{1,2})h(?:(\d{2}))?\b',
        mensagem.lower()
    )

    if horario:
        dados["horario"] = horario.group(0)

    return dados


if __name__ == "__main__":
    mensagem = input("Digite a mensagem da doação: ")
    dados = extrair_dados(mensagem)
    print("Dados extraídos:", dados)
