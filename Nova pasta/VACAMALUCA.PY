import random
import textwrap

# Lista de curiosidades perturbadoras sobre guerra, armas, tortura e experimentos científicos em humanos
curiosidades_assustadoras = [
    "O 'Experimento de Harlow', realizado nos anos 50, envolveu a separação de filhotes de macacos de suas mães para estudar os efeitos da privação emocional. O trauma resultante foi devastador e causou problemas psicológicos irreversíveis.",
    "Durante a Segunda Guerra Mundial, os médicos nazistas realizaram experimentos horríveis em prisioneiros de guerra, incluindo testes de congelamento, infecção de doenças e cirurgias sem anestesia.",
    "O Projeto MKUltra, realizado pela CIA nos anos 50 e 60, envolveu experimentos com drogas alucinógenas em civis e prisioneiros sem seu consentimento, com o objetivo de explorar o controle mental.",
    "Os cientistas japoneses da Unidade 731, durante a Segunda Guerra Mundial, realizaram experimentos com prisioneiros chineses, testando armas biológicas e bacteriológicas, além de praticar vivissecção sem anestesia, resultando em dezenas de milhares de mortes.",
    "O 'Experimento de Tuskegee', que começou em 1932, envolveu centenas de homens negros infectados com sífilis, mas nunca tratados, para estudar o curso da doença. Mesmo após a descoberta de tratamentos eficazes, os médicos continuaram o experimento até 1972.",
    "Durante a Guerra do Vietnã, soldados americanos e vietcongues foram usados como cobaias para testes com armas químicas como o Agente Laranja, que causou mortes e deformidades em gerações de pessoas.",
    "Na União Soviética, durante os anos 50, os cientistas realizaram experimentos com radiação em crianças órfãs, sem informar os responsáveis ou garantir seu consentimento. Muitas dessas crianças desenvolveram câncer e outras doenças graves.",
    "Durante a Primeira Guerra Mundial, as trincheiras eram um lugar de horror absoluto, com soldados expostos a doenças, fome, ratos, e, muitas vezes, mutilados por ataques de gás venenoso e balas. A 'guerra de trincheiras' se tornou um símbolo de desumanização.",
    "O 'Projeto Paperclip', após a Segunda Guerra Mundial, trouxe cientistas nazistas para os EUA para trabalhar em pesquisas, ignorando suas atrocidades. Muitos desses cientistas estavam envolvidos em experimentos com prisioneiros, como a exposição a radiação e doenças.",
    "Na década de 1940, os nazistas realizaram experimentos em prisioneiros em Auschwitz, tentando desenvolver uma 'cura' para a homossexualidade, incluindo tratamentos com choques elétricos, castração e outros métodos cruéis.",
    "Em 1967, o Dr. John Money conduziu um experimento envolvendo um menino chamado David Reimer, que teve seu pênis acidentalmente destruído após uma circuncisão mal feita. Money sugeriu que o menino fosse criado como uma menina, mas o experimento levou a tragédias emocionais e suicídios.",
    "Durante a Guerra Civil Espanhola, foi utilizado o 'terror psicológico' como uma forma de tortura, onde prisioneiros eram forçados a ouvir sons perturbadores ou ver filmes de atrocidades enquanto eram privados de alimentação e descanso.",
    "O uso de armas químicas na Primeira Guerra Mundial foi devastador. O gás mostarda, cloro e fosgênio causavam queimaduras, cegueira e morte lenta. Aqueles que sobreviviam, muitas vezes, carregavam sequelas físicas e psicológicas pelo resto de suas vidas.",
    "O 'Experimento de Stanford' fez com que estudantes universitários fossem divididos entre prisioneiros e guardas em uma prisão simulada. O experimento teve que ser interrompido depois de apenas seis dias devido ao comportamento extremamente abusivo e torturante dos 'guardas'.",
    "Nos campos de concentração nazistas, os prisioneiros eram frequentemente forçados a realizar trabalhos exaustivos e mortais, além de serem submetidos a torturas físicas e psicológicas, como o uso de cães de ataque e câmaras de gás.",
    "Em 1951, Henrietta Lacks, uma mulher negra, teve suas células retiradas sem seu consentimento para criar uma linha celular que foi usada para milhares de experimentos médicos, tornando-se a base para estudos até hoje.",
    "Na década de 1940, o governo dos EUA realizou testes com radiação em prisioneiros, soldados e até civis, expondo-os deliberadamente à radiação para ver os efeitos a longo prazo, sem seu consentimento ou conhecimento.",
    "O uso de agentes químicos como o 'Agente Laranja' na Guerra do Vietnã deixou uma marca profunda, matando e deformando tanto civis quanto soldados, causando doenças crônicas e sendo responsável por milhares de mortes ao longo de décadas.",
    "Durante a Segunda Guerra Mundial, o regime nazista testou várias armas experimentais em prisioneiros de guerra, incluindo pistolas de raio e outras armas não convencionais. Esses experimentos tinham como objetivo a criação de uma 'superarma' que nunca chegou a ser utilizada.",
    "A tortura psicológica em prisioneiros de guerra, especialmente durante a Guerra Fria, incluía o uso de métodos como privação sensorial, isolamento extremo e condicionamento mental com o intuito de quebrar a resistência psicológica dos prisioneiros.",
    "Na década de 1950, o governo dos EUA realizou testes em civis com a radiação nuclear, sem informar a população dos riscos envolvidos. Muitas vítimas sofreram sérios danos à saúde e, em alguns casos, faleceram de câncer devido à exposição à radiação.",
    "Em 1975, a Alemanha Ocidental revelou que centenas de prisioneiros haviam sido usados para testar medicamentos experimentais durante a Guerra Fria, sem seu conhecimento ou consentimento. Esses testes resultaram em danos físicos e psicológicos irreversíveis.",
    "Durante a Revolução Cultural Chinesa, milhares de intelectuais e opositores do regime foram torturados e mortos em campos de trabalho forçado, em uma tentativa de erradicar a dissidência política e cultural.",
    "O 'Experimento de Privação Sensorial', realizado nos anos 50, envolveu a tentativa de isolar indivíduos de qualquer estímulo externo. Os resultados mostraram que a privação sensorial prolongada causava alucinações, psicose e graves distúrbios psicológicos.",
    "A 'Guerra do Golfo' utilizou mísseis de urânio empobrecido, cujos resíduos radioativos afetaram os soldados e civis, levando ao que ficou conhecido como 'Síndrome da Guerra do Golfo', com uma série de doenças crônicas e mortes prematuras entre os veteranos.",
    "Na Segunda Guerra Mundial, os japoneses realizaram experimentos biológicos e bacteriológicos em prisioneiros de guerra chineses, usando-os como cobaias para desenvolver armas biológicas letais, resultando em uma imensa perda de vidas humanas."
]

# Escolhe uma curiosidade aleatória e adiciona "Muuu..." no início
curiosidade = "Muuu... " + random.choice(curiosidades_assustadoras)

# Quebra a frase em linhas para caber no balão
curiosidade_formatada = textwrap.fill(curiosidade, width=50)

# Monta o balão de fala
linha_superior = " " + "_" * (len(max(curiosidade_formatada.split('\n'), key=len)) + 2)
linha_inferior = " " + "-" * (len(max(curiosidade_formatada.split('\n'), key=len)) + 2)
fala = f"{linha_superior}\n< {curiosidade_formatada} >\n{linha_inferior}"

# Vaca em ASCII, agora com uma expressão sombria e perturbada
vaca = r"""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||  << algo está errado...
"""

# Exibe no terminal
print(fala + vaca)
