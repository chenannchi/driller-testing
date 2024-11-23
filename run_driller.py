import driller
import logging

logging.basicConfig(level=logging.DEBUG)

# Path to the AFL input file and bitmap
# afl_input_file = './afl_inputs/input1'
# afl_bitmap_file = './afl_outputs/fuzz_bitmap'

with open('./afl_outputs/queue/id:000000,orig:input1', 'rb') as f:
    afl_input_data = f.read()

with open('./afl_outputs/fuzz_bitmap', 'rb') as f:
    afl_bitmap = f.read()

# Read the AFL input file
# with open(afl_input_file, 'rb') as f:
#     afl_input_data = f.read()

# Read the AFL bitmap (optional, but improves accuracy)
# try:
#     with open(afl_bitmap_file, 'rb') as f:
#         afl_bitmap = f.read()
# except FileNotFoundError:
#     print("Warning: AFL bitmap not found. Using placeholder.")
#     afl_bitmap = b'\xff' * 65535

# Initialize Driller
d = driller.Driller(
    "./target_binary",  # Target binary
    afl_input_data,     # Initial test case from AFL input
    afl_bitmap          # AFL bitmap
)

# Run Driller to find new test cases
try:
    new_inputs = d.drill()
    print("New test cases found:", new_inputs)
except Exception as e:
    print("Error during drilling:", e)
