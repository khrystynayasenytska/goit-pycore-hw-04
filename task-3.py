import sys
from pathlib import Path
from colorama import Fore, Style, init

# Initialize colorama for color support across different OS
init(autoreset=True)


def display_directory_structure(path, prefix="", is_last=True):
    """
    Args:
        path (Path): Path to directory or file
        prefix (str): Prefix for tree formatting
        is_last (bool): Whether the element is last in the list
    """
    try:
        # Define symbols for building the tree
        connector = "┗━━ " if is_last else "┣━━ "
        
        if path.is_dir():
            # Display directory name in blue color with folder emoji
            print(f"{prefix}{connector}{Fore.BLUE}📂 {path.name}/{Style.RESET_ALL}")
            
            # Get list of elements in the directory
            try:
                contents = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
            except PermissionError:
                print(f"{prefix}{'   ' if is_last else '┃  '}{Fore.RED}[Access Denied]{Style.RESET_ALL}")
                return
            
            # Define new prefix for nested elements
            extension = "   " if is_last else "┃  "
            
            # Recursively process each element
            for i, item in enumerate(contents):
                is_last_item = (i == len(contents) - 1)
                display_directory_structure(item, prefix + extension, is_last_item)
        else:
            # Display file name in green color with document emoji
            print(f"{prefix}{connector}{Fore.GREEN}📜 {path.name}{Style.RESET_ALL}")
            
    except Exception as e:
        print(f"{prefix}{connector}{Fore.RED}[Error: {e}]{Style.RESET_ALL}")


def main():
    """
    Main function of the script. Processes command line arguments
    and launches directory structure visualization.
    """
    # Check if command line argument is provided
    if len(sys.argv) < 2:
        # Use testenv directory as default
        directory_path = Path(r"")
    else:
        # Get path from command line arguments
        directory_path = Path(sys.argv[1])
    
    # Check if path exists
    if not directory_path.exists():
        print(f"{Fore.RED}Error: Path '{directory_path}' does not exist{Style.RESET_ALL}")
        sys.exit(1)
    
    # Check if it's a directory
    if not directory_path.is_dir():
        print(f"{Fore.RED}Error: '{directory_path}' is not a directory{Style.RESET_ALL}")
        sys.exit(1)
    
    # Display header
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Directory Structure: {Fore.YELLOW}{directory_path.absolute()}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}\n")
    
    # Display root directory
    print(f"{Fore.BLUE}📦 {directory_path.name}/{Style.RESET_ALL}")
    
    # Get and sort directory contents
    try:
        contents = sorted(directory_path.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
        
        # Process each element
        for i, item in enumerate(contents):
            is_last = (i == len(contents) - 1)
            display_directory_structure(item, "", is_last)
            
    except PermissionError:
        print(f"{Fore.RED}Error: No permissions to read directory{Style.RESET_ALL}")
        sys.exit(1)
    except Exception as e:
        print(f"{Fore.RED}Error processing directory: {e}{Style.RESET_ALL}")
        sys.exit(1)
    
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}\n")


if __name__ == "__main__":
    main()
