### Redis Options
REDIS_HOST=None
REDIS_PORT=None
REDIS_DB=None

### Celery Options
BROKER_URL= None

CELERY_ROUTES = None

### Environment Options

# directory contain driller-qemu versions, relative to the directoy node.py is invoked in
QEMU_DIR=None

# directory containing the binaries, used by the driller node to find binaries
BINARY_DIR="./target_program"
# directory containing the pcap corpus
PCAP_DIR=None
# directory containing the seeds for fuzzing
SEED_DIR="./afl_inputs"

### Driller options
# how long to drill before giving up in seconds
DRILL_TIMEOUT=60

MEM_LIMIT=None

# where to write a debug file that contains useful debugging information like
# AFL's fuzzing bitmap, input used, binary path, time started.
# Uses following naming convention:
#   <binary_basename>_<input_str_md5>.py
DEBUG_DIR = None

### Fuzzer options

# how often to check for crashes in seconds
CRASH_CHECK_INTERVAL=1

# how long to fuzz before giving up in seconds
FUZZ_TIMEOUT=300

# how long before we kill a dictionary creation process
DICTIONARY_TIMEOUT=30

# how many fuzzers should be spun up when a fuzzing job is received
FUZZER_INSTANCES=2

# where the fuzzer should place it's results on the filesystem
FUZZER_WORK_DIR="./afl_outputs"
