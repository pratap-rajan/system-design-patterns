class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # break SRP - By Adding the save and load method within a class
    # save and load can be placed in a separate class - See - class - PersistenceManager
    def save(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()

    def load(self, filename):
        pass

    def load_from_web(self, uri):
        pass


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):   # same as def save as above
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("I went to school today.")
j.add_entry("I ate sandwich for lunch.")
j.add_entry("PE was great!")
j.remove_entry(2)
print(f"Journal entries:\n{j}\n")

p = PersistenceManager()
file = r'journal.txt'
p.save_to_file(j, file)

# verify!
with open(file) as fh:
    print(fh.read())
