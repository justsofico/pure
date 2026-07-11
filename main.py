from organizer import Organizer
from sample_notes import notes
from exporter import export

organizer = Organizer()

for note in notes:
    organizer.add(note)

export(organizer.all())
