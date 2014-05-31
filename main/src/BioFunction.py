# Special Bioinformatics function

def readFASTA(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line[1:], []       #Убирает знак ">" из имени
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))