import os
import time

def create_directory_structure(base_path):
    for i in range(0, 10):
        path_level_1 = os.path.join(base_path, str(i))
        os.makedirs(path_level_1, exist_ok=True)
        
        for j in range(0, 10):
            path_level_2 = os.path.join(path_level_1, str(j))
            os.makedirs(path_level_2, exist_ok=True)
            
            for k in range(0, 10):
                path_level_3 = os.path.join(path_level_2, str(k))
                os.makedirs(path_level_3, exist_ok=True)
                
                for l in range(0, 10):
                    path_level_4 = os.path.join(path_level_3, str(l))
                    os.makedirs(path_level_4, exist_ok=True)

# Set the base path where you want to create the directory structure
base_path = r'F:/Confidential'

# Measure the time taken to create the directory structure
start_time = time.time()
create_directory_structure(base_path)
end_time = time.time()

print(f"Time taken: {end_time - start_time} seconds")
