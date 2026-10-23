# How Lightbulbs Work: Theory and Calculations  

## **1. Basic Operation of Lightbulbs**  
Lightbulbs convert electrical energy into light through different mechanisms depending on their type:  

### **a. Incandescent Bulbs**  
- **Mechanism**: A tungsten filament (resistance ≈ 10–100 Ω) is heated by electric current to ~2,500°C, emitting thermal radiation (black-body spectrum) in infrared and visible wavelengths.  
- **Key Process**: Joule heating ($ P = V^2/R $ or $ P = I^2R $) converts electrical energy to thermal energy, with ~90% radiated as infrared and 10% as visible light.  
- **Efficiency**: 10–15 lumens per watt (LPW), with most energy lost as heat.  

### **b. LED Bulbs**  
- **Mechanism**: Electrons recombine in a semiconductor material (gallium nitride), releasing photons via bandgap emission (quantum mechanics).  
- **Efficiency**: 80–100 LPW, with ~20–25% of energy converted to light (75–85% thermal loss).  

### **c. CFL Bulbs**  
- **Mechanism**: Mercury vapor emits ultraviolet light, which excites a phosphor coating to produce visible light.  
- **Efficiency**: 60–80 LPW, with ~15–20% energy converted to light.  

---

## **2. Core Calculations**  
### **a. Electrical Power**  
- **Formula**: $ P = V \times I $, where $ P $ is power (watts), $ V $ is voltage (volts), and $ I $ is current (amperes).  
- **Resistive Loads**: $ P = \frac{V^2}{R} $ or $ P = I^2R $ (for constant resistance $ R $).  

**Example**: A 60W incandescent bulb at 120V draws $ I = P/V = 0.5A $, with resistance $ R = V^2/P = 24 \Omega $.  

---

### **b. Photon Energy**  
- **Formula**: $ E = h \times f $, where $ h = 6.626 \times 10^{-34} \, \text{J·s} $ (Planck’s constant), and $ f $ is frequency (Hz).  
- **Wavelength Relation**: $ E = \frac{hc}{\lambda} $, where $ c $ is the speed of light ($ 3 \times 10^8 \, \text{m/s} $), and $ \lambda $ is wavelength (m).  

**Example**: A 500 nm LED photon has energy $ E = \frac{(6.626 \times 10^{-34})(3 \times 10^8)}{500 \times 10^{-9}} \approx 3.98 \times 10^{-19} \, \text{J} $.  

---

## **3. Efficiency and Energy Conversion**  
| Bulb Type     | Power (W) | Luminous Efficiency (LPW) | Thermal Loss (%) |  
|---------------|-----------|---------------------------|------------------|  
| Incandescent  | 60        | 10–15                     | 90–95            |  
| LED           | 8–12      | 80–100                    | 75–85            |  
| CFL           | 15–20     | 60–80                     | 80–90            |  

**Thermal Energy**: For a 60W incandescent bulb, 52W is lost as heat ($ P_{\text{thermal}} = P_{\text{input}} - P_{\text{light}} $).  

---

## **4. Limitations and Considerations**  
- **Incandescent Limitations**: Low efficiency due to infrared radiation; filament oxidation in air reduces lifespan.  
- **LED Advantages**: Higher efficiency, longer lifespan, and directional light emission.  
- **CFL Challenges**: Contains mercury, requiring careful disposal.  

---

## **References**  
1. [Incandescent Bulb Specifications](https://www.energy.gov)  
2. [LED Efficiency Data](https://www.energy.gov)  
3. [CFL Efficiency Data](https://www.energy.gov)  
4. [Physics Fundamentals](https://hyperphysics.phy-astr.gsu.edu)  
5. [Spectroscopy Data](https://www.nist.gov)  

This report synthesizes the physics and engineering principles behind lightbulb operation, emphasizing energy conversion and efficiency.