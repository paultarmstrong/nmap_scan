#!usr/bin/evn python
# Integrating nmap scanner

import nmap
import optparse


# defining nmap scan function with arguments
# targetHost holds the host address and targetPort holds the port number
def nmap_scan(target_host, target_port):
    ns = nmap.PortScanner()
    ns.scan(target_host, target_port)
    state = ns[target_host]['tcp'][int(target_port)]['state']
    print(" [*] " + target_host + " tcp/" + target_port + " " + state)


def main():
    # printing Help to inform How to use this script
    parser = optparse.OptionParser('Script Usage:' + '-H <target host> -p <target port>')

    parser.add_option('-H', dest='target_Host', type='string',
                      help='specify target host')

    parser.add_option('-p', dest='targetPort', type='string',
                      help='specify target port[s] separated by comma')

    (options, args) = parser.parse_args()
    target_host = options.target_Host
    target_ports = str(options.targetPort)

    print("--------------------------------------------------")
    print("The target ports to be scanned on IP address " + target_host + " are " + target_ports)
    print("--------------------------------------------------")
    if (target_host is None) | (target_ports[0] is None):
        print(parser.usage)
        exit(0)

    ports = target_ports.strip("'").split(',')

    for target_port in ports:
        print(target_host + " " + target_port)
        nmap_scan(target_host, target_port)


if __name__ == '__main__':
    main()
