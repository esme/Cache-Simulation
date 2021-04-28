class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    FAIL = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def simulate_cache():
  mm_size = 0x7ff+1 # size of main memory is 2048
  mm = [0]*mm_size
  cache_size = 16 # data part of the cache
  no_of_slots = 16 # number of slots in the cache
  slot_location = 0
  valid_location = 1
  tag_location = 2
  dirty_location = 3
  data_location = 4

  # initialize main memory array
  i = 0
  while i < mm_size:
    for j in range(0xFF + 1):
      mm[i] = j
      i += 1

  # initialize cache
  cache = [0]*no_of_slots
  for j in range(no_of_slots):
    cache[j] = [0]*(4+cache_size)
    cache[j][slot_location] = j

  def read():
    address = int(input(f'{bcolors.HEADER}What address would you like to read?\n{bcolors.ENDC}'), 16)
    while (address >= mm_size):
      address = int(input(f'{bcolors.FAIL}Please enter an address smaller than or equal to 0x7ff\n{bcolors.ENDC}'), 16)
    tag = (address & 0xF00) >> 8
    # print('tag: ', hex(tag))
    slot_no = (address & 0x0F0) >> 4
    # print('slot: ', hex(slot_no))
    offset = address & 0x00F
    # print('offset: ', hex(offset))
    
    # cache hit for same tag and slot
    if cache[slot_no][valid_location] == 1 and cache[slot_no][tag_location] == tag:
      print(f'{bcolors.OKCYAN}At that byte there is the value {format_to_hex(cache[slot_no][data_location+offset])} (Cache Hit){bcolors.ENDC}')

    # cache miss
    else:
      # if dirty bit is 1
      if cache[slot_no][dirty_location] == 1:
        # update main mem
        reverse_address = (cache[slot_no][tag_location] << 8) + (slot_no << 4)
        print(f'{bcolors.OKGREEN}Updating main mem starting at {format_to_hex(reverse_address)}...{bcolors.ENDC}')
        for i in range(cache_size):
          mm[reverse_address+i] = cache[slot_no][data_location+i]
        # set dirty bit to 0
        cache[slot_no][dirty_location] = not cache[slot_no][dirty_location]

      # set valid bit and tag
      cache[slot_no][valid_location] = 1
      cache[slot_no][tag_location] = tag

      # copy data from main mem to cache
      print(f'{bcolors.OKGREEN}Copying data from main mem to cache...{bcolors.ENDC}')
      block_start = address & 0xFF0
      for i in range(cache_size):
        cache[slot_no][data_location+i] = mm[block_start+i]

      print(f'{bcolors.OKCYAN}At that byte there is the value {format_to_hex(cache[slot_no][data_location+offset])} (Cache Miss){bcolors.ENDC}')

  def write():
    address = int(input(f'{bcolors.HEADER}What address would you like to write to?\n{bcolors.ENDC}'), 16)
    while (address >= mm_size):
      address = int(input(f'{bcolors.FAIL}Please enter an address smaller than or equal to 0x7ff\n{bcolors.ENDC}'), 16)
    tag = (address & 0xF00) >> 8
    slot_no = (address & 0x0F0) >> 4
    offset = address & 0x00F

    data = int(input(f'{bcolors.HEADER}What data would you like to write at that address?\n{bcolors.ENDC}'), 16)

    # cache hit for same tag and slot
    if cache[slot_no][valid_location] == 1 and cache[slot_no][tag_location] == tag:
      # write data
      cache[slot_no][data_location+offset] = data
      # set dirty bit to 1
      cache[slot_no][dirty_location] = not cache[slot_no][dirty_location]

      print(f'{bcolors.OKCYAN}Value {format_to_hex(data)} has been written to address {format_to_hex(address)}. (Cache Hit){bcolors.ENDC}')

    # cache miss
    else:
      # if dirty bit is 1
      if cache[slot_no][dirty_location] == 1:
        # update main mem
        reverse_address = (cache[slot_no][tag_location] << 8) + (slot_no << 4)
        print(f'Updating main mem starting at {format_to_hex(reverse_address)}...')
        for i in range(cache_size):
          mm[reverse_address+i] = cache[slot_no][data_location+i]
        # set dirty bit to 0
        cache[slot_no][dirty_location] = not cache[slot_no][dirty_location]

      # set valid bit and tag
      cache[slot_no][valid_location] = 1
      cache[slot_no][tag_location] = tag

      # copy data from main mem to cache
      print(f'{bcolors.OKGREEN}Copying data from main mem to cache...{bcolors.ENDC}')
      block_start = address & 0xFF0
      for i in range(cache_size):
        cache[slot_no][data_location+i] = mm[block_start+i]

      # write data
      cache[slot_no][data_location+offset] = data
      # set dirty bit to 1
      cache[slot_no][dirty_location] = not cache[slot_no][dirty_location]

      print(f'{bcolors.OKCYAN}Value {format_to_hex(data)} has been written to address {format_to_hex(address)}. (Cache Miss){bcolors.ENDC}')

  def display():
    cache_hex = [""]*no_of_slots
    for j in range(no_of_slots):
      cache_hex[j] = [""]*(4+cache_size)

    for i in range(no_of_slots):
      for j in range(data_location+cache_size):
        cache_hex[i][j] = format_to_hex(cache[i][j]).upper()

    cache_headers = [''] * (cache_size + 4)
    cache_headers[0] = 'Slot'
    cache_headers[1] = 'Valid'
    cache_headers[2] = 'Tag'
    cache_headers[3] = 'Dirty'
    cache_headers[4] = 'Data'
    format_row = "{:>6}" * (len(cache_headers) + 1)
    print(format_row.format("", *cache_headers))
    for row in cache_hex:
      print(format_row.format("", *row))

  def format_to_hex(decimal):
    return str(hex(decimal))[2:]

  operation = input(f'{bcolors.HEADER}(R)ead, (W)rite, or (D)isplay Cache?\n{bcolors.ENDC}')
  while (operation.lower() == 'r' or operation.lower() == 'w' or operation.lower() == 'd'):
    if operation.lower() == 'r':
      read()
    if operation.lower() == 'w':
      write()
    if operation.lower() == 'd':
      display()
    print('---')
    operation = input(f'{bcolors.HEADER}(R)ead, (W)rite, or (D)isplay Cache?\n{bcolors.ENDC}')

simulate_cache()