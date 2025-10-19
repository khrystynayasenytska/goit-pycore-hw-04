def get_cats_info(path):
    try:
        cats_list = []
        with open(path, 'r', encoding='utf-8') as file:
           
            for line in file:
                # remove leading and trailing whitespace
                line = line.strip()
                
                # ignore empty lines
                if not line:
                    continue
                
                try:
                    # split line by comma
                    parts = line.split(',')
                    
                    # check for correct format
                    if len(parts) != 3:
                        print(f"Error: Line should have exactly 3 parts (id,name,age): {line}")
                        continue
                    
                    # clean the parts
                    cat_id = parts[0].strip()
                    cat_name = parts[1].strip()
                    cat_age = parts[2].strip()
                    
                    # validate name is not empty
                    if not cat_name:
                        print(f"Error: Name cannot be empty in line: {line}")
                        continue
                    
                    # create dictionary with validated data
                    cat_info = {
                        "id": cat_id,
                        "name": cat_name,
                        "age": cat_age
                    }
                    
                    # add to list
                    cats_list.append(cat_info)
                    
                except Exception as e:
                    print(f"Error processing line '{line}': {str(e)}")
                    continue
        
        return cats_list
        
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found")
        return []
    
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{path}'")
        return []
    
    except UnicodeDecodeError:
        print(f"Error: The file '{path}' is not in UTF-8 format")
        return []
    
    except Exception as e:
        print(f"Error: An unexpected error occurred while reading the file: {str(e)}")
        return []
    
cats_info = get_cats_info("c:/Users/Tiara/Documents/repos/goit-pycore-hw-04/Cats_info_task2.txt")
print(cats_info)