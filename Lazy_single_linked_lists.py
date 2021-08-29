

"""define the Node"""
class Node(object):
    def __init__(self, value, next):
        """initialize"""
        self.value = value
        self.next = next

    def __str__(self):
        """to show the content of Lazy_linked_lists"""
        if type(self.next) is Node:
            return "{} -> {}".format(self.value, self.next)
        return str(self.value)

    def __eq__(self, other):
        """if all elements are equal,the list will be equal"""
        if other is None:
            return False
        if self.value != other.value:
            return False
        return self.next == other.next



def head(List):
    """return the first element of the list"""
    def temp():
        if List is None:
            print("None")
            raise NameError
        return Node(List.value, None)

    return temp

def take(List,n):
    """ take N first elements of the list"""
    def temp():
        current = List
        result=[]
        for i in range(0,n):
            result.append(current.value)
            current = current.next
        return result
    return temp

def drop(List,n):
    """drop N first elements of the list"""
    def temp():
        current = List
        result = []
        for i in range(0,n):
            current = current.next
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    return temp

def tail(List):
    """return the tail of the list"""
    def temp():
        if List is None:
            return "None"
        elif List:
            current = List
            while current.next is not None:
                current = current.next
            return current
        return "the List is empty"

    return temp



def length(List):
    """return the length of the list"""
    def temp():
        if List is None:
            return 0
        current = List
        count = 1
        while current.next is not None:
            current = current.next
            count += 1
        return count

    return temp



def map(List, fun):
    """map the value of the list by fun"""
    def temp():
        if List is None:
            return "None"
        else:
            current = List
            while current is not None:
                current.value = fun(current.value)
                current = current.next
        return List

    return temp



def reduce(List, fun, InitialState):
    """reduce the value in the list"""
    def temp():
        if List is None:
            return None
        else:
            state = InitialState
            current = List
            while current is not None:
                if current.value is None:
                    state = fun(0, state)
                else:
                    state = fun(current.value, state)
                current = current.next
        return state

    return temp



def mempty():
    """return None as empty"""
    return None



def mconcat(List1, List2):
    """mconcat list1 and list2"""
    def temp():
        if List1 is None:
            if List2 is None:
                return None
            return List2
        else:
            current = tail(List1)
            current().next = List2
            return List1

    return temp



def from_list(list):
    """change the list in python to lazylinkedlist"""
    def temp():
        res = None
        for e in list:
            if res is None:
                res = Node(e, None)
                current = res
            else:
                current.next = Node(e, None)
                current = current.next
        return res

    return temp



def to_list(List):
    """change lazylinkedlist to the list in python"""
    def temp():
        result = []
        if list is None:
            return "List is None"
        current = List
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

    return temp



def iterator(List):
    """iterate each value in the list"""
    current = List
    def temp():
        nonlocal current
        if current is None: raise StopIteration
        tmp = current.value
        current = current.next
        return tmp

    return temp



def cons(List1, List2):
    """connect List1 and List2;"""
    def temp():
        return Node(List1, List2)

    return temp



def natural_number_seq(x, n):
    """natural number sequence list"""
    def temp():
        res = cons(x, n)()
        return res, lambda: natural_number_seq(x + 1, res)()

    return temp


