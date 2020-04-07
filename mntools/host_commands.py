from mininet.log import setLogLevel, info

def startPythonHTTP( host ):
    "Start a simple Python web server on host"
    host.cmd('python -m SimpleHTTPServer 80 &')
    info("*** Starting http service on", host, '\n')

def makeHTTPRequest( client, host ):
    info(client.cmd( 'curl', host.IP()))

def setDefaultRoute( host ):
    IP_SETTING = {}

    info("*** setting default gateway on", host, '\n')

    info('*** setting default gateway of host %s\n' % host.name)
    if (host.name == 'server1'):
        routerip = IP_SETTING['sw0-eth1']
    elif (host.name == 'server2'):
        routerip = IP_SETTING['sw0-eth2']
    else:
        routerip = "gothere"

    print(host.name, routerip)
    host.cmd('route add %s/32 dev %s-eth0' % (routerip, host.name))
    host.cmd('route add default gw %s dev %s-eth0' % (routerip, host.name))
    # HARDCODED
    # host.cmd('route del -net 10.3.0.0/16 dev %s-eth0' % host.name)
    ips = IP_SETTING[host.name].split(".")
    host.cmd('route del -net %s.0.0.0/8 dev %s-eth0' % (ips[0], host.name))

