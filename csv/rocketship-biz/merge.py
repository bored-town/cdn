from web3.utils.address import to_checksum_address
from pprint import pprint as pp

csv_list = [
    './All Bored Town Collections.csv',
    './Space BLOBz Tier A.csv',
    './Space BLOBz Tier B.csv',
    './Space BLOBz Tier C.csv',
    './Space BLOBz Tier S.csv',
    './Tripster Travel Pass.csv',
]

wl = set()

for csv in csv_list:
    data = [ line.strip().split(',')[0].lower() for line in open(csv, 'r') ]
    wl.update(data)
    #print(csv)
    #print(len(data))
#exit()

for w in sorted(wl):
    print("{},0".format(to_checksum_address(w)))
