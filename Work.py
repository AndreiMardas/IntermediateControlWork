class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class NoteManager:
    def __init__(self):
        self.notes = []

    def create_note(self, title, content):
        note = Note(title, content)
        self.notes.append(note)

    def save_notes(self):
        with open("notes.txt", "w") as file:
            for note in self.notes:
                file.write(note.title + "\n")
                file.write(note.content + "\n")

    def read_notes(self):
        with open("notes.txt", "r") as file:
            lines = file.readlines()
            num_notes = len(lines) // 2
            self.notes.clear()
            for i in range(num_notes):
                title = lines[2*i].strip()
                content = lines[2*i+1].strip()
                note = Note(title, content)
                self.notes.append(note)

    def edit_note_title(self, index, new_title):
        if 0 <= index < len(self.notes):
            self.notes[index].title = new_title

    def edit_note_content(self, index, new_content):
        if 0 <= index < len(self.notes):
            self.notes[index].content = new_content

    def delete_note(self, index):
        if 0 <= index < len(self.notes):
            del self.notes[index]

if __name__ == "__main__":
    note_manager = NoteManager()

    while True:
        print("1. Create a note")
        print("2. Save notes")
        print("3. Read notes")
        print("4. Edit a note")
        print("5. Delete a note")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter note title: ")
            content = input("Enter note content: ")
            note_manager.create_note(title, content)
            print("Note created!")

        elif choice == 2:
            note_manager.save_notes()
            print("Notes saved!")

        elif choice == 3:
            note_manager.read_notes()
            for i, note in enumerate(note_manager.notes):
                print(f"Note {i + 1}:")
                print(f"Title: {note.title}")
                print(f"Content: {note.content}")
                print()

        elif choice == 4:
            index = int(input("Enter the index of the note to edit: "))
            if 0 <= index < len(note_manager.notes):
                title = input("Enter new note title: ")
                content = input("Enter new note content: ")
                note_manager.edit_note_title(index, title)
                note_manager.edit_note_content(index, content)
                print("Note edited!")

        elif choice == 5:
            index = int(input("Enter the index of the note to delete: "))
            if 0 <= index < len(note_manager.notes):
                note_manager.delete_note(index)
                print("Note deleted!")

        elif choice == 0:
            break

        else:
            print("Invalid choice, please try again.")