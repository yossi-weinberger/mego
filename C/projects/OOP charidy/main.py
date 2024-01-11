# TODO 2 classes
from datetime import datetime
from pymongo import MongoClient


class Income:
    total_tithe = 0

    # @classmethod
    # def new_income_file(cls):
    #     client = MongoClient("localhost",27017)
    #     db = client.charidy
    #     income_collection = db.income_collection
    #     income_collection.insert_one({"test3":"test3"})
    
    def __init__(self):
        self.description = input("Type the description: ")
        self.amunt = int(input("Type the amunt: "))
        self.day = datetime.now()
        self.day_date = self.day.strftime("%d/%m/%Y %H:%M:%S")
        self.tithe = self.amunt/10
        Income.total_tithe += self.tithe

    def save_income(self):
        client = MongoClient("localhost", 27017)
        db = client.charidy
        income_collection = db.income_collection
        income_collection.insert_one({"description": self.description,
                                      "amunt": self.amunt,
                                      "date": self.day_date,
                                      "tithe": self.tithe})
                                      # "Total tithe": Income.total_tithe})

    def save_total_income(self):
        total_tithe_collection = db.total_tithe_collection
        total_tithe_collection.insert_one({"total": Income.total_tithe})
        total_tithe_collection.updateOne(total_tithe,)

    def __repr__(self):
        return (f"description:{self.description}\n"
                f"amunt:{self.amunt}\n"
                f"date: {self.day_date}\n"
                f"tithe: {self.tithe}\n"
                f"total tithe: {Income.total_tithe}")

# new_income_file()

new_income = Income()
assert new_income.amunt >= 0, "Amunt can't be negative"
print(new_income)
new_income.save_income()
# print(Income.total_tithe)
