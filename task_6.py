class Database:
    def connect(self):
        raise NotImplementedError

    def get_row_by_id(self, id: int):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError


class SQLDatabase(Database):
    pass


class MongoDatabase(Database):
    pass


class NeoDatabase(Database):
    pass
