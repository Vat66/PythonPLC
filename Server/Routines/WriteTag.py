def write_tag(plc_connection, tag_name, value):
    status = plc_connection.write_tag(tag_name, value)
    print(f"Write to {tag_name} completed with status: {status}")
    return status
