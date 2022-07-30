from repositories.candidateRepository import CandidateRepository
from repositories.partyRepository import PartyRepository
from models.candidate import Candidate
from models.party import Party


class CandidateController:
    def __init__(self):
        self.candidateRepository = CandidateRepository()
        self.partyRepository = PartyRepository()

    def index(self):
        print("")
        return self.candidateRepository.findAll()

    def show(self, id):
        return self.candidateRepository.findById(id)

    def create(self, info, id_party):
        print("")
        candidate = Candidate(info)
        party = Party(self.partyRepository.findById(id_party))
        candidate.party = party
        return self.candidateRepository.save(candidate)

    def update(self, id, info, id_party):
        old_candidate = Candidate(self.candidateRepository.findById(id))
        party = Party(self.partyRepository.findById(id_party))

        old_candidate.accreditation = info["accreditation"]
        old_candidate.document = info["document"]
        old_candidate.name = info["name"]
        old_candidate.lastname = info["lastname"]
        old_candidate.party = party
        return self.candidateRepository.save(old_candidate)

    def update(self, id, info, id_party):
        old_data = self.candidateRepository.findById(id)
        party = Party(self.partyRepository.findById(id_party))

        old_candidate = Candidate(old_data)
        old_candidate.accreditation = info["accreditation"]
        old_candidate.document = info["document"]
        old_candidate.name = info["name"]
        old_candidate.lastname = info["lastname"]
        old_candidate.party = party
        return self.candidateRepository.save(old_candidate)

    def delete(self, id):
        return self.candidateRepository.delete(id)


