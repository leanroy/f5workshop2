from dns.resolver import Resolver
import csv

my1_r = Resolver()
my1_r.nameservers = ['8.8.8.8']
my2_r = Resolver()
my2_r.nameservers = ['8.8.4.4']

# Create empty dictionaries
names = {}
resolved1 = {}
resolved2 = {}

# Open toresolve.csv file and populate dictionary names
with open('toresolve.csv', mode='r') as infile:
    reader = csv.reader(infile)
    names = dict((rows[0],0) for rows in reader)
    infile.close()

print("Using server: ",my1_r.nameservers)

for x in names:
   try:
      hostip = my1_r.resolve(x,raise_on_no_answer=False)
   except:
      hostip = 'None'
   resolved1[x] = str(hostip.rrset[0])

print(resolved1)

print("""-------
-------
Using server: """,my2_r.nameservers)

for x in names:
   try:
      hostip = my2_r.resolve(x,raise_on_no_answer=False)
   except:
      hostip = 'None'
   resolved2[x] = str(hostip.rrset[0])

print(resolved2)
