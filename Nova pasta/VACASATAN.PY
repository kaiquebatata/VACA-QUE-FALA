import random
import textwrap

# Lista de curiosidades sobre rituais, deuses mesopotâmicos, grimórios e práticas ocultas
curiosidades_ocultismo_avancado = [
    "A deusa Ishtar (ou Inanna) da Mesopotâmia era uma das figuras mais poderosas do panteão sumério e acádio. Ela era associada ao amor, à fertilidade, à guerra e à morte. Seus cultos incluíam rituais sexuais sagrados que eram realizados para propiciar fertilidade e abundância.",
    "Marduk, deus patrono da Babilônia, foi uma divindade central no panteão mesopotâmico. Os babilônios acreditavam que Marduk lutou contra a serpente Tiamat, representando a luta entre o caos e a ordem. Os sacerdotes de Marduk realizavam rituais de sacrifício para garantir a proteção do deus.",
    "A magia de Assurbanipal, rei da Assíria, estava ligada ao uso de grimórios antigos, incluindo textos que permitiam a invocação de espíritos e a manipulação de forças sobrenaturais. Esses textos eram armazenados em bibliotecas secretas e eram usados apenas por magos e sacerdotes altamente treinados.",
    "O 'Livro de Thoth', considerado um grimório místico egípcio, era atribuído ao deus Thoth, que era o deus da sabedoria e da magia. Este livro esotérico continha feitiços, invocações de deuses e passagens que ensinavam os mistérios do universo e do além.",
    "O 'Clavícula de Salomão' (ou 'Chave de Salomão') é um dos grimórios mais conhecidos da magia medieval. A obra é atribuída ao rei Salomão e ensina como invocar demônios, espíritos e entidades sobrenaturais, utilizando símbolos e rituais complexos.",
    "Na antiga Mesopotâmia, o culto a Nergal, o deus da morte e das doenças, envolvia rituais sombrios em que os sacerdotes invocavam o deus através de sacrifícios de animais e oferendas de sangue. Nergal era visto como um deus de destruição, mas também como uma figura que ajudava a garantir a justiça divina no além.",
    "Os Sumerianos praticavam o 'Ritual da Descensão de Inanna', onde a deusa Ishtar (Inanna) descia até o submundo para resgatar seu amante. Este ritual simbólico representava o ciclo da vida, morte e renascimento e era realizado para garantir a fertilidade da terra.",
    "O 'Necronomicon', um grimório fictício criado por H.P. Lovecraft, é frequentemente associado a rituais macabros de invocação de entidades cósmicas e demoníacas. Embora o livro seja uma invenção literária, muitos ocultistas modernos o veem como um símbolo do medo do desconhecido e da busca pelo poder além da compreensão humana.",
    "O culto de Baphomet, associado à Ordem dos Templários, é um dos símbolos mais enigmáticos do ocultismo moderno. Baphomet é frequentemente retratado como uma figura antropomórfica com cabeça de bode, simbolizando a união das forças opostas – luz e escuridão, masculino e feminino, bem e mal.",
    "O 'Livro de Enoque', um texto apócrifo da Bíblia, contém descrições detalhadas dos anjos caídos e suas interações com os humanos. Segundo o texto, esses anjos ensinaram à humanidade os segredos proibidos da magia, como a astrologia e a alquimia, levando à corrupção da terra e à criação de monstros.",
    "Os Assírios praticavam rituais de exorcismo, onde sacerdotes realizavam cerimônias complexas para afastar espíritos malignos e demônios que causavam doenças ou desastres naturais. Esses rituais envolviam cantos sagrados, invocações de deuses protetores e o uso de amuletos mágicos.",
    "Os sacerdotes de Anu, o deus supremo do panteão mesopotâmico, realizavam rituais celestes em busca de sabedoria e orientação dos astros. Esses rituais eram realizados à noite e envolviam a observação dos céus e o sacrifício de animais para garantir a proteção divina.",
    "A magia cerimonial do 'Ritual de Invocação de Lúcifer', que surgiu no século XVI, envolve a criação de círculos mágicos e o uso de palavras e gestos específicos para invocar o príncipe das trevas. O objetivo era alcançar poder, conhecimento e riqueza, embora muitos ocultistas considerassem esses rituais extremamente perigosos.",
    "O 'Codex Gigas', também conhecido como 'Livro do Diabo', é um antigo manuscrito medieval que contém rituais e invocações demoníacas. Diz-se que o livro foi escrito por um monge condenado, que fez um pacto com o diabo em troca de ajuda para completar a obra. O livro é famoso por seu tamanho colossal e pela imagem do diabo presente na página inicial.",
    "O ritual de 'Sacrifício de Crianças', embora muitas vezes associado a cultos satânicos modernos, tem raízes profundas nas antigas civilizações. Em algumas culturas mesopotâmicas, como a babilônica, sacrifícios humanos eram realizados para apaziguar deuses poderosos e garantir boas colheitas e vitórias em batalhas.",
    "O culto de Osíris no Egito Antigo envolvia rituais de ressurreição e fertilidade, onde os sacerdotes imitavam a morte e o renascimento de Osíris para garantir que a terra se renovasse e que o faraó fosse abençoado pelo deus da morte e do além.",
    "O 'Ritual de Magia Negra', muitas vezes associado ao culto de Set, o deus egípcio das tempestades e da desordem, envolvia o uso de sangue e símbolos arcanos para invocar forças caóticas. Os praticantes acreditavam que ao dominar essas forças, poderiam atingir objetivos pessoais e obter poder sobrenatural.",
    "No ocultismo medieval, a prática do 'Evocação de Demônios', como detalhado na 'Ars Goetia' (parte do grimório 'A Chave de Salomão'), envolvia rituais complexos para invocar e controlar demônios específicos. Cada demônio tinha suas próprias características e habilidades, como o poder de provocar doenças, trazer riquezas ou controlar os pensamentos dos outros.",
    "O culto de Tiamat, a serpente primordial na mitologia babilônica, era associado ao caos e à criação do universo. Os rituais em honra a Tiamat envolviam invocações de forças destrutivas e eram realizados em lugares secretos, com sacrifícios realizados à beira de rios e lagos para apaziguar a deusa da criação e da destruição."
]

# Escolhe uma curiosidade aleatória e adiciona "Muuu..." no início
curiosidade = "Muuu... " + random.choice(curiosidades_ocultismo_avancado)

# Quebra a frase em linhas para caber no balão
curiosidade_formatada = textwrap.fill(curiosidade, width=50)

# Monta o balão de fala
linha_superior = " " + "_" * (len(max(curiosidade_formatada.split('\n'), key=len)) + 2)
linha_inferior = " " + "-" * (len(max(curiosidade_formatada.split('\n'), key=len)) + 2)
fala = f"{linha_superior}\n< {curiosidade_formatada} >\n{linha_inferior}"

# Vaca em ASCII com uma expressão mais misteriosa e enigmática
vaca = r"""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||  << Os segredos ocultos...
"""

# Exibe no terminal
print(fala + vaca)
