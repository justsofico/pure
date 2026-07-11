class Note:

    def __init__(self, title, content, tags):
        self.title = title
        self.content = content
        self.tags = tags

    def __str__(self):
        return (
            f"{self.title}\n"
            f"Tags: {', '.join(self.tags)}"
        )
