# IoT Data Flow

## Source-supported flow

The retained presentation describes the high-level flow as:

`parking slot -> sensor/microcontroller -> MQTT -> AWS -> mobile app`

The AWS slide further names IoT Core, Lambda, DynamoDB, API Gateway, and CloudWatch.

## Proposed event lifecycle

A production-oriented interpretation is:

1. An ultrasonic sensor measures distance at a parking slot.
2. Edge logic classifies the slot as `occupied` or `empty`.
3. The device publishes a compact MQTT event.
4. AWS IoT Core authenticates the device certificate and accepts authorized topics.
5. Serverless processing validates the event and updates current state.
6. DynamoDB stores the latest parking-slot state and relevant metadata.
7. A mobile client reads availability through an API boundary.
8. CloudWatch captures operational telemetry.

Steps 4–8 describe how the selected AWS services naturally fit together; they are architecture documentation, not retained deployment proof.

## Example MQTT topic design

```text
parkping/campus-a/parking-a/slot/A-001/state
```

Possible payload:

```json
{
  "slot_id": "A-001",
  "occupied": true,
  "observed_at": "2026-01-01T08:00:00Z",
  "device_id": "sensor-demo-001"
}
```

See `examples/mqtt-message.example.json`.

## Event-design considerations

A production implementation should address:

- duplicate delivery and idempotent updates;
- out-of-order telemetry;
- stale sensor state;
- retained MQTT messages where appropriate;
- device reconnect behavior;
- calibration and noisy distance readings;
- timestamps generated at the edge vs received in the cloud;
- offline devices and heartbeat strategy.

These concerns are not evidence that the camp prototype implemented them; they document the engineering work required to mature the proposal.