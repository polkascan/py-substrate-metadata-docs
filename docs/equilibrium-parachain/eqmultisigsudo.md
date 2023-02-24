
# EqMultisigSudo

---------
## Calls

---------
### add_key
Adds a key to the multisig signatory list. Requires root.
#### Attributes
| Name | Type |
| -------- | -------- | 
| key | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'EqMultisigSudo', 'add_key', {'key': 'AccountId'}
)
```

---------
### approve
Approves a proposal. Requires an account be in the multisig signatory list.
#### Attributes
| Name | Type |
| -------- | -------- | 
| call_hash | `[u8; 32]` | 

#### Python
```python
call = substrate.compose_call(
    'EqMultisigSudo', 'approve', {'call_hash': '[u8; 32]'}
)
```

---------
### cancel_proposal
Cancels an earlier submitted proposal.
#### Attributes
| Name | Type |
| -------- | -------- | 
| call_hash | `[u8; 32]` | 

#### Python
```python
call = substrate.compose_call(
    'EqMultisigSudo', 'cancel_proposal', {'call_hash': '[u8; 32]'}
)
```

---------
### modify_threshold
Modifies the multisig threshold value i.e. the required number of signatories for a call to proceed. Requires root.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_value | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'EqMultisigSudo', 'modify_threshold', {'new_value': 'u32'}
)
```

---------
### propose
Proposes a call to be signed. Requires account to be in multisig signatory list.
#### Attributes
| Name | Type |
| -------- | -------- | 
| call | `Box<<T as Config>::Call>` | 

#### Python
```python
call = substrate.compose_call(
    'EqMultisigSudo', 'propose', {'call': 'Call'}
)
```

---------
### remove_key
Removes a key from the multisig signatory list. Requires root.
#### Attributes
| Name | Type |
| -------- | -------- | 
| key | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'EqMultisigSudo', 'remove_key', {'key': 'AccountId'}
)
```

---------
## Events

---------
### Initialized
The storage has been initialized
#### Attributes
No attributes

---------
### KeyAdded
A key has been added to the multisig signatory list
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### KeyRemoved
A key has been removed to the multisig signatory list
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### MultisigSudid
Sudo was executed on the proposal after enough signatures
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CallHash` | ```[u8; 32]```
| None | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
### NewProposal
A new multisig proposal
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `CallHash` | ```[u8; 32]```

---------
### ProposalApproved
The proposal was approved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `CallHash` | ```[u8; 32]```

---------
### ProposalCancelled
The proposal was cancelled
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CallHash` | ```[u8; 32]```

---------
### SudoFailed
Sudo critical failure
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CallHash` | ```[u8; 32]```

---------
### ThresholdModified
The signatory threshold was modified; a new value is supplied.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `u32` | ```u32```

---------
## Storage functions

---------
### Keys
 The multisig signatory key list.

#### Python
```python
result = substrate.query(
    'EqMultisigSudo', 'Keys', ['AccountId']
)
```

#### Return value
```python
'bool'
```
---------
### MultisigProposals
 The map storing proposals by a call hash key (CallHash)

#### Python
```python
result = substrate.query(
    'EqMultisigSudo', 'MultisigProposals', ['[u8; 32]']
)
```

#### Return value
```python
{'approvals': ['AccountId'], 'call': 'Bytes', 'cancels': ['AccountId'], 'proposer': 'AccountId'}
```
---------
### Threshold
 The threshold required to proceed a call.

#### Python
```python
result = substrate.query(
    'EqMultisigSudo', 'Threshold', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### MaxSignatories
 Maximal number of signatories
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('EqMultisigSudo', 'MaxSignatories')
```
---------
## Errors

---------
### AlreadyApproved
The account already approved a proposal

---------
### AlreadyCancelled
The account already voted to cancel a proposal

---------
### AlreadyInKeyList
The key is already in the multisig signatory list

---------
### FewSignatories
Too few signatories for the set threshold

---------
### InvalidThresholdValue
The threshold is invalid

---------
### NotInKeyList
The key is not in the multisig signatory list

---------
### NotProposalOwner
Trying to delete a proposal that is not ours

---------
### ProposalNotFound
The proposal not found in the map

---------