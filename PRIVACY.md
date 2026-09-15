# Privacy

## Design principle from the presentation

ParkPing's source deck explicitly states: **no personal vehicle data stored (privacy-friendly)**.

That means the core product can answer a useful question — *which spaces are free?* — without requiring license plates, driver identities, or movement profiles.

## Data minimization

A minimal slot-state record can contain:

- parking area;
- slot identifier;
- occupied / empty state;
- observation timestamp;
- device health metadata.

It does not need:

- plate number;
- driver name;
- student/staff identifier;
- photo of the vehicle;
- persistent user-location history.

## Future-feature warning

The source presentation mentions **ALPR camera integration** as a possible future upgrade. ALPR would materially change the privacy and security profile because license-plate information can become identifying data.

If ALPR were ever introduced, it should be treated as a separate privacy review requiring purpose limitation, retention rules, access controls, auditability, and applicable legal/institutional review. The current ParkPing portfolio does **not** claim ALPR implementation.