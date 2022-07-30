from repositories.reportRepository import ReportRepository
from models.report import Report


class ReportController:
    def __init__(self):
        self.repository = ReportRepository()

    def index(self):
        print("")
        return self.repository.findAll()

    def create(self, info):
        print("")
        report = Report(info)
        return self.repository.save(report)


