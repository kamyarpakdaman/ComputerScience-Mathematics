# In this program, we will create a hash map that takes a string, converts it to bytes
# and generates a hash code. It then looks for the index to put the corresponding value in.
# Further, this hash map uses Open Addressing in case it faces hash code collisions.

class HashMap:

  def __init__(self, array_size):

    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key, count_collisions=0):

    # Although count_collisions is set to be 0 by default, we'll later use this parameter
    # for handling collisions in setting and getting values for keys.

    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions

  def compressor(self, hash_code):
    
    # Finding the corresponding array index for a hash code. 

    return hash_code % self.array_size

  def assign(self, key, value):
    
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    if current_array_value is None:
      self.array[array_index] = [key, value]
      return

    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    # If none of the above if scenarios are the case, it means we're facing a collision.
    # As follows, through a while loop, we'll count collisions and add the count to a new
    # variable, and then, create a new hash code using this variable as the fourth parameter.
    # The process follows until we find an appropriate array index.

    number_collisions = 1

    while(current_array_value[0] != key):
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array[new_array_index]

      if current_array_value is None:
        self.array[new_array_index] = [key, value]
        return

      if current_array_value[0] == key:
        self.array[new_array_index] = [key, value]
        return

      number_collisions += 1

    return

  def retrieve(self, key):
    
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]

    if possible_return_value is None:
      return None

    if possible_return_value[0] == key:
      return possible_return_value[1]

    # Just as what we did for the .assign() method, for retrieving, we check the indices for our
    # desired key. If the indice isn't either None or containing our key, we understand we need
    # to search further for our key, which we expect to have been dropped somewhere else in the
    # assignment process.

    retrieval_collisions = 1

    while (possible_return_value != key):
      new_hash_code = self.hash(key, retrieval_collisions)
      retrieving_array_index = self.compressor(new_hash_code)
      possible_return_value = self.array[retrieving_array_index]

      if possible_return_value is None:
        return None

      if possible_return_value[0] == key:
        return possible_return_value[1]

      retrieval_collisions += 1

    return

# Creating some stuff. 

hash_map = HashMap(15)
hash_map.assign('gabbro', 'igneous')
hash_map.assign('sandstone', 'sedimentary')
hash_map.assign('gneiss', 'metamorphic')

print(hash_map.retrieve('gabbro'))
print(hash_map.retrieve('sandstone'))
print(hash_map.retrieve('gneiss'))

print('\nThanks for reviewing')

# Thanks for reviewing 
