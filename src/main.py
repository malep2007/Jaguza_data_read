import listener

if listener.check_port_is_available() is False:
    # print("\nThe Listening port is not available")
    print "\nThe Listening port is not available"
    exit()
else:
    # print("\n\t\t\tThe Listening Port is available\n")
    print "\n\t\t\tThe Listening Port is available\n"
    listener.listen_process()
