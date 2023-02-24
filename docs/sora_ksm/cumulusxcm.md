
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
| None | `[u8; 8]` | ```[u8; 8]```
| None | `Outcome` | ```{'Complete': 'u64', 'Incomplete': ('u64', {'Overflow': None, 'Unimplemented': None, 'UntrustedReserveLocation': None, 'UntrustedTeleportLocation': None, 'MultiLocationFull': None, 'MultiLocationNotInvertible': None, 'BadOrigin': None, 'InvalidLocation': None, 'AssetNotFound': None, 'FailedToTransactAsset': None, 'NotWithdrawable': None, 'LocationCannotHold': None, 'ExceedsMaxMessageSize': None, 'DestinationUnsupported': None, 'Transport': None, 'Unroutable': None, 'UnknownClaim': None, 'FailedToDecode': None, 'TooMuchWeightRequired': None, 'NotHoldingFees': None, 'TooExpensive': None, 'Trap': 'u64', 'UnhandledXcmVersion': None, 'WeightLimitReached': 'u64', 'Barrier': None, 'WeightNotComputable': None}), 'Error': {'Overflow': None, 'Unimplemented': None, 'UntrustedReserveLocation': None, 'UntrustedTeleportLocation': None, 'MultiLocationFull': None, 'MultiLocationNotInvertible': None, 'BadOrigin': None, 'InvalidLocation': None, 'AssetNotFound': None, 'FailedToTransactAsset': None, 'NotWithdrawable': None, 'LocationCannotHold': None, 'ExceedsMaxMessageSize': None, 'DestinationUnsupported': None, 'Transport': None, 'Unroutable': None, 'UnknownClaim': None, 'FailedToDecode': None, 'TooMuchWeightRequired': None, 'NotHoldingFees': None, 'TooExpensive': None, 'Trap': 'u64', 'UnhandledXcmVersion': None, 'WeightLimitReached': 'u64', 'Barrier': None, 'WeightNotComputable': None}}```

---------
### InvalidFormat
Downward message is invalid XCM.
\[ id \]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `[u8; 8]` | ```[u8; 8]```

---------
### UnsupportedVersion
Downward message is unsupported version of XCM.
\[ id \]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `[u8; 8]` | ```[u8; 8]```

---------