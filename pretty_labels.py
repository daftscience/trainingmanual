import os

print(os.getcwd())
with open("labels.tex") as f:
    content = f.readlines()


# String to search for: newlabel\{[^}]*\}

auxlines = []

start = False
stop = False
for line in content:

    if not start:
        if "CernerTrainingManual.aux" in line:
            start = True
    elif "OneDrive" in line:
            stop = True
    else:
        if len(line) > 5:
            if "@cref" not in line:
                if "gdef" not in line:
                    # print(line)
                    auxlines.append(line)


for line in auxlines:
    print(line)

with open("labels_stripped.tex", 'w') as f:

    for line in auxlines:
        new_line = line.replace("\label{", " & ")

        # print(line)


        if line != '\n':
            if "C:" not in line:
                new_line = line.split('}')
                new_line = new_line[0].split('{')
                if "@cref" not in new_line[-1]:
                        # print(new_line[-1])
                        if "part" not in new_line[-1]:
                            f.write('\t')
                        f.write(new_line[-1]+'\n')



auxlines.sort()
for i in range(0,len(auxlines)-1):
               if auxlines[i] == auxlines[i+1]:
                   print(str(auxlines[i]) + ' is a duplicate')