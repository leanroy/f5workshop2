from dns.resolver import Resolver

my1_r = Resolver()
my1_r.nameservers = ['8.8.8.8']

names = ['secure.worldpay.com','cisco.com']
print("Using server: ",my1_r.nameservers)

for name in names:
    print("-")
    for qtype in 'A', 'CNAME':
        answer1 = my1_r.query(name,qtype,raise_on_no_answer=False)
        if answer1.rrset is not None:
            print(answer1.rrset)


my2_r = Resolver()
my2_r.nameservers = ['8.8.4.4']

print("""-------
-------
Using server: """,my2_r.nameservers)

for name in names:
    print("-")
    for qtype in 'A', 'CNAME':
        answer2 = my2_r.query(name,qtype,raise_on_no_answer=False)
        if answer2.rrset is not None:
            print(answer2.rrset)


