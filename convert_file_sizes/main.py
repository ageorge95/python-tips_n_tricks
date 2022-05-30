def convert_unit(size_in_bytes, unit):
    """ Convert the size from bytes to other units like KB, MB or GB"""

    if unit == "KB":
        return size_in_bytes / 1024

    elif unit == "MB":
        return size_in_bytes / (1024 * 1024)

    elif unit == "GB":
        return size_in_bytes / (1024 * 1024 * 1024)

    else:
        return size_in_bytes

if __name__ == '__main__':
    print(f"1000 bytes is"
          f" {convert_unit(1000, 'KB')}KB"
          f" {convert_unit(1000, 'MB')}MB"
          f" {convert_unit(1000, 'GB')}GB"
          )