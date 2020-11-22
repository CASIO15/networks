def mac_look(addr):

    addr = addr.replace('-', ':')
    IS_VALID = None

    if ':' in addr and len(addr) == 17:
        for i in addr.split(':'):
            if len(i) == 2 and bin(int(str(i), 16))[-1] == '1':
                IS_VALID = 'valid'
                break
            elif len(i) == 2 and bin(int(str(i), 16))[-1] == '0':
                IS_VALID = 'valid'

    else:
        IS_VALID = 'Invalid'

    if IS_VALID == 'valid':
        for i in addr.split(':'):
            if bin(int(str(i), 16))[-1] == '1':
                return f'[{IS_VALID}] Vendor id: {addr[:8]} Type: Multicast'
            else:
                return f'[{IS_VALID}] Vendor id: {addr[:8]} Type: Unicast'

    else:
        return IS_VALID
