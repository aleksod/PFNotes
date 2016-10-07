# import this
#
# def decode_zen_of_python():
#    zen_decoder = this.d
#    coded_zen = this.s
#    print coded_zen
#    decoded_chars = []
#    for char in coded_zen:
#        if char.isalpha():
#            decoded_chars.append(zen_decoder[char])
#        else:
#            decoded_chars.append(char)
#    decoded_text = ''.join(decoded_chars)
#    print '\n' + decoded_text

import this

def decode_zen_of_python():

    zen_decoder = this.d
    coded_zen = this.s
    print coded_zen

    def decoder_to_chars(zen_decoder, coded_zen):
        decoded_chars = []
        for char in coded_zen:
            if char.isalpha():
                decoded_chars.append(zen_decoder[char])
            else:
                decoded_chars.append(char)
        decoded_text = ''.join(decoded_chars)
        return decoded_text

    print '\n' + decoder_to_chars(zen_decoder, coded_zen)

decode_zen_of_python()
