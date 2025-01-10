import math

def calculate_reactive_power_correction(vrms, apparent_power, pf_initial, pf_target):
    apparent_power_va = apparent_power * 1000
    q_initial = apparent_power_va * math.sin(math.acos(pf_initial))
    q_target = apparent_power_va * math.sin(math.acos(pf_target))
    q_correction = q_initial - q_target
    if q_correction > 0:
        capacitance = q_correction / (2 * math.pi * 50 * (vrms ** 2))
    else:
        capacitance = 0
    return q_initial, q_target, q_correction, capacitance

try:
    vrms = float(input("Enter RMS Voltage (V): "))
    apparent_power = float(input("Enter Apparent Power (kVA): "))
    pf_initial = float(input("Enter Initial Power Factor (0-1): "))
    pf_target = float(input("Enter Target Power Factor (0-1): "))

    if not (0 < pf_initial <= 1 and 0 < pf_target <= 1):
        raise ValueError("Power Factor must be between 0 and 1.")

    q_initial, q_target, q_correction, capacitance = calculate_reactive_power_correction(
        vrms, apparent_power, pf_initial, pf_target
    )

    print(f"\nInitial Reactive Power: {q_initial:.2f} VAR")
    print(f"Target Reactive Power: {q_target:.2f} VAR")
    print(f"Reactive Power Correction Needed: {q_correction:.2f} VAR")
    print(f"Required Capacitance: {capacitance * 1e6:.2f} µF")

except ValueError as e:
    print(f"Invalid input: {e}")
