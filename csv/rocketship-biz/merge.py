from web3.utils.address import to_checksum_address
from pprint import pprint as pp

csv_list = [
    './All Bored Town Collections.csv',
    './Space BLOBz Tier A.csv',
    './Space BLOBz Tier B.csv',
    './Space BLOBz Tier C.csv',
    './Space BLOBz Tier S.csv',
    './Tripster Travel Pass.csv',
    # TODO referal program
]
ban_addrs = [
    '0x0000000000000000000000000000000000000000',
    '0x000000000000000000000000000000000000dEaD',
]

wl = set()

# merge all addresses to wl
for csv in csv_list:
    data = [ line.strip().split(',')[0].lower() for line in open(csv, 'r') ]
    wl.update(data)
    #print(csv)
    #print(len(data))
#exit()

# remove ban addresses
for addr in ban_addrs:
    wl.discard(addr.lower())

# print output
for w in sorted(wl):
    print("{},0".format(to_checksum_address(w)))
