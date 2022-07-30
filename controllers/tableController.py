from repositories.tableRepository import TableRepository
from models.table import Table


class TableController:
    def __init__(self):
        self.repository = TableRepository()

    def index(self):
        print("")
        return self.repository.findAll()

    def create(self, info):
        print("")
        table = Table(info)
        return self.repository.save(table)

    def show(self, id):
        return self.repository.findById(id)

    def update(self, id, info):
        old_data = self .repository.findById(id)
        old_table = Table(old_data)
        old_table.number = info["number"]
        old_table.register_count = info["register_count"]
        return self.repository.save(old_table)

    def delete(self, id):
        return self.repository.delete(id)


