print ("""  ██████  ▄████▄   ██▓ ██▓███    ▄████ 
▒██    ▒ ▒██▀ ▀█  ▓██▒▓██░  ██▒ ██▒ ▀█▒
░ ▓██▄   ▒▓█    ▄ ▒██▒▓██░ ██▓▒▒██░▄▄▄░
  ▒   ██▒▒▓▓▄ ▄██▒░██░▒██▄█▓▒ ▒░▓█  ██▓
▒██████▒▒▒ ▓███▀ ░░██░▒██▒ ░  ░░▒▓███▀▒
▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░▓  ▒▓▒░ ░  ░ ░▒   ▒ 
░ ░▒  ░ ░  ░  ▒    ▒ ░░▒ ░       ░   ░ 
░  ░  ░  ░         ▒ ░░░       ░ ░   ░ 
      ░  ░ ░       ░                 ░ 
         ░                             """)

#fn is first name
fn = input ('Enter your First Name: ')
#mn is middle name
mn = input ('Enter your Middle Name: ')
#ln is last name
ln = input ('Enter your Last Name: ')
#nn is last name
nn = input ('Enter your Nickname: ')
#bm is birth month
bm = input ('Enter your Birth Month (decimals ex: 01) ')
#bd is birth date
bd = input ('Enter your Birth Date (decimals ex: 01) ')
#by is birth year
by = input ('Enter your Birth Year (decimals ex: 99) ')


#a single extra possible word used in the password
extra_question = input ('Is there any special word/number you would like to add (y/n)? ')

if extra_question == 'y':
    extras = input ('Input the word/number you would like to add! ')

elif extra_question == 'n':
    extras = 'nope'

cmnpasad = input ('Would you like to add ~200 common password to the list (y/n)? ')
if cmnpasad =='y':
    # Get the desired filename from the user
    file_name = input("Enter the desired filename (including extension, e.g., output.txt): ")

    # Open the file in write mode ('w')
    with open(file_name, 'w') as f:
        print (fn , file=f)
        print (mn , file=f)
        print (ln , file=f)
        print (nn , file=f)
        print (fn + bm + bd , file=f)
        print (mn + bm + bd , file=f)
        print (ln + bm + bd , file=f)
        print (nn + bm + bd , file=f)
        print (fn + bd + bm , file=f)
        print (mn + bd + bm , file=f)
        print (ln + bd + bm , file=f)
        print (nn + bd + bm , file=f)
        print (fn + bm + by , file=f)
        print (mn + bm + by , file=f)
        print (ln + bm + by , file=f)
        print (nn + bm + by , file=f)
        print (extras + fn + bm + bd , file=f)
        print (extras + mn + bm + bd , file=f)
        print (extras + ln + bm + bd , file=f)
        print (extras + nn + bm + bd , file=f)
        print (extras + fn + bd + bm , file=f)
        print (extras + mn + bd + bm , file=f)
        print (extras + ln + bd + bm , file=f)
        print (extras + nn + bd + bm , file=f)
        print (extras + fn + bm + by , file=f)
        print (extras + mn + bm + by , file=f)
        print (extras + ln + bm + by , file=f)
        print (extras + nn + bm + by , file=f)
        print (extras + bm + bd , file=f)
        print (extras + bd + bm , file=f)
        print (extras + bm + by , file=f)
        print (extras + fn , file=f)
        print (extras + mn , file=f)
        print (extras + ln , file=f)
        print (extras + nn , file=f)
        print (fn + extras , file=f)
        print (mn + extras , file=f)
        print (ln + extras , file=f)
        print (nn + extras , file=f)
        
        #2000s
        print (fn + bm + '20' + by , file=f)
        print (mn + bm + '20' + by , file=f)
        print (ln + bm + '20' + by , file=f)
        print (nn + bm + '20' + by , file=f)
        print (extras + fn + bm + '20' + by , file=f)
        print (extras + mn + bm + '20' + by , file=f)
        print (extras + ln + bm + '20' + by , file=f)
        print (extras + nn + bm + '20' + by , file=f)
        print (extras + bm + '20' + by , file=f)
        
        #1900s
        print (fn + bm + '19' + by , file=f)
        print (mn + bm + '19' + by , file=f)
        print (ln + bm + '19' + by , file=f)
        print (nn + bm + '19' + by , file=f)
        print (extras + fn + bm + '19' + by , file=f)
        print (extras + mn + bm + '19' + by , file=f)
        print (extras + ln + bm + '19' + by , file=f)
        print (extras + nn + bm + '19' + by , file=f)
        print (extras + bm + '19' + by , file=f)
        
        #most common password
        print ('123456' , file=f)
        print ('123456789' , file=f)
        print ('guest' , file=f)
        print ('qwerty' , file=f)
        print ('12345678' , file=f)
        print ('111111' , file=f)
        print ('12345' , file=f)
        print ('col123456' , file=f)
        print ('123123' , file=f)
        print ('1234567' , file=f)
        print ('1234' , file=f)
        print ('1234567890' , file=f)
        print ('000000' , file=f)
        print ('555555' , file=f)
        print ('666666' , file=f)
        print ('123321' , file=f)
        print ('654321' , file=f)
        print ('7777777' , file=f)
        print ('123' , file=f)
        print ('D1lakiss' , file=f)
        print ('777777' , file=f)
        print ('110110jp' , file=f)
        print ('1111' , file=f)
        print ('987654321' , file=f)
        print ('121212' , file=f)
        print ('Gizli' , file=f)
        print ('abc123' , file=f)
        print ('112233' , file=f)
        print ('azerty' , file=f)
        print ('159753' , file=f)
        print ('1q2w3e4r' , file=f)
        print ('54321' , file=f)
        print ('pass@123' , file=f)
        print ('222222' , file=f)
        print ('qwertyuiop' , file=f)
        print ('qwerty123' , file=f)
        print ('qazwsx' , file=f)
        print ('vip' , file=f)
        print ('asdasd' , file=f)
        print ('123qwe' , file=f)
        print ('123654' , file=f)
        print ('iloveyou' , file=f)
        print ('a1b2c3' , file=f)
        print ('999999' , file=f)
        print ('Groupd2013' , file=f)
        print ('1q2w3e' , file=f)
        print ('usr' , file=f)
        print ('Liman1000' , file=f)
        print ('1111111' , file=f)
        print ('333333' , file=f)
        print ('123123123' , file=f)
        print ('9136668099' , file=f)
        print ('11111111' , file=f)
        print ('1qaz2wsx' , file=f)
        print ('password1' , file=f)
        print ('mar20lt' , file=f)
        print ('987654321' , file=f)
        print ('gfhjkm' , file=f)
        print ('159357' , file=f)
        print ('abcd1234' , file=f)
        print ('131313' , file=f)
        print ('789456' , file=f)
        print ('luzit2000' , file=f)
        print ('aaaaaa' , file=f)
        print ('zxcvbnm' , file=f)
        print ('asdfghjkl' , file=f)
        print ('1234qwer' , file=f)
        print ('88888888' , file=f)
        print ('dragon' , file=f)
        print ('987654' , file=f)
        print ('888888' , file=f)
        print ('qwe123' , file=f)
        print ('football' , file=f)
        print ('3601' , file=f)
        print ('asdfgh' , file=f)
        print ('master' , file=f)
        print ('samsung' , file=f)
        print ('12345678910' , file=f)
        print ('killer' , file=f)
        print ('1237895' , file=f)
        print ('1234561' , file=f)
        print ('12344321' , file=f)
        print ('daniel' , file=f)
        print ('000000' , file=f)
        print ('444444' , file=f)
        print ('101010' , file=f)
        print ('qazwsxedc' , file=f)
        print ('789456123' , file=f)
        print ('super123' , file=f)
        print ('qwer1234' , file=f)
        print ('123456789a' , file=f)
        print ('823477aA' , file=f)
        print ('147258369' , file=f)
        print ('unknown' , file=f)
        print ('98765' , file=f)
        print ('q1w2e3r4' , file=f)
        print ('232323' , file=f)
        print ('102030' , file=f)
        print ('12341234' , file=f)
        print ('guest' , file=f)
        print ('123456' , file=f)
        print ('password' , file=f)
        print ('12345' , file=f)
        print ('a1b2c3' , file=f)
        print ('123456789' , file=f)
        print ('Password1' , file=f)
        print ('1234' , file=f)
        print ('abc123' , file=f)
        print ('12345678' , file=f)
        print ('qwerty' , file=f)
        print ('baseball' , file=f)
        print ('football' , file=f)
        print ('unknown' , file=f)
        print ('soccer' , file=f)
        print ('jordan23' , file=f)
        print ('iloveyou' , file=f)
        print ('monkey' , file=f)
        print ('shadow' , file=f)
        print ('g_czechout' , file=f)
        print ('1234567' , file=f)
        print ('1q2w3e4r' , file=f)
        print ('111111' , file=f)
        print ('fuckyou' , file=f)
        print ('princess' , file=f)
        print ('basketball' , file=f)
        print ('sunshine' , file=f)
        print ('jordan' , file=f)
        print ('michael' , file=f)
        print ('1234567890' , file=f)
        print ('reset' , file=f)
        print ('zinch' , file=f)
        print ('maiden' , file=f)
        print ('123123' , file=f)
        print ('81729373759' , file=f)
        print ('superman' , file=f)
        print ('hunter' , file=f)
        print ('anthony' , file=f)
        print ('maggie' , file=f)
        print ('super123' , file=f)
        print ('purple' , file=f)
        print ('love' , file=f)
        print ('ashley' , file=f)
        print ('andrew' , file=f)
        print ('justin' , file=f)
        print ('killer' , file=f)
        print ('pepper' , file=f)
        print ('tigger' , file=f)
        print ('buster' , file=f)
        print ('nicole' , file=f)
        print ('taylor' , file=f)
        print ('123' , file=f)
        print ('matthew' , file=f)
        print ('babygirl' , file=f)
        print ('michelle' , file=f)
        print ('cookie' , file=f)
        print ('jessica' , file=f)
        print ('datpiff' , file=f)
        print ('charlie' , file=f)
        print ('jasmine' , file=f)
        print ('peanut' , file=f)
        print ('abcd1234' , file=f)
        print ('cheese' , file=f)
        print ('brandon' , file=f)
        print ('hannah' , file=f)
        print ('pokemon' , file=f)
        print ('family' , file=f)
        print ('ginger' , file=f)
        print ('1qaz2wsx' , file=f)
        print ('hello' , file=f)
        print ('computer' , file=f)
        print ('joshua' , file=f)
        print ('money' , file=f)
        print ('letmein' , file=f)
        print ('yankees' , file=f)
        print ('bailey' , file=f)
        print ('hockey' , file=f)
        print ('batman' , file=f)
        print ('diamond' , file=f)
        print ('madison' , file=f)
        print ('michael1' , file=f)
        print ('amanda' , file=f)
        print ('thomas' , file=f)
        print ('passw0rd' , file=f)
        print ('harley' , file=f)
        print ('jennifer' , file=f)
        print ('music' , file=f)
        print ('daniel' , file=f)
        print ('samantha' , file=f)
        print ('mustang' , file=f)
        print ('freedom' , file=f)
        print ('robert' , file=f)
        print ('whatever' , file=f)
        print ('summer' , file=f)
        print ('asdfghjkl' , file=f)
        print ('football1' , file=f)
        print ('brooklyn' , file=f)
        print ('654321' , file=f)
        print ('william' , file=f)
        print ('trustno1' , file=f)

elif cmnpasad == 'n':
     # Get the desired filename from the user
    file_name = input("Enter the desired filename (including extension, e.g., output.txt): ")

    # Open the file in write mode ('w')
    with open(file_name, 'w') as f:
        print (fn , file=f)
        print (mn , file=f)
        print (ln , file=f)
        print (nn , file=f)
        print (fn + bm + bd , file=f)
        print (mn + bm + bd , file=f)
        print (ln + bm + bd , file=f)
        print (nn + bm + bd , file=f)
        print (fn + bd + bm , file=f)
        print (mn + bd + bm , file=f)
        print (ln + bd + bm , file=f)
        print (nn + bd + bm , file=f)
        print (fn + bm + by , file=f)
        print (mn + bm + by , file=f)
        print (ln + bm + by , file=f)
        print (nn + bm + by , file=f)
        print (extras + fn + bm + bd , file=f)
        print (extras + mn + bm + bd , file=f)
        print (extras + ln + bm + bd , file=f)
        print (extras + nn + bm + bd , file=f)
        print (extras + fn + bd + bm , file=f)
        print (extras + mn + bd + bm , file=f)
        print (extras + ln + bd + bm , file=f)
        print (extras + nn + bd + bm , file=f)
        print (extras + fn + bm + by , file=f)
        print (extras + mn + bm + by , file=f)
        print (extras + ln + bm + by , file=f)
        print (extras + nn + bm + by , file=f)
        print (extras + bm + bd , file=f)
        print (extras + bd + bm , file=f)
        print (extras + bm + by , file=f)
        print (extras + fn , file=f)
        print (extras + mn , file=f)
        print (extras + ln , file=f)
        print (extras + nn , file=f)
        print (fn + extras , file=f)
        print (mn + extras , file=f)
        print (ln + extras , file=f)
        print (nn + extras , file=f)
        
        #2000s
        print (fn + bm + '20' + by , file=f)
        print (mn + bm + '20' + by , file=f)
        print (ln + bm + '20' + by , file=f)
        print (nn + bm + '20' + by , file=f)
        print (extras + fn + bm + '20' + by , file=f)
        print (extras + mn + bm + '20' + by , file=f)
        print (extras + ln + bm + '20' + by , file=f)
        print (extras + nn + bm + '20' + by , file=f)
        print (extras + bm + '20' + by , file=f)
        
        #1900s
        print (fn + bm + '19' + by , file=f)
        print (mn + bm + '19' + by , file=f)
        print (ln + bm + '19' + by , file=f)
        print (nn + bm + '19' + by , file=f)
        print (extras + fn + bm + '19' + by , file=f)
        print (extras + mn + bm + '19' + by , file=f)
        print (extras + ln + bm + '19' + by , file=f)
        print (extras + nn + bm + '19' + by , file=f)
        print (extras + bm + '19' + by , file=f)