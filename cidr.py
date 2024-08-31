def ip_to_binary(ip):
    """
    Convert an IPv4 address or subnet mask from dotted decimal format to a 32-bit binary string.

    Parameters:
    ip (str): The IPv4 address or subnet mask in dotted decimal format (e.g., '192.168.1.1' or '255.255.255.0').

    Returns:
    str: The binary representation of the IP address or subnet mask as a 32-bit binary string.
    """
    # Split the IP address or subnet mask into its four octets (e.g., '192.168.1.1' -> ['192', '168', '1', '1'])
    # Convert each octet from decimal to an 8-bit binary string and concatenate them
    # `int(octet)` converts the string representation of the octet to an integer
    # `:08b` formats the integer as an 8-bit binary string
    return ''.join(f'{int(octet):08b}' for octet in ip.split('.'))

def calculate_cidr(ip_addr, subnet_mask):
    """
    Calculate the CIDR notation for a given IP address and subnet mask.

    Parameters:
    ip_addr (str): The IPv4 address (e.g., '192.168.1.10').
    subnet_mask (str): The subnet mask in dotted decimal format (e.g., '255.255.255.0').

    Returns:
    str: The CIDR notation in the format 'IP_ADDRESS/PREFIX_LENGTH'.
    """
    # Convert the subnet mask to a 32-bit binary string
    binary_mask = ip_to_binary(subnet_mask)
    
    # Count the number of '1's in the binary string to determine the prefix length
    # The prefix length represents the number of bits set to 1 in the subnet mask
    prefix_length = binary_mask.count('1')
    
    # Format the result as 'IP_ADDRESS/PREFIX_LENGTH'
    return f"{ip_addr}/{prefix_length}"

def main():
    """
    Main function to prompt the user for an IP address and subnet mask,
    calculate the CIDR notation, and display the result.
    """
    # Prompt the user to enter an IPv4 address
    ip_addr = input("Enter an IPv4 address (e.g., 192.168.1.10): ")
    
    # Prompt the user to enter a subnet mask
    subnet_mask = input("Enter a subnet mask (e.g., 255.255.255.0): ")

    try:
        # Calculate the CIDR notation using the provided IP address and subnet mask
        cidr_notation = calculate_cidr(ip_addr, subnet_mask)
        
        # Display the CIDR notation result
        print(f"The CIDR notation for the network is: {cidr_notation}")
    except ValueError as e:
        # Handle any errors that occur (e.g., invalid IP address or subnet mask)
        print(f"Error: {e}")

# Check if the script is being run directly (not imported as a module)
if __name__ == "__main__":
    main()
