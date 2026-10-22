
from nlu import identificar_intencao
from regex_extracao import extrair_dados


def responder(mensagem):
    intencao, confianca = identificar_intencao(mensagem)

    print(f"\nIntenção: {intencao}")
    print(f"Confiança: {confianca:.2f}")

    if intencao == "fallback":
        return "Desculpe, não entendi. Você quer doar alimentos, solicitar alimentos ou consultar um status?"

    if intencao == "cadastrar_doacao":
        dados = extrair_dados(mensagem)
        return f"Entendi que você quer cadastrar uma doação. Dados extraídos: {dados}"

    if intencao == "solicitar_alimentos":
        dados = extrair_dados(mensagem)
        return f"Entendi que você precisa de alimentos. Dados identificados: {dados}"

    if intencao == "consultar_status":
        return "Vamos consultar o status. Qual é o número da sua doação ou solicitação?"

    return "Como posso ajudar com doações de alimentos?"


if __name__ == "__main__":
    print("MESAFARTAI - Chatbot contra a fome")
    print("Digite 'sair' para encerrar.\n")

    while True:
        mensagem = input("Você: ")

        if mensagem.lower() == "sair":
            print("Chatbot: Até logo!")
            break

        print("Chatbot:", responder(mensagem))
