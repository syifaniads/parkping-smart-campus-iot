# Validation Plan

The retained source is a solution presentation rather than an implementation report, so there is no responsible basis for claiming an end-to-end deployment test. This document turns the architecture into a concrete validation plan.

## Edge validation

- Calibrate HC-SR04 distance thresholds for occupied and empty states.
- Test false positives caused by people, motorcycles, nearby objects, rain, or sensor angle.
- Measure state-change detection delay.
- Verify behavior during Wi-Fi/network loss.

## MQTT validation

- Confirm valid device certificate can connect.
- Confirm revoked/invalid certificate is rejected.
- Confirm a device can publish only to its permitted topic namespace.
- Test reconnect and duplicate-message behavior.

## Cloud validation

- Confirm IoT event reaches the processing function.
- Confirm malformed payload is rejected safely.
- Confirm idempotent handling of duplicate events.
- Confirm DynamoDB reflects the newest accepted state.
- Measure end-to-end event latency.

## API/mobile validation

- Compare API occupancy response to known physical slot state.
- Test stale/offline device representation.
- Validate simultaneous mobile reads during peak simulation.

## Observability validation

- Alarm on processing errors.
- Detect stale devices.
- Track ingestion volume, Lambda failures, throttling, API error rate, and latency.

## Suggested acceptance criteria

Acceptance thresholds should be defined only after sensor behavior and operational requirements are measured. The original presentation does not provide numeric SLOs, so this portfolio intentionally does not invent them.