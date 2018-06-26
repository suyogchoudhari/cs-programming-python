'''
few assumptions
bit index starts from 0
set bit means, setting bit to 1
clear bit mean, setting bit to 0
'''


def clear_all_bits_from_mst_to_ith_bit(val, i):
    mask = ~((1 << i+1) - 1)
    val = val & mask
    return val


def clear_all_bits_from_lsb_to_ith_bit(val, i):
    mask = (1 << i) - 1
    val = val & mask
    return val


# set 6th bit to convert character to lower case
def convert_upper_case_to_lower_case(ch):
    mask = 1 << 5
    return chr(ord(ch) | mask)


# clear 6th bit
def convert_lower_case_to_upper_case(ch):
    mask = ~(1 << 5)
    return chr(ord(ch) & mask)


def count_set_bits(val):
    count = 0
    while val > 0:
        val = val & (val - 1)
        count = count + 1

    return count


def check_if_power_of_2(val):
    return 0 == (val & (val - 1))


def log2(num):
    log = 0
    while num > 1:
        num = num >> 1
        log = log + 1

    return log


print(clear_all_bits_from_mst_to_ith_bit(29, 3))
print(clear_all_bits_from_lsb_to_ith_bit(215, 4))
print(convert_upper_case_to_lower_case('A'))
print(convert_lower_case_to_upper_case('a'))
print(count_set_bits(15))
print(count_set_bits(16))
print(check_if_power_of_2(15))
print(check_if_power_of_2(16))
print(log2(17))
