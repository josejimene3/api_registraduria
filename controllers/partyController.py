from repositories.partyRepository import PartyRepository
from models.party import Party


class PartyController:
    def __init__(self):
        self.repository = PartyRepository()

    def index(self):
        print("")
        return self.repository.findAll()

    def create(self, info):
        print("")
        party = Party(info)
        return self.repository.save(party)

    def show(self, id):
        print("", id)
        return self.repository.findById(id)

    def update(self, id, info):
        print("", id)
        old_data = self.repository.findById(id)
        old_party = Party(old_data)
        old_party.name = info["name"]
        old_party.slogan = info["slogan"]
        return self.repository.save(old_party)

    def delete(self, id):
        print("", id)
        return self.repository.delete(id)




