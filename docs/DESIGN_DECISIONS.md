# Design Decisions

## D1 — Slot-level sensing

**Source:** HC-SR04 ultrasonic sensor is listed as a hardware option.

**Reasoning:** Slot-level sensing directly maps the physical parking-space state into a binary occupancy model.

**Open question:** The presentation does not provide calibration thresholds or accuracy measurements.

## D2 — MQTT for telemetry

**Source:** The proposed solution states that real-time data is sent to AWS via MQTT.

**Reasoning:** MQTT reduces coupling between edge publishers and cloud consumers and suits compact IoT messages.

## D3 — Managed AWS components

**Source:** IoT Core, Lambda, DynamoDB, API Gateway, and CloudWatch are explicitly listed.

**Reasoning:** Together they form a serverless/event-driven path with relatively low operational overhead compared with managing custom brokers and servers.

## D4 — Privacy-friendly occupancy data

**Source:** The presentation explicitly says no personal vehicle data is stored.

**Reasoning:** Parking availability does not inherently require user identity or license-plate information.

## D5 — Security by certificate + least privilege

**Source:** Encrypted MQTT using AWS certificates and strict minimal-privilege IAM are explicit security considerations.

**Reasoning:** Device identity and permission scope are key trust boundaries in IoT deployments.

## D6 — Do not claim unproven deployment

**Portfolio decision:** The deck is a proposal/design artifact. Without source/runtime evidence, this repository documents architecture rather than presenting the system as a completed production implementation.