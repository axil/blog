import re
s = open(r'C:\Documents\blog\output\a-comprehensive-guide-to-numpy-data-types.html', encoding='utf8').read()
s = re.sub('<script.*?</script>', '', s, flags=re.S)
open(r'C:\Documents\blog\output\1.html', 'w', encoding='utf8').write(s)

