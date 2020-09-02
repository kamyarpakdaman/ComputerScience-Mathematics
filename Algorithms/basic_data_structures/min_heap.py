# In this program, we will create a min-heap class which has some methods. In this heap,
# each child is smaller than its left- and right-child. As we add a new element to the end
# of the heap or remove the min value from the very top, we respectively use .heapify_up()
# and heapify_down() methods to keep the order as it's supposed to be.

class MinHeap:

    # We use a list as the underlying data structure for our heap.

    def __init__(self):
        self.heap_list = [None]
        self.count = 0

    # Finding the parent index for each index. It's a helper method.

    def parent_idx(self, idx):
        return idx // 2

    # Finding the left child index for each index. It's a helper method.

    def left_child_idx(self, idx):
        return idx * 2

    # Finding the right child index for each index. It's a helper method.

    def right_child_idx(self, idx):
        return idx * 2 + 1

    # Checking if an index has a left child. It's a helper method.

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count

    # Since we're creating a Min-Heap, the min value is the top parent, which is
    # placed at index 1, after None. Using .retrieve(), we can retrieve the min value.

    def retrieve_min(self):
        if self.count == 0:
            print("No items in heap")
            return None

        # Saving the min value to a new variable.

        min = self.heap_list[1]

        # Replacing the retrieved mean with the last element of the heap, which has no children.

        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1

        # Removing the retrieved ex-min value of the heap.

        self.heap_list.pop()

        # Performing the .heapify_down() to re-order the heap.

        self.heapify_down()
        print('Min value retrieved: {}'.format(min))
        return min

    # Adding a new element to the heap.

    def add(self, element):
        self.count += 1
        self.heap_list.append(element)

        # Performing the .heapify_up() to re-order the heap.

        self.heapify_up()


    # Getting the smaller child for a parent. It's a helper method.

    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child < right_child:
                return self.left_child_idx(idx)
            else:
                return self.right_child_idx(idx)
    
    # Through .heapify_up(), we move a new added element upwards until the principle of
    # 'each child is smaller than its parent' is maintained. Note that since we add the
    # new element to the end of the list, its index would be self.count.

    def heapify_up(self):
        idx = self.count
        while self.parent_idx(idx) > 0:
            if self.heap_list[self.parent_idx(idx)] > self.heap_list[idx]:
                tmp = self.heap_list[self.parent_idx(idx)]
                self.heap_list[self.parent_idx(idx)] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            idx = self.parent_idx(idx)   

    # Through .heapify_down(), we move a new replaced top parent downwards until the principle
    # of 'each child is smaller than its parent' is maintained. Note that since the new parent
    # is at the top of the heap, its index would be 1.
     
    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            smaller_child_idx = self.get_smaller_child_idx(idx)
            if self.heap_list[idx] > self.heap_list[smaller_child_idx]:
                tmp = self.heap_list[smaller_child_idx]
                self.heap_list[smaller_child_idx] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            idx = smaller_child_idx 

min_heap = MinHeap()

min_heap.heap_list = [None, 10, 13, 21, 61, 22, 23, 99]
min_heap.count = 7

while len(min_heap.heap_list) != 1:
  print(min_heap.heap_list)
  min_heap.retrieve_min()

print('\nThanks for reviewing')

# Thanks for reviewing
