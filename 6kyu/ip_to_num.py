# Write a function that takes an IPv4 address and returns it as an integer,
# and a function that takes an integer and returns it as an IPv4 address string

def ip_to_num(ip):
    bits = ip.split('.')
    addr_sum = 0
    for y in bits:
        addr_sum = (addr_sum * 256) + int(y)
    return(addr_sum)

def num_to_ip(num):
    addr_bits = []
    for _ in range(4):
        num = num / 256
        rem = int((num - int(num)) * 256)
        addr_bits.insert(0,str(rem))
    addr_str = f"{addr_bits[0]}.{addr_bits[1]}.{addr_bits[2]}.{addr_bits[3]}"
    return(addr_str)
