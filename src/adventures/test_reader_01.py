import os
print(os.getcwd())
os.chdir("G:\\Documents\\projects\\Programming Projects\\Python Projects\\Rogue Trader Game\\python src\\adventures")
print(os.getcwd())
count = 1

def file_reader(file_name):
    data_dump = []
    with open(file_name,'r', encoding='utf8') as fileHandle:
        for line_string in fileHandle.readlines():
            data_dump.append(line_string)
    return data_dump
def list_testing(list_item):
    print("Testing the list")
    for item in list_item:
        print(item)
def adv_module_maker(data_list):
    """takes a list built from an .adv file and parses out the bits for each segment of an adventure"""
    valid_adv_data = []
    adv_header_check = False
    npc_data_check = False
    item_data_check = False
    room_data_check = False
    exit_data_check = False
    data_phase = 0
    npcDataType = "NPCs"
    rmsDataType = "Rooms"
    exitsDataType = "Exits"
    itemsDataType = "items"
    valid_data_types = [ npcDataType, rmsDataType, exitsDataType, itemsDataType  ]
    curr_data_type = None
    curr_data_block = []
    for item in data_list:
        valid_adv_data.append(item)
        if item.startswith("==="):
            curr_data_type = None
            continue
        if item.startswith("NPCs:"):
            data_phase = 1
        elif item.startswith("Items:"):
            data_phase = 2
        elif item.startswith("Rooms:"):
            data_phase = 3
        elif item.startswith("Exits:"):
            data_phase = 4
        else:
            data_phase = 99
        if data_phase == 1:
            while item.startswith("---")

        
        
 
    print("End of file")
    #list_testing(curr_data_block)
    return valid_adv_data




testfile = file_reader("test.adv")
adv_test = adv_module_maker(testfile)