class Payroll:
    basic=0
    benefits=0
    gross=0
    def __init__(self,ba,be):
        self.basic = ba
        self.benefits = be
        self.gross_salary()


    def gross_salary(self):
        self.gross = self.basic+self.benefits
