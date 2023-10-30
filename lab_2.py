class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class Notebook:
    def __init__(self):
        self.notes = []

    def add(self, title, content):
        new_note = Note(title, content)
        self.notes.append(new_note)

    def del_n(self):
        del self.notes[-1]

    def display(self):
        for i, note in enumerate(self.notes):
            print(f"Note {i+1}:")
            print(f"Title: {note.title}")
            print(f"Content: {note.content}")
            print("----------")


# notebook = Notebook()

# notebook.add("Заголовок 1", "Вміст нотатка 1")
# notebook.add("Заголовок 2", "Вміст нотатка 2")

# notebook.display()

# notebook.del_n()

# notebook.display()
