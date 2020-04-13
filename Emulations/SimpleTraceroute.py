# import mininet.net
# import mininet.node
from mininet.net import Mininet

import time
import sys
sys.path.append('../')
from mntools.controllers import POX
from mininet.log import setLogLevel, info
from mininet.cli import CLI
from mininet.topo import Topo
# from mntools.routers.LinuxRouter import LinuxRouter
from mntools.topologies import *
from mntools.host_commands import *

class SimpleTreeTopo( Topo ):

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


def runSimpleTracerouteSim():
    info("*** Creating network\n")
    topo = TreeTopoClassic(n=5, seed=115)
    net = Mininet(topo=topo, controller=POX)

    net.start()
    info('*** Routing Table on Router:\n')
    info(net['r0'].cmd('route'))

    h1, h2, router = net.get('h1', 'h2', 'r0')
    startPythonHTTP(h1)
    time.sleep( 2 )
    # makeHTTPRequest(h2, h1)

    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    runSimpleTracerouteSim()