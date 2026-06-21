import time
import threading
import hashlib

# System Constraints
EARTH_RESONANCE_HZ = 7.83
T_SYS = 1 / EARTH_RESONANCE_HZ  # 0.1277 seconds

# Virtual Perimeters (Data Volumes representing Radial Distance)
ALPHA_PERIMETER_SIZE = 10_000       # Small data volume (Inner Orbit)
BETA_PERIMETER_SIZE = 5_000_000     # Massive data volume (Outer Orbit)

BASELINE_HEX = b"0xDEADBEEFCAFEBABE"

class OscillationThread(threading.Thread):
    def __init__(self, name, perimeter_size):
        super().__init__()
        self.name = name
        self.perimeter_size = perimeter_size
        self.completed = False
        self.data_corruption = False

    def run(self):
        """Simulates the moving particle traveling along its designated perimeter."""
        start_time = time.time()
        
        try:
            # The 'travel' is represented by processing the hex data payload
            # over the volume of the designated perimeter
            for _ in range(self.perimeter_size):
                # Simulating load via cryptographic hashing
                _ = hashlib.sha256(BASELINE_HEX).hexdigest()
            
            execution_time = time.time() - start_time
            
            # If the transit exceeds the allowed temporal window (angular velocity sync),
            # it simulates wave compression failure and signal decay.
            if execution_time > T_SYS:
                self.data_corruption = True
            else:
                self.completed = True
                
        except Exception:
            self.data_corruption = True

def execute_synchronized_oscillation():
    print(f"--- INITIALIZING VIRTUAL BIPOLAR AXIS ---")
    print(f"Enforcing Angular Velocity Window: {T_SYS:.4f}s (7.83 Hz)\n")

    alpha_thread = OscillationThread("Trace Alpha", ALPHA_PERIMETER_SIZE)
    beta_thread = OscillationThread("Trace Beta", BETA_PERIMETER_SIZE)

    # Inject signals simultaneously
    alpha_thread.start()
    beta_thread.start()

    # Wait for the strict temporal window to close
    time.sleep(T_SYS)

    print("--- POLLING EXIT NODES ---")
    
    if alpha_thread.completed and not alpha_thread.data_corruption:
        print("[ALPHA] Transit Complete. Signal Intact. Minimal Load Verified.")
    else:
        print("[ALPHA] CRITICAL ERROR: Signal Decay Detected.")

    # Beta will likely fail or corrupt due to the massive perimeter requirement
    # within the exact same timeframe, proving the variance theory computationally.
    if beta_thread.completed and not beta_thread.data_corruption:
        print("[BETA] Transit Complete. Signal Intact.")
    else:
        print("[BETA] DECAY DETECTED: Computational Load Exceeded Temporal Window.")

if __name__ == "__main__":
    execute_synchronized_oscillation()
