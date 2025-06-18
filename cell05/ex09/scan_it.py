import sys
import re
if len(sys.argv) != 3:
    print("none")
    sys.exit
keyword = sys.argv[1]
text = sys.argv[2]
pattern = f'(?={re.escape(keyword)})'
matches = re.findall(pattern, text)
if not matches :
    print("none")
else:
    print(len(matches))