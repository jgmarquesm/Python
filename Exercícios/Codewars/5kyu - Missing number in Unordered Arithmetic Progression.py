def find(seq):
    seq.sort()
    d=min(seq[1]-seq[0],seq[-1]-seq[-2])
    for i in range(1,len(seq)):
        if seq[i]-seq[i-1]!=d:
            return seq[i-1]+d