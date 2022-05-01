flag_enc = "饇饍饂饈饜餕饆餗餙饅餒餗饂餗餒饃饄餓饆饂餘餓饅餖饇餚餘餒餔餕餕饆餙餕饇餒餒饞飫"

for k in range(0xFFFD):
    ct = ''
    for c in flag_enc:
        ct += chr((ord(c) - k + 0xFFFD) % 0xFFFD)
    if ct.startswith('f'):
        print(ct)
        break
