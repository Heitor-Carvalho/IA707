import numpy as np

# TO DO: Use numpy bool array, option to show number

bin_repr_par = {'min_val': -2, 'max_val': 16, 'seq_len': 10}


class BinRepresentation(object):
    
    def __init__(self, bin_repr_par):
        self.bin_parameters = bin_repr_par


    def get_bin_repr(self, number):
        'From positive integer to list of binary bits, msb at index 0'

        number = float(number)
        number = (number - self.bin_parameters["min_val"])/(self.bin_parameters["max_val"] - self.bin_parameters["min_val"])
        number = int(number*2**self.bin_parameters["seq_len"])

        if number:
            bits = []
            while number:
                number,remainder = divmod(number, 2)
                bits.insert(0, remainder)
            i = len(bits)
            while i < self.bin_parameters["seq_len"]:
                bits.insert(0, 0)
                i += 1
            return np.array(bits).astype('bool')
        else: 
            return np.array([0]*self.bin_parameters["seq_len"]).astype('bool')

    def get_real_from_bin(self, bits):
        'From binary bits, msb at index 0 to integer'
        
        i = float(0)
        for bit in bits.astype('int'):
            i = i * 2 + bit
        
        return (i/2**self.bin_parameters["seq_len"])*(self.bin_parameters["max_val"] - self.bin_parameters["min_val"]) + self.bin_parameters["min_val"]

    
    def get_gray_repr(self, number):
        bits = self.get_bin_repr(number).astype('int').tolist()
        return np.array(bits[:1] + [i ^ ishift for i, ishift in zip(bits[:-1], bits[1:])]).astype('bool')

    def get_real_from_gray(self, bits):
        bits = bits.astype('int')
        b = [bits[0]]
        for nextb in bits[1:]:
            b.append(b[-1] ^ nextb)
        
        return self.get_real_from_bin(np.array(b).astype('bool'))

 	
def main():
    bin_repr = BinRepresentation(bin_repr_par)
    for i in range(1, 11):
        bits = bin_repr.get_bin_repr(i)
        print bits.astype('int'), bin_repr.get_real_from_bin(bits)

    for i in range(1, 11):
        gray = bin_repr.get_gray_repr(i)
        print gray.astype('int'), bin_repr.get_real_from_gray(gray)


if __name__ == '__main__':
    main()