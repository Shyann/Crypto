def rc4(key):
    s = range(256)

    # key scheduling algorithm
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]

    # output first 20 bytes
    i = 0
    j = 0
    for i in range(20):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        k = s[(s[i] + s[j]) % 256]
        print k
    
rc4([1,2,3])