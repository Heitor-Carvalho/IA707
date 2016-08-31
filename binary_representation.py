import numpy


class BinRepresentation(object):
    
    def get_bin_repr(self, number, max_dec):
        'From positive integer to list of binary bits, msb at index 0'
        n = int(number*10**max_dec)
        if n:
            bits = []
            while n:
                n,remainder = divmod(n, 2)
                bits.insert(0, remainder)
            return bits
        else: 
            return [0]

    def get_real_from_bin(self, bits):
        'From binary bits, msb at index 0 to integer'

        i = 0
        for bit in bits:
            i = i * 2 + bit

        return i
    
    def get_gray_repr(self, number, max_dec):
        bits = self.get_bin_repr(number, max_dec)
        return bits[:1] + [i ^ ishift for i, ishift in zip(bits[:-1], bits[1:])]

    def get_real_from_gray(self, bits):

        b = [bits[0]]
        for nextb in bits[1:]:
            b.append(b[-1] ^ nextb)

        return self.get_real_from_bin(b)



class Representation(object):

    def get_representation(self):
        pass

    def get_original_value(self):
    	pass


    	
def main():
    bin_repr = BinRepresentation()
    for i in range(1, 10):
        bits = bin_repr.get_bin_repr(i, 0)
        print bits, bin_repr.get_real_from_bin(bits)

    for i in range(1, 10):
        gray = bin_repr.get_gray_repr(i, 0)
        print gray, bin_repr.get_real_from_gray(gray)


if __name__ == '__main__':
    main()