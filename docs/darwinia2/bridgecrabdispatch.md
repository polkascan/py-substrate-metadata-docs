
# BridgeCrabDispatch

---------
## Events

---------
### MessageCallDecodeFailed
We have failed to decode Call from the message.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ChainId` | ```[u8; 4]```
| None | `BridgeMessageIdOf<T, I>` | ```('[u8; 4]', 'u64')```

---------
### MessageCallValidateFailed
The call from the message has been rejected by the call validator.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ChainId` | ```[u8; 4]```
| None | `BridgeMessageIdOf<T, I>` | ```('[u8; 4]', 'u64')```
| None | `TransactionValidityError` | ```{'Invalid': {'Call': None, 'Payment': None, 'Future': None, 'Stale': None, 'BadProof': None, 'AncientBirthBlock': None, 'ExhaustsResources': None, 'Custom': 'u8', 'BadMandatory': None, 'MandatoryValidation': None, 'BadSigner': None}, 'Unknown': {'CannotLookup': None, 'NoUnsignedValidator': None, 'Custom': 'u8'}}```

---------
### MessageDispatchPaymentFailed
The origin account has failed to pay fee for dispatching the message.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ChainId` | ```[u8; 4]```
| None | `BridgeMessageIdOf<T, I>` | ```('[u8; 4]', 'u64')```
| None | `<T as frame_system::Config>::AccountId` | ```[u8; 20]```
| None | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```

---------
### MessageDispatched
Message has been dispatched with given result.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ChainId` | ```[u8; 4]```
| None | `BridgeMessageIdOf<T, I>` | ```('[u8; 4]', 'u64')```
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}}```

---------
### MessageRejected
Message has been rejected before reaching dispatch.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ChainId` | ```[u8; 4]```
| None | `BridgeMessageIdOf<T, I>` | ```('[u8; 4]', 'u64')```

---------
### MessageSignatureMismatch
Message signature mismatch.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ChainId` | ```[u8; 4]```
| None | `BridgeMessageIdOf<T, I>` | ```('[u8; 4]', 'u64')```

---------
### MessageVersionSpecMismatch
Message has been rejected by dispatcher because of spec version mismatch.
Last two arguments are: expected and passed spec version.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ChainId` | ```[u8; 4]```
| None | `BridgeMessageIdOf<T, I>` | ```('[u8; 4]', 'u64')```
| None | `SpecVersion` | ```u32```
| None | `SpecVersion` | ```u32```

---------
### MessageWeightMismatch
Message has been rejected by dispatcher because of weight mismatch.
Last two arguments are: expected and passed call weight.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ChainId` | ```[u8; 4]```
| None | `BridgeMessageIdOf<T, I>` | ```('[u8; 4]', 'u64')```
| None | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```
| None | `Weight` | ```{'ref_time': 'u64', 'proof_size': 'u64'}```

---------
### _Dummy
Phantom member, never used. Needed to handle multiple pallet instances.
#### Attributes
No attributes

---------