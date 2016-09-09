from numpy import *

# TO DO: Use numpy bool array, option to show number

bin_repr_par = {'min_val': -30, 'max_val': 21, 'seq_len': 32}


class BinRepresentation(object):
    
    def __init__(self, bin_repr_par):
        self.bin_parameters = bin_repr_par

    def normalize(self, number_array):
        number_array = (number_array - self.bin_parameters["min_val"]).astype('float')/(self.bin_parameters["max_val"] - self.bin_parameters["min_val"])
        return (number_array*2**self.bin_parameters["seq_len"]).astype('int')

    def unnormalize(self, number_array):
        return (number_array/2**self.bin_parameters["seq_len"])*(self.bin_parameters["max_val"] - self.bin_parameters["min_val"]) + self.bin_parameters["min_val"]

    def get_bin_repr(self, number_array):
        norm_array = self.normalize(number_array)
        import pdb; pdb.set_trace()
        return array([array(map(int, list(binary_repr(nb, self.bin_parameters["seq_len"])))).astype('bool') for nb in norm_array])

    def get_gray_repr(self, number_array):
        bits_array = self.get_bin_repr(number_array).tolist()
        return array([array(bits[:1] + [i ^ ishift for i, ishift in zip(bits[:-1], bits[1:])]) for bits in bits_array]) 

    def get_real_from_bin(self, bits_array):

        real_number = []
        for bits in bits_array: 
            i = float(0)
            for bit in bits.astype('int'):
                i = i * 2 + bit
            real_number.append(self.unnormalize(i))

        return array(real_number)

    def get_real_from_gray(self, bits_array):
        
        bin_bits = []
        for gray in bits_array:
            bits = gray.astype('int')
            b = [bits[0]]
            for nextb in bits[1:]:
                b.append(b[-1] ^ nextb)
            bin_bits.append(b)

        return self.get_real_from_bin(array(bin_bits).astype('bool'))

    
def main():

    bin_repr = BinRepresentation(bin_repr_par)

    bits = bin_repr.get_bin_repr(array([1, 2, 3, 4, 5]))
    print bits.astype('int'), bin_repr.get_real_from_bin(bits)

    bits = bin_repr.get_gray_repr(array([1, 2, 3, 4, 5]))
    print bits.astype('int'), bin_repr.get_real_from_gray(bits)

if __name__ == '__main__':
    main()