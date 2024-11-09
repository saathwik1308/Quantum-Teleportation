# Quantum Teleportation Simulation

## Table of Contents
- [Project Description](#project-description)
- [Abstract](#abstract)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Details](#project-details)
- [Example Output](#example-output)
- [Challenges and Future Scope](#challenges-and-future-scope)
- [Acknowledgements](#acknowledgements)
- [References](#references)

## Project Description
This project simulates quantum teleportation using Python. The simulation demonstrates the principles of quantum teleportation, focusing on how quantum information can be transferred using entanglement and measurement, rather than physically moving particles.

## Abstract
Quantum teleportation enables the transmission of quantum information between locations without physical transport of the particles. Through a Python simulation, this project illustrates the teleportation process, including the roles of Alice (the sender) and Bob (the receiver), and the critical concept of entanglement. The simulation captures essential steps like state encoding, Bell state measurement, and classical information transfer, highlighting teleportation's potential in quantum communication and computation.

## Requirements
- Python 3.x
- Libraries:
  - `numpy`

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/quantum-teleportation-simulation.git
   
## Usage
To run the quantum teleportation simulation:

Open your terminal in the project directory.
Run the main script:
bash
Copy code
python teleportation_simulation.py
The simulation will output results based on the initial quantum state defined within the code.

## Project Details
This simulation involves several steps:

Entangled Partners: The project simulates entangled particles, linking them so that measurement on one affects the other.
State Encoding (Alice's Side): Alice combines her qubit with one of the entangled particles.
Bell State Measurement: Alice measures the combined qubits, impacting Bob's qubit through their entangled connection.
Classical Information Transfer: Alice sends classical bits to Bob, guiding his next steps.
State Reconstruction (Bob's Side): Bob applies corrections to his qubit to match Alice’s initial quantum state.
##Core Functions:
apply_gate: Applies single-qubit gates.
apply_cnot: Applies the CNOT gate to entangled pairs.
measure: Simulates measurement on specific qubits.
teleportation: Orchestrates the quantum teleportation process by combining these operations.
## Example Output
The following shows a sample input and output for the simulation:

Input: [0, 1] (representing |1> state)
Output: The teleported state displayed in the terminal.

## Challenges and Future Scope
While this simulation demonstrates the basics of quantum teleportation, it also highlights some challenges and areas for future work:

Error Correction: Mitigating quantum noise to maintain the accuracy of teleported states.
Scalability: Scaling up to multiple entangled qubits for complex teleportation tasks.
Applications: Exploring uses in secure communication networks and advanced quantum computing.

## Acknowledgements
This project was developed by Smitha Thodupunoori, Kongani Sai Sandeep, and Saathwik Penala under the guidance of Dr. Maheswara Rao Valluri as part of an internship at Quinfosystems Pvt Ltd.
## References
H. Bao et al., "Generation of two-dimensional cluster states for quantum computation," Physical Review Letters, 2014.
P. W. Shor and R. Laflamme, "Quantum error-correcting codes," Quantum Cryptography and Quantum Computation, Springer, 1998.
M. D. Lukin et al., "Quantum networks for entanglement distribution," Reviews of Modern Physics, 2015.
N. Gisin et al., "Quantum cryptography," Reviews of Modern Physics, 2002.
