#from web3.utils.address import to_checksum_address
from pprint import pprint as pp

"""
csv_bt       = './bt_full.csv'
csv_tripster = './tripster.csv'
csv_wally    = './wally_zksync.csv' # fix zksync snap not complete

addr_bt       = [ line.strip().split(',')[0].lower() for line in open(csv_bt, 'r') ]
addr_tripster = [ line.strip().lower() for line in open(csv_tripster, 'r') ]
addr_wally    = [ line.strip().split(',')[0].lower() for line in open(csv_wally, 'r') ]

wl = set(addr_bt + addr_tripster + addr_wally)

for w in sorted(wl):
    print("{},0".format(to_checksum_address(w)))
"""

snap_wl = [
    './snap_wl_x2/BLOBz Base.csv',
    './snap_wl_x2/BLOBz Mode.csv',
    './snap_wl_x2/BLOBz OP.csv',
    './snap_wl_x2/BLOBz Zora.csv',
]

for src in snap_wl:
    amount = sum([ int(line.strip().split(',')[1]) for line in open(src, 'r') ])
    print(src, amount)
