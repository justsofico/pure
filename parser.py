def collect_tags(notes):

    tags = set()

    for note in notes:
        tags.update(note.tags)

    return sorted(tags)
