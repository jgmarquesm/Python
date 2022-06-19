import os

try:
    from random import randint as ri
except ImportError:
    os.system("pip install random")
    from random import randint as ri


def random_quote():
    dict_of_quotes = {
        0: ["A leitura engrandece a alma.", "Voltaire"],
        1: ["A leitura é para o intelecto o que o exercício é para o corpo.", " Joseph Addison"],
        2: ["Leitura, antes de mais nada é estímulo, é exemplo.", "Ruth Rocha"],
        3: ["A paixão da leitura é a mais inocente, aprazível e a menos dispendiosa.", "Marquês de Maricá"],
        4: ["A leitura do mundo precede a leitura da palavra.", "Paulo Freire"],
        5: ["É preciso que a leitura seja um ato de amor.", "Paulo Freire"],
        6: ["A leitura é, provavelmente, uma outra maneira de estar em um lugar.", "José Saramago"],
        7: ["Alguma frase legal.", "João Gabriel"],
        8: ["Os verdadeiros analfabetos são os que aprenderam a ler e não leem.", "Mário Quintana"],
        9: ["Sempre imaginei que o paraíso fosse uma espécie de livraria.", "Jorge Luis Borges"],
        10: ["Ler quer dizer pensar com uma cabeça alheia, em lugar da própria.", "Arthur Schopenhauer"],
        11: ["A leitura é uma porta aberta para um mundo de descobertas sem fim.", "Sandro Costa"],
        12: ["A Leitura abre as janelas do entendimento e desperta do sono a Sabedoria.", "Rafael de Oliveira"],
        13: ["A leitura amplia o campo do pensamento.", "Allann Xavier"],
        14: ["Quem gosta de ler não morre só.", "Ariano Suassuna"],
        15: ["Sem a literatura, a vida é um inferno.", "Charles Bukowski"],
        16: ["Tenha cuidado com a tristeza. É um vício.", "Gustave Flaubert"],
        17: ["Não há mentira pior do que uma verdade mal compreendida por aqueles que a ouvem.", "Henry James"],
        18: ["É permissível a cada um de nós morrer pela sua fé, mas não matar por ela.", "Hermann Hesse"],
        19: ["A verdadeira função do homem é viver, não existir.", "Jack London"],
        20: ["Viver é negócio muito perigoso.", "João Guimarães Rosa"],
        21: ["Qual é a tarefa mais difícil do mundo? Pensar.", "Ralph Waldo Emerson"],
        22: ["O que leva uma criança a ler é o exemplo.", "Ana Maria Machado"],
        23: ["Nunca tive desgosto algum que uma hora de leitura não dissipasse.", "Barão de Montesquieu"],
        24: ["Nem todo aprendizado precisa de leitura, mas toda leitura gera um aprendizado.", "Flávia Savoia"],
        25: ["A leitura faz de vagos pensamentos, solenes informações", "Weslley Hiemard"],
        26: ["O bom da leitura é conversar com a fala do escritor.", "Rosa Berg"],
        27: ["A leitura é importante para aprimorar nossas próprias ideias.", "Iris Borges"],
        28: ["A leitura é a melhor maneira de poder viajar.", "Alexandre Boarro"],
        29: ["O importante é motivar a criança para a leitura, para a aventura de ler.", "Ziraldo"],
        30: ["A leitura faz florescer novos conceitos, novas ideias e novas atitudes.", "Antonio Costta"],
        31: ["A leitura é o passaporte para a sabedoria.", "Zacarias Menezes"]
    }

    n = ri(0, len(dict_of_quotes)-1)
    quote_of_the_day = dict_of_quotes[n]
    return quote_of_the_day
