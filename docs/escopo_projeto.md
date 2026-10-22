# MESAFARTAI — Escopo do Projeto

## 1. Problema de negócio

O desperdício de alimentos acontece quando supermercados, restaurantes, feirantes e produtores descartam alimentos próprios para consumo. Ao mesmo tempo, ONGs, abrigos e cozinhas comunitárias enfrentam dificuldades para conseguir alimentos para pessoas em situação de vulnerabilidade.

O MESAFARTAI busca facilitar a comunicação entre doadores e ONGs por meio de uma aplicação inteligente que recebe mensagens, identifica informações sobre doações e ajuda a encontrar instituições próximas para receber os alimentos.

O projeto está alinhado à ODS 2 da ONU, que busca acabar com a fome, alcançar a segurança alimentar e promover a agricultura sustentável.

## 2. Público-alvo

### Doadores

Supermercados, restaurantes, feirantes, produtores e outros estabelecimentos que possuem alimentos disponíveis para doação.

### ONGs

Organizações não governamentais, abrigos e cozinhas comunitárias que precisam receber alimentos para atender pessoas em situação de vulnerabilidade.

## 3. Intenções tratadas pelo sistema

O sistema deverá reconhecer quatro intenções principais:

- cadastrar_doacao: identificar mensagens de pessoas ou estabelecimentos que desejam doar alimentos.
- solicitar_alimentos: identificar pedidos de alimentos feitos por ONGs.
- consultar_status: identificar consultas sobre o andamento de doações e coletas.
- fora_de_escopo: identificar mensagens que não estejam relacionadas às funcionalidades do sistema.

Quando uma mensagem for ambígua ou o sistema não tiver confiança suficiente na classificação, deverá apresentar uma resposta amigável solicitando mais informações.

## 4. Dados coletados pelo chat

O chat deverá identificar e utilizar informações necessárias para o funcionamento do sistema, incluindo:

- Nome e tipo de usuário: doador ou ONG.
- Informações de contato, como telefone.
- Localização, como CEP, latitude e longitude.
- Tipo de alimento disponível ou solicitado.
- Quantidade de alimentos, em quilogramas, caixas ou unidades.
- Data ou prazo de validade dos alimentos.
- Informações sobre o status da doação e da coleta.

## 5. Tecnologias utilizadas

- Python: linguagem principal do projeto.
- Scikit-learn: classificação de intenções e algoritmos de Machine Learning.
- Regex: extração de quantidades, alimentos e prazos nas mensagens.
- SQLite3: armazenamento de usuários, doações e matches logísticos.
- KNN: identificação de ONGs próximas para direcionar as doações.

## 6. Objetivo final

Desenvolver uma solução que facilite a destinação de alimentos próprios para consumo, reduza desperdícios e aproxime doadores de organizações que combatem a fome.