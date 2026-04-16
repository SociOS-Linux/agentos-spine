# Mesh Transport Interface

Packet request:
- topic-scoped publish
- contains payload hash, AAD, algorithm, and signing context

Packet response:
- validator COSE envelope bytes
- validator identifier metadata
- optional transport diagnostics

The integration spine treats transport as swappable.
