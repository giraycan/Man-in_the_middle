import scapy.all as scapy
import optparse
def get_input():
    parser=optparse.OptionParser()
    parser.add_option("-r","--radar",dest="scanner_ip",help="input scanner ip example:10.0.2.0/24")
    (user_input,arguments) = parser.parse_args()
    if not user_input.scanner_ip:
        print("Enter IP Address")
    return user_input

def net_scanner(scanner_ip):
    arp_request_packet=scapy.ARP(pdst=scanner_ip)
    #scapy.ls(scapy.ARP())
    broadcast_packet=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    return (broadcast_packet/arp_request_packet)
def answered_func(combined_packet):
    return scapy.srp(combined_packet,timeout=1)


user_input=get_input()

combined_packet=net_scanner(user_input.scanner_ip)

(answered_list,unanswered_list)=answered_func(combined_packet)

answered_list.summary()