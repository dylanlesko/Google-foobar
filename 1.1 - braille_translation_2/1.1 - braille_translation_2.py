def answer(plaintext):

    encoding = {}
    encoding['a'] =     '100000'
    encoding['b'] =     '110000'
    encoding['c'] =     '100100'
    encoding['d'] =     '100110'
    encoding['e'] =     '100010'
    encoding['f'] =     '110100'
    encoding['g'] =     '110110'
    encoding['h'] =     '110010'
    encoding['i'] =     '010100'
    encoding['j'] =     '010110'
    encoding['k'] =     '101000'
    encoding['l'] =     '111000'
    encoding['m'] =     '101100'
    encoding['n'] =     '101110'
    encoding['o'] =     '101010'
    encoding['p'] =     '111100'
    encoding['q'] =     '111110'
    encoding['r'] =     '111010'
    encoding['s'] =     '011100'
    encoding['t'] =     '011110'
    encoding['u'] =     '101001'
    encoding['v'] =     '111001'
    encoding['w'] =     '010111'
    encoding['x'] =     '101101'
    encoding['y'] =     '101111'
    encoding['z'] =     '101011'
    encoding[' '] =     '000000'
    
    output = ''
    for i in range(len(plaintext)):
        if plaintext[i].istitle():
            output = output + '000001'
        output = output + encoding[plaintext[i].lower()]
        
    return output

print answer('The quick brown fox jumps over the lazy dog')