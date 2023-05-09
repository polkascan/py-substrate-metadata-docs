
# CumulusXcm

---------
## Events

---------
### ExecutedDownward
Downward message executed with the given outcome.
\[ id, outcome \]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `[u8; 32]` | ```[u8; 32]```
| None | `Outcome` | ```{'Complete': {'ref_time': 'u64', 'proof_size': 'u64'}, 'Incomplete': ({'ref_time': 'u64', 'proof_size': 'u64'}, {'Overflow': None, 'Unimplemented': None, 'UntrustedReserveLocation': None, 'UntrustedTeleportLocation': None, 'LocationFull': None, 'LocationNotInvertible': None, 'BadOrigin': None, 'InvalidLocation': None, 'AssetNotFound': None, 'FailedToTransactAsset': None, 'NotWithdrawable': None, 'LocationCannotHold': None, 'ExceedsMaxMessageSize': None, 'DestinationUnsupported': None, 'Transport': None, 'Unroutable': None, 'UnknownClaim': None, 'FailedToDecode': None, 'MaxWeightInvalid': None, 'NotHoldingFees': None, 'TooExpensive': None, 'Trap': 'u64', 'ExpectationFalse': None, 'PalletNotFound': None, 'NameMismatch': None, 'VersionIncompatible': None, 'HoldingWouldOverflow': None, 'ExportError': None, 'ReanchorFailed': None, 'NoDeal': None, 'FeesNotMet': None, 'LockError': None, 'NoPermission': None, 'Unanchored': None, 'NotDepositable': None, 'UnhandledXcmVersion': None, 'WeightLimitReached': {'ref_time': 'u64', 'proof_size': 'u64'}, 'Barrier': None, 'WeightNotComputable': None, 'ExceedsStackLimit': None}), 'Error': {'Overflow': None, 'Unimplemented': None, 'UntrustedReserveLocation': None, 'UntrustedTeleportLocation': None, 'LocationFull': None, 'LocationNotInvertible': None, 'BadOrigin': None, 'InvalidLocation': None, 'AssetNotFound': None, 'FailedToTransactAsset': None, 'NotWithdrawable': None, 'LocationCannotHold': None, 'ExceedsMaxMessageSize': None, 'DestinationUnsupported': None, 'Transport': None, 'Unroutable': None, 'UnknownClaim': None, 'FailedToDecode': None, 'MaxWeightInvalid': None, 'NotHoldingFees': None, 'TooExpensive': None, 'Trap': 'u64', 'ExpectationFalse': None, 'PalletNotFound': None, 'NameMismatch': None, 'VersionIncompatible': None, 'HoldingWouldOverflow': None, 'ExportError': None, 'ReanchorFailed': None, 'NoDeal': None, 'FeesNotMet': None, 'LockError': None, 'NoPermission': None, 'Unanchored': None, 'NotDepositable': None, 'UnhandledXcmVersion': None, 'WeightLimitReached': {'ref_time': 'u64', 'proof_size': 'u64'}, 'Barrier': None, 'WeightNotComputable': None, 'ExceedsStackLimit': None}}```

---------
### InvalidFormat
Downward message is invalid XCM.
\[ id \]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `[u8; 32]` | ```[u8; 32]```

---------
### UnsupportedVersion
Downward message is unsupported version of XCM.
\[ id \]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `[u8; 32]` | ```[u8; 32]```

---------