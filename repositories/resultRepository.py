import pymongo
from bson import ObjectId

from repositories.interfaceRepository import InterfaceRepository
from models.result import Result


class ResultRepository(InterfaceRepository[Result]):
    pass

    def find_by_party(self, id_party):
        query = {"party.$id": ObjectId(id_party)}
        return self.query(query)

    def sum_votes_candidate(self):
        query1 = {
            "$lookup": {
                "from": "candidate",
                "localField": "candidate.$id",
                "foreignField": "_id",
                "as": "candidate"
            }
        }

        query2 = {
            "$lookup": {
                "from": "party",
                "localField": "candidate.party.$id",
                "foreignField": "_id",
                "as": "party"
            }
        }

        query3 = {
            "$unwind": {
                "path": "$candidate",
            }
        }

        query4 = {
            "$unwind": {
                "path": "$party",
            }
        }

        query5 = {
            "$group": {
                "_id": "$candidate",
                "total": {
                    "$sum": "$votes"
                },
                "candidate": {
                    "$first": "$candidate"
                },
                "party": {
                    "$first": "$party"
                }
            }
        }

        query6 = {
            "$project": {
                "_id": "$_id._id",
                "total": 1,
                "document": "$candidate.document",
                "name": "$candidate.name",
                "lastname": "$candidate.lastname",
                "party": "$party.name"
            }
        }

        query7 = {
            "$sort": {
                "total": -1
            }
        }
        pipeline = [query1, query2, query3, query4, query5, query6, query7]
        return self.queryAggregation(pipeline)

    def sum_votes_candidate_table(self, id_table):
        query1 = {
            "$match": {"table.$id": ObjectId(id_table)}
        }

        query2 = {
            "$lookup": {
                "from": "candidate",
                "localField": "candidate.$id",
                "foreignField": "_id",
                "as": "candidate"
            }
        }

        query3 = {
            "$lookup": {
                "from": "party",
                "localField": "candidate.party.$id",
                "foreignField": "_id",
                "as": "party"
            }
        }

        query4 = {
            "$unwind": {
                "path": "$candidate",
            }
        }

        query5 = {
            "$unwind": {
                "path": "$party",
            }
        }

        query6 = {
            "$group": {
                "_id": "$candidate",
                "total": {
                    "$sum": "$votes"
                },
                "candidate": {
                    "$first": "$candidate"
                },
                "party": {
                    "$first": "$party"
                }
            }
        }

        query7 = {
            "$project": {
                "_id": "$_id._id",
                "total": 1,
                "document": "$candidate.document",
                "name": "$candidate.name",
                "lastname": "$candidate.lastname",
                "party": "$party.name"
            }
        }
        pipeline = [query1, query2, query3, query4, query5, query6, query7]
        return self.queryAggregation(pipeline)

    def sum_votes_tables(self):
        query1 = {
            "$lookup": {
                "from": "table",
                "localField": "table.$id",
                "foreignField": "_id",
                "as": "table"
            }
        }

        query2 = {
            "$unwind": {
                "path": "$table",
            }
        }

        query3 = {
            "$group": {
                "_id": "$table",
                "total": {
                    "$sum": "$votes"
                },
                "table": {
                    "$first": "$table"
                }
            }
        }

        query4 = {
            "$project": {
                "_id": "$table._id",
                "total": 1,
                "table": "$table.number"
            }
        }

        query5 = {
            "$sort": {
                "total": -1
            }
        }
        pipeline = [query1, query2, query3, query4, query5]
        return self.queryAggregation(pipeline)

    def sum_votes_table(self, id_table):
        query1 = {
            "$match": {"table.$id": ObjectId(id_table)}
        }

        query2 = {
            "$lookup": {
                "from": "table",
                "localField": "table.$id",
                "foreignField": "_id",
                "as": "table"
            }
        }

        query3 = {
            "$unwind": {
                "path": "$table",
            }
        }

        query4 = {
            "$group": {
                "_id": "$table",
                "total": {
                    "$sum": "$votes"
                },
                "table": {
                    "$first": "$table"
                }
            }
        }

        query5 = {
            "$project": {
                "_id": "$table._id",
                "total": 1,
                "table": "$table.number"
            }
        }

        pipeline = [query1, query2, query3, query4, query5]
        return self.queryAggregation(pipeline)

    def sum_votes_parties(self):
        query1 = {
            "$lookup": {
                "from": "candidate",
                "localField": "candidate.$id",
                "foreignField": "_id",
                "as": "candidate"
            }
        }

        query2 = {
            "$lookup": {
                "from": "party",
                "localField": "candidate.party.$id",
                "foreignField": "_id",
                "as": "party"
            }
        }

        query3 = {
            "$unwind": {
                "path": "$candidate",
            }
        }

        query4 = {
            "$unwind": {
                "path": "$party",
            }
        }

        query5 = {
            "$group": {
                "_id":  "$party",
                "total": {
                    "$sum": "$votes"
                },
                "party": {
                    "$first": "$party"
                }
            }
        }

        query6 = {
            "$project": {
                "_id": "$_id._id",
                "total": 1,
                "party": "$party.name"
            }
        }

        query7 = {
            "$sort": {
                "total": -1
            }
        }

        pipeline = [query1, query2, query3, query4, query5, query6, query7]
        return self.queryAggregation(pipeline)

    def sum_votes_party(self, id_table):
        query1 = {
            "$match": {"table.$id": ObjectId(id_table)}
        }

        query2 = {
            "$lookup": {
                "from": "candidate",
                "localField": "candidate.$id",
                "foreignField": "_id",
                "as": "candidate"
            }
        }

        query3 = {
            "$lookup": {
                "from": "party",
                "localField": "candidate.party.$id",
                "foreignField": "_id",
                "as": "party"
            }
        }

        query4 = {
            "$unwind": {
                "path": "$candidate",
            }
        }

        query5 = {
            "$unwind": {
                "path": "$party",
            }
        }

        query6 = {
            "$group": {
                "_id": "$party",
                "total": {
                    "$sum": "$votes"
                },
                "party": {
                    "$first": "$party"
                }
            }
        }

        query7 = {
            "$project": {
                "_id": "$_id._id",
                "total": 1,
                "party": "$party.name"
            }
        }

        pipeline = [query1, query2, query3, query4, query5, query6, query7]
        return self.queryAggregation(pipeline)