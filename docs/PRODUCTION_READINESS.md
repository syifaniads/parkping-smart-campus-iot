# Production Readiness Roadmap

ParkPing's source artifact is a solution design. Moving from design to production would require evidence across the following stages.

## Stage 1 — Sensor proof of concept

- Build one slot prototype.
- Calibrate sensor thresholds.
- Measure false positives/negatives.
- Test outdoor/environmental constraints.

## Stage 2 — Secure IoT ingestion

- Provision unique certificate per device.
- Configure least-privilege IoT policy.
- Establish topic naming and payload schema.
- Test reconnect, duplicate, stale, and invalid messages.

## Stage 3 — Cloud state pipeline

- Implement event validation.
- Make updates idempotent.
- Define DynamoDB access patterns.
- Add logs, metrics, alarms, and failure handling.

## Stage 4 — Mobile/API experience

- Define API schema.
- Represent stale/offline devices explicitly.
- Add caching/aggregation for parking-area views.
- Validate accessibility and usability.

## Stage 5 — Multi-area scale test

- Simulate expected sensor fleet and event rates.
- Measure latency and error rate.
- Estimate AWS cost.
- Test operational response to device and cloud failures.

## Stage 6 — Operations

- Device inventory and ownership.
- Certificate lifecycle and revocation.
- Firmware rollout strategy.
- Sensor maintenance schedule.
- Incident response and monitoring runbooks.