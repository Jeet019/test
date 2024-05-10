import math
def cat(page_size_kb, physical_memory_kb, address_space_bits):
  if not (page_size_kb & (page_size_kb - 1) == 0 and physical_memory_kb & (physical_memory_kb - 1) == 0):
    raise ValueError("Both page size and physical memory size must be powers of two.")

  page_offset_bits = int(round(math.log2(page_size_kb * 1024)))

  vpn_bits = address_space_bits - page_offset_bits
  page_size_by=page_size_kb * 1024
  num_frames =  physical_memory_kb *1024 //page_size_by
  frame_number_bits = int(round(math.log2(num_frames)))

  offset_within_frame_bits = page_offset_bits
  return {
      "VPN": vpn_bits,
      "Page Offset": page_offset_bits,
      "Page Table Index": vpn_bits,  
      "Frame Number": frame_number_bits,
      "Offset within a Frame": offset_within_frame_bits,
  }

page_size_kb=int(input())
physical_memory_kb=int(input())
address_space_bits=int(input())
try:
  result = cat(page_size_kb,physical_memory_kb ,address_space_bits )
  for key, value in result.items():
    print(f"{key}: {value} bits")
except ValueError as e:
  print(e)