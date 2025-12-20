# Hardware Requirements: Magnon Electrodynamics Tabletop Experiment

---

## Overview

This document specifies the complete hardware needed for a Phase 1 validation experiment using Magnon Electrodynamics. Total estimated cost: **$150K - $250K**.

---

## Core Components

### 1. Magnonic Crystals (Sender and Receiver)

| Specification | Requirement | Options |
|---------------|-------------|---------|
| Material | Topological magnon insulator | YIG, kagome ferromagnet, MnBi₂Te₄ |
| Chern number | Tunable 𝒞 = 1-5 | Via DM interaction + Zeeman field |
| Size | 0.3 - 1 mm diameter | Spheres preferred for uniform mode |
| Quality | Low Gilbert damping (α < 10⁻⁴) | Single crystal, polished |
| Quantity | Minimum 2 matched + 2 mismatched | 4-6 total recommended |

**Cost:** $5K - $20K (custom growth or commercial YIG spheres)

**Suppliers:**
- Surface Preparation Laboratory (YIG spheres)
- Denselight Semiconductors
- Custom growth via university collaboration

---

### 2. Cryogenic System

| Specification | Requirement | Notes |
|---------------|-------------|-------|
| Base temperature | ≤ 4K | 4K sufficient; mK not required |
| Type | Closed-cycle or flow cryostat | Closed-cycle preferred (lower OpEx) |
| Sample space | > 2 cm diameter | Must fit microwave cavity |
| Optical access | Optional | Useful for alignment |
| Magnetic field compatibility | Must tolerate 1-2 T | Non-magnetic construction |

**Cost:** $50K - $80K

**Options:**
- Montana Instruments Cryostation (~$80K)
- attocube attoDRY800 (~$70K)
- Custom Janis/Bluefors 4K insert (~$50K)

**Note:** Room-temperature experiments possible with YIG, but 4K improves signal-to-noise significantly.

---

### 3. Magnet System

| Specification | Requirement | Notes |
|---------------|-------------|-------|
| Field strength | 0 - 2 T | Tune magnon frequency + Chern number |
| Orientation | Ideally 3-axis (vector) | 1-axis sufficient for initial tests |
| Homogeneity | < 0.1% over sample | Critical for sharp FMR linewidth |
| Sweep rate | 0.01 - 1 T/min | For field-sweep FMR |

**Cost:** $20K - $40K

**Options:**
- GMW 3470 electromagnet ($15K)
- American Magnetics superconducting 2T ($35K)
- Cryogenic Ltd vector magnet ($40K)

---

### 4. Microwave Cavity

| Specification | Requirement | Notes |
|---------------|-------------|-------|
| Frequency | 1 - 20 GHz tunable | Match magnon FMR frequency |
| Q factor | > 10⁴ | High Q for strong coupling |
| Mode | TE₁₀₁ or similar | Uniform E-field at sample |
| Material | Copper or superconducting | OFHC copper for 4K operation |
| Coupling | Adjustable input/output | Critical coupling for transmission |

**Cost:** $10K - $20K

**Options:**
- Custom machined 3D cavity ($5K)
- Coplanar waveguide resonator ($3K)
- Commercial microwave cavity (Anritsu, $15K)

---

### 5. Microwave Electronics

| Component | Specification | Cost |
|-----------|---------------|------|
| Vector Network Analyzer | 10 MHz - 20 GHz, 2-port | $30K - $50K |
| Microwave source | 1 - 20 GHz, low phase noise | $10K - $20K |
| Low-noise amplifier | 1 - 18 GHz, NF < 1 dB | $3K - $5K |
| Cryogenic LNA | 4K operation, NF < 0.5 dB | $5K - $8K |
| Isolators/circulators | Frequency-matched | $2K |

**Total microwave electronics:** $50K - $85K

**Recommended:**
- Keysight PNA-X or Rohde & Schwarz ZNB ($40K used)
- Mini-Circuits amplifiers
- Quinstar cryogenic LNA

---

### 6. Data Acquisition and Control

| Component | Specification | Cost |
|-----------|---------------|------|
| Lock-in amplifier | Dual-phase, 100 kHz+ | $8K - $15K |
| DAQ system | 16-bit, 1 MS/s | $2K - $5K |
| Magnet power supply | Bipolar, 0-100A | $5K - $10K |
| Temperature controller | 4K - 300K range | $3K - $5K |
| Computer + software | Python/LabVIEW compatible | $3K |

**Total DAQ:** $20K - $35K

---

### 7. Shielding and Infrastructure

| Component | Specification | Cost |
|-----------|---------------|------|
| Mu-metal shield | 2-3 layer, > 40 dB attenuation | $3K - $5K |
| RF enclosure | Copper mesh or solid | $2K |
| Vibration isolation | Optical table or active | $5K - $10K |
| Cables/connectors | Low-loss microwave | $2K |

**Total shielding:** $12K - $20K

---

## Complete Budget Summary

| Category | Low Estimate | High Estimate |
|----------|--------------|---------------|
| Magnonic crystals | $5K | $20K |
| Cryogenic system | $50K | $80K |
| Magnet system | $20K | $40K |
| Microwave cavity | $10K | $20K |
| Microwave electronics | $50K | $85K |
| DAQ and control | $20K | $35K |
| Shielding/infrastructure | $12K | $20K |
| **TOTAL** | **$167K** | **$300K** |

**Realistic target: ~$200K** with strategic equipment choices and university shared resources.

---

## Comparison to Superconducting Qubit Setup

| Component | Qubit Cost | Magnon Cost | Savings |
|-----------|------------|-------------|---------|
| Cooling | $500K (dilution fridge) | $70K (4K cryostat) | **$430K** |
| Quantum control | $300K (AWG, readout) | $50K (VNA, LNA) | **$250K** |
| Fabrication | $200K (cleanroom time) | $10K (crystal growth) | **$190K** |
| Samples | $50K (qubit arrays) | $10K (YIG spheres) | **$40K** |
| **Total** | **~$1.05M** | **~$140K** | **~$910K** |

---

## What Existing Labs Already Have

Many condensed matter labs already possess:

- ✅ 4K cryostat
- ✅ Electromagnet
- ✅ VNA or microwave source
- ✅ Lock-in amplifier
- ✅ Basic shielding

**For an equipped lab, incremental cost may be only $30K - $50K** (crystals + cavity + minor upgrades).

---

## Minimum Viable Setup

For initial proof-of-concept with maximum cost reduction:

| Component | Minimum Spec | Cost |
|-----------|--------------|------|
| YIG spheres (2) | 0.5 mm, commercial | $500 |
| Room-temp setup | No cryostat | $0 |
| Permanent magnet | 0.3 T, adjustable | $1K |
| Simple cavity | Machined copper | $2K |
| Used VNA | 10 MHz - 10 GHz | $5K |
| Basic amplifier | Room temp LNA | $500 |
| DAQ | Arduino + laptop | $200 |
| **Total** | | **~$10K** |

This "garage physics" setup could detect the basic effect, though with lower signal-to-noise.

---

## Procurement Timeline

| Phase | Duration | Items |
|-------|----------|-------|
| Week 1-2 | Order magnonic crystals | 4-8 week lead time |
| Week 2-4 | Design/order cavity | Custom machining |
| Week 4-8 | Assemble cryostat + magnet | Integration |
| Week 8-12 | Install microwave chain | Calibration |
| Week 12-16 | First cooldown | System checkout |
| Week 16+ | Data collection | Science! |

**Total setup time: ~4 months** for a new installation.

---

## Next Steps

1. **Identify lab partner** with existing FMR capability
2. **Source magnonic crystals** (YIG available immediately; topological materials 4-8 weeks)
3. **Design experiment geometry** (cavity size, field orientation)
4. **Establish baseline** (characterize crystals individually)
5. **Run correlation experiment** (matched vs. mismatched)

---

*See [EXPERIMENTAL_PROTOCOL.md](EXPERIMENTAL_PROTOCOL.md) for detailed measurement sequence.*
