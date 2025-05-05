
import random
import textwrap

# Lista expandida com muitas curiosidades extremamente específicas e inteligentes demais
curiosidades = [
    "A constante de estrutura fina (aproximadamente 1/137) determina a força do eletromagnetismo, e sua origem ainda é um mistério fundamental na física teórica.",
    "Os tardígrados conseguem sobreviver no vácuo do espaço porque entram em criptobiose, substituindo quase toda a água do corpo por um açúcar chamado trealose.",
    "Na mecânica quântica, partículas idênticas são indistinguíveis até no princípio, o que significa que não é apenas que não sabemos qual é qual — elas realmente não têm identidade separada.",
    "A biblioteca de Babel, descrita por Borges, possui 10^1,834,097 livros possíveis — mais do que átomos no universo observável.",
    "O cérebro humano gasta cerca de 20% da energia total do corpo mesmo representando apenas 2% da massa corporal — e essa energia vai, em grande parte, para manter o ruído sináptico.",
    "A notação lambda do cálculo funcional, usada em linguagens como Haskell, vem do trabalho de Alonzo Church nos anos 1930 — que também foi professor de Alan Turing.",
    "O número de Graham, usado em teoria de Ramsey, é tão absurdamente grande que mesmo exponenciações repetidas não chegam perto — ele é maior do que o número de partículas no universo.",
    "A cor azul é rara na natureza não por pigmentação, mas por estrutura — borboletas azuis e penas de pavão refletem azul por microestruturas que manipulam a luz.",
    "Em 1977, um radiotelescópio captou o 'sinal WOW!', uma possível transmissão de origem extraterrestre. Nunca mais foi detectado algo parecido.",
    "A linguística computacional permite reconstruir idiomas perdidos com base em modelos probabilísticos de som — o protoindo-europeu, por exemplo, é parcialmente reconstituído com algoritmos bayesianos.",
    "O Teorema de Gödel prova que todo sistema lógico suficientemente poderoso contém proposições que não podem ser provadas dentro dele — e isso se aplica à própria matemática.",
    "Existe um número chamado Aleph-1, que representa a cardinalidade do conjunto de todos os números reais, e ele é maior que o infinito 'normal' (Aleph-0).",
    "A célula de um polvo contém material genético que é extensivamente editado por RNA após a transcrição — algo extremamente raro no reino animal.",
    "Em redes complexas, o efeito de 'centralidade de intermediação' explica por que alguns nós (como hubs de aeroportos) são mais importantes para a conectividade do que os maiores nós em si.",
    "A geometria hiperbólica permite a existência de infinitas linhas paralelas que nunca se cruzam, e é usada para modelar a estrutura do espaço-tempo em certos cosmologias.",
    "Em teoria dos jogos, o dilema do prisioneiro iterado mostra que estratégias como 'tit for tat' evoluem naturalmente em populações de agentes com memória limitada.",
    "Os neutrinos mudam de tipo (flavor) enquanto viajam, o que implica que eles têm massa — contrariando o Modelo Padrão da física, e indicando física além dele.",
    "Certas espécies de fungos da floresta tropical trocam informações químicas com árvores por meio de redes micorrízicas — formando uma espécie de 'internet subterrânea'.",
    "A fórmula de Euler (e^(iπ) + 1 = 0) conecta cinco das constantes matemáticas mais fundamentais em uma única equação — chamada por muitos de 'a equação mais bela'.",
    "A linguagem Pirahã, falada na Amazônia, não tem números, tempos verbais ou recursividade — e desafia a noção universal da gramática de Chomsky.",
    "A função zeta de Riemann, uma das questões mais difíceis da matemática, está relacionada com a distribuição dos números primos, e sua solução pode mudar toda a teoria dos números.",
    "O teorema de Poincaré é considerado um dos maiores avanços em topologia, descrevendo como uma esfera em três dimensões é o único objeto tridimensional sem buracos.",
    "O efeito Casimir ocorre quando duas superfícies metálicas muito próximas no vácuo experimentam uma força atraente devido à flutuação quântica do vácuo.",
    "Na biologia, a simbiose mutualística entre as abelhas e as flores evoluiu de tal maneira que as abelhas se tornaram especializadas para extrair néctar, enquanto as flores dependem delas para polinização.",
    "A Teoria das Cordas sugere que as partículas fundamentais não são pontuais, mas pequenas cordas vibrantes, e sua teoria poderia unificar todas as forças fundamentais da natureza.",
    "A ideia de múltiplos universos (multiverso) sugere que o nosso universo poderia ser apenas um entre muitos, com diferentes leis físicas em cada um deles.",
    "O fenômeno de supercondutividade ocorre quando certos materiais são resfriados a temperaturas muito baixas, permitindo que eles conduzam eletricidade sem resistência.",
    "A conjectura de Collatz, um dos maiores mistérios não resolvidos na matemática, afirma que qualquer número natural, quando submetido a uma sequência específica de operações, eventualmente chega ao número 1.",
    "Na biologia evolutiva, o conceito de 'seleção sexual' explica como características como o colorido da plumagem de um pavão evoluíram devido à preferência das fêmeas por características atraentes.",
    "O 'efeito Doppler' é a mudança na frequência de uma onda (como som ou luz) em relação ao observador em movimento, e é uma ferramenta fundamental na astronomia para medir a velocidade das estrelas.",
    "O teorema de Fermat, que afirma que não existem soluções inteiras para a equação \(x^n + y^n = z^n\) para \(n > 2\), foi conjecturado em 1637 e só foi provado em 1994 por Andrew Wiles."
]

# Escolhe uma curiosidade aleatória e adiciona "Muuu..." no início
curiosidade = "Muuu... " + random.choice(curiosidades)

# Quebra a frase em linhas para caber no balão
curiosidade_formatada = textwrap.fill(curiosidade, width=50)

# Monta o balão de fala
linha_superior = " " + "_" * (len(max(curiosidade_formatada.split('\n'), key=len)) + 2)
linha_inferior = " " + "-" * (len(max(curiosidade_formatada.split('\n'), key=len)) + 2)
fala = f"{linha_superior}\n< {curiosidade_formatada} >\n{linha_inferior}"

# Vaca em ASCII, agora pensativa
vaca = r"""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||  << pensa demais
"""

# Exibe no terminal
print(fala + vaca)
