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
    npcDataType = "NPCs"
    rmsDataType = "Rooms"
    exitsDataType = "Exits"
    itemsDataType = "items"
    valid_data_types = [ npcDataType, rmsDataType, exitsDataType, itemsDataType  ]
    curr_data_type = None
    curr_data_block = []
    for item in data_list:
        valid_adv_data.append(item.strip("\n"))
        if item.startswith("==="):
            curr_data_type = None
            continue
        split_item_list = item.split(":")
        if split_item_list[0] in valid_data_types:
            curr_data_type = split_item_list[0]
            continue
        if item.startswith("---"):
            if curr_data_type:
                if curr_data_type == npcDataType:
                    print("Call the NPC method with args " + ",".join(curr_data_block))
                elif curr_data_type == rmsDataType:
                    print("Call the Room method with args " + ",".join(curr_data_block))
                elif curr_data_type == exitsDataType:
                    print("Call the NPC method with args " + ",".join(curr_data_block))
                elif curr_data_type == itemsDataType:
                    print("Call the item method with args " + ",".join(curr_data_block))
                else:
                    print("Unknown data type state, unsure what to do with " + item)
            else:
                print("current data type unset during block parse")
            curr_data_block = []
        else:
            curr_data_block.append(item)
    print("End of file")
    #list_testing(curr_data_block)
    return valid_adv_data

testfile = file_reader("test.adv")
adv_test = adv_module_maker(testfile)




#if adv_header_check:
#    if item.startswith("NPCs:"):
#        print("Call the NPC method")
#        adv_header_check = False
#    elif item.startswith("Rooms:"):
#        print("Call the NPC method")
#        adv_header_check = False
 #   elif item.startswith("Exits:"):
#        print("Call the NPC method")
#        adv_header_check = False
#    elif item.startswith("items:"):
#        print("Call the item method")
 #       adv_header_check = False
#    else:
#        print("End of file")