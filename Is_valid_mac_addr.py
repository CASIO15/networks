from mac_vendor_lookup import MacLookup

addr = input('Enter a MAC addr: ').strip(' ')
IS_VALID = ''

#Calling MacLookUp
mac = MacLookup()

if ':' in addr and len(addr) == 17:
    for i in addr.split(':'):
        if len(i) == 2:
            IS_VALID = 'valid'
        break
else:
    IS_VALID = 'Invalid'

if IS_VALID == 'valid':
    print(f'[{IS_VALID}] Vendor id: {addr[:8]} |Vendor: {mac.lookup(addr)}|')

else:
    print(IS_VALID)

