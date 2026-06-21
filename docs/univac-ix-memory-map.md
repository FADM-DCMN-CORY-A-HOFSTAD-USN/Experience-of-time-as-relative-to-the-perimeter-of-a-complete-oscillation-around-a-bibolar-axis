# Univac-IX Native Hardware Memory Allocation

## 1. System Architecture Overview
The Univac-IX processor utilizes a hardcoded memory map to isolate the temporal variance diagnostic data. The registers are physically located at the exit nodes of the respective electromagnetic oscillation traces.

## 2. Register Definitions
To ensure strict synchronization at the 7.83 Hz Earth-Resonance frequency, the diagnostic poller must read directly from the following hardcoded physical addresses:

*   **`0x1000_F1A0` (REG_ALPHA_OUT):** The 64-bit termination register for Trace Alpha (Minimal Perimeter). Located immediately adjacent to the central bipolar axis.
*   **`0x1000_F1B0` (REG_BETA_OUT):** The 64-bit termination register for Trace Beta (Maximum Perimeter). Located on the extreme outer edge of the silicon die.
*   **`0x1000_C000` (REG_SYS_CLOCK):** The central hardware clock enforcing the identical angular velocity ($\omega$). 
*   **`0x1000_E000` (REG_DECAY_FLAG):** A 1-bit hardware flag triggered when wave compression limits cause a voltage drop (signal decay) at the Beta exit node.

## 3. Read/Write Constraints
These addresses are strictly **Read-Only** for the diagnostic software. The native hardware logic writes to these registers once per 0.1277-second execution cycle. The diagnostic poller must ingest this data before the next cycle overwrites the register.
