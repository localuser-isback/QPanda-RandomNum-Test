from pyqpanda import *

# Initialize the QVM
qvm = CPUQVM()
qvm.init_qvm()

# Create a quantum program
prog = QProg()

# Allocate a quantum register and a classical register
q = qvm.qAlloc()
c = qvm.cAlloc()

# Apply a Hadamard gate to the qubit
prog << H(q[0])

# Measure the qubit
prog << Measure(q[0], c[0])

# Run the program on the QVM
result = qvm.run(prog)

# Convert the measurement result to a decimal number
random_number = int(result[0])

# Print the random number
print("Random number:", random_number)

# Finalize the QVM
qvm.finalize()
