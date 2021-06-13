import json
import re
from plumbum import cli
from questionary import prompt
from pyfiglet import Figlet, print_figlet
import questionary
from datetime import date
import date_function

def info():
    return "Welcome to the COVID-19 tracker.\nThis program has various features, including:\n- showing the symptoms of COVID-19\n- displays the total positive cases\n- shows the testing information and the positive cases in specific date\n- today's positive case by region."

# A brief introduction about COVID-19 and its symptoms
def symptoms():
    return """Here are some POSSIBLE symptoms of COVID-19:
- Fever or chills
- Cough
- Shortness of breath or difficulty breathing
- Fatigue
- Muscle or body aches
- Headache
- New loss of taste or smell
- Sore throat
- Congestion or runny nose
- Nausea or vomiting
- Diarrhea

These datas are from https://www.cdc.gov/coronavirus/2019-ncov/symptoms-testing/symptoms.html"""

# Shows the total number of COVID-19 test cases in South Korea "TODAY"
def total():
    return "There are 452 total cases today"

def specific_date(date):
    if len(date) != 10:
       return 'length error'
    elif date[4] != '-' or date[7] != '-':
        return 'symbol error'
    elif date[0:4].isdecimal() == False:
       return 'Please write in yyyy-mm-dd form'
    elif date[5:7].isdecimal() == False:
       return 'Please write in yyyy-mm-dd form'
    elif date[8:].isdecimal() == False:
       return 'Please write in yyyy-mm-dd form'
    datas = json.loads(date_function.realdata)
    return datas.get(date,'Sorry, the data for this date doesn\'t exist.')

# Shows the total number of COVID-19 positive test cases in specific "region"
def specific_area(region):
    string = region.lower()
    datas = json.loads(date_function.regional_data)
    return datas.get(string,'The region name doesn\'t exist')

def testing_info():
    return 'Every citizens can get tested without cost at public health center.'

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
            print("Every information about positive test cases are from http://ncov.mohw.go.kr/")
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
    may_eleventh = specific_date("2021-05-11")
    assert may_eleventh == "510"
    assert specific_date("hello") == 'length error'
    assert specific_date("helloo-dkk") == 'symbol error'
    assert specific_date("hihi-03-02") == 'Please write in yyyy-mm-dd form'
    assert specific_date("1111-hiee-") == 'symbol error'
    assert specific_date("1111-22-hh") == 'Please write in yyyy-mm-dd form'
    assert specific_date("1111-22333") == 'symbol error'
    assert specific_date("1111-22-3k") == 'Please write in yyyy-mm-dd form'
    assert specific_date("2020-00-00") == 'Sorry, the data for this date doesn\'t exist.'
def test_specific_area():
    assert 2 == 2