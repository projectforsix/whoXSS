import requests
import re
import argparse
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
        print(f"[!] error: {error}")

def load_payloads(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"[!] error: File '{filename}' not found.")
        return []

def process_targets(targets, payloads):
    try:
        for target in targets:
            for payload in payloads:
                testing_xss(target, payload)
    except KeyboardInterrupt:
        print("\n    ....bye...!")
        exit()

def main():
    parser = argparse.ArgumentParser(description=print_banner())
    parser.add_argument('-t', '--targets', nargs='+', help='target URLs to scan', required=True)
    parser.add_argument('-p', '--payloads', help='file containing payloads', required=True)

    args = parser.parse_args()

    print_banner()
    
    payloads = load_payloads(args.payloads)
    if not payloads:
        print("[!] no payloads. bye... :/")
        exit()

    process_targets(args.targets, payloads)

if __name__ == "__main__":
    main()

threading.Thread(target=process_targets()).start()
threading.Thread(target=testing_xss()).start()
