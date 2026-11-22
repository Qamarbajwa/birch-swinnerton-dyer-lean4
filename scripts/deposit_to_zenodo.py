"""
deposit_to_zenodo.py
====================
Creates a deposition on Zenodo using the Zenodo REST API and uploads the
release bundle and SHA256 manifest.
"""

import os
import sys
import json
import requests
from pathlib import Path

def main():
    token = os.environ.get("ZENODO_TOKEN")
    if not token:
        print("[ERROR] ZENODO_TOKEN environment variable not set.")
        sys.exit(1)

    root_dir = Path(__file__).resolve().parent.parent
    zenodo_json_path = root_dir / ".zenodo.json"
    dist_dir = root_dir / "dist"
    bundle_zip = dist_dir / "BIRCH_SWINNERTON_DYER_LEAN4_ZENODO_BUNDLE_v1.0.0.zip"
    manifest_txt = dist_dir / "SHA256SUMS.txt"

    if not bundle_zip.exists():
        print(f"[ERROR] Bundle not found at {bundle_zip}")
        sys.exit(1)

    with open(zenodo_json_path, "r", encoding="utf-8") as f:
        zenodo_meta = json.load(f)

    api_url = "https://zenodo.org/api/deposit/depositions"
    headers = {"Authorization": f"Bearer {token}"}

    payload = {
        "metadata": {
            "title": zenodo_meta["title"],
            "upload_type": "software",
            "description": zenodo_meta["description"],
            "creators": zenodo_meta["creators"],
            "keywords": zenodo_meta["keywords"],
            "access_right": "open",
            "license": "Apache-2.0",
            "version": "1.0.0"
        }
    }

    print("=" * 70)
    print("CREATING ZENODO DEPOSITION FOR BIRCH AND SWINNERTON-DYER (v1.0.0)")
    print("=" * 70)

    try:
        r = requests.post(api_url, json=payload, headers=headers, timeout=30)
        if r.status_code not in [200, 201]:
            print(f"[ERROR] Failed to create deposition: {r.status_code} {r.text[:400]}")
            sys.exit(1)

        dep_data = r.json()
        dep_id = dep_data.get("id")
        bucket_url = dep_data.get("links", {}).get("bucket")
        html_url = dep_data.get("links", {}).get("html")

        print(f"[SUCCESS] Created Deposition ID: {dep_id}")
        print(f"Deposition URL: {html_url}")
        print(f"Bucket URL: {bucket_url}")

        # Upload bundle zip
        print("\nUploading release bundle...")
        with open(bundle_zip, "rb") as fp:
            r_zip = requests.put(
                f"{bucket_url}/{bundle_zip.name}",
                data=fp,
                headers={"Authorization": f"Bearer {token}", "Content-Type": "application/octet-stream"},
                timeout=120
            )
        print(f"  Bundle upload status: {r_zip.status_code} ({'OK' if r_zip.status_code in [200, 201] else 'FAILED'})")

        # Upload SHA256 manifest
        if manifest_txt.exists():
            print("Uploading SHA256 manifest...")
            with open(manifest_txt, "rb") as fp:
                r_man = requests.put(
                    f"{bucket_url}/{manifest_txt.name}",
                    data=fp,
                    headers={"Authorization": f"Bearer {token}", "Content-Type": "application/octet-stream"},
                    timeout=30
                )
            print(f"  Manifest upload status: {r_man.status_code} ({'OK' if r_man.status_code in [200, 201] else 'FAILED'})")

        receipt = {
            "deposition_id": dep_id,
            "deposition_url": html_url,
            "bucket_url": bucket_url,
            "status": "draft_created_and_files_uploaded",
            "bundle": bundle_zip.name,
            "bundle_sha256": r_zip.json().get("checksum", "") if r_zip.status_code in [200, 201] else ""
        }

        receipt_path = root_dir / "reports" / "zenodo_deposition_receipt.json"
        with open(receipt_path, "w", encoding="utf-8") as fp:
            json.dump(receipt, fp, indent=2)

        print("-" * 70)
        print(f"Zenodo receipt written to: {receipt_path}")
        print("Deposition is ready in draft status for inspection and publication.")
        print("=" * 70)

    except Exception as e:
        print(f"[EXCEPTION] Zenodo API call failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
