# Read header and create dictionary
input_text = r"L:\groups\TSG\dataops\Social_Relations\Pretest\timing\ATreport\060914\temp.txt"

f = open(input_text, 'rb')
# Set the output file format #
c = csv.reader(f, delimiter='!')
d = {}
i = 0
for row in c:
    if i == 0:
        header = row
    else:
        d[i] = {}
        for h in range(0,len(header)):
            d[i][header[h]] = row[h]
    i = i + 1
print len(d)
print d[1]
