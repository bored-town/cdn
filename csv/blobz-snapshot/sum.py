from pprint import pprint as pp
import json

sources = [
    [
        '1_1.json',
        '1_2.json',
        '1_3.json',
    ],
    [
        '2_1.json',
        '2_2.json',
        '2_3.json',
        '2_4.json',
    ],
    [
        '3_1.json',
        '3_2.json',
    ],
    [
        '4_1.json',
        '4_2.json',
    ],
    [
        '5_1.json',
        '5_2.json',
    ],
]

chunk = {}

for ss in sources:
    ss_vote = 0
    for s in ss:
        with open(s, 'r') as file:
            json_data = json.load(file)
            votes = json_data['data']['votes']
            ss_vote += len(votes)

            for v in votes:
                voter = v['voter']
                chunk[voter] = (chunk.get(voter) or 0) + 1

    #print(ss_vote)
    #print('-'*10)

# reshape + sort
chunk = list(chunk.items())
chunk = sorted(chunk, key=lambda x: (-x[1], x[0]))

# print output
for c in chunk:
    print("{},{}".format(c[0], c[1]))
