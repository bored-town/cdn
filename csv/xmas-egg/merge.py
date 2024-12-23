from web3.utils.address import to_checksum_address
from pprint import pprint as pp
import json

snapshot = [
    '../../../rocketship-pass/snapshot/Rocketship Biz Arb.csv',
    '../../../rocketship-pass/snapshot/Rocketship Biz Metis.csv',
    '../../../rocketship-pass/snapshot/Rocketship Biz Mode.csv',
    '../../../rocketship-pass/snapshot/Rocketship Biz Nova.csv',
    '../../../rocketship-pass/snapshot/Rocketship Biz OP.csv',
    '../../../rocketship-pass/snapshot/Rocketship Biz Zora.csv',
    '../../../rocketship-pass/snapshot/Rocketship Eco Arb.csv',
    '../../../rocketship-pass/snapshot/Rocketship Eco Metis.csv',
    '../../../rocketship-pass/snapshot/Rocketship Eco Mode.csv',
    '../../../rocketship-pass/snapshot/Rocketship Eco Nova.csv',
    '../../../rocketship-pass/snapshot/Rocketship Eco OP.csv',
    '../../../rocketship-pass/snapshot/Rocketship Eco Zora.csv',
    '../../../rocketship-pass/snapshot/Rocketship First.csv',
]
ban_addrs = [
    '0x0000000000000000000000000000000000000000',
    '0x000000000000000000000000000000000000dEaD',
]

wl = set()

# merge all addresses to wl
for csv in snapshot:
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
