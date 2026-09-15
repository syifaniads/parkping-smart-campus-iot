# Scalability

## What the source says

The presentation states that ParkPing is:

- extendable to all parking areas on campus;
- based on MQTT, which is described as supporting hundreds of sensors with low bandwidth usage;
- open to future features such as reservation, ALPR camera integration, and analytics.

These statements describe the design intent. The retained material does not include a load test proving a particular sensor count.

## Scaling dimensions

### Device count

Each additional parking space introduces a device identity, telemetry stream, health state, and lifecycle-management requirement.

### Message rate

A good design should avoid publishing unchanged occupancy at an unnecessarily high frequency. State-change events plus periodic heartbeat messages can reduce bandwidth and cloud cost.

### Storage

Two different workloads should be considered:

- **current state** for the mobile parking map;
- **historical events** for analytics.

They may deserve different retention and storage strategies.

### API traffic

Peak mobile traffic may occur at the same times as parking demand. Caching aggregated parking-area availability can prevent every user request from becoming a large backend query.

## No benchmark overclaim

This repository does not claim a measured capacity, request rate, p95 latency, or proven 'hundreds of sensors' benchmark because the source presentation provides no benchmark evidence.