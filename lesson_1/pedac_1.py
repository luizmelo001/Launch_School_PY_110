"""
Write a program that, given the number of available blocks, calculates the number of blocks left over 
after building the tallest possible valid structure.
"""

def calculate_leftover_blocks(total_blocks):
    if total_blocks <= 0:
        return 0
    
    layer = 1
    while True:
        blocks_for_layer = layer ** 2
        
        if total_blocks < blocks_for_layer:
            return total_blocks
        
        total_blocks -= blocks_for_layer
        layer += 1



print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True == 1
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True