import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        g.add_vertex('v0')
        g.add_edge('v0', 'v1')
        self.assertEqual(g.conn_components(), [['v0', 'v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        v = g.get_vertex('v0')
        self.assertEqual(v.adjacent_to, ['v1'])
        
    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())

    def test_03(self):
        g = Graph('test3.txt')
        self.assertTrue(g.is_bipartite())

    

if __name__ == '__main__':
   unittest.main()
