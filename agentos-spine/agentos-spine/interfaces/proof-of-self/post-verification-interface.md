# PoST Verification Interface

Accepted inputs:
- `ProofOfSelfToken` / PoST object
- local trust roots
- optional x5chain material in validator COSE envelopes

Verification order:
1. x5c + x5t if present
2. kid -> local trust store
3. fail closed
