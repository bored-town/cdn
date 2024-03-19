#from web3.utils.address import to_checksum_address
from pprint import pprint as pp

SNAP_WL = [
    './snap_wl_x2/BLOBz Base.csv',
    './snap_wl_x2/BLOBz Mode.csv',
    './snap_wl_x2/BLOBz OP.csv',
    './snap_wl_x2/BLOBz Zora.csv',
]

SNAP_PB = [
    './snap_public_x15/BLOBz Base.csv',
    './snap_public_x15/BLOBz Mode.csv',
    './snap_public_x15/BLOBz OP.csv',
    './snap_public_x15/BLOBz Zora.csv',
]

ZERO_WALLET = '0x0000000000000000000000000000000000000000'

def load_dict_from_file(src):
    data = {}
    for line in open(src, 'r'):
        (addr, qty) = line.strip().split(',')
        if addr == ZERO_WALLET:
            continue
        data[addr.lower()] = int(qty)
    return data

def load_round(srcs):
    data = {}
    for src in srcs:
        for (addr, qty) in load_dict_from_file(src).items():
            if data.get(addr) is None:
                data[addr] = 0
            data[addr] += qty
    return data

data_wl = load_round(SNAP_WL)
data_pb = load_round(SNAP_PB)

pp(data_wl)
pp(data_pb)
