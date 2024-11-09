import numpy as np

# Define the Pauli matrices and Hadamard gate
sigma_x = np.array([[0, 1], [1, 0]])
sigma_z = np.array([[1, 0], [0, -1]])
hadamard = (1 / np.sqrt(2)) * np.array([[1, 1], [1, -1]])

def apply_gate(gate, state, qubit, num_qubits):
    """Apply a single-qubit gate to a specific qubit in a multi-qubit state."""
    full_gate = np.eye(1)
    for i in range(num_qubits):
        if i == qubit:
            full_gate = np.kron(full_gate, gate)
        else:
            full_gate = np.kron(full_gate, np.eye(2))
    return np.dot(full_gate, state)

def apply_cnot(control, target, state, num_qubits):
    """Apply a CNOT gate to a specific pair of qubits in a multi-qubit state."""
    dim = 2 ** num_qubits
    cnot = np.eye(dim)
    for i in range(dim):
        if (i >> control) & 1:
            j = i ^ (1 << target)
            cnot[i, i], cnot[i, j] = 0, 1
    return np.dot(cnot, state)

def measure(state, qubit, num_qubits):
    """Measure a specific qubit in a multi-qubit state."""
    basis_0 = np.zeros_like(state)
    basis_1 = np.zeros_like(state)
    basis_0[0::2**(num_qubits - qubit - 1)] = 1 / np.sqrt(2)  # |0> basis
    basis_1[1::2**(num_qubits - qubit - 1)] = 1 / np.sqrt(2)  # |1> basis
    
    prob_0 = np.linalg.norm(np.dot(basis_0, state)) ** 2
    measurement = 0 if np.random.random() < prob_0 else 1
    new_state = basis_0 if measurement == 0 else basis_1
    return measurement, new_state

def teleportation(psi):
    """
    Perform quantum teleportation of the state psi.
    
    Parameters:
    psi (np.array): The quantum state to be teleported. Should be a 1D array of length 2.
    
    Returns:
    np.array: The teleported state.
    """
    # Number of qubits
    num_qubits = 3
    
    # Create the initial state |psi> ⊗ |00>
    initial_state = np.kron(np.kron(psi, [1, 0]), [1, 0])
    
    # Apply a Hadamard gate to the second qubit
    state = apply_gate(hadamard, initial_state, 1, num_qubits)
    
    # Apply a CNOT gate with the second qubit as control and the third qubit as target
    state = apply_cnot(1, 2, state, num_qubits)
    
    # Apply a CNOT gate with the first qubit as control and the second qubit as target
    state = apply_cnot(0, 1, state, num_qubits)
    
    # Apply a Hadamard gate to the first qubit
    state = apply_gate(hadamard, state, 0, num_qubits)
    
    # Measure the first and second qubits
    m0, state = measure(state, 0, num_qubits)
    m1, state = measure(state, 1, num_qubits)
    print("Alice's measurements:", m0, m1)
    
    # Apply the necessary corrections to the third qubit based on the measurement results
    if m0 == 0 and m1 == 1:
        state = apply_gate(sigma_x, state, 2, num_qubits)
    elif m0 == 1 and m1 == 0:
        state = apply_gate(sigma_z, state, 2, num_qubits)
    elif m0 == 1 and m1 == 1:
        state = apply_gate(sigma_x, state, 2, num_qubits)
        state = apply_gate(sigma_z, state, 2, num_qubits)
    
    # Extract Bob's qubit (the third qubit)
    bob_state = state[4:6]  # indices where the third qubit is 1 (100 and 101)
    
    # Normalize Bob's state
    bob_state /= np.linalg.norm(bob_state)
    
    return bob_state

# Function to parse user input
def parse_input(input_str):
    try:
        parsed_input = list(map(int, input_str.split(',')))
        if len(parsed_input) != 2 or not all(x in [0, 1] for x in parsed_input):
            raise ValueError
        return np.array(parsed_input)
    except ValueError:
        print("Invalid input. Please enter exactly two values, each being 0 or 1.")
        return None

# Main loop to get user input
while True:
    input_state = input("Enter the state as a comma-separated pair of 0 or 1 (e.g., 0,1): ")
    psi = parse_input(input_state)
    if psi is not None:
        break

# Perform teleportation
teleported_state = teleportation(psi)
print("Teleported state:", teleported_state)