lfsr = 172 # initial seed in hex

# print first 20 output bits
for i in range(20):
    bit = ((lfsr >> 1) ^ (lfsr >> 5)) & 1
    lfsr = (lfsr >> 1) | (bit << 8)
    print("{}".format(bit))    