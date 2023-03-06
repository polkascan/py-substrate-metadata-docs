
# Grandpa

---------
## Calls

---------
### note_stalled
Note that the current authority set of the GRANDPA finality gadget has
stalled. This will trigger a forced authority set change at the beginning
of the next session, to be enacted `delay` blocks after that. The delay
should be high enough to safely assume that the block signalling the
forced change will not be re-orged (e.g. 1000 blocks). The GRANDPA voters
will start the new authority set using the given finalized block as base.
Only callable by root.
#### Attributes
| Name | Type |
| -------- | -------- | 
| delay | `T::BlockNumber` | 
| best_finalized_block_number | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Grandpa', 'note_stalled', {
    'best_finalized_block_number': 'u32',
    'delay': 'u32',
}
)
```

---------
### report_equivocation
Report voter equivocation/misbehavior. This method will verify the
equivocation proof and validate the given key ownership proof
against the extracted offender. If both are valid, the offence
will be reported.
#### Attributes
| Name | Type |
| -------- | -------- | 
| equivocation_proof | `Box<EquivocationProof<T::Hash, T::BlockNumber>>` | 
| key_owner_proof | `T::KeyOwnerProof` | 

#### Python
```python
call = substrate.compose_call(
    'Grandpa', 'report_equivocation', {
    'equivocation_proof': {
        'equivocation': {
            'Precommit': {
                'first': (
                    {
                        'target_hash': '[u8; 32]',
                        'target_number': 'u32',
                    },
                    '[u8; 64]',
                ),
                'identity': '[u8; 32]',
                'round_number': 'u64',
                'second': (
                    {
                        'target_hash': '[u8; 32]',
                        'target_number': 'u32',
                    },
                    '[u8; 64]',
                ),
            },
            'Prevote': {
                'first': (
                    {
                        'target_hash': '[u8; 32]',
                        'target_number': 'u32',
                    },
                    '[u8; 64]',
                ),
                'identity': '[u8; 32]',
                'round_number': 'u64',
                'second': (
                    {
                        'target_hash': '[u8; 32]',
                        'target_number': 'u32',
                    },
                    '[u8; 64]',
                ),
            },
        },
        'set_id': 'u64',
    },
    'key_owner_proof': (),
}
)
```

---------
### report_equivocation_unsigned
Report voter equivocation/misbehavior. This method will verify the
equivocation proof and validate the given key ownership proof
against the extracted offender. If both are valid, the offence
will be reported.

This extrinsic must be called unsigned and it is expected that only
block authors will call it (validated in `ValidateUnsigned`), as such
if the block author is defined it will be defined as the equivocation
reporter.
#### Attributes
| Name | Type |
| -------- | -------- | 
| equivocation_proof | `Box<EquivocationProof<T::Hash, T::BlockNumber>>` | 
| key_owner_proof | `T::KeyOwnerProof` | 

#### Python
```python
call = substrate.compose_call(
    'Grandpa', 'report_equivocation_unsigned', {
    'equivocation_proof': {
        'equivocation': {
            'Precommit': {
                'first': (
                    {
                        'target_hash': '[u8; 32]',
                        'target_number': 'u32',
                    },
                    '[u8; 64]',
                ),
                'identity': '[u8; 32]',
                'round_number': 'u64',
                'second': (
                    {
                        'target_hash': '[u8; 32]',
                        'target_number': 'u32',
                    },
                    '[u8; 64]',
                ),
            },
            'Prevote': {
                'first': (
                    {
                        'target_hash': '[u8; 32]',
                        'target_number': 'u32',
                    },
                    '[u8; 64]',
                ),
                'identity': '[u8; 32]',
                'round_number': 'u64',
                'second': (
                    {
                        'target_hash': '[u8; 32]',
                        'target_number': 'u32',
                    },
                    '[u8; 64]',
                ),
            },
        },
        'set_id': 'u64',
    },
    'key_owner_proof': (),
}
)
```

---------
## Events

---------
### NewAuthorities
New authority set has been applied.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| authority_set | `AuthorityList` | ```[('[u8; 32]', 'u64')]```

---------
### Paused
Current authority set has been paused.
#### Attributes
No attributes

---------
### Resumed
Current authority set has been resumed.
#### Attributes
No attributes

---------
## Storage functions

---------
### CurrentSetId
 The number of changes (both in terms of keys and underlying economic responsibilities)
 in the &quot;set&quot; of Grandpa validators from genesis.

#### Python
```python
result = substrate.query(
    'Grandpa', 'CurrentSetId', []
)
```

#### Return value
```python
'u64'
```
---------
### NextForced
 next block number where we can force a change.

#### Python
```python
result = substrate.query(
    'Grandpa', 'NextForced', []
)
```

#### Return value
```python
'u32'
```
---------
### PendingChange
 Pending change: (signaled at, scheduled change).

#### Python
```python
result = substrate.query(
    'Grandpa', 'PendingChange', []
)
```

#### Return value
```python
{
    'delay': 'u32',
    'forced': (None, 'u32'),
    'next_authorities': [('[u8; 32]', 'u64')],
    'scheduled_at': 'u32',
}
```
---------
### SetIdSession
 A mapping from grandpa set ID to the index of the *most recent* session for which its
 members were responsible.

 TWOX-NOTE: `SetId` is not under user control.

#### Python
```python
result = substrate.query(
    'Grandpa', 'SetIdSession', ['u64']
)
```

#### Return value
```python
'u32'
```
---------
### Stalled
 `true` if we are currently stalled.

#### Python
```python
result = substrate.query(
    'Grandpa', 'Stalled', []
)
```

#### Return value
```python
('u32', 'u32')
```
---------
### State
 State of the current authority set.

#### Python
```python
result = substrate.query(
    'Grandpa', 'State', []
)
```

#### Return value
```python
{
    'Live': None,
    'Paused': None,
    'PendingPause': {'delay': 'u32', 'scheduled_at': 'u32'},
    'PendingResume': {'delay': 'u32', 'scheduled_at': 'u32'},
}
```
---------
## Constants

---------
### MaxAuthorities
 Max Authorities in use
#### Value
```python
32
```
#### Python
```python
constant = substrate.get_constant('Grandpa', 'MaxAuthorities')
```
---------
## Errors

---------
### ChangePending
Attempt to signal GRANDPA change with one already pending.

---------
### DuplicateOffenceReport
A given equivocation report is valid but already previously reported.

---------
### InvalidEquivocationProof
An equivocation proof provided as part of an equivocation report is invalid.

---------
### InvalidKeyOwnershipProof
A key ownership proof provided as part of an equivocation report is invalid.

---------
### PauseFailed
Attempt to signal GRANDPA pause when the authority set isn&\#x27;t live
(either paused or already pending pause).

---------
### ResumeFailed
Attempt to signal GRANDPA resume when the authority set isn&\#x27;t paused
(either live or already pending resume).

---------
### TooSoon
Cannot signal forced change so soon after last.

---------