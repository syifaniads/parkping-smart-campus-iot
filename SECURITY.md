# Security

## Source requirements

The ParkPing presentation explicitly includes three security/privacy considerations:

1. **Encrypted MQTT using AWS certificates**.
2. **Strict IAM minimal-privilege policy**.
3. **No personal vehicle data stored**.

This repository preserves those requirements and avoids claiming controls for which no implementation evidence was supplied.

## Recommended trust boundaries

### Device -> AWS IoT Core

Risks include cloned devices, leaked certificates, unauthorized topic publishing, replayed or forged occupancy events, and compromised firmware.

Recommended controls include unique device certificates, certificate rotation/revocation, topic-scoped IoT policies, TLS, device identity inventory, and secure firmware/update procedures.

### Cloud processing

Lambda and persistence permissions should be least-privilege. A processing function that only updates parking state should not receive broad account permissions.

### API -> mobile client

Public occupancy data may be low sensitivity, but administrative functions and security-operator capabilities should be authenticated and authorized separately.

## Public-repository policy

Do not commit:

- AWS access keys;
- IoT private keys or device certificates;
- `.env` files with secrets;
- production account IDs/resource identifiers when unnecessary;
- mobile signing secrets;
- personal user or vehicle information.

Example files in this repository contain synthetic values only.