# import json

# def read_file(filePath):
#     file = open(filePath, "r")
#     content = file.read()
#     file.close()
#     return content
    
    
# def read_json(filePath):
#     file = open(filePath)
#     data = json.load(file)
#     file.close()
#     return data



def read_blocks(input_file, i, j):
    empty_lines = 0
    blocks = []
    for line in open(input_file):
        # Check for empty/commented lines
        if not line or line.startswith(".I"):
            # If 1st one: new block
            if empty_lines == 0:
                blocks.append([])
            empty_lines += 1
        # Non empty line: add line in current(last) block
        else:
            empty_lines = 0
            blocks[-1].append(" ".join(str(line).split()))
    return blocks[i:j+1]


def blockToString(b):
    r=""
    for l in b:
        r=r+str(l)+" "
    return r



def docsAsStrings(dataset):
    das=[]
    if dataset=="CISI":
        B= read_blocks('CISI.txt', 0, 1460)
    elif dataset=="cacm":
        B=read_blocks('cacm.txt', 0, 3204)

    for b in B: 
        das.append(blockToString(b)) 
    return das

