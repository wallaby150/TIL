N = int(input())
dna = list(input())
rule = {"AA": "A", "AG": "C", "AC": "A", "AT": "G", "GA": "C", "GG": "G",
        "GC": "T", "GT": "A", "CA": "A", "CG": "T", "CC": "C", "CT": "G",
        "TA": "G", "TG": "A", "TC": "G", "TT": "T"}

while len(dna) > 1:
    last = dna.pop() + dna.pop()
    dna.append(rule[last])

print(dna[0])
