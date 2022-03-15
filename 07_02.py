# Use the file name mbox-short.txt as the file name
fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('File does not exist:', fname)
    quit()
count = 0
confidence = 0
for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    if line.startswith('X-DSPAM-Confidence:'):
        line.rstrip()
        count = count + 1
        print(line)
print('Done')
