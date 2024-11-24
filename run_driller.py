import os
import driller

import logging
logging.basicConfig(level=logging.DEBUG)


# Path to the binary
binary_path = "./target_program"

# Path to AFL outputs
afl_outputs = "./afl_outputs/queue"

# Collect initial inputs from AFL outputs
initial_inputs = []
for filename in os.listdir(afl_outputs):
    file_path = os.path.join(afl_outputs, filename)
    if os.path.isfile(file_path):  # Ensure it's a file, not a directory
        with open(file_path, 'rb') as f:
            initial_inputs.append(f.read())

# Run Driller for each initial input
for initial_input in initial_inputs:
    dr = driller.Driller(binary_path, initial_input)
    new_inputs = dr.drill()
    for inp in new_inputs:
        print("New input discovered:", inp)