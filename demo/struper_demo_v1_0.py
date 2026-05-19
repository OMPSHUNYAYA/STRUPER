#!/usr/bin/env python3
import hashlib
import json
import time


VERSION = "1.0"


def certificate(payload):
    text = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def traditional_total(orders, item_price, shipping):
    start = time.perf_counter()

    total = 0.0
    steps = 0

    for _ in range(orders):
        subtotal = item_price
        final_total = subtotal + shipping
        total += final_total
        steps += 1

    elapsed = time.perf_counter() - start

    payload = {
        "method": "traditional_procedural_realization",
        "orders": orders,
        "item_price": item_price,
        "shipping": shipping,
        "steps": steps,
        "output": total,
    }

    return {
        "state": "RESOLVED",
        "total": total,
        "steps": steps,
        "time": elapsed,
        "method_certificate": certificate(payload),
    }


def struper_total(structure):
    start = time.perf_counter()

    subtotal = structure["ITEM_PRICE"]
    final_total = subtotal + structure["SHIPPING"]
    total = structure["ORDERS"] * final_total

    elapsed = time.perf_counter() - start

    payload = {
        "method": "struper_structural_resolution",
        "structure": structure,
        "output": total,
    }

    return {
        "state": "RESOLVED",
        "total": total,
        "capsules_resolved": len(structure),
        "time": elapsed,
        "method_certificate": certificate(payload),
    }


def output_certificate(output):
    payload = {
        "output": output,
    }
    return certificate(payload)


def main():
    print("STRUPER Demo v1.0")
    print("Structural Resolution Beyond Procedural Realization")
    print()

    print("Traditional view: procedural realization creates output")
    print("STRUPER view: mature structure resolves bounded realization")
    print()

    print("Principle: realization = resolve(structure)")
    print("Law: same mature structure -> same bounded realization -> same output certificate")
    print("Boundary: applies only where structure is complete and resolvable")
    print()

    print("Important distinction")
    print("This is not ordinary speed optimization research.")
    print("Speed is only a visible byproduct.")
    print("The deeper claim is structural correctness beyond procedural realization dependence.")
    print()

    orders = 500000
    item_price = 120.0
    shipping = 15.0

    structure = {
        "ORDERS": orders,
        "ITEM_PRICE": item_price,
        "SHIPPING": shipping,
    }

    traditional = traditional_total(orders, item_price, shipping)
    structural = struper_total(structure)

    traditional_output_certificate = output_certificate(traditional["total"])
    structural_output_certificate = output_certificate(structural["total"])

    print("Traditional procedural result")
    print(f"State: {traditional['state']}")
    print(f"Final total: {traditional['total']}")
    print(f"Procedural steps: {traditional['steps']}")
    print(f"Time: {traditional['time']:.6f} seconds")
    print(f"Method certificate: {traditional['method_certificate']}")
    print(f"Output certificate: {traditional_output_certificate}")
    print()

    print("STRUPER structural result")
    print(f"State: {structural['state']}")
    print(f"Final total: {structural['total']}")
    print(f"Capsules resolved: {structural['capsules_resolved']}")
    print(f"Time: {structural['time']:.6f} seconds")
    print(f"Method certificate: {structural['method_certificate']}")
    print(f"Output certificate: {structural_output_certificate}")
    print()

    same_output = traditional["total"] == structural["total"]
    same_output_certificate = traditional_output_certificate == structural_output_certificate
    different_method_certificates = (
        traditional["method_certificate"] != structural["method_certificate"]
    )

    if structural["time"] > 0:
        speedup = traditional["time"] / structural["time"]
        speedup_text = f"{speedup:.2f}x"
    else:
        speedup_text = "effectively unbounded at timer resolution"

    print("Verification")
    print(f"Same final total: {same_output}")
    print(f"Same output certificate: {same_output_certificate}")
    print(f"Different method certificates: {different_method_certificates}")
    print(f"Approx speedup on this machine: {speedup_text}")
    print()

    print("Interpretation")
    print("The initial structure may take more care.")
    print("After structure matures, realization can resolve structurally.")
    print("STRUPER does not claim that all procedures disappear.")
    print("It demonstrates bounded realization beyond procedural realization dependence.")


if __name__ == "__main__":
    main()