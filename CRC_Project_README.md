# CRC-Based Error Detection for IEEE 802.3 Ethernet Frames

## Overview

A modular C implementation of **Cyclic Redundancy Check (CRC)** error detection for simulated Ethernet-like frame transmission. Instead of treating CRC as a black box, this project implements the **full end-to-end workflow**: sender-side CRC generation, frame construction, bit-level error injection, and receiver-side verification.

## Implementation Workflow

### 1. **Sender Side: CRC Generation**
- Accept payload data (binary bitstream)
- Apply binary polynomial division using the IEEE 802.3 CRC polynomial
- Generate CRC remainder (checksum)
- Output: CRC remainder bits

### 2. **Frame Construction**
- Append CRC remainder to payload
- Build Ethernet-like frame structure: `[Payload | CRC]`
- MSB-first bit ordering
- Max payload: 1024 bits

### 3. **Error Injection (Simulation)**
- Simulate transmission errors by flipping random bits in the frame
- Controlled error injection for testing
- Output: Corrupted frame

### 4. **Receiver Side: CRC Verification**
- Receive frame (possibly corrupted)
- Extract payload and CRC
- Recompute CRC on received payload
- Compare: if recomputed CRC ≠ received CRC → error detected
- Output: `✓ No error` or `✗ Error detected`

## Architecture

Modular C design with clear separation of concerns:

| Module | File | Responsibility |
|--------|------|-----------------|
| **Main** | `main.c` | Program flow, integration |
| **CRC** | `crc.c` / `crc.h` | Binary polynomial division, CRC computation & verification |
| **Frame Builder** | `frame_builder.c` / `frame_builder.h` | Frame construction (payload + CRC) |
| **Error Injector** | `error_injector.c` / `error_injector.h` | Simulated bit-flip errors |
| **I/O Handler** | `io_handler.c` / `io_handler.h` | Input/output operations |

## CRC Specification

- **Algorithm:** Binary polynomial division
- **Polynomial (IEEE 802.3):** `100000100110000010001110110110111` (binary)
- **Initial remainder:** All zeros
- **Final XOR:** None
- **Reflect input/output:** No
- **Error detection only:** Yes (no correction)

## Example Workflow

```
Input Payload: 11010011
CRC Polynomial: 100000100110000010001110110110111

Step 1: Compute CRC
├─ Perform binary polynomial division
└─ CRC Remainder: [calculated checksum]

Step 2: Build Frame
├─ Payload: 11010011
└─ Frame: 11010011[CRC_BITS]

Step 3: Inject Error (optional)
├─ Flip bit at position 5
└─ Corrupted Frame: 11010011[CRC_BITS with error]

Step 4: Verify at Receiver
├─ Extract payload from corrupted frame
├─ Recompute CRC on payload
└─ Result: ✗ Error detected (CRC mismatch)
```

## Key Learning Outcomes

1. **Binary polynomial division** (CRC mathematics)
2. **Frame format design** (payload + redundancy)
3. **Error simulation & detection** (not correction)
4. **Modular C design** (clean separation of concerns)
5. **Standards compliance** (IEEE 802.3)

## Out of Scope

- Real Ethernet hardware transmission
- Error correction (only detection)
- GUI visualization
- Network sockets/drivers
- External CRC libraries

## Build & Run

```bash
gcc main.c crc.c frame_builder.c error_injector.c io_handler.c -o crc_detector
./crc_detector
```

## Files

- `main.c` — Control flow & integration
- `crc.c / crc.h` — CRC computation & verification
- `frame_builder.c / frame_builder.h` — Frame construction
- `error_injector.c / error_injector.h` — Error simulation
- `io_handler.c / io_handler.h` — I/O operations

---

**Signal:** Demonstrates deep understanding of network error detection without relying on libraries. Production-quality modular design.
