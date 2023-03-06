
# AresChallenge

---------
## Calls

---------
### challenge_success
#### Attributes
| Name | Type |
| -------- | -------- | 
| challenge_hash | `<T as frame_system::Config>::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'AresChallenge', 'challenge_success', {'challenge_hash': '[u8; 32]'}
)
```

---------
### new_challenge
#### Attributes
| Name | Type |
| -------- | -------- | 
| delegatee | `<T::Lookup as StaticLookup>::Source` | 
| validator | `<T::Lookup as StaticLookup>::Source` | 
| block_hash | `T::Hash` | 
| deposit | `BalanceOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'AresChallenge', 'new_challenge', {
    'block_hash': '[u8; 32]',
    'delegatee': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'deposit': 'u128',
    'validator': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### reserve
#### Attributes
| Name | Type |
| -------- | -------- | 
| deposit | `BalanceOf<T, I>` | 

#### Python
```python
call = substrate.compose_call(
    'AresChallenge', 'reserve', {'deposit': 'u128'}
)
```

---------
## Events

---------
### CheckedNoPassSlashed
parameters. [who, value]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T, I>` | ```u128```

---------
### Deposit
Some funds have been deposited. \[deposit\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T, I>` | ```u128```

---------
### Reserved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id | `[u8; 8]` | ```[u8; 8]```
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T, I>` | ```u128```

---------
## Storage functions

---------
### Proposals

#### Python
```python
result = substrate.query(
    'AresChallenge', 'Proposals', ['[u8; 32]']
)
```

#### Return value
```python
{
    'deposit': 'u128',
    'end': 'u32',
    'proposal': '[u8; 32]',
    'target': {'block_hash': '[u8; 32]', 'validator': 'AccountId'},
    'who': 'AccountId',
}
```
---------
## Constants

---------
### MinimumDeposit
 The minimum amount to be checked price
#### Value
```python
100000000000000000
```
#### Python
```python
constant = substrate.get_constant('AresChallenge', 'MinimumDeposit')
```
---------
### MinimumThreshold
#### Value
```python
6
```
#### Python
```python
constant = substrate.get_constant('AresChallenge', 'MinimumThreshold')
```
---------
### PalletId
#### Value
```python
'0x70792f617264656d'
```
#### Python
```python
constant = substrate.get_constant('AresChallenge', 'PalletId')
```
---------
## Errors

---------
### BadOrigin

---------
### DepositLow
Deposit too low

---------
### DuplicateProposal
Proposal already noted

---------
### FreeBalanceLow
Free balance too low

---------
### MissingProposal
Proposal is missing

---------
### NoneValue
Error names should be descriptive.

---------
### StorageOverflow
Errors should have helpful documentation associated with them.

---------
### ThresholdTooLow
Threshold too low

---------