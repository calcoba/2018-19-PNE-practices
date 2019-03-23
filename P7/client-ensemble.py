import requests
import sys
from SeqP7 import Seq

# Connecting to the ensemble database to get the info
server = "http://rest.ensembl.org"
ext = "/sequence/id"
headers = {"Content-Type": "application/json", "Accept": "application/json"}
r = requests.post(server + ext, headers=headers, data='{ "ids" : ["ENSG00000165879"]}')

if not r.ok:
    r.raise_for_status()
    sys.exit()

decoded = r.json()

# Get the seq from the received message and p convert it to an object
seq = Seq(decoded[-1]['seq'])

# Do the requested calculation
bases = set(seq.strbases)
perc_bases = {}
count_bases = {}
total_len = seq.len()

for base in bases:
    perc_bases.update({base: seq.perc(base)})
    count_bases.update({base: seq.count(base)})
max_perc = max(perc_bases.items(), key=lambda x: x[1])

# Printing the results
print("The FRAT1 gen has {} bases.".format(total_len))
print("There are {} T bases in the FRAT1 gene.".format(count_bases["T"]))
print("The most popular base in the FRAT1 gene is {} and it represents the {}%.".format(max_perc[0], max_perc[1]))
print("The percentage for every base in the FRAT1 gene are {}.".format(perc_bases))
