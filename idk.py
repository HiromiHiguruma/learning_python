class linked_list_node:

    def __init__(self, value, next_node = None):
        
        self.value = value

        self.next_node = next_node

node1 = linked_list_node (3)

node2 = linked_list_node (5)

node3 = linked_list_node (2)


node1.next_node = node2 
node2.next_node = node3

new_node1 = linked_list_node (1)

new_node2 = linked_list_node (2)

new_node3 = linked_list_node (7)

new_node1.next_node = new_node2

new_node2.next_node = new_node3

def testfunc (linked_list_1, linked_list_2):

    head_node = linked_list_node (linked_list_1.value + linked_list_2.value)

    return head_node


print (testfunc (node1, new_node1))