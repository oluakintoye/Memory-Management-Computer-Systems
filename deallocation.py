# Case 2: Joining Three Free Blocks

import pandas as pd

job = [
            [4075,105, "Free"],
            [5225, 5, "Free"],
            [6785, 600, "Free"],
            [7560, 20, "Free"],
            [7580, 20, '(Busy)'],
            [7600, 205, "Free"],
            [10250, 4050, "Free"],
            [15125, 230, "Free"],
            [24500, 1000, "Free"]

     ]

free_list = pd.DataFrame(data=job, columns=['Beginning Address', 'Memory Block Size', 'Status'])

print(free_list)

def Deallocation():
    #check for busy blocks
    for index, row in free_list.iterrows():
        if free_list.at[index,'Status'] == "(Busy)":
            print('Checking for Free Adjacent Blocks..........')
            check_adjacent_free_blocks(index)

    #The free list after a job has released memory.
    print("The Deallocated Free List")
    print()
    print(free_list)



def check_adjacent_free_blocks(index):
    adj_block_1_index = index - 1
    adj_block_2_index = index + 1

    if free_list.at[adj_block_1_index,'Status'] == "Free" and free_list.at[adj_block_2_index,'Status'] == "Free":
        print('Success!. Both Adjacent Blocks Free')
        add_free_partitions(index,adj_block_1_index,adj_block_2_index)
    else:
        print('Both Adjacent Blocks not Free...Next')


def add_free_partitions(index,adj_block_1_index,adj_block_2_index):
    Memory_Block_Size_1 = free_list.at[index,'Memory Block Size']
    Memory_Block_Size_2 = free_list.at[adj_block_1_index,'Memory Block Size']
    Memory_Block_Size_3 = free_list.at[adj_block_2_index,'Memory Block Size']

    print(Memory_Block_Size_1,Memory_Block_Size_2, Memory_Block_Size_3)
    Memory_Block_Size = Memory_Block_Size_1 + Memory_Block_Size_2 + Memory_Block_Size_3

    print(Memory_Block_Size)
    sba = smallest_beginning_address(index, adj_block_1_index, adj_block_2_index)
    print("Sba:", sba)
    free_list.at[sba,'Memory Block Size'] = Memory_Block_Size



def smallest_beginning_address(index,adj_block_1_index,adj_block_2_index):
    Beginning_Address_1 = free_list.at[index, 'Beginning Address']
    Beginning_Address_2 = free_list.at[adj_block_1_index, 'Beginning Address']
    Beginning_Address_3 = free_list.at[adj_block_2_index, 'Beginning Address']

    print(Beginning_Address_1,Beginning_Address_2,Beginning_Address_3)

    Beginning_Address = min([Beginning_Address_1,Beginning_Address_2,Beginning_Address_3])
    print(Beginning_Address)

    if Beginning_Address_2 == Beginning_Address:
        set_null_entry(adj_block_2_index)
        drop_row(index)
        return adj_block_1_index
    else:
        set_null_entry(adj_block_1_index)
        drop_row(index)
        return adj_block_2_index


def set_null_entry(index):
    free_list['Beginning Address'] = free_list['Beginning Address'].astype('str')
    free_list['Memory Block Size'] = free_list['Memory Block Size'].astype('str')

    free_list.at[index,'Beginning Address'] = '*'
    free_list.at[index,'Memory Block Size'] = ''
    free_list.at[index,'Status'] = '(null entry)'

def drop_row(index):
    free_list.drop([index],inplace=True)





Deallocation()
