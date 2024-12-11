def read_tag(plc_connection, tag_name):
    tag_name, value, status = plc_connection.read_tag(tag_name)
    print(f"Tag: {tag_name}, Value: {value}, Status: {status}")
    return tag_name, value, status
