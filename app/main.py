from sys import argv
import mac_copy


if __name__ == '__main__':
    source = argv[1]
    destination = argv[2]

    mac_copy.check_files.check_source(source, destination)
