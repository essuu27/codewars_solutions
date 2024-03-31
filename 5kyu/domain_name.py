# Write a function that when given a URL as a string, parses out just the domain
# name and returns it as a string
def domain_name(url):
    bits = url.split('/')[2] if ':' in url else url
    fqdn = bits.replace('www.', '')
    bits2 = fqdn.split('.')
    return bits2[0]
