from parser import collect_tags


def export(notes):

    print("=" * 30)
    print("NOTES")
    print("=" * 30)

    for note in notes:
        print(note)
        print()

    print("-" * 30)
    print(f"Total Notes: {len(notes)}")
    print(f"Unique Tags: {len(collect_tags(notes))}")

    print("\nTags:")

    for tag in collect_tags(notes):
        print(f"- {tag}")
