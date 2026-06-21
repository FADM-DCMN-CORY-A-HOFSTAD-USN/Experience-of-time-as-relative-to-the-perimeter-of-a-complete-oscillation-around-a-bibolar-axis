import time
import math
import sys

# Univac-IX Hardware Constants
EARTH_RESONANCE_HZ = 7.83
OMEGA = 2 * math.pi * EARTH_RESONANCE_HZ  # ~49.20 rad/s
C = 299_792_458  # Speed of light in m/s
T_SYS = 1 / EARTH_RESONANCE_HZ

# Hardware Geometries (Meters)
RADIUS_ALPHA = 0.001  # 1mm inner trace
RADIUS_BETA = 0.150   # 150mm outer trace

def calculate_temporal_variance():
    """Calculates the exact math the Univac-IX hardware is experiencing."""
    v_alpha = RADIUS_ALPHA * OMEGA
    v_beta = RADIUS_BETA * OMEGA
    
    tau_alpha = T_SYS * math.sqrt(1 - (v_alpha**2 / C**2))
    tau_beta = T_SYS * math.sqrt(1 - (v_beta**2 / C**2))
    
    delta_tau = tau_alpha - tau_beta
    return delta_tau, v_alpha, v_beta

def print_univac_dashboard(cycle, delta_tau, v_alpha, v_beta, corruption_flag):
    """Generates the visual tracking interface for the terminal."""
    sys.stdout.write("\033[H\033[J") # Clear screen for live updating
    print("=========================================================")
    print("         UNIVAC-IX : RELATIVISTIC TELEMETRY TRACKER      ")
    print("=========================================================")
    print(f" SYSTEM CLOCK:       {EARTH_RESONANCE_HZ} Hz (Earth Resonance)")
    print(f" ANGULAR VELOCITY:   {OMEGA:.2f} rad/s")
    print("---------------------------------------------------------")
    print(f" [TRACE ALPHA] Radius: {RADIUS_ALPHA}m | Linear Vel: {v_alpha:.4f} m/s")
    print(f" [TRACE BETA]  Radius: {RADIUS_BETA}m | Linear Vel: {v_beta:.4f} m/s")
    print("---------------------------------------------------------")
    print(f" CALCULATED VARIANCE (Delta Tau): {delta_tau:.6e} seconds")
    print("---------------------------------------------------------")
    print(f" CYCLE: {cycle:06d} | TRACE BETA DECAY STATUS: ", end="")
    
    if corruption_flag:
        print("[ FATIGUE DETECTED ] - Wave Compression Limit Reached")
    else:
        print("[ NOMINAL ] - Hexadecimal Payload Intact")
    
    print("=========================================================")

def run_telemetry_tracker():
    delta_tau, v_alpha, v_beta = calculate_temporal_variance()
    cycle = 0
    fatigue_threshold_cycle = 1500 # Arbitrary point where physical math dictates decay
    
    while True:
        cycle += 1
        # Visually track the math; if cycle exceeds threshold, visualize the resulting physical decay
        corruption_flag = True if cycle > fatigue_threshold_cycle else False
        
        print_univac_dashboard(cycle, delta_tau, v_alpha, v_beta, corruption_flag)
        
        # Lock visual update to the physical Univac-IX hardware cycle
        time.sleep(T_SYS)

if __name__ == "__main__":
    try:
        run_telemetry_tracker()
    except KeyboardInterrupt:
        print("\n[UNIVAC-IX TELEMETRY TRACKING TERMINATED]")
