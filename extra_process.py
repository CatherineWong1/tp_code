import json
def ExtraProcessSteps(load_data):
    steps_list = []
    table_dict = load_data["cells"]
    table_content = table_dict["data"] #每个元素都包含表格中的内容
    serial_prosteps = 0
    for i in range(len(table_content)):
        l_item = len(table_content[i])
        #print(l_item)
        if table_content[i][l_item-1] == "Process Steps":
            serial_content = i+1
            print(table_content[i][l_item-1])
            break
    print("1-", serial_content)
    print(len(table_content))
    for i in range(serial_content, len(table_content)):
        print("2-", i)

        l_content = len(table_content[i])
        if table_content[i][l_content - 1] != "Considerations":
            steps_list.append(table_content[i][l_content - 1])
        else:
            break
    return steps_list

with open("table.json", "r", encoding="utf-8") as load_f:
    load_dict = json.load(load_f)
print(load_dict)
process_steps = ExtraProcessSteps(load_dict)
print(process_steps)


