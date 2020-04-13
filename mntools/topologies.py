import networkx as nx
from mininet.topo import Topo
import sys

sys.path.append('../')
from mntools.routers.LinuxRouter import LinuxRouter
from mntools.ip import *

class TreeTopoClassic( Topo ):

    def build(self, n, seed):
        for i in range(0,25):
            print(randomIP(prefix="256.116.192."))
        tree = nx.generators.trees.random_tree(n, seed)

        hostCounter, routerCounter = 0,0
        nodes = {}
        for node in tree:
            if tree.degree[node] > 1: # node is a router
                name = 'r%s' % routerCounter
                routerIP = randomIP()
                nodes[node] = {'name': name, 'object': self.addNode(name,
                                                                    cls=LinuxRouter,
                                                                    ip=routerIP+"/24")}

                for neighbor in tree.neighbors(node):
                    if tree.degree[neighbor] <= 1:

                        name = 'h%s' % hostCounter
                        nodes[node] = {'name': name, 'object': self.addHost(name, ip=randomIP(),
                                                                            defaultRoute=routerIP)}
                        hostCounter += 1

            else: # node is a router or switch
                name = 'r%s' % routerCounter
                nodes[node] = {'name': name, 'object': self.addNode(name,
                                                                    cls=LinuxRouter,
                                                                    ip=randomIP(subnetMask="/24"))}
                routerCounter += 1

        for e in tree.edges(data=False):
            if tree.degree[e[0]] <= 1:
                host   = nodes[ e[0] ]['object']
                router = nodes[ e[1] ]['object']
                self.addLink(host, router, intfName2='r%s-eth%s' % (e[1], e[0]))

            elif tree.degree[e[1]] <=1:
                host   = nodes[e[1]]['object']
                router = nodes[e[0]]['object']
                self.addLink(host, router, intfName2='r%s-eth%s' % (e[0], e[1]))

            else:
                router1 = nodes[e[1]]['object']
                router2 = nodes[e[0]]['object']
                self.addLink(router1, router2, intfName2='r%s-ethr%s' % e)


# randomly generate IP for router
# get

def classic_from_graphml(file):
    "Returns a mininet topology based on graphml file"
    return file



