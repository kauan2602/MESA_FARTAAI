
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

frases = [
    "quero doar alimentos",
    "tenho arroz para doar",
    "quero cadastrar uma doação",
    "precisamos de comida para o abrigo",
    "quero receber alimentos",
    "a ONG precisa de arroz",
    "quero consultar minha doação",
    "qual o status da minha doação",
    "quando vão buscar os alimentos",
    "qual é a capital do Brasil",
    "me conte uma piada",
    "como está o tempo hoje"
]

intencoes = [
    "cadastrar_doacao",
    "cadastrar_doacao",
    "cadastrar_doacao",
    "solicitar_alimentos",
    "solicitar_alimentos",
    "solicitar_alimentos",
    "consultar_status",
    "consultar_status",
    "consultar_status",
    "fora_de_escopo",
    "fora_de_escopo",
    "fora_de_escopo"
]

vetorizador = TfidfVectorizer()
X = vetorizador.fit_transform(frases)

modelo = LogisticRegression()
modelo.fit(X, intencoes)


def identificar_intencao(mensagem):
    entrada = vetorizador.transform([mensagem])
    probabilidades = modelo.predict_proba(entrada)[0]
    indice = probabilidades.argmax()
    confianca = probabilidades[indice]

    if confianca < 0.60:
        return "fallback", confianca

        return modelo.predict(entrada)[0], confianca


if __name__ == "__main__":
    while True:
        mensagem = input("Digite sua mensagem (ou 'sair'): ")

        if mensagem.lower() == "sair":
            break

        intencao, confianca = identificar_intencao(mensagem)
        print("Intenção:", intencao)
        print(f"Confiança: {confianca:.2f}")

