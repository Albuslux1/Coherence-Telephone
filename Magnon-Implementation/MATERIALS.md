# Materials: Candidate Crystals for Magnon Electrodynamics

---

## Selection Criteria

For Magnon Electrodynamics, the ideal material must have:

1. **Magnetic order** — breaks time-reversal symmetry (nonzero θ baseline)
2. **Topological magnon bands** — nonzero Chern number 𝒞
3. **Low Gilbert damping** — long magnon lifetime for coherent transfer
4. **Magnetoelectric coupling** — intrinsic θE·B response
5. **Crystal availability** — single crystals for clean spectroscopy

---

## Tier 1: Immediately Available

### Yttrium Iron Garnet (Y₃Fe₅O₁₂, YIG)

**The workhorse of magnonics.**

| Property | Value | Notes |
|----------|-------|-------|
| Structure | Cubic garnet | Ferrimagnetic |
| Ordering temp | 560 K | Room temperature operation |
| Gilbert damping | α ~ 3×10⁻⁵ | **Lowest known in any material** |
| Magnon lifetime | > 1 μs | Exceptional |
| FMR frequency | 1-20 GHz | Field-tunable |
| Availability | Commercial | 0.1-1 mm spheres readily available |

**Topology:**
- Standard YIG has trivial topology (𝒞 = 0)
- **Doping with rare earths** (Tm, Tb) introduces DMI → nonzero 𝒞
- **Strain engineering** can induce topological magnon bands
- **Thin films on substrates** with spin-orbit coupling

**Advantages:**
- Mature growth technology
- Ultra-low loss
- Room temperature operation
- Extensive literature

**Limitations:**
- Requires modification for topology
- Relatively weak magnetoelectric coupling

**Cost:** $50 - $500 per sphere (commercial)

---

### Lithium Ferrite (LiFe₅O₈)

| Property | Value | Notes |
|----------|-------|-------|
| Structure | Spinel | Ferrimagnetic |
| Gilbert damping | α ~ 10⁻⁴ | Good, not as low as YIG |
| Magnetoelectric | Weak intrinsic | Can be enhanced |

**Cost:** $100 - $300 per crystal

---

## Tier 2: Topological Magnon Materials

### Kagome Ferromagnets with DMI

**Intrinsic topological magnon bands.**

| Property | Value | Notes |
|----------|-------|-------|
| Examples | Cu(1,3-bdc), Fe₃Sn₂ | Metal-organic or intermetallic |
| Topology | 𝒞 = ±1, ±2 demonstrated | Intrinsic, no engineering needed |
| DMI | Strong | Built into crystal structure |
| Magnon gap | Present | Topological protection |

**Theory Reference:** Owerre, J. Phys.: Condens. Matter 28, 386001 (2016)

**Advantages:**
- Native topology — no modifications needed
- Chern number tunable via field direction

**Limitations:**
- Less mature growth
- Higher damping than YIG
- Some require low temperature

**Cost:** $1K - $5K (custom growth)

---

### Honeycomb Ferromagnets (CrI₃, CrBr₃)

**2D van der Waals magnets with topological magnons.**

| Property | Value | Notes |
|----------|-------|-------|
| Structure | Honeycomb layers | Layered, exfoliatable |
| Ordering temp | 45-61 K | Requires cryogenics |
| Topology | 𝒞 = ±1 | From spin-orbit + honeycomb geometry |
| Stacking | Tunable | Changes magnetic order and 𝒞 |

**Advantages:**
- Well-studied topological properties
- Tunable by stacking, gating, strain
- 2D nature allows heterostructures

**Limitations:**
- Low ordering temperature
- Air-sensitive
- Small crystal sizes (μm to mm)

**Cost:** $500 - $2K per crystal (commercial); free via collaboration

---

### MnBi₂Te₄

**The magnetic topological insulator with demonstrated dynamical axion.**

| Property | Value | Notes |
|----------|-------|-------|
| Structure | Layered | Antiferromagnetic TI |
| Ordering temp | 25 K | Requires cryogenics |
| Axion frequency | ~44 GHz | Observed in Nature 2025 paper |
| θ | Oscillates with AF magnon | **This is exactly what we need** |

**The Nature Observation:**
In MnBi₂Te₄, the antiferromagnetic magnon mode directly drives θ oscillations. This is **dynamical axion electrodynamics in action**.

**Advantages:**
- Proven θ oscillation from magnons
- Intrinsic magnetoelectric coupling
- Large crystals available

**Limitations:**
- Antiferromagnetic (harder to drive/detect)
- Low temperature required
- Complex band structure

**Cost:** $2K - $5K per crystal (university collaborations)

---

### Breathing Pyrochlores (LiGaCr₄O₈, LiInCr₄O₈)

**Magnonic Weyl points.**

| Property | Value | Notes |
|----------|-------|-------|
| Structure | Breathing pyrochlore | Frustrated magnetism |
| Topology | Weyl magnons | 𝒞 ≠ 0 on Fermi arcs |
| Magnon bands | Complex, gapped | Multiple topological sectors |

**Advantages:**
- Rich topology
- Bulk crystals available
- High-𝒞 states accessible

**Limitations:**
- Complex magnon spectrum
- Requires detailed characterization
- Less studied than other options

**Cost:** $1K - $3K (custom synthesis)

---

## Tier 3: Advanced Materials (Future)

### Synthetic Kagome Magnets

Lithographically patterned magnetic thin films with kagome geometry.

- Full control over geometry
- Expensive fabrication
- Enables systematic 𝒞 tuning

### Magnon-Polariton Hybrids

YIG coupled to superconducting resonators:
- Combines low loss of YIG with quantum control
- Requires mK temperatures
- Bridge to qubit implementation

### Twisted Magnetic Bilayers

Moiré engineering of magnetic 2D materials:
- Artificial topology from twist angle
- Highly tunable
- Very new field

---

## Material Selection Guide

### For First Experiment (Proof of Concept)

**Recommended: YIG spheres + external DMI enhancement**

- Commercial availability
- Well-characterized FMR
- Add DMI via interface with heavy metal (Pt, W) thin film

### For Demonstrating Intrinsic Topology

**Recommended: CrI₃ or kagome ferromagnet**

- Native topological bands
- Established theory predictions
- Active research community

### For Maximum Axion Coupling

**Recommended: MnBi₂Te₄**

- Proven dynamical axion oscillation
- Direct θ modulation by magnons
- Published experimental protocol

---

## Material-Topology-Cost Matrix

| Material | Max 𝒞 | Magnetoelectric | Damping | Temp | Cost | Readiness |
|----------|--------|-----------------|---------|------|------|-----------|
| YIG | 0* | Weak | Ultra-low | 300K | Low | ★★★★★ |
| YIG + Pt | 1-2 | Moderate | Low | 300K | Low | ★★★★☆ |
| CrI₃ | 1 | Moderate | Moderate | <60K | Med | ★★★☆☆ |
| Fe₃Sn₂ | 1-2 | Moderate | Moderate | 300K | Med | ★★★☆☆ |
| MnBi₂Te₄ | N/A† | **Strong** | High | <25K | High | ★★★☆☆ |
| Kagome MOF | 2-3 | Moderate | High | <100K | High | ★★☆☆☆ |

*YIG native 𝒞=0; requires interface engineering
†MnBi₂Te₄ is antiferromagnetic; topology enters differently

---

## Sourcing Contacts

### Commercial Suppliers
- **Ferrisphere Inc.** — YIG spheres
- **2D Semiconductors** — CrI₃, CrBr₃ crystals
- **HQ Graphene** — Magnetic 2D materials

### Academic Collaborations
- **Penn State (Nitin Samarth)** — MnBi₂Te₄
- **MIT (Pablo Jarillo-Herrero)** — 2D magnets
- **Berkeley (Ramamoorthy Ramesh)** — Magnetoelectrics
- **Vienna (Andrii Chumak)** — YIG magnonics

---

## Recommendation

**Start with YIG, progress to topological materials.**

1. **Phase 1:** Commercial YIG spheres — establish FMR baseline, test cavity coupling
2. **Phase 2:** YIG/Pt bilayer — introduce interfacial DMI, measure topology effects
3. **Phase 3:** Intrinsic topological material (CrI₃ or MnBi₂Te₄) — validate full framework

This progression minimizes risk while building toward the definitive test.

---

*See [HARDWARE_REQUIREMENTS.md](HARDWARE_REQUIREMENTS.md) for integration into experimental setup.*
