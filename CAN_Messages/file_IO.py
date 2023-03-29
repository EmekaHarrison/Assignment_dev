import json


def write_output(filename, data):
    with open(filename, "w") as file_fd:
        file_fd.writelines(data)


def include_guard_class_constructor(json_filename):
    top = []  # include guard, class declaration and constructor
    bottom = ""  # ending of include guard

    filename_upper = json_filename.upper()
    include_guard = f" HEADER_CAN_{filename_upper}"
    top.append(f"#ifndef{include_guard}_H\n")
    top.append(f"#define{include_guard}_H\n")
    top.append(f"#include <string>")
    top.append("\n")
    top.append(f"class CAN_{json_filename} {{\n")
    top.append("    public:\n")
    top.append(f"        CAN_{json_filename}();")

    bottom = ["};", f"\n#endif //{include_guard}_H"]
    return top, bottom


def generate_getter_h(signal_name, signal_comment):
    buffer = f"\n\t\t/*\n\t\tget {signal_comment}\n\t\t*/"
    buffer += f"\n\t\tstd::string get_{signal_name}();"
    return buffer


def generate_setter_h(signal_name, signal_type, signal_comment):
    buffer = f"\n\t\t/*\n\t\tset {signal_comment}\n\t\t*/"
    buffer += f"\n\t\tstd::string set_{signal_name}({signal_type} newValue);"
    return buffer


def generate_get_set_functions(json_dict):
    content = []
    for signal in json_dict["signals"]:
        signal_name = signal["name"]
        signal_type = signal["type"]
        signal_length = signal["length"]
        signal_comment = signal["comment"]
        get_prototype = generate_getter_h(signal_name, signal_comment)
        set_prototype = generate_setter_h(signal_name, signal_type, signal_comment)
        content.append(get_prototype)
        content.append(set_prototype)
    return content


def generate_private_fields(json_filename):
    content = []
    content.append("\n    private:")
    return content


def generate_private_data(json_filename):
    info = []
    data_type = "\n\t\tuint8_t"
    info.append(f"        {data_type} m_startMsgId;")
    info.append(f"        {data_type} m_temperatureGetMsGid;")
    info.append(f"        {data_type} m_temperatureSetMsGid;")
    info.append(f"        {data_type} m_humidityGetMsGid;")
    info.append(f"        {data_type} m_humiditySetMsGid;\n")

    return info


def generate_header(json_filename, json_dict):
    output = []
    header_top, header_bottom = include_guard_class_constructor(json_filename)

    output += header_top

    output += generate_get_set_functions(json_dict)
    output += generate_private_fields(json_filename)
    output += generate_private_data(json_filename)
    output += header_bottom  # output = output + header_bottom

    return output


def write_func_header_file(filename, data):
    if filename is None or filename == "":
        return
    with open(filename, "w") as file_fd:
        file_fd.writelines(data)


def write_func_source_file(filename, data):
    if filename is None or filename == "":
        return
    with open(filename, "w") as file_fd:
        file_fd.writelines(data)


def source_guard_class_constructor(json_filename):
    top = []  # include guard, class declaration and constructor
    bottom = ""  # ending of include guard
    m_startmsgid = 100
    startmsgid = "m_startMsgId"
    j_filename_lower = json_filename.lower()
    id = json_dict["id"]
    top.append(f'#include "../include/can_messages/CAN_{j_filename_lower}.h"\n')
    top.append(f"#include <sstream>")
    top.append(f"\nCAN_{j_filename_lower}::CAN_{j_filename_lower}() {{\n")
    top.append(f"    {startmsgid} = {id};\n")

    i = 2
    for element in json_dict["signals"]:
        element_name = element["name"]
        top.append(f"    m_{element_name}GetMsGid = {startmsgid} + {i};\n")
        top.append(f"    m_temperatureSetMsGid = m_startMsgId + {i} + 1;\n")

        i = i + 2

    top.append(f"}}")

    for element in json_dict["signals"]:
        element_name = element["name"]
        element_type = element["type"]
        element_length = element["length"]
        top.append(f"\nstd::string CAN_{j_filename_lower}::get_{element_name}(){{\n")
        top.append(f"    std::stringstream sstream;\n")
        top.append(f'    sstream << "{{\\"ID\\": " << m_{element_name}GetMsGid\n')
        top.append(f'            << ", \\"length\\":0 "\n')
        top.append(f'            << ", \\"value\\": \\"\\" }}";\n')
        top.append(f"    return sstream.str();\n}}")

    n = 10
    for element in json_dict["signals"]:
        element_name = element["name"]
        element_type = element["type"]
        element_length = element["length"]
        top.append(
            f"std::string CAN_{j_filename_lower}::set_{element_name}({element_type} newValue){{\n"
        )
        top.append(f"    std::stringstream sstream;\n")
        top.append(f'    sstream << "{{\\"ID\\": " << m_{element_name}SetMsGid\n')
        top.append(f'            << ", \\"length\\":{n}"\n')
        top.append(f'            << ", \\"value\\":\\""\n')
        top.append(f"            << newValue\n")
        top.append(f'            << "\\" }}";\n')
        top.append(f"    return sstream.str();\n")

        n = n - 2
        top.append(f"}}\n")
    return top, bottom


def generate_source(json_filename, json_dict):
    output = []
    header_top, header_bottom = source_guard_class_constructor(json_filename)

    output += header_top
    output += header_bottom
    return output


if __name__ == "__main__":
    input_filename = "min_signals.json"

    filename_h = "/mnt/c/Users/nwabu/OneDrive/Desktop/CI_Assignment/CAN_Messages/output/include/can_messages/CAN_min_signals.h"
    filename_cpp = "/mnt/c/Users/nwabu/OneDrive/Desktop/CI_Assignment/CAN_Messages/output/src/min_signals.cpp"
    json_dict = {}
    with open(input_filename, "r") as file_fd:
        json_raw_content = file_fd.read()
        json_dict = json.loads(json_raw_content)
    print(json_dict)
    json_filename = input_filename.replace(".json", "")
    print(json_filename)

    header_content = generate_header(json_filename, json_dict)
    for element in header_content:
        print(element)
    write_func_header_file(filename_h, header_content)

    source_content = generate_source(json_filename, json_dict)
    for elements in source_content:
        print(elements)
    write_func_source_file(filename_cpp, source_content)
