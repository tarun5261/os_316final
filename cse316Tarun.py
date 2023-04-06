disk = [None] * 1024 # 1024 blocks in the disk
total_blocks = len(disk)
used_blocks = 0

def add_file(name, size):
    global used_blocks
    free_blocks = []
    for i in range(total_blocks):
        if disk[i] == None:
            free_blocks.append(i)
            if len(free_blocks) == size:
                for j in free_blocks:
                    disk[j] = name
                used_blocks += size
                return True
        else:
            free_blocks = []
    return False

def delete_file(name):
    flag = False
    global used_blocks
    for i in range(total_blocks):
        if disk[i] == name:
            flag = True
            disk[i] = None
            used_blocks -= 1
    return flag

def rename_file(old_name, new_name):
    flag = False
    for i in range(total_blocks):
        if disk[i] == old_name:
            flag = True
            disk[i] = new_name
    return flag

def move_file(name, new_location):
    global used_blocks
    size = 0
    old_location = []
    for i in range(total_blocks):
        if disk[i] == name:
            size += 1
            old_location.append(i)
    free_blocks = 0
    for i in range(new_location, total_blocks):
        if disk[i] == None:
            free_blocks += 1
        else:
            free_blocks = 0
        if free_blocks == size:
            for j in old_location:
                disk[j] = None
            for j in range(new_location, new_location+size):
                disk[j] = name
            used_blocks -= size
            return True
    return False

def calculate_fragmentation():
    free_blocks = 0
    for i in range(total_blocks):
        if disk[i] == None:
            free_blocks += 1
    return free_blocks

choice = -1
print("=== File System Simulation ===")
print("1. Create a file")
print("2. Delete a file")
print("3. Rename a file")
print("4. Move a file")
print("5. Calculate fragmentation")
print("0. Stop the simulation")
print("=============================")

while(choice != 0):
    choice = int(input("Enter choice: "))
    if choice == 1:
        name = input("Enter name of file with extension: ")
        size = int(input("Enter size of file in MB: "))
        if add_file(name, size):
            print("The file has been added successfully.")
        else:
            print("Insufficient space. The file was not added.")
    elif choice == 2:
        name = input("Enter name of file with extension: ")
        if delete_file(name):
            print("The file has been removed successfully.")
        else:
            print("File not found. The file was not removed.")
    elif choice == 3:
        old_name = input("Enter old name of file with extension: ")
        new_name = input("Enter new name of file with extension: ")
        if rename_file(old_name, new_name):
            print("The file has been renamed successfully.")
        else:
            print("File not found. The file was not renamed.")
    elif choice == 4:
        name = input("Enter name of file with extension: ")
        location = int(input("Enter the location to which the file should be moved: "))
        if(move_file(name,location)):
            print("The file has been sucessfully moved to the new location")
        else:
            print("The file doesn't exist or not enough space at new location")
    elif choice == 5:
        print("No. of Fragmented blocks are: {}".format(calculate_fragmentation())) 
