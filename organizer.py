class Organizer:

    def __init__(self):
        self.notes = []

    def add(self, note):
        self.notes.append(note)

    def all(self):
        return self.notes
