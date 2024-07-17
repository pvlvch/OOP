class Names:
    def __init__(self, name):
        self.name = list(name)

    def get_name(self):
        return self.name

    def set_name(self, need):
        self.name.append(need)

    def __iter__(self):
        return iter(self.name)

pr = Names(["Kirill", "Danil"])
pr.set_name("Olga")
for i in pr:
    print(i)