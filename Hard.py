class Toys:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

class СartoonСharacter:
    def production(self):
        print(f'Создана игрушка героя мультфильма')

class Animal:
    def production(self):
        print(f'Создана игрушка животного')

class Factory(Toys):
    def __init__(self, name, model, color):
        super().__init__(name, model, color)
        self._purchase_materials()
        self._sewing()
        self._painting()

        if self.model == 'animal':
            Animal().production()
        if self.model == 'cartoon character':
            СartoonСharacter().production()

    def _purchase_materials(self):
        print(f'Закупка сырья для {self.name}')

    def _sewing(self):
        print(f'Пошив {self.name}')

    def _painting(self):
        print(f'Окраска {self.name} в {self.color}')

toy1 = Factory('lion', 'animal', 'yellow')
toy2 = Factory('spider-man', 'cartoon character', 'red')