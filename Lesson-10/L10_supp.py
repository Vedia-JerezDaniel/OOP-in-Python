class Book:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        print('inside the getter')
        return self._title
    @title.setter
    def title(self, title):
        print('inside the setter')
        self._title = title


b = Book('Python Programming')
print(b.title)
print(b.__dict__)

