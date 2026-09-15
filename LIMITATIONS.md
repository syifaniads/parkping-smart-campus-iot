# Limitations

## Evidence limitations

The current portfolio is grounded in the Group 2 APIE Camp presentation. It verifies the problem statement, proposed architecture, hardware options, AWS service choices, target users, security principles, privacy intent, and scalability direction.

It does **not** provide retained evidence for:

- a physical sensor prototype operating in a parking space;
- an AWS IoT Core thing/certificate/policy deployment;
- Lambda source or execution logs;
- DynamoDB records from live telemetry;
- an API Gateway endpoint;
- a working mobile application connected to live data;
- measured detection accuracy;
- measured end-to-end latency;
- measured load capacity or cost.

## Design limitations

Ultrasonic parking detection can be affected by installation height, vehicle geometry, obstacles, environmental conditions, and sensor calibration.

A production system also needs a strategy for device provisioning, firmware updates, certificate lifecycle, offline devices, stale data, monitoring, maintenance, and operational ownership.

## Future features

Reservation, ALPR, and analytics appeared as future-upgrade ideas. They are not represented here as completed functionality.