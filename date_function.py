import json

# from http://ncov.mohw.go.kr/

realdata = """
{
    "2021-05-01":"627","2021-05-02":"606","2021-05-03":"488","2021-05-04":"541",
    "2021-05-05":"676","2021-05-06":"574","2021-05-07":"525","2021-05-08":"701",
    "2021-05-09":"564","2021-05-10":"463","2021-05-11":"510","2021-05-12":"634",
    "2021-05-13":"715","2021-05-14":"747","2021-05-15":"681","2021-05-16":"610",
    "2021-05-17":"619","2021-05-18":"528","2021-05-19":"654","2021-05-20":"646",
    "2021-05-21":"561","2021-05-22":"666","2021-05-23":"585","2021-05-24":"530",
    "2021-05-25":"516","2021-05-26":"701","2021-05-27":"629","2021-05-28":"587",
    "2021-05-29":"533","2021-05-30":"480","2021-05-31":"430","2021-06-01":"459",
    "2021-06-02":"677","2021-06-03":"681","2021-06-04":"695","2021-06-05":"744",
    "2021-06-06":"556","2021-06-07":"485","2021-06-08":"454","2021-06-09":"602",
    "2021-06-10":"610","2021-06-11":"556","2021-06-12":"565","2021-06-13":"452"
}
"""


regional_data = """
{
    "seoul":"176","gyeonggi":"149","daegu":"15","incheon":"15",
    "busan":"13","gyeongbuk":"7","gyeongnam":"8","airport":"17",
    "chungnam":"10","gangwon":"10","chungbuk":"6","gwangju":"3",
    "ulsan":"2","daejeon":"11","jeonbuk":"1","jeonnam":"3",
    "jeju":"5","sejong":"1"
}

"""


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