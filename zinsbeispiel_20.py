# python Zinsbeispiel mit 20 % Verzinsung per anno. Zins wird jährlich abgerechnet (bei Krediten i.d.R. monatlich)
import sys
#print len(sys.argv)
if len(sys.argv) != 3:
	print ('Usage zinsbeispiel Startanlagebetrag Monatl_Anlagebetrag ')
	exit(0)
else:
	pass
try:
	a1=float(sys.argv[1])
except ValueError:
	print ('Usage zinsbeispiel Startanlagebetrag Monatl_Anlagebetrag ')
	print (' Die Beträge müssen numerisch sein')
	exit(0)
try:
	a2=float(sys.argv[2])
except ValueError:
	print ('Usage zinsbeispiel Startanlagebetrag Monatl_Anlagebetrag ')
	print (' Die Beträge müssen numerisch sein')
	exit(0)

i1=1.4
a4=a1*i1
a3=a1*i1 + a2*11 + a2*66/12*(i1-1) 
#for i in range(1,11): Don't need the loop any more. A loop would be needed für mon. Zinszahlungen
print ('Einmalanlagebetrag verzinst:' + str(a4))
print ('zus. Anlage ' + str(a2))
a4+= a2*12
print ('Zins für zus. Anlage=a2*1,4*131/12:' + str(a2*(i1-1)/12*132/2))
a4+=a2*(i1-1)/12*132/2
#	a4+= a2*(i1-1)+a2*(i1-1)/12 eh falsch
print ('Endbetrag ohne Zinseszins:' + str(a3))
print ('Endbetrag mit Zinseszins:'	 + str(a4))

	