# Threat Model

This threat model expands the presentation's security principles into reviewable engineering concerns. It is not evidence that every mitigation existed in the original camp project.

| Threat | Impact | Recommended mitigation |
|---|---|---|
| Stolen device certificate | Attacker can impersonate a sensor | Unique certificates, revocation, rotation, inventory |
| Over-permissive IoT policy | Device can publish/read unrelated topics | Topic-scoped least privilege |
| Forged occupancy event | False parking availability | Device auth, validation, anomaly detection |
| Replay / stale event | Incorrect current state | Timestamps, monotonic/version checks, stale-state policy |
| Compromised edge device | Persistent false telemetry | Firmware controls, credential protection, fleet monitoring |
| Lambda over-permission | Wider cloud compromise | Function-specific IAM roles |
| Public API abuse | Availability/operational impact | Authorization where needed, throttling, WAF/rate controls |
| Sensitive data creep | Privacy risk | Enforce occupancy-only schema, retention policy |
| Device outage | Stale map shown as current | Heartbeat, offline state, monitoring alarm |

## Privacy-sensitive future feature

ALPR appears only as a future idea in the source presentation. If introduced, license-plate processing would create a substantially different threat/privacy model and should not inherit the assumptions of the occupancy-only system.