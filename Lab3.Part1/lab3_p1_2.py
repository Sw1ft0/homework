class Notebook:
    def __init__(self):
        self.entries = []

    def add_member(self, name: str, surname: str, phone: str, birthday: str):
        self.entries.append({
            "name": name,
            "surname": surname,
            "phone": phone,
            "birthday": birthday
        })

    def delete_member(self, name: str, surname: str):
        self.entries = [inf for inf in self.entries if inf["name"] != name or inf["surname"] != surname]

    def search(self, query: str):
        return [inf for inf in self.entries if query in inf.values()]

    def __add__(self, other):
        self.entries.extend(other.entries)
        return self

    def __sub__(self, other):
        self.entries = [inf for inf in self.entries if inf not in other.entries]
        return self

    def __mul__(self, query: str):
        return self.search(query)


nb1 = Notebook()
nb1.add_member("Bob", "Smith", "050-556-8970", "19/02/1964")
nb1.add_member("Alice", "Stone", "050-357-3032", "04/12/1965")

nb2 = Notebook()
nb1.add_member("Charlie", "Smith", "095-42-58-188", "12/07/2004")

print("nb1 before merging:")
for entry in nb1.entries:
    print(entry)

nb1 += nb2

print("\nnb1 after merging with nb2:")
for entry in nb1.entries:
    print(entry)

print("\nnb1 before removing entries present in nb2:")
for entry in nb1.entries:
    print(entry)

nb1 -= nb2

print("\nnb1 after removing entries present in nb2:")
for entry in nb1.entries:
    print(entry)
