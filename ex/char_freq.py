
st = input("Enter string :")

freq = {}

# for ch in st:
#     if ch not in freq:
#         freq[ch] = st.count(ch)

for ch in set(st):
   freq[ch] = st.count(ch)


for c,cnt in sorted(freq.items()):
    print(c, cnt)

