
# Beefy

---------
## Calls

---------
### report_equivocation
See [`Pallet::report_equivocation`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| equivocation_proof | `Box<EquivocationProof<BlockNumberFor<T>, T::BeefyId,<T::BeefyId
as RuntimeAppPublic>::Signature,>,>` | 
| key_owner_proof | `T::KeyOwnerProof` | 

#### Python
```python
call = substrate.compose_call(
    'Beefy', 'report_equivocation', {
    'equivocation_proof': {
        'first': {
            'commitment': {
                'block_number': 'u32',
                'payload': [
                    (
                        '[u8; 2]',
                        'Bytes',
                    ),
                ],
                'validator_set_id': 'u64',
            },
            'id': '[u8; 33]',
            'signature': '[u8; 65]',
        },
        'second': {
            'commitment': {
                'block_number': 'u32',
                'payload': [
                    (
                        '[u8; 2]',
                        'Bytes',
                    ),
                ],
                'validator_set_id': 'u64',
            },
            'id': '[u8; 33]',
            'signature': '[u8; 65]',
        },
    },
    'key_owner_proof': {
        'session': 'u32',
        'trie_nodes': ['Bytes'],
        'validator_count': 'u32',
    },
}
)
```

---------
### report_equivocation_unsigned
See [`Pallet::report_equivocation_unsigned`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| equivocation_proof | `Box<EquivocationProof<BlockNumberFor<T>, T::BeefyId,<T::BeefyId
as RuntimeAppPublic>::Signature,>,>` | 
| key_owner_proof | `T::KeyOwnerProof` | 

#### Python
```python
call = substrate.compose_call(
    'Beefy', 'report_equivocation_unsigned', {
    'equivocation_proof': {
        'first': {
            'commitment': {
                'block_number': 'u32',
                'payload': [
                    (
                        '[u8; 2]',
                        'Bytes',
                    ),
                ],
                'validator_set_id': 'u64',
            },
            'id': '[u8; 33]',
            'signature': '[u8; 65]',
        },
        'second': {
            'commitment': {
                'block_number': 'u32',
                'payload': [
                    (
                        '[u8; 2]',
                        'Bytes',
                    ),
                ],
                'validator_set_id': 'u64',
            },
            'id': '[u8; 33]',
            'signature': '[u8; 65]',
        },
    },
    'key_owner_proof': {
        'session': 'u32',
        'trie_nodes': ['Bytes'],
        'validator_count': 'u32',
    },
}
)
```

---------
### set_new_genesis
See [`Pallet::set_new_genesis`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| delay_in_blocks | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Beefy', 'set_new_genesis', {'delay_in_blocks': 'u32'}
)
```

---------
## Storage functions

---------
### Authorities
 The current authorities set

#### Python
```python
result = substrate.query(
    'Beefy', 'Authorities', []
)
```

#### Return value
```python
['[u8; 33]']
```
---------
### GenesisBlock
 Block number where BEEFY consensus is enabled/started.
 By changing this (through privileged `set_new_genesis()`), BEEFY consensus is effectively
 restarted from the newly set block number.

#### Python
```python
result = substrate.query(
    'Beefy', 'GenesisBlock', []
)
```

#### Return value
```python
(None, 'u32')
```
---------
### NextAuthorities
 Authorities set scheduled to be used with the next session

#### Python
```python
result = substrate.query(
    'Beefy', 'NextAuthorities', []
)
```

#### Return value
```python
['[u8; 33]']
```
---------
### SetIdSession
 A mapping from BEEFY set ID to the index of the *most recent* session for which its
 members were responsible.

 This is only used for validating equivocation proofs. An equivocation proof must
 contains a key-ownership proof for a given session, therefore we need a way to tie
 together sessions and BEEFY set ids, i.e. we need to validate that a validator
 was the owner of a given key on a given session, and what the active set ID was
 during that session.

 TWOX-NOTE: `ValidatorSetId` is not under user control.

#### Python
```python
result = substrate.query(
    'Beefy', 'SetIdSession', ['u64']
)
```

#### Return value
```python
'u32'
```
---------
### ValidatorSetId
 The current validator set id

#### Python
```python
result = substrate.query(
    'Beefy', 'ValidatorSetId', []
)
```

#### Return value
```python
'u64'
```
---------
## Constants

---------
### MaxAuthorities
 The maximum number of authorities that can be added.
#### Value
```python
100000
```
#### Python
```python
constant = substrate.get_constant('Beefy', 'MaxAuthorities')
```
---------
### MaxNominators
 The maximum number of nominators for each validator.
#### Value
```python
512
```
#### Python
```python
constant = substrate.get_constant('Beefy', 'MaxNominators')
```
---------
### MaxSetIdSessionEntries
 The maximum number of entries to keep in the set id to session index mapping.

 Since the `SetIdSession` map is only used for validating equivocations this
 value should relate to the bonding duration of whatever staking system is
 being used (if any). If equivocation handling is not enabled then this value
 can be zero.
#### Value
```python
168
```
#### Python
```python
constant = substrate.get_constant('Beefy', 'MaxSetIdSessionEntries')
```
---------
## Errors

---------
### DuplicateOffenceReport
A given equivocation report is valid but already previously reported.

---------
### InvalidConfiguration
Submitted configuration is invalid.

---------
### InvalidEquivocationProof
An equivocation proof provided as part of an equivocation report is invalid.

---------
### InvalidKeyOwnershipProof
A key ownership proof provided as part of an equivocation report is invalid.

---------