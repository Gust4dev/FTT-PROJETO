class Personagem:
    def __init__(self, nome, desc, imagem, programa, animador):
        self.nome = nome
        self.descricao = desc
        self.link_imagem = imagem
        self.programa = programa
        self.animador = animador

    def exibir(self):
        print(f"Nome: {self.nome}")
        print(f"Descrição: {self.descricao}")
        print(f"Link da imagem: {self.link_imagem}")
        print(f"Programa: {self.programa}")
        print(f"Animador: {self.animador}")

personagem1 = Personagem(
    nome="Luffy",
    desc="Personagem principal de One Piece!",
    imagem="(https://http2.mlstatic.com/D_NQ_NP_716382-MLB51836121288_102022-O.webp)",
    programa="One Piece",
    animador="Eiichiro Oda"
)

personagem2 = Personagem(
    nome="Goku",
    desc="Protagonista da serie Dragon Ball",
    imagem="(https://www.einerd.com.br/wp-content/uploads/2019/09/Dragon-Ball-Heroes-Goku-instinto-superior-capa.jpg)",
    programa="Dragon Ball",
    animador="RIP Akira Toriyama"
)

personagem1.exibir()
personagem2.exibir()
