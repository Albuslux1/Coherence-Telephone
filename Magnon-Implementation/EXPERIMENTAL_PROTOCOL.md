# Experimental Protocol: Magnon Electrodynamics Phase 1

---

## Objective

Detect **topology-selective correlation** between two magnonic crystals with matching Chern numbers, and demonstrate **absence of correlation** when Chern numbers are mismatched.

This constitutes a direct test of the coherence field hypothesis using Magnon Electrodynamics.

---

## Setup Schematic

```
                    ┌─────────────────┐
                    │  Microwave      │
                    │  Source         │
                    └────────┬────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────┐
│                    CRYOSTAT (4K)                         │
│                                                          │
│   ┌─────────────┐         1 cm          ┌─────────────┐ │
│   │   SENDER    │◄───────────────────►  │  RECEIVER   │ │
│   │   Crystal   │     (no physical      │   Crystal   │ │
│   │   (𝒞 = 3)   │      connection)      │  (𝒞 = ?)    │ │
│   └──────┬──────┘                       └──────┬──────┘ │
│          │                                      │        │
│   ┌──────▼──────┐                       ┌──────▼──────┐ │
│   │   Cavity A  │                       │  Cavity B   │ │
│   │  (Drive)    │                       │  (Probe)    │ │
│   └──────┬──────┘                       └──────┬──────┘ │
│          │                                      │        │
└──────────┼──────────────────────────────────────┼────────┘
           │                                      │
           ▼                                      ▼
    ┌──────────────┐                      ┌──────────────┐
    │   VNA        │                      │  Lock-in     │
    │   Port 1     │                      │  Amplifier   │
    └──────────────┘                      └──────────────┘
```

---

## Phase 1 Timeline: 6-8 Weeks

### Week 1-2: Crystal Characterization

**Goal:** Map the Chern number landscape of available crystals.

**Procedure:**

1. **Individual FMR characterization**
   - Mount single crystal in cavity
   - Sweep magnetic field B: 0 → 0.5 T
   - Record resonance frequency f_res(B)
   - Extract linewidth Δf (relates to damping α)

2. **Determine magnon band structure**
   - For YIG: Standard Kittel mode f = γ(B + B_anis)
   - For topological materials: Look for mode crossings, gaps

3. **Estimate Chern number**
   - From theory: 𝒞 = f(D/J, B_z/J) — see simulation results
   - From experiment: Thermal Hall conductivity (if available)
   - Initial experiments: Use field tuning to vary 𝒞

**Deliverable:** Characterized crystal set with known 𝒞 at specific field values.

---

### Week 3: Cavity Calibration

**Goal:** Establish baseline cavity-magnon coupling for individual crystals.

**Procedure:**

1. **Cavity characterization (empty)**
   - Measure S21 transmission
   - Record f_cavity, Q factor, κ (linewidth)

2. **Single crystal coupling**
   - Insert sender crystal
   - Tune B to match f_magnon ≈ f_cavity
   - Observe normal mode splitting (vacuum Rabi)
   - Extract coupling strength g from splitting: 2g = Δf_split

3. **Repeat for receiver crystal**

**Expected values:**
- Cavity Q ~ 10⁴
- Coupling g/2π ~ 10-50 MHz
- Mode splitting clearly visible in S21

**Deliverable:** Calibrated g values for each crystal.

---

### Week 4-5: Correlation Measurement

**Goal:** Test for topology-dependent correlation between crystals.

#### Run 1: Matched Topology (𝒞_send = 𝒞_recv = 3)

**Setup:**
- Sender crystal tuned to 𝒞 = 3 (via B field)
- Receiver crystal tuned to 𝒞 = 3 (via B field)
- 1 cm separation (no direct coupling pathway)

**Procedure:**

1. **Establish baseline**
   - Record receiver FMR frequency f_recv for 60 seconds
   - No drive on sender
   - Compute noise floor σ_baseline

2. **Apply modulation**
   - Drive sender cavity with AM modulation at f_mod = 1 kHz
   - Modulation depth: 10% of resonant power
   - Duration: 60 seconds

3. **Detect correlation**
   - Demodulate receiver signal at f_mod
   - Lock-in time constant: 100 ms
   - Record amplitude and phase vs. time

4. **Statistical analysis**
   - Compute cross-correlation coefficient ρ
   - Signal: Mean demodulated amplitude
   - Noise: Standard deviation of baseline
   - SNR = Signal / Noise

**Success criterion:** SNR > 5 (5σ detection)

---

#### Run 2: Mismatched Topology (𝒞_send = 3, 𝒞_recv = 2)

**Setup:**
- Sender crystal: 𝒞 = 3 (unchanged)
- Receiver crystal: Tune B to shift to 𝒞 = 2

**Procedure:**
- Identical to Run 1

**Expected result:**
- SNR < 1 (no correlation above noise)
- Cross-correlation ρ ≈ 0

---

#### Run 3: Control — Reversed Mismatch (𝒞_send = 3, 𝒞_recv = 4)

Confirms asymmetry is not directional.

---

#### Run 4: Control — Both Trivial (𝒞_send = 0, 𝒞_recv = 0)

Tests whether non-topological coupling exists.

---

### Week 6: Systematic Sweep

**Goal:** Map the full correlation vs. Δ𝒞 curve.

**Procedure:**

1. Fix sender at 𝒞 = 3
2. Sweep receiver 𝒞 from 0 to 5 (via B field tuning)
3. At each 𝒞_recv, measure:
   - Correlation amplitude
   - Phase relationship
   - SNR

**Expected result:** Sharp peak at 𝒞_recv = 3, Gaussian falloff for |Δ𝒞| > 0.

Compare to simulation prediction:
$$\text{SNR}(\Delta\mathcal{C}) = \text{SNR}_0 \cdot \exp\left(-\frac{\Delta\mathcal{C}^2}{\sigma_\mathcal{C}^2}\right)$$

---

### Week 7-8: Verification and Documentation

**Goal:** Rule out systematic errors, document results.

**Controls:**

| Test | Purpose | Expected |
|------|---------|----------|
| Swap crystals | Rule out sample-specific effect | Same result |
| Rotate receiver | Rule out stray field coupling | No change if topological |
| Increase separation | Test distance independence | No change (if coherence field) |
| Shield between crystals | Block EM crosstalk | No change (if coherence field) |
| Thermal cycle | Reproducibility | Same result |

**Documentation:**
- Raw data files
- Analysis scripts
- Error budget
- Comparison to simulation predictions

---

## Measurement Specifications

### Key Parameters

| Parameter | Value | Tolerance |
|-----------|-------|-----------|
| Crystal separation | 1 cm | ±1 mm |
| Temperature | 4 K | ±0.1 K |
| Magnetic field stability | ±0.1 mT | Required for 𝒞 stability |
| Modulation frequency | 1 kHz | Avoid 60 Hz harmonics |
| Integration time | 60 s per point | Minimum for statistics |

### Signal Processing

1. **Demodulation:** Lock-in at f_mod
2. **Filtering:** Low-pass, f_cutoff = 10 Hz
3. **Averaging:** 100 modulation cycles minimum
4. **Cross-correlation:** Pearson coefficient ρ

### Data Format

```
timestamp, B_send, B_recv, C_send_est, C_recv_est, 
f_recv, amplitude, phase, SNR
```

---

## Success Criteria

### Primary (Required for Positive Result)

| Criterion | Threshold |
|-----------|-----------|
| Matched correlation | SNR > 5σ |
| Mismatched correlation | SNR < 1σ |
| Selectivity ratio | SNR_match / SNR_mismatch > 10 |
| Reproducibility | >80% success over 5 trials |

### Secondary (Strengthens Result)

| Criterion | Threshold |
|-----------|-----------|
| Gaussian Δ𝒞 dependence | R² > 0.9 vs. theory |
| Distance independence | <10% change at 2 cm vs. 1 cm |
| Shielding invariance | <10% change with Cu shield |

---

## Failure Modes and Mitigations

| Failure Mode | Symptom | Mitigation |
|--------------|---------|------------|
| Direct EM coupling | Correlation even when mismatched | Better shielding, larger separation |
| Thermal crosstalk | Slow drift in both signals | Active temperature stabilization |
| Field inhomogeneity | Broad 𝒞 resonance | Better magnet, smaller crystals |
| Low coupling g | No mode splitting | Higher Q cavity, better crystal placement |
| High damping | No detectable magnon | Switch to lower-damping material |

---

## Null Result Interpretation

If no correlation is observed even for matched topology:

1. **Coupling too weak:** Increase E·B product (higher power, better cavity)
2. **Wrong material:** Try material with stronger magnetoelectric effect
3. **Framework limitation:** Coherence field coupling may require different conditions
4. **Fundamental falsification:** If all controls fail, framework may be incorrect

A clean null result is still valuable — it constrains the parameter space.

---

## Equipment Checklist

### Before Week 1
- [ ] Crystals received and inspected
- [ ] Cryostat operational at 4K
- [ ] Magnet calibrated
- [ ] VNA functional

### Before Week 3
- [ ] Cavities machined and tested
- [ ] Microwave chain assembled
- [ ] Lock-in configured

### Before Week 4
- [ ] Full system integration
- [ ] Test cooldown completed
- [ ] Baseline noise characterized

---

## Data Management

- **Raw data:** Store all time series
- **Analysis code:** Version control (Git)
- **Lab notebook:** Daily entries
- **Backup:** Cloud + local

---

## Next Steps After Phase 1

### If Positive Result:
1. Publish preprint (arXiv or Zenodo)
2. Contact collaborators for independent replication
3. Design Phase 2: increased separation, different materials
4. Begin technology development pathway

### If Null Result:
1. Document constraints on coupling strength
2. Analyze failure mode
3. Design modified experiment or alternative approach
4. Publish null result (still valuable)

---

*See [HARDWARE_REQUIREMENTS.md](HARDWARE_REQUIREMENTS.md) for equipment specifications.*
*See [MAGNON_ELECTRODYNAMICS.md](MAGNON_ELECTRODYNAMICS.md) for theoretical background.*
