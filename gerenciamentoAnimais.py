class Animal:
    def __init__(self, nome: str, especie: str, idade: int):
        self._nome = nome
        self._especie = especie
        self.__idade = idade
        self._disponivel = True

    def _estaDisponivel(self):
        return self._disponivel
    
    def exibirInformacoes(self):
        if self._estaDisponivel():
            print(f"Nome: {self._nome}")
            print(f"Especie: {self._especie}")
            print(f"Idade: {self.__idade}")
        else:
            print(f"{self._nome} nao esta disponivel no momento")

    def tornarDisponivel(self):
        self._disponivel = True

    def tornarIndisponivel(self):
        self._disponivel = False


class Mamifero(Animal):
    def __init__(self, nome: str, especie: str, idade: int, tipoPelo: str):
        super().__init__(nome, especie, idade)
        self._tipoPelo = tipoPelo

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f"Tipo do pelo: {self._tipoPelo}")


class Ave(Animal):
    def __init__(self, nome: str, especie: str, idade: int, corDasPenas: str):
        super().__init__(nome, especie, idade)
        self._corDasPenas = corDasPenas

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f"Cor das penas: {self._corDasPenas}")


class Reptill(Animal):
    def __init__(self, nome: str, especie: str, idade: int, venenoso: bool):
        super().__init__(nome, especie, idade)
        self._venenoso = venenoso

    def __ehVenenoso(self):
        return self._venenoso

    def exibirInformacoes(self):
        super().exibirInformacoes()
        if self.__ehVenenoso():
            print("Venenoso")
        else:
            print("Nao eh venenoso")


class Zoologico:
    def __init__(self):
        self.__animal = []

    def adicionarNovoAnimal(self, animal: Animal):
        self.__animal.append(animal)

    def exibirAnimaisDisponiveis(self):
        if len(self.__animal) > 0:
            for i in self.__animal:
                if i._estaDisponivel():
                    i.exibirInformacoes()
        else:
            print("Voce precisa adicionar um animal para fazer isso")

    def removerAnimal(self, animal: Animal):
        encontrei = False
        for i, buscaAnimal in enumerate(self.__animal):
            if buscaAnimal._nome == animal._nome:
                encontrei = True
                self.__animal.pop(i)
                break
        if not encontrei:
            print("Este animal nao esta no zoologico")
    
    def BuscarAnimalNome(self, animal: Animal):
        encontrei = False
        for buscaAnimal in self.__animal:
            if buscaAnimal._nome == animal._nome:
                encontrei = True
                buscaAnimal.exibirInformacoes()
                break
        if not encontrei:
            print("Este animal nao esta registrado no sistema")


# Criando instâncias de animais
elefante = Mamifero("Dumbo", "Elefante", 10, "Cinza")
aguia = Ave("Fenix", "Aguia", 5, "Branca")
cobra = Reptill("Python", "Cobra", 5, True)

# Criando instância do zoológico
zoologico = Zoologico()

# Adicionando animais ao zoológico
zoologico.adicionarNovoAnimal(elefante)
zoologico.adicionarNovoAnimal(aguia)
zoologico.adicionarNovoAnimal(cobra)

# exibindo todos os animais disponiveis
zoologico.exibirAnimaisDisponiveis()

zoologico.removerAnimal(cobra) #removendo cobra

zoologico.BuscarAnimalNome(cobra) #provando que foi removida