# Hardware Specification: Dual-Orbital Temporal Variance Apparatus

## 1. System Overview
The apparatus comprises a synchronized constellation of two orbital satellites (Satellite Alpha and Satellite Beta) rotating around a central planetary body (the bipolar axis). The system is designed to measure the relative experience of time and signal decay based on the orbital radius, validating that time variance is directly proportional to the perimeter of a complete oscillation. 

## 2. Orbital Mechanics & Flight Telemetry
Unlike standard Keplerian orbits where velocity is inversely proportional to altitude, Satellite Alpha (inner orbit) and Satellite Beta (outer orbit) are dynamically locked to the exact same angular velocity ($\omega$). 
* **Satellite Alpha:** Positioned at a short radial distance. Travels a shorter perimeter per single oscillation.
* **Satellite Beta:** Positioned at a longer radial distance. Travels a greater perimeter per single oscillation.
* **Station-Keeping:** To maintain identical angular velocity despite differing altitudes, continuous active propulsion is required. Real-time flight telemetry and collision avoidance software will constantly adjust the thrust vectors to keep both satellites perfectly aligned along the same radial line originating from the Earth's center.

## 3. The Measurement Payload (Hexadecimal Timing)
Both satellites will be equipped with identical, native-hardware hexadecimal logic clocks. 
* Because the Earth acts as a massive electromagnet (a planetary coil), Satellite Alpha represents an oscillation closer to the "inside of an electric coil," while Satellite Beta represents an orbit further outside.
* The payloads will continuously ping each other using hexadecimal digital signals. The system will measure the delta in signal decay, physical component fatigue, and clock drift between the two satellites over continuous orbital oscillations.
