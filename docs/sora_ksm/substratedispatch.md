
# SubstrateDispatch

---------
## Events

---------
### MessageDecodeFailed
We have failed to decode a Call from the message.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::MessageId` | ```{'sender': {'EVM': '[u64; 4]', 'Sub': {'Mainnet': None, 'Kusama': None, 'Polkadot': None, 'Rococo': None, 'Custom': 'u32'}, 'EVMLegacy': 'u32'}, 'receiver': {'EVM': '[u64; 4]', 'Sub': {'Mainnet': None, 'Kusama': None, 'Polkadot': None, 'Rococo': None, 'Custom': 'u32'}, 'EVMLegacy': 'u32'}, 'batch_nonce': (None, 'u64'), 'message_nonce': 'u64'}```

---------
### MessageDispatched
Message has been dispatched with given result.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::MessageId` | ```{'sender': {'EVM': '[u64; 4]', 'Sub': {'Mainnet': None, 'Kusama': None, 'Polkadot': None, 'Rococo': None, 'Custom': 'u32'}, 'EVMLegacy': 'u32'}, 'receiver': {'EVM': '[u64; 4]', 'Sub': {'Mainnet': None, 'Kusama': None, 'Polkadot': None, 'Rococo': None, 'Custom': 'u32'}, 'EVMLegacy': 'u32'}, 'batch_nonce': (None, 'u64'), 'message_nonce': 'u64'}```
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
### MessageRejected
Message has been rejected
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::MessageId` | ```{'sender': {'EVM': '[u64; 4]', 'Sub': {'Mainnet': None, 'Kusama': None, 'Polkadot': None, 'Rococo': None, 'Custom': 'u32'}, 'EVMLegacy': 'u32'}, 'receiver': {'EVM': '[u64; 4]', 'Sub': {'Mainnet': None, 'Kusama': None, 'Polkadot': None, 'Rococo': None, 'Custom': 'u32'}, 'EVMLegacy': 'u32'}, 'batch_nonce': (None, 'u64'), 'message_nonce': 'u64'}```

---------