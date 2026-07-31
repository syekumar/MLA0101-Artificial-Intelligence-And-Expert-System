facts = {
    "computer_not_starting": True,
    "power_supply_ok": True,
    "fan_not_working": True
}

if (facts["computer_not_starting"] and
    facts["power_supply_ok"] and
    facts["fan_not_working"]):

    print("Diagnosis: Motherboard Fault")
else:
    print("No conclusion")
