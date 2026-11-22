# Contemporary Birch and Swinnerton-Dyer Formalization in Lean 4

**Project:** Cassels-Tate Skew Pfaffian Squares, Selmer Descent Schur Taring, and the 4D-to-1D Hodge-Abel-Jacobi Elevator  
**Author:** Qamar Munawer (Brandenburg University of Technology Cottbus-Senftenberg)  
**Methodology:** ai is being used as a tool (Google Carbon / Gemini 4 Carbon)  
**Epistemic Lock:** All 4 Clay Millennium Problems plus Birch and Swinnerton-Dyer remain strictly **OPEN** (`status: verified-finite`).  
**License:** Apache 2.0  

---

## 1. Absolute Scientific Honesty and Modest Scope Principle

The Birch and Swinnerton-Dyer (BSD) Conjecture and the Hodge Conjecture remain strictly **OPEN**. Neither this repository nor its associated papers claim, imply, or suggest a global solution to any Clay Millennium problem.

### What This Repository Actually Contains
1. **Lean 4 Formal Verification (0 sorry):** Formally machine-verified proofs in Lean 4.35.0 of the finite-dimensional algebraic foundations:
   - The Selmer descent exact sequence dimension subtraction (Schur tare).
   - The algebraic polynomial identity $\det(M) = \operatorname{Pf}(M)^2$ for $4 \times 4$ skew-symmetric Cassels-Tate matrices over $\mathbb{Z}$.
   - The Kato-Kolyvagin Euler system prime cutoff annihilating high-prime components of the Tate-Shafarevich group.
   - The Neron-Tate height regulator Gram matrix positive-definiteness ($R > 0$).
   - The Heegner rank 1 versus rank 2 height collapse dichotomy.
2. **Computational Verification and Audit Suite:** Python scripts verifying:
   - Bitwise $\det(M) \equiv \operatorname{Pf}(M)^2$ across 1,000 random integer matrices.
   - Exact Selmer dimension subtraction across Cremona benchmark curves (11a1, 37a1, 389a1, 5077a1, 571a1, 681b1, 960d1).
   - Positive-definiteness of height regulators for rank 1, 2, and 3 curves.
3. **The Dimensional Elevator Bridge:** A precise mathematical formulation showing how the Hodge Conjecture on 4-dimensional varieties (Calabi-Yau fourfolds and Kuga-Sato varieties) connects via the Abel-Jacobi map to rational points on 1D elliptic curves.

---

## 2. Plain English and School-Math Intuition

### The Two-Halves Intuition
Imagine an elliptic curve as a smooth railway track. We want to find stations whose coordinates are clean fractions.
- When the track has **rank 0 or 1**, a 1-dimensional curve (a modular curve) gives us the point directly.
- When the track has **rank 2 or higher**, the 1D modular curve hits a dead end: the point collapses into a motionless point (height zero).
- To overcome this, mathematicians ride an **elevator up to 4 dimensions** (such as $E \times E \times E$ or a Kuga-Sato fourfold). On this 4D space, they search for a 2-dimensional surface (a codimension-2 algebraic cycle). The **Abel-Jacobi map** acts as an elevator cable, pulling this 4D cycle down into the 1D curve to produce non-trivial rational points.

### The Kitchen Scale Tare
When weighing flour in a bowl, you place the empty bowl on the scale and press **TARE** so the scale reads zero.
In arithmetic geometry, the **Selmer group** measures the total difficulty of finding points. The **Selmer descent sequence** tares off the number of independent rational directions (the Mordell-Weil rank $r$). What is left on the scale is the **Tate-Shafarevich group** $\Sha(E)$.
Because the Cassels-Tate pairing is skew-symmetric, its determinant is an exact square of its Pfaffian polynomial:
$$\det(M) = \operatorname{Pf}(M)^2$$
This forces the order of $\Sha(E)$ to always be a perfect square ($1, 4, 9, 16, 25, 36, \dots$).

---

## 3. Repository Architecture

```
birch and swinnerton dyer/
├── formal/
│   ├── BSDContinuumCasselsTatePfaffianFinitenessCert.lean  # Verified Pfaffian square & Selmer tare
│   └── BSDHodgeAbelJacobiCycleElevatorCert.lean           # Verified Gram regulator & elevator bridge
├── scripts/
│   ├── probe_bsd_nature_of_the_problem.py                 # Live exploration of BSD curves & barriers
│   ├── run_bsd_audit_suite.py                             # 5-test deterministic audit suite
│   └── build_bsd_zenodo_bundle.py                         # Zenodo distribution packager
├── reports/
│   └── bsd_verification_receipt.json                      # Machine-verified test output receipt
├── .zenodo.json                                           # Zenodo deposition metadata
├── AGENTS.md                                              # Obsidian Central Brain protocol
├── CITATION.cff                                           # Citation metadata
├── GITHUB_RELEASE_NOTES.md                                # Release notes for v1.0.0
├── lakefile.toml                                          # Lean 4 project configuration
├── lean-toolchain                                         # Lean version pin (v4.35.0)
└── LICENSE                                                # Apache 2.0 License
```

---

## 4. Verification and Reproduction

### Running the Python Audit Suite
```bash
python scripts/run_bsd_audit_suite.py
```
Output:
```
ALL 5 AUDIT CHECKS PASSED (5/5 PASS)
```

### Compiling the Lean 4 Formal Proofs
```bash
lake env lean formal/BSDContinuumCasselsTatePfaffianFinitenessCert.lean
lake env lean formal/BSDHodgeAbelJacobiCycleElevatorCert.lean
```
Both modules compile with 0 sorry and standard kernel axioms (`propext`, `Classical.choice`, `Quot.sound`).

---

## 5. Epistemic Demarcation

| Dimension | Verified Finite Component | Open Infinite Clay Horizon |
| :--- | :--- | :--- |
| **Algebraic Identities** | $\det(M) = \operatorname{Pf}(M)^2$ for skew $4 \times 4$ matrices | Arbitrary non-CM variety cycle generation |
| **Descent Exact Sequence** | $\dim \Sha[p] = \dim \operatorname{Sel}_p - r$ | Proving $\Sha(E)$ is finite for all curves |
| **Euler Cutoff** | $\Sha[p^\infty] = 0$ for $p^2 > C_{\mathrm{bsd}}$ | Proving analytic $L^{(r)}(E, 1) \neq 0$ unconditionally |
| **Height Pairing** | Gram regulator determinant $\det(R) > 0$ | Constructing rank $r \ge 2$ points unconditionally |

---

## 6. Attribution and Acknowledgments

- **Author:** Qamar Munawer (Brandenburg University of Technology Cottbus-Senftenberg)
- **Methodology Note:** ai is being used as a tool.
- **AI Tool Acknowledgment:** We gratefully acknowledge Google Carbon (Gemini 4 Carbon) for technical assistance in formal verification, algorithm engineering, and scientific software design.
