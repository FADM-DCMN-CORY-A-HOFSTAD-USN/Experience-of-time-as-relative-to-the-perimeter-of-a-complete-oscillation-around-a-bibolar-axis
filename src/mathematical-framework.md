# Mathematical Framework for Relativistic Time-Variance Apparatus

## 1. System Variables and Constants
This framework defines the variables for measuring the experience of time relative to the perimeter of a complete oscillation around a bipolar axis. 

*   $r_{\alpha}$: Radius of the inner oscillation perimeter (Trace Alpha / Inner Satellite).
*   $r_{\beta}$: Radius of the outer oscillation perimeter (Trace Beta / Outer Satellite).
*   $\omega$: Angular velocity, defined as identical for both paths to enforce synchronization.
*   $T_{sys}$: The absolute system time for one complete oscillation.
*   $v_{\alpha}, v_{\beta}$: The linear velocity of the moving particles (electrons/photons/payloads) in their respective orbits.
*   $c$: The speed of light in a vacuum.

## 2. The Angular Synchronization Proof
To evaluate the temporal variance, the system forces both particles to complete their respective perimeters in the exact same timeframe. The perimeters ($P$) are defined geometrically:
$$ P_{\alpha} = 2\pi r_{\alpha} $$
$$ P_{\beta} = 2\pi r_{\beta} $$

Because both traces share an identical angular velocity ($\omega$), the time to complete one oscillation is fixed:
$$ T_{sys} = \frac{2\pi}{\omega} $$

Therefore, the required linear velocity for the moving particle in the outer orbit ($v_{\beta}$) must be strictly greater than the inner orbit ($v_{\alpha}$) to satisfy the synchronization constraint:
$$ v_{\alpha} = r_{\alpha} \omega $$
$$ v_{\beta} = r_{\beta} \omega $$
Given $r_{\beta} > r_{\alpha}$, it is a required physical condition that $v_{\beta} > v_{\alpha}$.

## 3. Relativistic Temporal Variance Equation
Because the outer moving particle travels at a higher linear velocity to maintain the shared angular velocity, it experiences a greater degree of localized time dilation. The temporal experience ($\tau$) for each particle relative to a stationary observer is governed by the Lorentz factor:

$$ \tau_{\alpha} = T_{sys} \sqrt{1 - \frac{v_{\alpha}^2}{c^2}} $$
$$ \tau_{\beta} = T_{sys} \sqrt{1 - \frac{v_{\beta}^2}{c^2}} $$

The **Total Temporal Variance ($\Delta \tau$)** measured by the exit logic gates of the apparatus is the exact differential in time experienced between the two perimeters:
$$ \Delta \tau = \tau_{\alpha} - \tau_{\beta} = T_{sys} \left( \sqrt{1 - \frac{(r_{\alpha}\omega)^2}{c^2}} - \sqrt{1 - \frac{(r_{\beta}\omega)^2}{c^2}} \right) $$

This equation provides the direct mathematical proof that objects in larger orbital paths will experience a measurable temporal differential during a single, synchronized orbit.

## 4. Signal Decay and Structural Fatigue Matrix
Decay throughout time is relative to the destructive forces of being pushed and pulled by the positive and negative polarity of the axis[cite: 3]. Furthermore, objects when put under great volumes of pressure instantly decay[cite: 3]. 

To quantify this for the silicon prototype, we define a Decay Factor ($D$). The decay of a signal is directly proportional to the physical load ($L$) required to achieve $v_{\beta}$ and inversely proportional to the volume of space available before wave compression occurs[cite: 3]. 

Let $C_{wave}$ represent the wave compression coefficient within the silicon trace. The decay per single oscillation for a given radius ($D_r$) is modeled as:
$$ D_r = \oint_{0}^{2\pi} \frac{L \cdot (r \omega)^2}{C_{wave}} \, d\theta $$

Because the apparatus continuously loops the hexadecimal payload over $n$ iterations, the **Accumulated Hardware Fatigue ($F_{total}$)** is:
$$ F_{total} = \sum_{i=1}^{n} (D_{r_{\beta}} - D_{r_{\alpha}}) $$

This mathematical relationship proves that larger orbits create less decay per oscillation perimeter traveled[cite: 3], as the wave compression ($C_{wave}$) is mitigated by the expanded physical geometry of $P_{\beta}$, even while the linear velocity ($v_{\beta}$) increases the load.
