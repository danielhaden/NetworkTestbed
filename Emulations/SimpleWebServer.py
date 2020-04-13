from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.topo import Topo
from mininet.cli import CLI
import sys
import time
sys.path.append('../')
from mntools.controllers import POX
from mntools.host_commands import *
from mntools.routers.LinuxRouter import LinuxRouter

""" 
Topology: Client and Server connected via Linux Router
Behavior: Server starts simple HTTP Python service and requests
page.
Controller: POX however network functions as non-SDN network.
"""

class SimpleWebServerTopo( Topo ):

    def build(self, **_opts):
        defaultIP = '192.168.1.1/24'
        router = self.addNode('r0', cls=LinuxRouter, ip=defaultIP)

        h1 = self.addHost('h1', ip='192.168.1.100/24',
                          defaultRoute='via 192.168.1.1')
        h2 = self.addHost('h2', ip='172.16.0.100/12',
                          defaultRoute='via 172.16.0.1')

        self.addLink(h1, router, intfName2='r0-eth1',
                     params2={'ip': defaultIP})
        self.addLink(h2, router, intfName2='r0-eth2',
                     params2={'ip': '172.16.0.1/12'})

def runSimpleWebServerSim():
    info("*** Creating network\n")
    topo = SimpleWebServerTopo()
    net = Mininet(topo=topo, controller=POX)

    net.start()
    info('*** Routing Table on Router:\n')
    info(net['r0'].cmd('route'))

    h1, h2, router = net.get('h1', 'h2', 'r0')
    startPythonHTTP(h1)
    time.sleep( 2 )
    makeHTTPRequest(h2, h1)

    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    runSimpleWebServerSim()