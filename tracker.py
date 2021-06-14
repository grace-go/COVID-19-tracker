"""Import a module that tracks COVID-19 positive test cases"""
import json
from datetime import date
from plumbum import cli
from pyfiglet import print_figlet
import questionary
import date_function

def info():
    """Provides a basic information about tracker.py"""
    return """Welcome to the COVID-19 tracker.
This program has various features, including:
- showing the symptoms of COVID-19
- displays the total positive cases
- shows the testing information and the positive cases in specific date
- today's positive case by region."""

def symptoms():
    """A brief introduction about COVID-19 and its symptoms"""
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

def total():
    """Shows the total number of COVID-19 test cases in South Korea \"TODAY\""""
    return "There are 452 total cases today"

def specific_date(when):
    """Shows the total number of COVID-19 positive test cases in specific date"""
    if len(when) != 10:
        return 'length error'
    elif when[4] != '-' or when[7] != '-':
        return 'symbol error'
    elif not when[0:4].isdecimal():
        return 'Please write in yyyy-mm-dd form'
    elif not when[5:7].isdecimal():
        return 'Please write in yyyy-mm-dd form'
    elif not when[8:].isdecimal():
        return 'Please write in yyyy-mm-dd form'
    datas = json.loads(date_function.realdata)
    return datas.get(when,'Sorry, the data for this date doesn\'t exist.')

def specific_area(region):
    """ Shows the total number of COVID-19 positive test cases in specific \"region\""""
    string = region.lower()
    datas = json.loads(date_function.regional_data)
    return datas.get(string,'The region name doesn\'t exist')

def testing_info():
    """Provides a testing info"""
    return 'Every citizens can get tested without cost at public health center.'

def total_regional_data():
    """Returns the positive cases in each region"""
    return date_function.regional_data

class CovidTracker(cli.Application):
    """Main class that runs tracker.py"""
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
            print("If you want to quit the program, press ctrl + c")
            multiple = ['Symptoms', 'Total Positive Cases',
            'Testing info', 'Positive Cases in specific date', 'Today\'s positive case by region',
            'Today\'s \"total\" positive case by region']
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
                print("There were " + specific_date(another_q) + " positive cases in " + another_q)
            elif response == 'Today\'s positive case by region':
                region = questionary.text("Please type the name of the region").ask()
                print("There are " + specific_area(region) +
                " positive cases in " + region + " today")
            elif response == 'Today\'s \"total\" positive case by region':
                print(total())
                print(total_regional_data())

if __name__ == "__main__":
    CovidTracker()

### TESTS

def test_specific_date():
    """Tests the specific_date function"""
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
    june_thirteenth = specific_date("2021-06-13")
    assert june_thirteenth == "452"

def test_specific_area():
    assert specific_area("hi") == 'The region name doesn\'t exist'
    # Check for case-insensitive
    assert specific_area("SEOUL") == "176"
    assert specific_area("Seoul") == "176"
    assert specific_area("seoul") == "176"
    assert specific_area("seouL") == "176"
