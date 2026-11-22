"""
build_bsd_zenodo_bundle.py
==========================
Packages the Birch and Swinnerton-Dyer Lean 4 project into a standalone,
reproducible release bundle for Zenodo and generates SHA256 checksums.
"""

import os
import sys
import zipfile
import hashlib

def sha256_file(filepath):
    h = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def build_bundle():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dist_dir = os.path.join(root_dir, "dist")
    os.makedirs(dist_dir, exist_ok=True)

    bundle_name = "BIRCH_SWINNERTON_DYER_LEAN4_ZENODO_BUNDLE_v1.0.0.zip"
    bundle_path = os.path.join(dist_dir, bundle_name)
    manifest_path = os.path.join(dist_dir, "SHA256SUMS.txt")

    included_files = [
        "README.md",
        "LICENSE",
        "CITATION.cff",
        ".zenodo.json",
        "GITHUB_RELEASE_NOTES.md",
        "AGENTS.md",
        "lakefile.toml",
        "lean-toolchain",
        ".gitignore",
        "formal/BSDContinuumCasselsTatePfaffianFinitenessCert.lean",
        "formal/BSDHodgeAbelJacobiCycleElevatorCert.lean",
        "scripts/probe_bsd_nature_of_the_problem.py",
        "scripts/run_bsd_audit_suite.py",
        "scripts/build_bsd_zenodo_bundle.py",
        "reports/bsd_verification_receipt.json"
    ]

    print("=" * 70)
    print("BUILDING BIRCH AND SWINNERTON-DYER ZENODO RELEASE BUNDLE")
    print(f"Target: {bundle_path}")
    print("=" * 70)

    manifest_lines = []
    with zipfile.ZipFile(bundle_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for rel_path in included_files:
            abs_path = os.path.join(root_dir, rel_path)
            if os.path.exists(abs_path):
                file_hash = sha256_file(abs_path)
                arcname = f"birch-swinnerton-dyer-lean4-1.0.0/{rel_path}"
                zipf.write(abs_path, arcname=arcname)
                manifest_lines.append(f"{file_hash}  {rel_path}\n")
                print(f"  Added: {rel_path} ({file_hash[:16]}...)")
            else:
                print(f"  WARNING: File missing: {rel_path}")

    # Write manifest
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.writelines(manifest_lines)

    bundle_size_mb = os.path.getsize(bundle_path) / (1024 * 1024)
    bundle_hash = sha256_file(bundle_path)

    print("-" * 70)
    print(f"Bundle successfully created: {bundle_name}")
    print(f"Size: {bundle_size_mb:.4f} MB")
    print(f"SHA-256: {bundle_hash}")
    print(f"Manifest written to: {manifest_path}")
    print("=" * 70)

if __name__ == "__main__":
    build_bundle()
