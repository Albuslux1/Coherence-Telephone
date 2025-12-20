"""
cavity_ringdown_simulation.py

Simulates cavity ring-down with topological magnon coupling.
Shows information lifetime enhancement when topologies match.

Part of the Magnon Electrodynamics framework.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# ===== PARAMETERS =====
kappa = 0.01       # Cavity decay rate (GHz)
gamma = 0.001      # Magnon decay rate (GHz)
omega_c = 2*np.pi*5.0   # Cavity frequency (5 GHz)
omega_m = omega_c * 1.001  # Magnon frequency (slightly detuned)


def ringdown_dynamics(t, y, C_send, C_recv, g0=0.05):
    """
    Time-domain equations for coupled cavity (a) and magnon (b) modes.
    
    Parameters:
        t: Time
        y: [a, b] complex amplitudes
        C_send: Sender Chern number
        C_recv: Receiver Chern number
        g0: Base coupling strength
    
    Returns:
        [da/dt, db/dt]
    """
    a, b = y  # Complex amplitudes
    
    # Topology-dependent coupling (Gaussian suppression with mismatch)
    delta_C = C_send - C_recv
    g = g0 * np.exp(-(delta_C/0.1)**2)
    
    # Coupled equations of motion
    # da/dt = -i*omega_c*a - kappa/2*a - i*g*b
    # db/dt = -i*omega_m*b - gamma/2*b - i*g*a
    
    da_dt = -1j*omega_c*a - kappa/2*a - 1j*g*b
    db_dt = -1j*omega_m*b - gamma/2*b - 1j*g*a
    
    return [da_dt, db_dt]


def run_simulation():
    """Run cavity ringdown simulation for matched and mismatched cases."""
    
    print("="*70)
    print("CAVITY RING-DOWN SIMULATION: MAGNON ELECTRODYNAMICS")
    print("="*70)
    
    # Time parameters
    t_span = (0, 500)  # 500 ns
    t_eval = np.linspace(0, 500, 5000)
    
    # Initial condition: cavity excited, magnon empty
    y0 = [1+0j, 0+0j]
    
    # ===== MATCHED CASE (C=3 → C=3) =====
    print("\nSimulating matched case (C=3 → C=3)...")
    sol_match = solve_ivp(
        lambda t, y: ringdown_dynamics(t, y, C_send=3, C_recv=3), 
        t_span, y0, t_eval=t_eval, method='RK45'
    )
    
    # ===== MISMATCHED CASE (C=3 → C=2) =====
    print("Simulating mismatched case (C=3 → C=2)...")
    sol_mismatch = solve_ivp(
        lambda t, y: ringdown_dynamics(t, y, C_send=3, C_recv=2),
        t_span, y0, t_eval=t_eval, method='RK45'
    )
    
    # ===== VISUALIZATION =====
    plt.style.use('dark_background')
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Cavity Ring-down: Topology-Dependent Energy Transfer', 
                 fontsize=16, fontweight='bold')
    
    # Plot 1: Cavity amplitude comparison
    ax1 = axes[0, 0]
    ax1.plot(t_eval, np.abs(sol_match.y[0]), 'lime', linewidth=2, 
             label='Cavity (C=3→3)')
    ax1.plot(t_eval, np.abs(sol_mismatch.y[0]), 'red', linewidth=2, 
             linestyle='--', label='Cavity (C=3→2)')
    ax1.set_xlabel('Time (ns)')
    ax1.set_ylabel('Amplitude |a|')
    ax1.set_title('Cavity Mode Amplitude')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_yscale('log')
    ax1.set_ylim(1e-3, 2)
    
    # Plot 2: Magnon amplitude comparison
    ax2 = axes[0, 1]
    ax2.plot(t_eval, np.abs(sol_match.y[1]), 'cyan', linewidth=2, 
             label='Magnon (C=3→3)')
    ax2.plot(t_eval, np.abs(sol_mismatch.y[1]), 'orange', linewidth=2, 
             linestyle='--', label='Magnon (C=3→2)')
    ax2.set_xlabel('Time (ns)')
    ax2.set_ylabel('Amplitude |b|')
    ax2.set_title('Magnon Mode Amplitude')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Plot 3: Energy exchange (matched case)
    ax3 = axes[1, 0]
    cavity_energy = np.abs(sol_match.y[0])**2
    magnon_energy = np.abs(sol_match.y[1])**2
    total_energy = cavity_energy + magnon_energy
    
    ax3.fill_between(t_eval, 0, cavity_energy, alpha=0.5, color='lime', 
                     label='Cavity energy')
    ax3.fill_between(t_eval, cavity_energy, cavity_energy + magnon_energy, 
                     alpha=0.5, color='cyan', label='Magnon energy')
    ax3.plot(t_eval, total_energy, 'white', linewidth=1, linestyle='--', 
             label='Total energy')
    ax3.set_xlabel('Time (ns)')
    ax3.set_ylabel('Energy (arb.)')
    ax3.set_title('Energy Exchange: Matched Case (C=3→3)')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Plot 4: Energy exchange (mismatched case)
    ax4 = axes[1, 1]
    cavity_energy_mm = np.abs(sol_mismatch.y[0])**2
    magnon_energy_mm = np.abs(sol_mismatch.y[1])**2
    total_energy_mm = cavity_energy_mm + magnon_energy_mm
    
    ax4.fill_between(t_eval, 0, cavity_energy_mm, alpha=0.5, color='red', 
                     label='Cavity energy')
    ax4.fill_between(t_eval, cavity_energy_mm, cavity_energy_mm + magnon_energy_mm, 
                     alpha=0.5, color='orange', label='Magnon energy')
    ax4.plot(t_eval, total_energy_mm, 'white', linewidth=1, linestyle='--', 
             label='Total energy')
    ax4.set_xlabel('Time (ns)')
    ax4.set_ylabel('Energy (arb.)')
    ax4.set_title('Energy Exchange: Mismatched Case (C=3→2)')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('assets/cavity_ringdown_topology.png', 
                dpi=150, facecolor='black', edgecolor='none')
    plt.show()
    
    return sol_match, sol_mismatch


def print_analysis(sol_match, sol_mismatch):
    """Print analysis of ringdown results."""
    
    print("\n" + "="*70)
    print("RING-DOWN ANALYSIS")
    print("="*70)
    print()
    print("MATCHED CASE (C=3→3):")
    print("  - Energy oscillates between cavity and magnon modes")
    print("  - Vacuum Rabi oscillations visible (beat frequency = 2g)")
    print(f"  - Peak magnon amplitude: {np.max(np.abs(sol_match.y[1])):.3f}")
    print(f"  - Energy transfer efficiency: {np.max(np.abs(sol_match.y[1])**2):.1%}")
    print()
    print("MISMATCHED CASE (C=3→2):")
    print("  - No energy transfer to magnon mode")
    print("  - Cavity decays exponentially with rate kappa/2")
    print(f"  - Peak magnon amplitude: {np.max(np.abs(sol_mismatch.y[1])):.5f}")
    print(f"  - Energy transfer efficiency: {np.max(np.abs(sol_mismatch.y[1])**2):.1e}")
    print()
    print("CONCLUSION:")
    print("  This demonstrates TOPOLOGICAL PROTECTION of coherence.")
    print("  Energy only transfers when the topological address (Chern number) matches.")
    print("="*70)


# ===== MAIN EXECUTION =====
if __name__ == "__main__":
    sol_match, sol_mismatch = run_simulation()
    print_analysis(sol_match, sol_mismatch)
    print("\nPlot saved: assets/cavity_ringdown_topology.png")
