class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next  
        current.next = prev       
        prev = current            
        current = next_node       
    
    return prev

def insertion_sort_list(head):
    dummy = ListNode(0)  
    current = head
    
    while current:
        prev = dummy
        next_node = current.next
      
        while prev.next and prev.next.value < current.value:
            prev = prev.next

        current.next = prev.next
        prev.next = current

        current = next_node
    
    return dummy.next

def merge_sorted_lists(l1, l2):
    dummy = ListNode(0)
    current = dummy
    
    while l1 and l2:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    if l1:
        current.next = l1
    if l2:
        current.next = l2
    
    return dummy.next

# Приклад використання

# Функція для створення списку з масиву
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Функція для виведення списку
def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next
    print(" -> ".join(map(str, values)))

# Створення списку
lst = create_linked_list([4, 3, 1, 5, 2])
print("Оригінальний список:")
print_linked_list(lst)

# Реверсування списку
reversed_lst = reverse_list(lst)
print("Реверсований список:")
print_linked_list(reversed_lst)

# Сортування списку вставками
sorted_lst = insertion_sort_list(reversed_lst)
print("Відсортований список:")
print_linked_list(sorted_lst)

# Створення двох відсортованих списків
lst1 = create_linked_list([1, 3, 5])
lst2 = create_linked_list([2, 4, 6])
print("Список 1:")
print_linked_list(lst1)
print("Список 2:")
print_linked_list(lst2)

# Об'єднання двох відсортованих списків
merged_lst = merge_sorted_lists(lst1, lst2)
print("Об'єднаний відсортований список:")
print_linked_list(merged_lst)

