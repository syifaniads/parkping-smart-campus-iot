#!/usr/bin/env python3
"""Validate the sanitized ParkPing portfolio contracts.

This validates documentation/reference artifacts only. It does not claim live
AWS IoT Core, Lambda, DynamoDB, hardware, or mobile application deployment.
"""
from __future__ import annotations

from datetime import datetime
import json
from pathlib import Path
import sys

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def main() -> int:
    schema = load("schemas/parking-event.schema.json")
    event = load("examples/mqtt-message.example.json")
    item = load("examples/dynamodb-item.example.json")

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(event), key=lambda error: list(error.path))
    if errors:
        rendered = "; ".join(error.message for error in errors)
        raise AssertionError(f"MQTT example violates event contract: {rendered}")

    # The materialized state should preserve the identity and latest occupancy
    # carried by the telemetry event.
    expected_pk = f"AREA#{event['parking_area']}"
    expected_sk = f"SLOT#{event['slot_id']}"
    if item.get("pk") != expected_pk:
        raise AssertionError(f"DynamoDB pk should be {expected_pk!r}")
    if item.get("sk") != expected_sk:
        raise AssertionError(f"DynamoDB sk should be {expected_sk!r}")
    for field in ("slot_id", "device_id", "occupied"):
        if item.get(field) != event.get(field):
            raise AssertionError(f"DynamoDB projection drift for {field}")
    if item.get("last_observed_at") != event.get("observed_at"):
        raise AssertionError("materialized timestamp must match the observed event")

    # Explicitly ensure the example timestamp remains timezone-aware.
    parsed = datetime.fromisoformat(event["observed_at"].replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise AssertionError("observed_at must be timezone-aware")

    if item.get("device_status") not in {"online", "offline", "unknown"}:
        raise AssertionError("unexpected device_status value")

    print("ParkPing portfolio contract validation passed")
    print("- MQTT example conforms to the versioned JSON Schema")
    print("- DynamoDB keys derive from parking area + slot identity")
    print("- occupancy/device identity are preserved in materialized state")
    print("- event timestamp is timezone-aware and propagated")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1)
