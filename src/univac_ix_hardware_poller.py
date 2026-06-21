import time
import math
import sys

# Univac-IX Hardcoded Memory Addresses
ADDR_ALPHA_OUT = "0x1000_F1A0"
ADDR_BETA_OUT  = "0x1000_F1B0"
ADDR_DECAY_FLG = "0x1000_E000"

# Physical Constraints
F_EARTH = 7.83
T_SYS = 1 / F_EARTH
BASELINE_HEX = "0xDEADBEEFCAFEBABE"

def mem_read_64bit(address, cycle):
    """
    Simulates a direct C-style pointer read from the physical silicon register.
    In the native Univac-IX environment, this executes via assembly IN instructions.
    """
    # Simulate wave compression failure at Beta trace after prolonged orbital load
    fatigue_limit = 500 
    
    if address == ADDR_ALPHA_OUT:
        return BASELINE_HEX
        
    elif address == ADDR_BETA_OUT:
        if cycle > fatigue_limit:
            return "0xDEADBEEFCAFEBA00" # Hardware corruption / bit-flip simulated
        return BASELINE_HEX
        
    elif address == ADDR_DECAY_FLG:
        return 1 if cycle > fatigue_limit else 0
        
    return "0x0000000000000000"

def stream_telemetry():
    """Outputs raw, Alice-compliant diagnostic lines directly from memory addresses."""
    cycle = 0
    sys.stdout.write(f"INIT_UNIVAC_IX_MEM_POLLER | CLK:{F_EARTH}Hz | LOCK:TRUE\n")
    
    while True:
        cycle += 1
        
        # Direct hardware memory reads
        alpha_hex = mem_read_64bit(ADDR_ALPHA_OUT, cycle)
        beta_hex  = mem_read_64bit(ADDR_BETA_OUT, cycle)
        decay_flg = mem_read_64bit(ADDR_DECAY_FLG, cycle)
        
        # Raw log output format: [TIMESTAMP] [CYCLE] [ADDR_A_DATA] [ADDR_B_DATA] [HW_FLAG]
        log_line = f"{time.time():.4f} | CYC:{cycle:06d} | [{ADDR_ALPHA_OUT}]:{alpha_hex} | [{ADDR_BETA_OUT}]:{beta_hex} | FLAG:{decay_flg}\n"
        sys.stdout.write(log_line)
        sys.stdout.flush()
        
        time.sleep(T_SYS)

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
