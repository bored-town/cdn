from web3.utils.address import to_checksum_address
from pprint import pprint as pp

SNAP_WL = [
    './snap_wl_x2/BLOBz Base.csv',
    #'./snap_wl_x2/BLOBz Mode.csv',
    #'./snap_wl_x2/BLOBz OP.csv',
    #'./snap_wl_x2/BLOBz Zora.csv',
]

SNAP_PB = [
    './snap_public_x15/BLOBz Base.csv',
    #'./snap_public_x15/BLOBz Mode.csv',
    #'./snap_public_x15/BLOBz OP.csv',
    #'./snap_public_x15/BLOBz Zora.csv',
]

ZERO_WALLET  = '0x0000000000000000000000000000000000000000'
BLOBZ_PER_WL = 1_000_000
BLOBZ_PER_PB =   750_000

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

def calc_blobz(info):
    (wl, pb) = (info['wl'], info['pb'])

    # 0) no nft left on public
    if pb == 0:
        return 0
    # 1) mint public only
    elif wl == 0:
        return pb * BLOBZ_PER_PB
    # 2.1) mint wl and transfer some out
    # 2.2) mint wl only
    elif wl >= pb:
        return pb * BLOBZ_PER_WL
    # 3) mint wl & tranfer some pb in
    else:
        from_pb = pb - wl
        return (wl * BLOBZ_PER_WL) + (from_pb * BLOBZ_PER_PB)

# load mint data
data_wl = load_round(SNAP_WL)
data_pb = load_round(SNAP_PB)

# combine 2 rounds
chunk = {}
for (addr, qty) in data_wl.items():
    chunk[addr] = { 'addr': addr, 'wl': qty, 'pb': 0 }
for (addr, qty) in data_pb.items():
    if chunk.get(addr) is None:
        chunk[addr] = { 'addr': addr, 'wl': 0, 'pb': 0 }
    chunk[addr]['pb'] = qty

# reshape to list
chunk = chunk.values()

# calc blobz
for c in chunk:
    c['blobz'] = calc_blobz(c)

# remove 0 BLOBz, sort from max to min
chunk = filter(lambda c: c['blobz'] > 0, chunk)
chunk = sorted(chunk, key=lambda c: (-c['blobz'], c['addr']))

# add no
cur_no = None
cur_points = None
for (idx, info) in enumerate(chunk):
    if info['blobz'] != cur_points:
        cur_no = idx + 1
        cur_points = info['blobz']
    info['no'] = cur_no

# print output
print("#,Address,WL,Public,$BLOBZ")
for c in chunk:
    (no, addr, wl, pb, blobz) = (c['no'], c['addr'], c['wl'], c['pb'], c['blobz'])
    print('{},{},{},{},{}'.format(no, to_checksum_address(addr), wl, pb, blobz))
