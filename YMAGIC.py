import socket
import requests
from colorama import Fore
def clear_page():
    from os import system, name
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
while True:
    clear_page()
    print(Fore.GREEN + """
          
                                    ██╗░░░██╗███╗░░░███╗░█████╗░░██████╗░██╗░█████╗░
                                    ╚██╗░██╔╝████╗░████║██╔══██╗██╔════╝░██║██╔══██╗
                                    ░╚████╔╝░██╔████╔██║███████║██║░░██╗░██║██║░░╚═╝
                                    ░░╚██╔╝░░██║╚██╔╝██║██╔══██║██║░░╚██╗██║██║░░██╗
                                    ░░░██║░░░██║░╚═╝░██║██║░░██║╚██████╔╝██║╚█████╔╝
                                    ░░░╚═╝░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝░╚════╝░
                                    
                                    Github  : https://github.com/ya3in3a44ri/YMAGIC
                                    Website : RedBlueZone.top
                                    Blog    : yasinsaffari.blog.ir
          """)
    print(Fore.GREEN + "[+] " + Fore.WHITE + "If you want WHOIS just type : " + Fore.RED + "whois")
    print(Fore.GREEN + "[+] " + Fore.WHITE + "If you want SUBDOMAIN-FINDER just type : " + Fore.RED + "sub")
    print(Fore.GREEN + "[+] " + Fore.WHITE + "If you want to EXIT just type : " + Fore.RED + "exit")
    a = Fore.GREEN + "[+] " + Fore.WHITE + "YMAGIC > "
    select_options = input(a)
    if select_options == "whois":
        b = Fore.GREEN + "[+] " + Fore.WHITE + "YMAGIC/WOIS/HOST > "
        host = input(b).lower()
        host = host.replace("http://","")
        host = host.replace("https://","")
        host = host.replace("www.","")
        if host[-3:] == "org" or host[-3:] == "com" or host[-3:] == "net":
            whois_server = "whois.internic.net"
        else:
            whois_server =  "whois.iana.org"
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.connect((whois_server,43))
        s.send((host+"\r\n").encode())
        msg = s.recv(10000)
        print(Fore.WHITE + str(msg.decode()))
        input(Fore.YELLOW + "[!] " + Fore.WHITE + "Press any key to clear page and start tool again")
    elif select_options == "sub":
        file = "subdomain.txt"
        domain = input(Fore.GREEN + "[+] " + Fore.WHITE + "YMAGIC/WOIS/SUBDOMAIN/Domain name > ")
        file = open(file)
        content = file.read()
        subdomains = content.splitlines()
        discovered_subdomains = []
        for subdomain in subdomains:
            url = f"http://{subdomain}.{domain}"
            try:
                requests.get(url)
            except requests.ConnectionError:
                pass
            else:
                print(Fore.GREEN + "[+] " + Fore.WHITE + " Discovered subdomain:", Fore.YELLOW + str(url))
                discovered_subdomains.append(url)
        input(Fore.YELLOW + "[!] " + Fore.WHITE + "Press any key to clear page and start tool again")
    elif select_options == "exit" :
        break
    else:
        pass
    
