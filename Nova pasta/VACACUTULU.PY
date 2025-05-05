import random
import textwrap

# Lista de curiosidades sobre horror cósmico e crises existenciais
curiosidades_horror_cosmico = [
    "Muuu... Existe uma teoria que afirma que, no vasto universo, as civilizações avançadas poderiam ter passado por estágios tão elevados que, ao atingir a perfeição, elas se tornaram inconcebíveis para nós, mortais. Nós, simples seres humanos, seríamos apenas uma falha passageira no grande esquema da realidade.",
    "Muuu... E se as estrelas que vemos no céu forem apenas fragmentos de algo muito maior, uma consciência cósmica que observa a humanidade sem qualquer compreensão do que somos? E se elas nos olharem como nós olhamos para formigas, sem nenhum tipo de compaixão ou interesse?",
    "Muuu... Já pensou que, talvez, o cosmos não seja vasto, mas apenas uma prisão? As leis da física, o tempo e o espaço, poderiam ser limites impostos a nós, de forma que nunca seremos capazes de perceber o verdadeiro e infinito caos que nos cerca. E, talvez, a própria noção de 'realidade' seja uma ilusão para nos manter controlados.",
    "Muuu... Há quem diga que, em algum lugar nas profundezas do universo, existem entidades que transcendem nossa percepção. Seres que não possuem forma ou consciência em nosso sentido, mas que são responsáveis por forças que não compreendemos. Essas entidades poderiam estar apenas aguardando o momento certo para se revelarem... ou nem sequer saber que existimos.",
    "Muuu... A entropia universal, o conceito de que tudo tende ao caos e à destruição, é talvez a maior força do universo. Tudo que existe está fadado a se desintegrar. E se isso não fosse apenas algo que aconteceria, mas algo que já está acontecendo agora, em escalas que não conseguimos perceber? E se o fim do mundo já estivesse acontecendo bem diante de nós?",
    "Muuu... O universo, em sua imensidão, pode ser cheio de vida e civilizações, mas e se essas civilizações forem tão diferentes da nossa que, quando tentarmos nos comunicar com elas, seremos consumidos em um momento de incompreensão irreparável? O que significaria uma comunicação que nós não poderíamos entender, mas que poderia destruir nossa psique por ser tão alienígena?",
    "Muuu... Em muitos relatos de encontros com o desconhecido, aqueles que alegam ter visto seres ou entidades do além relatam uma sensação de total perda de identidade. A compreensão de que a vida, o corpo e a mente não são mais do que um truque passageiro da existência, um engano para nos manter ocupados enquanto o cosmos, com toda sua indiferença, nos observa como um experimento acidental.",
    "Muuu... Se a Terra, de fato, for apenas um ponto minúsculo em um universo em expansão infinitamente, a vida humana poderia ser apenas um capricho do acaso. Somos apenas uma anomalia no grande plano do cosmos, e o universo seguiria sem perceber nossa existência, indiferente à nossa luta por sentido e compreensão.",
    "Muuu... O famoso 'Paradoxo de Fermi' questiona por que, apesar da enorme probabilidade de vida inteligente no universo, nunca encontramos sinais de outras civilizações. E se isso for apenas um reflexo da nossa própria insignificância? Talvez a explicação seja que a vida inteligente não é algo que sobreviva muito tempo em um universo tão imenso, e acabamos de ser uma de suas últimas faíscas.",
    "Muuu... E se, ao fim da nossa existência, o que percebemos como 'morte' fosse na verdade uma transição para um novo estado de consciência? Talvez o espaço-tempo que entendemos seja apenas uma prisão temporária, e ao morrermos, nossa mente será finalmente libertada para enfrentar realidades que são muito mais aterradoras do que podemos compreender.",
    "Muuu... Imagine que o que chamamos de 'realidade' não seja nada mais do que uma ilusão gerada por uma gigantesca força cósmica. E se o universo que vemos, o tempo que experimentamos, e até mesmo os conceitos de vida e morte, forem apenas mecanismos criados por uma entidade superior que se diverte com nosso sofrimento e confusão, sem nenhum propósito além da perpetuação do caos?"
]

# Escolhe uma curiosidade aleatória e adiciona "Muuu..." no início
curiosidade = "Muuu... " + random.choice(curiosidades_horror_cosmico)

# Quebra a curiosidade em linhas para caber no balão
curiosidade_formatada = textwrap.fill(curiosidade, width=50)

# Monta o balão de fala
linha_superior = " " + "_" * (len(max(curiosidade_formatada.split('\n'), key=len)) + 2)
linha_inferior = " " + "-" * (len(max(curiosidade_formatada.split('\n'), key=len)) + 2)
fala = f"{linha_superior}\n< {curiosidade_formatada} >\n{linha_inferior}"

# Vaca com uma expressão sombria e contemplativa
vaca = r"""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||  << O que você faria se soubesse que somos apenas poeira no cosmos?
"""

# Exibe no terminal
print(fala + vaca)
