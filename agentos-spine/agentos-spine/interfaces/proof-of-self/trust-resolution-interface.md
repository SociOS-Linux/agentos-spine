# Trust Resolution Interface

A validator receipt is trusted if:
- its COSE envelope verifies cryptographically
- its x5t matches x5chain[0], if x5chain is present
- or its protected kid resolves to a local trust PEM
- and the trust root is not revoked
