import gzip, json
import random

LIMERICK_ID = [45482, 56697, 982, 13646, 13648, 13650]
def main():
    all_lines = []
    for line in gzip.open("gutenberg-poetry-v001.ndjson.gz"):
        poem_line = json.loads(line.strip())
        if int(poem_line['gid']) in LIMERICK_ID:
            all_lines.append(poem_line['s'])
    print(len(all_lines))  
    stringPoem = '\n'.join(str(line) for line in all_lines) 
    print(stringPoem)
    
    
    limerick = False
    corpus = []

    """
    while not limerick:
        print(line)
        for component in line:
            if int(component['gid']) in LIMERICK_ID:
                limerick = True   
            else:
                line = random.sample(all_lines, 1)
    print(line)
    """

if __name__ == "__main__":
    main()