#! python Verzinsungsermittlung in Fonds mit Einmalanlage und monatlicher Anlage eines Festbetrages
# Szenario: Anlage von a1 Euro zum Zeitpunkt t1, a2 1 Monat später, a2 1 Monat später, a2 1 Monat später,.... ein ganzes Jahr, Wert a3 nach 1 Jahr
# Also zinsermittlung a1 a2 a3
# Umschreiben: Der Endwert muss ermittelt werden wie in Zinsbeispiel.py. Der Zinssatz wird probiert in einer Schleife wie bisher. Evtl. aufpeppen um die Schrittweite als zus. Argument einzugeben. Diese Idee berücksichtigt aber den Zinseszins nicht, das fehlt noch.
import sys
if len(sys.argv) != 4:
	print 'Usage zinsermittlung Startanlagebetrag Monatl_Anlagebetrag Endwert'
	exit(0)
else:
	pass
try:
	a1=float(sys.argv[1])
except ValueError:
	print 'Usage zinsermittlung Startanlagebetrag Monatl_Anlagebetrag Endwert'
	print ' Die Beträge müssen numerisch sein'
	exit(0)
try:
	a2=float(sys.argv[2])
except ValueError:
	print 'Usage zinsermittlung Startanlagebetrag Monatl_Anlagebetrag Endwert'
	print ' Die Beträge müssen numerisch sein'
	exit(0)
try:
	a3=float(sys.argv[3])
except ValueError:
	print 'Usage zinsermittlung Startanlagebetrag Monatl_Anlagebetrag Endwert'
	print ' Die Beträge müssen numerisch sein'
	exit(0)
# Trying to find an approximate solution by probing different interest rates
i1=0

print 'Start Iteration'
while (i1<10):
	i1+=.01
	print 'Zinssatz:'+str(i1)
	a4=a1*(1+i1) + a2*12 + a2*i1*66/12
# Die Formel am Ende stellt den anteiligen Jahreszins dar für den monatl. Anlagebetrag

#	print 'Endbetrag a3:' + str(a3)
#	print 'Verz.Startbetrag:'+str(a1*(1+i1))

#	print 'Zusatzanlage:' + str(a2*12)
	print 'Zins:' + str(i1)
#	print 'Summe a4:' + str(a4)
#	print 'Differenz a4-a3:'+str(a4-a3)
#	print 'Test a4==a3:' + str(a4==a3)
#	print 'Print a4-a3:'+str(a4-a3)
#	b=raw_input	()

	
	if (a4>a3):

		print 'Zins ist unter' + str(i1) + ' also aus'
		quit()
		
	elif a4==a3:
		print 'Zins ist exakt' + str(i1)
		quit()
	else:
	# Zins ist über i1, also weiter

		print'Zins ist über:' + str(i1) + ' also weiter'
		pass

		