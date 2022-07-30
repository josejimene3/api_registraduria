
from repositories.resultRepository import ResultRepository
from repositories.candidateRepository import CandidateRepository
from repositories.tableRepository import TableRepository
from repositories.partyRepository import PartyRepository
from models.result import Result
from models.candidate import Candidate
from models.table import Table
from models.party import Party
from datetime import datetime


def date():
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    return dt_string


class ResultController:
    def __init__(self):
        self.resultRepository = ResultRepository()
        self.candidateRepository = CandidateRepository()
        self.tableRepository = TableRepository()
        self.partyRepository = PartyRepository();

    def index(self):
        print("")
        return self.resultRepository.findAll()

    def show(self, id):
        return self.resultRepository.findById(id)

    def create(self, info, id_table, id_candidate):
        print("Create result")
        result = Result(info)
        table = Table(self.tableRepository.findById(id_table))
        candidate = Candidate(self.candidateRepository.findById(id_candidate))

        result.date_insert = date()
        result.table = table
        result.candidate = candidate
        return self.resultRepository.save(result)

    def update(self, id, info, id_table, id_candidate):
        print("Update result")
        old_result = Result(self.resultRepository.findById(id))
        table = Table(self.tableRepository.findById(id_table))
        candidate = Candidate(self.candidateRepository.findById(id_candidate))

        old_result.votes = info["votes"]
        old_result.date_update = date()
        old_result.table = table
        old_result.candidate = candidate
        return self.resultRepository.save(old_result)

    def delete(self, id):
        return self.resultRepository.delete(id)

    def find_by_party(self, id_party):
        return self.resultRepository.find_by_party(id_party)

    def total_votes_candidate(self):
        return self.resultRepository.sum_votes_candidate()

    def total_votes_candidate_table(self, id_table):
        return self.resultRepository.sum_votes_candidate_table(id_table)

    def total_votes_tables(self):
        return self.resultRepository.sum_votes_tables()

    def total_votes_table(self, id_table):
        return self.resultRepository.sum_votes_table(id_table)

    def total_votes_parties(self):
        return self.resultRepository.sum_votes_parties()

    def total_votes_party(self, id_table):
        return self.resultRepository.sum_votes_party(id_table)
