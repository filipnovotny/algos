from tree import Tree
try:
    import networkx as nx
except:
    pass
import matplotlib.pyplot as plt
from draw_utils import hierarchy_pos

class DrawableTree(object):
    def __init__(self, *args, **kwargs):
        super(DrawableTree,self).__init__()
        self._graph = nx.Graph()
        self._pos = None

    def get_root(self):
        raise NotImplementedError()

    def nodes_to_graph(self):
        self.get_root().compute_edges()

        edges = [("{}".format(edge[0]),"{}".format(edge[1])) for edge in self.get_root().edges]
        self._graph.add_edges_from(edges)
        self._pos = hierarchy_pos(self.graph,"{}".format(self.get_root().data))

    @property
    def graph(self):
        '''getter for graph'''
        return self._graph

    @property
    def pos(self):
        '''getter for pos'''
        return self._pos



# tree = MyTree(0, fixed_size=3)
# tree.get_root().children_datas = [1, 2, 3]
# tree.get_root().children[0].children_datas = [5, 6, 7]
# tree.get_root().children[0].children[2].children_datas = [11]

# tree.get_root().children[2].children_datas = [8, 9]
# tree.nodes_to_graph()
# nx.draw(tree.graph, pos=tree.pos, with_labels=True)
# plt.show()