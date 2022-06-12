#!/usr/bin/python3

#import art
import sys


def Pwn_Rev():
    print("""
    --- Pwn & Rev ---
    > gdb(https://github.com/longld/peda)
    > radare2(https://github.com/radareorg/radare2)
    > ghidra(https://github.com/NationalSecurityAgency/ghidra)
    > pwntools(https://github.com/Gallopsled/pwntools)
    > apktool(https://github.com/iBotPeaches/Apktool)
    > IDA Pro(https://hex-rays.com/ida-free/)
    > Immunity Debugger(https://www.immunityinc.com/products/debugger/)
    > checksec(https://github.com/slimm609/checksec.sh)
    > Binary Exploitation Notes(https://ir0nstone.gitbook.io/notes/)
    > strace
    > ltrace
    > strings
    > xxd
    > od
    > printf
    > hexdump
    > objdump
    > rp++(https://github.com/0vercl0k/rp)
    > socat(https://gist.github.com/takuma-saito/dc057658c9f7f550fd61)
    """)

def Crypto():
    print("""
    --- Crypto ---
    > FeatherDuster(https://github.com/nccgroup/featherduster)
    > Hash Extender(https://github.com/iagox86/hash_extender)
    > PkCrack(https://github.com/keyunluo/pkcrack)
    > RSACTFTool(https://github.com/Ganapati/RsaCtfTool)
    > xortool(https://github.com/hellman/xortool)
    > padbuster(https://github.com/AonCyberLabs/PadBuster)
    > hash-identifier(https://github.com/blackploit/hash-identifier)
    > factordb(http://factordb.com/)
    > hashcat(https://github.com/hashcat/hashcat)
    > John The Ripper(https://github.com/openwall/john)
    > dcode.fr(https://www.dcode.fr/identification-chiffrement)
    > Substitution Solver(https://www.guballa.de/substitution-solver)
    > Vigenere Solver(https://www.guballa.de/vigenere-solver)
    > CyberChef(https://gchq.github.io/CyberChef/)
    """)

def Forensics():
    print("""
    --- Forensics ---
    > exiftool
    > binwalk
    > foremost
    > steghide 
    > fls
    > icat
    > stegoveritas(https://github.com/bannsec/stegoVeritas)
    > strong-qr-decoder(https://github.com/waidotto/strong-qr-decoder)
    > qrazybox(https://github.com/Merricx/qrazybox or https://h3110w0r1d.com/qrazybox/)
    > strings
    > ImageMagick(https://github.com/ImageMagick/ImageMagick)
    > CyberChef
    """)

def OSINT():
    print("""
    --- OSINT ---
    > OSINT Framework(https://osintframework.com/)
    > CheckUserNames(https://checkusernames.com/)
    > BeenVerified(https://www.beenverified.com/)
    > shodan(https://www.shodan.io/)
    > BuiltWith(https://builtwith.com/)
    > Google Dorks(https://securitytrails.com/blog/google-hacking-techniques)
    > Maltego(https://www.paterva.com/web7/downloads.php)
    > theHarvester(https://github.com/laramies/theHarvester)
    > SpiderFoot(http://www.spiderfoot.net/)
    > Jigsaw(https://www.jigsawsecurityenterprise.com/)
    > Creepy(https://www.geocreepy.com/)
    > Metagoofil(https://tools.kali.org/information-gathering/metagoofil)
    """)

def Web():
    print("""
    --- Web ---
    > ffuf(https://github.com/ffuf/ffuf)
    > commix(https://github.com/commixproject/commix)
    > wpscan(https://github.com/wpscanteam/wpscan)
    > OWASP-ZAP(https://www.zaproxy.org/)
    > postman(https://www.postman.com/)
    > raccoon(https://github.com/evyatarmeged/Raccoon)
    > sqlmap(https://github.com/sqlmapproject/sqlmap)
    > tplmap(https://github.com/epinna/tplmap)
    > xsser(https://github.com/epsylon/xsser)
    > SecLists(https://github.com/danielmiessler/SecLists)
    > git-dumper(https://github.com/arthaud/git-dumper)
    > Web-CTF-CheatSheet(https://github.com/w181496/Web-CTF-Cheatsheet)
    > WEB checklist(https://fareedfauzi.gitbook.io/ctf-checklist-for-beginner/web)
    """)

def Misc():
    print("""
    > CyberChef(https://gchq.github.io/CyberChef/)
    > impacket(https://github.com/SecureAuthCorp/impacket)
    > cmd5(http://cmd5.com/)
    > somd5(https://somd5.com/)
    > crackstation(https://crackstation.net/)
    > hashkiller(https://hashkiller.co.uk/)
    """)

def category():
    #art.tprint("CTF SUPPORT",font="cyber")
    print("""
    1) Pwn & Rev
    2) Crypto
    3) Forensics
    4) OSINT
    5) Web
    6) Misc
    
    0) Exit
    """)
    number = int(input("Number-> "))
    return number
    
def main():
    number = category()
    if number == 1:
        Pwn_Rev()
    elif number == 2:
        Crypto()
    elif number == 3:
        Forensics()
    elif number == 4:
        OSINT()
    elif number == 5:
        Web()
    elif number == 6:
        Misc()
    else:
        sys.exit(0)


if __name__ == '__main__':
    main()
