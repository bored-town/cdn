from web3.utils.address import to_checksum_address
from pprint import pprint as pp

src_zora = '../../docs/blobz-mint/zora.csv'
src_mode = '../../docs/blobz-mint/mode.csv'
#src_ss   = '../blobz-snapshot/sum.csv'

def load_mint_data(src):
    result = []
    with open(src, "r") as file:
      lines = file.readlines()[1:] # skip header line
      for line in lines:
        [ _, addr, wl, pb, qty ] = line.strip().split(',')
        # cast
        addr = addr.lower() # lower
        wl = int(wl)
        pb = int(pb)
        qty = int(qty)
        # append
        result.append((addr, wl, pb, qty))
    return result

chunk = {}

# load zora
for (addr, wl, pb, qty) in load_mint_data(src_zora):
    chunk[addr] = {
        'addr'    : addr,
        'zora_wl' : wl,
        'zora_pb' : pb,
        'mode_wl' : 0,
        'mode_pb' : 0,
        'blobz'   : qty,
    }

# load mode
for (addr, wl, pb, qty) in load_mint_data(src_mode):
    if chunk.get(addr) is None:
        chunk[addr] = {
            'addr'    : addr,
            'zora_wl' : 0,
            'zora_pb' : 0,
            'blobz'   : 0,
        }
    chunk[addr]['mode_wl'] = wl
    chunk[addr]['mode_pb'] = pb
    chunk[addr]['blobz']  += qty

# load snapshot
#with open(src_ss, "r") as file:
#  lines = file.readlines()
#  for line in lines:
#    [ addr, votes ] = line.strip().split(',')
#    # cast
#    addr = addr.lower() # lower
#    votes = int(votes)
#    # update chunk
#    if chunk.get(addr) is None:
#        chunk[addr] = { 'addr': addr }
#    chunk[addr]['votes'] = votes

# reshape + sort
chunk = [ c for c in chunk.values() ]
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
print("#,Address,$BLOBZ,Zora WL,Zora Public,Mode WL,Mode Public")
for c in chunk:
    no      = c['no']
    addr    = to_checksum_address(c['addr'])
    zora_wl = c['zora_wl']
    zora_pb = c['zora_pb']
    mode_wl = c['mode_wl']
    mode_pb = c['mode_pb']
    blobz   = c['blobz']
    print("{},{},{},{},{},{},{}".format(no, addr, blobz, zora_wl, zora_pb, mode_wl, mode_pb))
