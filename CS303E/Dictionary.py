

def main():

    i = input("Enter string:")

    freqs = {}

    for ch in i:

        if ch != ' ':

            freqs[ch] = i.count(ch)

    print(freqs)
main()
