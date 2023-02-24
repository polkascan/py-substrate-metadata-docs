
# Airdrop

---------
## Calls

---------
### change_merkle_root
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_root | `[u8; 32]` | 

#### Python
```python
call = substrate.compose_call(
    'Airdrop', 'change_merkle_root', {'new_root': '[u8; 32]'}
)
```

---------
### dispatch_exchange_claim
#### Attributes
| Name | Type |
| -------- | -------- | 
| icon_address | `types::IconAddress` | 
| ice_address | `types::IceAddress` | 
| total_amount | `types::BalanceOf<T>` | 
| defi_user | `bool` | 
| proofs | `types::MerkleProofs<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Airdrop', 'dispatch_exchange_claim', {
    'defi_user': 'bool',
    'ice_address': '[u8; 32]',
    'icon_address': '[u8; 20]',
    'proofs': ['[u8; 32]'],
    'total_amount': 'u128',
}
)
```

---------
### dispatch_user_claim
Dispatchable to be called by server with privileged account
dispatch claim
#### Attributes
| Name | Type |
| -------- | -------- | 
| icon_address | `types::IconAddress` | 
| ice_address | `types::IceAddress` | 
| message | `types::RawPayload` | 
| icon_signature | `types::IconSignature` | 
| ice_signature | `types::IceSignature` | 
| total_amount | `types::BalanceOf<T>` | 
| defi_user | `bool` | 
| proofs | `types::MerkleProofs<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Airdrop', 'dispatch_user_claim', {
    'defi_user': 'bool',
    'ice_address': '[u8; 32]',
    'ice_signature': '[u8; 64]',
    'icon_address': '[u8; 20]',
    'icon_signature': '[u8; 65]',
    'message': '[u8; 289]',
    'proofs': ['[u8; 32]'],
    'total_amount': 'u128',
}
)
```

---------
### set_airdrop_server_account
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_account | `types::AccountIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Airdrop', 'set_airdrop_server_account', {'new_account': 'AccountId'}
)
```

---------
### update_airdrop_state
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_state | `types::AirdropState` | 

#### Python
```python
call = substrate.compose_call(
    'Airdrop', 'update_airdrop_state', {
    'new_state': {
        'block_claim_request': 'bool',
        'block_exchange_request': 'bool',
    },
}
)
```

---------
## Events

---------
### AirdropStateUpdated
AirdropState have been updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_state | `types::AirdropState` | ```{'block_claim_request': 'bool', 'block_exchange_request': 'bool'}```
| new_state | `types::AirdropState` | ```{'block_claim_request': 'bool', 'block_exchange_request': 'bool'}```

---------
### ClaimPartialSuccess
PartialClaimRequest have been ok for given icon address
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `types::IconAddress` | ```[u8; 20]```

---------
### ClaimSuccess
ClaimRequest have been ok for given icon address
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `types::IconAddress` | ```[u8; 20]```

---------
### CreditorBalanceLow
Creditor balance is running low
#### Attributes
No attributes

---------
### MerkleRootUpdated
New merkle root have been set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_root | `Option<[u8; 32]>` | ```(None, '[u8; 32]')```
| new_root | `[u8; 32]` | ```[u8; 32]```

---------
### ServerAccountChanged
Value of ServerAccount storage have been changed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_account | `Option<types::AccountIdOf<T>>` | ```(None, 'AccountId')```
| new_account | `types::AccountIdOf<T>` | ```AccountId```

---------
## Storage functions

---------
### AirdropChainState

#### Python
```python
result = substrate.query(
    'Airdrop', 'AirdropChainState', []
)
```

#### Return value
```python
{'block_claim_request': 'bool', 'block_exchange_request': 'bool'}
```
---------
### CreditorAccount

#### Python
```python
result = substrate.query(
    'Airdrop', 'CreditorAccount', []
)
```

#### Return value
```python
'AccountId'
```
---------
### ExchangeAccountsMap

#### Python
```python
result = substrate.query(
    'Airdrop', 'ExchangeAccountsMap', ['[u8; 20]']
)
```

#### Return value
```python
'u128'
```
---------
### IceIconMap

#### Python
```python
result = substrate.query(
    'Airdrop', 'IceIconMap', ['AccountId']
)
```

#### Return value
```python
'[u8; 20]'
```
---------
### IconSnapshotMap

#### Python
```python
result = substrate.query(
    'Airdrop', 'IconSnapshotMap', ['[u8; 20]']
)
```

#### Return value
```python
{
    'amount': 'u128',
    'defi_user': 'bool',
    'done_instant': 'bool',
    'done_vesting': 'bool',
    'ice_address': 'AccountId',
    'initial_transfer': 'u128',
    'instant_block_number': (None, 'u32'),
    'vesting_block_number': (None, 'u32'),
}
```
---------
### MerkleRoot

#### Python
```python
result = substrate.query(
    'Airdrop', 'MerkleRoot', []
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### ServerAccount

#### Python
```python
result = substrate.query(
    'Airdrop', 'ServerAccount', []
)
```

#### Return value
```python
'AccountId'
```
---------
### StorageVersion

#### Python
```python
result = substrate.query(
    'Airdrop', 'StorageVersion', []
)
```

#### Return value
```python
'u32'
```
---------
## Errors

---------
### ArithmeticError
Internal arithmetic error

---------
### CantApplyVesting
Some operation while applying vesting failed

---------
### ClaimAlreadyMade
Claim has already been made so can&\#x27;t be made again at this time

---------
### DeniedOperation
Error to return when unauthorised operation is attempted

---------
### FailedConversion
Conversion between partially-compatible type failed

---------
### FailedExtractingIceAddress
Couldn&\#x27;t get embedded ice address from message

---------
### IceAddressInUse
This ice address have already been mapped to another icon address

---------
### IconAddressInUse
This icon address have already been mapped to another ice address

---------
### IncompatibleAccountId
Unexpected format of AccountId

---------
### IncompleteData
Not all data required are supplied with

---------
### InsufficientCreditorBalance
Creditor account do not have enough USABLE balance to
undergo this transaction

---------
### InvalidClaimAmount
Claim amount was not expected in this exchanged airdrop

---------
### InvalidIceAddress
Provided ice address is not in expected format

---------
### InvalidIceSignature
Invalid signature provided

---------
### InvalidMerkleProof
Given proof set was invalid to expected tree root

---------
### InvalidMessagePayload
Given message payload is invalid or is in unexpected format

---------
### InvalidSignature
This error will occur when signature validation failed.

---------
### NewClaimRequestBlocked
Currently no new claim request is being accepted

---------
### NewExchangeRequestBlocked
Currently processing of exchange request is blocked

---------
### NoCreditorAccount
Creditor account is not set on chain yet

---------
### NoMerkleRoot
Merkle root is not set on chain yet

---------
### ProofTooLarge
Provided proof size exceed the maximum limit

---------