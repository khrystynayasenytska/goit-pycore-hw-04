def total_salary(path):
  
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0
            
            for line in file:
                # delete leading and trailing whitespace
                line = line.strip()
                
                # ignore empty lines
                if not line:
                    continue
                
                try:
                    # replace multiple commas with a single comma
                    line = line.replace(',,', ',')
                    
                    # if no comma found, replace last space with comma
                    if ',' not in line and ' ' in line:
                        last_space_index = line.rindex(' ')
                        line = line[:last_space_index] + ',' + line[last_space_index + 1:]
                    
                    # split line by comma
                    parts = line.split(',')
                    
                    if len(parts) != 2:
                        print(f"Wrong string format: {line}")
                        continue
                    
                    # get salary as float
                    salary = float(parts[1].strip())
                    
                    # sum up
                    total += salary
                    count += 1
                    
                except (ValueError, IndexError) as e:
                    print(f"We could not use the string '{line}': {e}")
                    continue
            
            # check the data validity
            if count == 0:
                print("The file does not contain valid salary data.")
                return (0, 0)
            
            # Avg salary
            average = total / count
            
            return (total, average)
            
    except FileNotFoundError:
        print(f"The file '{path}' was not found")
        return (0, 0)
    
    except PermissionError:
        print(f"You do not have right to read the file '{path}'")
        return (0, 0)
    
    except Exception as e:
        print(f"An error occured while working with the file: {e}")
        return (0, 0)
    

total, average = total_salary("c:/Users/Tiara/Documents/repos/goit-pycore-hw-04/salary_task1.txt")
print(f"Total salary: {total:.2f}, Avg salary: {average:.2f}")