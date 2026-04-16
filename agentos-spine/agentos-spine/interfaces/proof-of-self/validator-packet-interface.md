# Validator Packet Interface

Input object: `ValidatorPacket` from `sourceos-spec`
Output object: `ValidatorReceipt` or a validator COSE envelope.

Required behaviors:
- stable AAD usage
- deterministic SigStructure generation
- no PEM adjuncts in PoST v2
- validator trust resolution by x5c+x5t or kid->trust store
