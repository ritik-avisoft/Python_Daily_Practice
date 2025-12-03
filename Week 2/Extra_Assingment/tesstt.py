import re
text = "#python is awesome! I also like #coding"
temp=re.findall(r"^#\w" \
"", text)
print(temp)