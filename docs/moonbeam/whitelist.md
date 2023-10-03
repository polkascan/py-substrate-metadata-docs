
# Whitelist

---------
## Calls

---------
### dispatch_whitelisted_call
#### Attributes
| Name | Type |
| -------- | -------- | 
| call_hash | `PreimageHash` | 
| call_encoded_len | `u32` | 
| call_weight_witness | `Weight` | 

#### Python
```python
call = substrate.compose_call(
    'Whitelist', 'dispatch_whitelisted_call', {
    'call_encoded_len': 'u32',
    'call_hash': '[u8; 32]',
    'call_weight_witness': {
        'proof_size': 'u64',
        'ref_time': 'u64',
    },
}
)
```

---------
### dispatch_whitelisted_call_with_preimage
#### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config>::RuntimeCall>` | 

#### Python
```python
call = substrate.compose_call(
    'Whitelist', 'dispatch_whitelisted_call_with_preimage', {'call': 'Call'}
)
```

---------
### remove_whitelisted_call
#### Attributes
| Name | Type |
| -------- | -------- | 
| call_hash | `PreimageHash` | 

#### Python
```python
call = substrate.compose_call(
    'Whitelist', 'remove_whitelisted_call', {'call_hash': '[u8; 32]'}
)
```

---------
### whitelist_call
#### Attributes
| Name | Type |
| -------- | -------- | 
| call_hash | `PreimageHash` | 

#### Python
```python
call = substrate.compose_call(
    'Whitelist', 'whitelist_call', {'call_hash': '[u8; 32]'}
)
```

---------
## Events

---------
### CallWhitelisted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| call_hash | `PreimageHash` | ```[u8; 32]```

---------
### WhitelistedCallDispatched
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| call_hash | `PreimageHash` | ```[u8; 32]```
| result | `DispatchResultWithPostInfo` | ```{'Ok': {'actual_weight': (None, {'ref_time': 'u64', 'proof_size': 'u64'}), 'pays_fee': ('Yes', 'No')}, 'Err': {'post_info': {'actual_weight': (None, {'ref_time': 'u64', 'proof_size': 'u64'}), 'pays_fee': ('Yes', 'No')}, 'error': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable', 'Blocked'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None, 'RootNotAllowed': None}}}```

---------
### WhitelistedCallRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| call_hash | `PreimageHash` | ```[u8; 32]```

---------
## Storage functions

---------
### WhitelistedCall

#### Python
```python
result = substrate.query(
    'Whitelist', 'WhitelistedCall', ['[u8; 32]']
)
```

#### Return value
```python
()
```
---------
## Errors

---------
### CallAlreadyWhitelisted
The call was already whitelisted; No-Op.

---------
### CallIsNotWhitelisted
The call was not whitelisted.

---------
### InvalidCallWeightWitness
The weight of the decoded call was higher than the witness.

---------
### UnavailablePreImage
The preimage of the call hash could not be loaded.

---------
### UndecodableCall
The call could not be decoded.

---------