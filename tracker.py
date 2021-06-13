import json
import re
from plumbum import cli
from questionary import prompt
from pyfiglet import Figlet, print_figlet
import questionary
from datetime import date
import date_function

def info():
    return "Welcome to the COVID-19 tracker.\nThis program features "

# A brief introduction about COVID-19 and its symptoms
def symptoms():
    return "Here are some symptoms of COVID-19"

# Shows the total number of COVID-19 test cases in South Korea "TODAY"
def total():
    return "total_number number of COVID-19 positive test cases TODAY"

def specific_date(date):
    if len(date) != 10:
       return 'length error'
    elif date[4] != '-' and date[7] != '-':
        return 'symbol error'
    elif date[0:4].isdecimal() == False:
       return 'Please write in yyyy-mm-dd form'
    elif date[5:7].isdecimal() == False:
       return 'Please write in yyyy-mm-dd form'
    elif date[8:].isdecimal() == False:
       return 'Please write in yyyy-mm-dd form'
    datas = json.loads(date_function.realdata)
    return datas.get(date,'keyerror')

# Shows the total number of COVID-19 positive test cases in specific "region"
def specific_area(region):
    string = region.lower()
    datas = json.loads(date_function.regional_data)
    return datas.get(string,'The region name doesn\'t exist')

def testing_info():
    return 'testing'

# Information about where to contact and test COVID-19
def contact_info():
    return "contact"

class CovidTracker(cli.Application):
    VERSION = "1.4"
    info = cli.Flag(['i', 'info'], help= "Shows the basic info about this CLI")

    def main(self):
        if self.info:
            print(info())
        else:
            print_figlet("COVID-19 Tracker")
            today = date.today()
            print("Today's date:", today)
            multiple = ['Symptoms', 'Total Positive Cases', 'Testing info', 'Positive Cases in specific date', 'Today\'s positive case by region']
            question = questionary.select("What do you want to know?", choices=multiple)
            response = question.ask()
            if response == 'Symptoms':
                print(symptoms())
            elif response == 'Total Positive Cases':
                print(total())
            elif response == 'Testing info':
                print(testing_info())
            elif response == 'Positive Cases in specific date':
                another_q = questionary.text("Please put the date in yyyy-mm-dd form.").ask()
                print(specific_date(another_q))
            elif response == 'Today\'s positive case by region':
                region = questionary.text("Please type the name of the region").ask()
                print(specific_area(region))

if __name__ == "__main__":
    CovidTracker()

### TESTS

def test_specific_date():
    return "i"
def test_specific_area():
    return "e"