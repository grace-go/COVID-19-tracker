import json

realdata = '{"2021-05-21":"john", "2021-06-05":"hey"}'

def date_function(date):
    # some JSON:
    #x =  '{ "name":"John", "age":30, "city":"New York"}'
    data = '{"1234":"success", "3":"hello"}'
    # parse x:
    # y = json.loads(x)
    z = json.loads(data)
    # the result is a Python dictionary:
    # print(y["age"])
    # file = json.dumps(data_by_date)
    # y = json.loads(data_by_date)
    return z[date]