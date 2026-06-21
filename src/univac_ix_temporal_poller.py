from chips.native.electromechanical.hex_native_bipolar_oscillator import HexNativeBipolarOscillator

class UnivacIXTemporalPoller:
    """
    Univac-IX SCADA integration for the RT Bipolar Oscillator.
    Polls the hardware-level time dilation and converts the analog 
    result to 72-character mainframe Fieldata standards.
    """
    def __init__(self):
        self.oscillator = HexNativeBipolarOscillator()

    def execute_diagnostic_poll(self, hull_velocity_state):
        """
        Initiates a read sequence on the Bipolar Oscillator based on current ship velocity.
        """
        variance_v = self.oscillator.measure_relativistic_time_variance(hull_velocity_state)
        
        # Convert hex voltage directly to Univac Fieldata telemetry format
        hex_char = hex(int(variance_v / 0.0625))[2:].upper()
        
        print("\n************************************************************************")
        print("U N I V A C - I X   T E M P O R A L   D I A G N O S T I C")
        print("************************************************************************")
        print(f"AXIS ALIGNMENT:      BIPOLAR (ALPHA/BETA SYNCED)")
        print(f"OSCILLATOR TEMP:     {self.oscillator.thermal_state_c:.1f}C")
        print(f"EXPERIENCED SHIFT:   HEX STATE {hex_char} ({variance_v}V)")
        print("STATUS:              NOMINAL. PERIMETER INTACT.")
        print("************************************************************************\n")
        
        return hex_char

# Execution
if __name__ == "__main__":
    poller = UnivacIXTemporalPoller()
    # Simulating the Saiya Hull moving at Hex A (0.625V / 62.5% Speed of Light)
    poller.execute_diagnostic_poll(velocity_state=0.625)
