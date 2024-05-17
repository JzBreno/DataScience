class Foo:
    def hello(self):
        print(self.__class__.__name__.upper())


class Bar(Foo):
    def hello(self):
        return super().hello()


bar = Bar().hello()
