class RailwayForm:
    formType = "RailwayForm"

    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")


saqapplication = RailwayForm()

saqapplication.name = "Saquib"
saqapplication.train = "Cord Line local"

saqapplication.printData()