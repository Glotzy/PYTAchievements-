Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
KeyboardInterrupt
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> # Verander <JOUW NAAM HIER> in je eigen naam
>>> print('Mijn naam is <JOUW NAAM HIER>')
Mijn naam is <JOUW NAAM HIER>
>>> naam = '<JOUW NAAM HIER>'
>>> print(naam)
<JOUW NAAM HIER>
>>> print(naam.upper())
<JOUW NAAM HIER>
>>> print(naam[0:2])
<J
>>> print(naam[::-1])
>REIH MAAN WUOJ<
>>> # Verander dit in je eigen leeftijd
>>> leeftijd = 15print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
SyntaxError: invalid syntax
>>> leeftijd = 15
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo <JOUW NAAM HIER> ben je al 15 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
16
>>> leeftijd-=1
>>> leeftijd
15
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	 print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
	 
SyntaxError: unexpected indent
>>>  print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
 
SyntaxError: unexpected indent
>>> print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
NameError: name 'hoelang_tot18jaar' is not defined
>>> 
KeyboardInterrupt
>>> if leeftijd < 18:
	hoelang_tot18jaar = 18 - leeftijd
	print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
	
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> elif leeftijd > 18:
	
SyntaxError: invalid syntax
>>> elif leeftijd > 18:
	
SyntaxError: invalid syntax
>>>  hoelang_al18jaar = leeftijd - 18
 
SyntaxError: unexpected indent
>>> 
KeyboardInterrupt
>>> hoelang_al18jaar = leeftijd - 18
>>> print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
Het is alweer -3 jaar geleden dat je 18 werd ;-)
>>> else:
	
SyntaxError: invalid syntax
>>> print('Je bent precies ' + str(leeftijd) + ' jaar')
Je bent precies 15 jaar
>>> # Let op: hier 2x een enter doen!
>>> # Willekeurige getallen genereren
>>> from random import randint
>>> randint(0,1000)
873
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
933
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))

Willekeurig getal tussen 0 en 1000: 933
>>> # Datum en tijd
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-18 11:56:02.678592
>>> datum.strftime('%A %d %B %Y')
'Friday 18 September 2020'
>>> # Nu in een andere taal
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'vrijdag 18 september 2020'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'venerdì 18 settembre 2020'
>>> 