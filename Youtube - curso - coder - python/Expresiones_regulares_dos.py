# Rangos, rangos negados, clases predefinidas, cuantificadores etc.


import re
cadena = "abcdef qhi"\
        "8123456789-"


# print(re.findall("[a-d2-5]", cadena))

print(re.findall("[\d]", cadena))