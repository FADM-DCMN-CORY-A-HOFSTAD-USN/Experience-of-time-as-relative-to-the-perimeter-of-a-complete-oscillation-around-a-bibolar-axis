import time
import math
import sys

# Univac-IX Hardcoded Physical Constraints
F_EARTH = 7.83
OMEGA = 2 * math.pi * F_EARTH
C = 299_792_458
T_SYS = 1 / F_EARTH

R_ALPHA = 0.001
R_BETA = 0.150
BASELINE_HEX = "0xDEADBEEFCAFEBABE"

def calculate_delta_tau():
    """Executes the core temporal variance calculation based on hardware radii."""
    v_a = R_ALPHA * OMEGA
    v_b = R_BETA * OMEGA
    tau_a = T_SYS * math.sqrt(1 - (v_a**2 / C**2))
    tau_b = T_SYS * math.sqrt(1 - (v_b**2 / C**2))
    return tau_a - tau_b

def poll_hardware_registers(cycle):
    """
    Simulates low-level polling of the physical exit node registers.
    In production, this reads directly from Univac-IX memory addresses.
    """
    # Simulate the physical wave compression failure at Beta trace after prolonged load
    fatigue_limit = 500 
    
    alpha_reg = BASELINE_HEX
    if cycle > fatigue_limit:
        beta_reg = "0xDEADBEEFCAFEBA00" # Hardware corruption / bit-flip simulated
        decay_flag = 1
    else:
        beta_reg = BASELINE_HEX
        decay_flag = 0
        
    return alpha_reg, beta_reg, decay_flag

def stream_telemetry():
    """Outputs raw, Alice-compliant diagnostic lines to the terminal."""
    delta_tau = calculate_delta_tau()
    cycle = 0
    
    sys.stdout.write(f"INIT_UNIVAC_IX_POLLER | OMEGA:{OMEGA:.4f} | D_TAU:{delta_tau:.6e}\n")
    
    while True:
        cycle += 1
        alpha_hex, beta_hex, decay_flag = poll_hardware_registers(cycle)
        
        # Raw log output format: [TIMESTAMP] [CYCLE] [ALPHA_REG] [BETA_REG] [DECAY_STATE]
        log_line = f"{time.time():.4f} | CYC:{cycle:06d} | A:{alpha_hex} | B:{beta_hex} | ERR:{decay_flag}\n"
        sys.stdout.write(log_line)
        sys.stdout.flush()
        
        time.sleep(T_SYS)

if __name__ == "__main__":
    stream_telemetry()
