import unittest
from hypothesis import given
import hypothesis.strategies as st
from Lazy_single_linked_lists import *



class TestLazySingleLinkedList(unittest.TestCase):
    """show the LazySingleLinkedList"""
    def test(self):
            res1, f1 = natural_number_seq(1, None)()
            tempList = []
            tempList.append(res1)
            for i in range(233):
                resi, fi = f1()
                f1 = fi
                tempList.append(resi)
            print(tempList[233])


    def test_head(self):
        List1 = Node(1, Node(2, None))
        List2 = Node(3, Node(1, Node(2, None)))

        self.assertEqual(head(List1)().value, 1)
        self.assertEqual(head(List2)(), Node(3, None))

    def test_hail(self):
        List1 = Node(1, Node(2, Node(3, None)))
        List2 = Node(3, Node(2, Node(1, None)))

        self.assertEqual(tail(List1)().value, 3)
        self.assertEqual(tail(List2)(), Node(1, None))

    def test_length(self):
        List1 = Node(1, Node(2, None))
        List2 = Node(3, List1)

        self.assertEqual(length(List1)(), length(Node('s', Node('a', None)))())
        self.assertEqual(length(List2)(), 3)

    @given(st.integers())
    def test_map(self,a):
        List1 = Node(1, Node(2, None))
        List2 = None
        self.assertEqual(map(List1, str)(), Node('1', Node('2', None)))
        self.assertEqual(map(List2, str)(), "None")
        """show the infinite list work inside map"""
        def get_natural_List(x):
            """this function is use to :
             at first generate a infinite list and insert in the lazy list in get_natural_List
             this lazy list never stops and continues printing natural numbers by constantly cons in the tail of lazy list.
            """
            tempList = []
            if x == 0:
                return tempList
            res, f = natural_number_seq(1, None)()
            tempList.append(res)
            for i in range(x):
                resi, fi = f()
                f = fi
                tempList.append(resi)
            return tempList

        if a > 0 and a < 9999:
            s = a
            list_1 = []
            while s > 0:
                list_1.append(str(s))    #the map use str so it compare with the list_1 which include str num
                s = s - 1
            l2 = get_natural_List(a)  #use the infinite to work in map
            self.assertEqual(to_list(map(l2[a - 1],str)())(), list_1)
            """show the infinite list work inside map"""
        if a == 0:
            l3 = get_natural_List(a)
            self.assertEqual(l3, [])

    def test_reduce(self):
        List1 = Node(1, Node(2, None))
        List0 = Node(-1, Node(4, None))
        List2 = None
        List3 = Node(None, None)
        self.assertEqual(reduce(List1, lambda x, y: x + y, 0)(), 3)
        self.assertEqual(reduce(List1, lambda x, y: x + y, 0)(), reduce(List0, lambda x, y: x + y, 0)())
        self.assertEqual(reduce(List2, lambda x, y: x + y, 0)(), None)
        self.assertEqual(reduce(List3, lambda x, y: x + y, 0)(), 0)

    def test_mconcat(self):
        List0 = None
        List1 = Node(1, Node(2, None))
        List2 = None
        List3 = Node(3, None)
        self.assertEqual(mconcat(List0, List2)(), None)
        self.assertEqual(mconcat(List0, List1)(), List1)
        self.assertEqual(mconcat(List3, List1)(), Node(3, Node(1, Node(2, None))))

    def test_take(self):
        List1 = Node(1, Node(2, Node(3,None)))
        lst1=[1,2]
        self.assertEqual((take(List1,2))(),lst1)

    def test_drop(self):
        List1 = Node(1, Node(2, Node(3,None)))
        lst1=[3]
        self.assertEqual((drop(List1,2))(),lst1)

    def test_from_list(self):
        lst = [1, 2, 3, 4]
        List = Node(1, Node(2, Node(3, Node(4, None))))
        self.assertEqual(from_list(lst)(), List)

    def test_to_list(self):
        lst = [1, 2, 3, 4]
        List = Node(1, Node(2, Node(3, Node(4, None))))
        self.assertEqual(to_list(List)(), lst)

    @given(st.lists(st.integers()))
    def test_from_list_to_List_equal(self, lst):
        self.assertEqual(to_list(from_list(lst)())(), lst)

    def test_iterator(self):
        x = [1, 2, 3]
        lst = from_list(x)()
        tmp = []
        try:
            get_next = iterator(lst)
            while True:
                tmp.append(get_next())
        except StopIteration:
            pass
        self.assertEqual(x, tmp)
        self.assertEqual(to_list(lst)(), tmp)
        get_next = iterator(None)
        self.assertRaises(StopIteration, lambda: get_next())

    @given(st.integers())
    def test_natural_seq(self, a):
        """this is infinite list test
            at first generate a infinite list and insert in the lazy list in get_natural_List
        """
        def get_natural_List(x):
            tempList = []
            if x == 0:
                return tempList
            res, f = natural_number_seq(1, None)()
            tempList.append(res)

            for i in range(x):
                resi, fi = f()
                f = fi
                tempList.append(resi)
            return tempList

        if a > 0 and a < 9999:
            s = a
            list_1 = []
            while s > 0:
                list_1.append(s)
                s = s - 1
            l2 = get_natural_List(a)
            self.assertEqual(to_list(l2[a - 1])(), list_1)
        if a == 0:
            l3 = get_natural_List(a)
            self.assertEqual(l3, [])



if __name__ == '__main__':
    unittest.main()
