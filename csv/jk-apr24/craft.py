from web3.utils.address import to_checksum_address
from pprint import pprint as pp

src = './3960_JK_Giveaway_40_2024_04_15_14_18.csv'
qty = 3960 / 40

wl = [ line.strip().split(',')[0].lower() for line in open(src, 'r') ]
wl = wl[1:] # remove header

for w in sorted(wl):
    print("{},{}".format(
        to_checksum_address(w),
        int(qty),
    ))
