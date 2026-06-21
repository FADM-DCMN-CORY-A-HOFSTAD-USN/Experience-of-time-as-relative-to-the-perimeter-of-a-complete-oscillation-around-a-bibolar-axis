# Univac-IX Hardware Diagnostic and Telemetry Logging

## 1. System Overview
The Univac-IX diagnostic suite is a low-level, non-transitory executable designed exclusively to poll the physical exit nodes of the Relativistic Time-Variance Measurement Apparatus. It does not generate a graphical user interface. It is a command-line interface (CLI) tool that extracts raw hexadecimal data from physical hardware registers and logs the mathematical calculations associated with physical wave compression limits.

## 2. Hardware Polling Vector
The diagnostic tool interfaces directly with the central logic core operating at the 7.83 Hz Earth-Resonance frequency constraint. It reads the raw bit-states of:
*   `REG_ALPHA_OUT`: The hardware register capturing the hexadecimal payload from the inner minimal oscillation perimeter.
*   `REG_BETA_OUT`: The hardware register capturing the hexadecimal payload from the outer maximum oscillation perimeter.

## 3. Mathematical Logging Output
The software processes the physical load differential and outputs a continuous chronological log file (e.g., `univac_telemetry.log`). For each physical 0.1277-second hardware cycle, it calculates the strict temporal variance:
$$ \Delta \tau = T_{sys} \left( \sqrt{1 - \frac{(r_{\alpha}\omega)^2}{c^2}} - \sqrt{1 - \frac{(r_{\beta}\omega)^2}{c^2}} \right) $$

The log records the raw hexadecimal strings, the computed $\Delta \tau$, and flags any bit-flip discrepancies as `PHYSICAL_DECAY_TRUE`, allowing engineers to track the exact clock cycle where the trace metal experienced structural fatigue due to orbital load.
