
# Paras

---------
## Calls

---------
### add_trusted_validation_code
Adds the validation code to the storage.

The code will not be added if it is already present. Additionally, if PVF pre-checking
is running for that code, it will be instantly accepted.

Otherwise, the code will be added into the storage. Note that the code will be added
into storage with reference count 0. This is to account the fact that there are no users
for this code yet. The caller will have to make sure that this code eventually gets
used by some parachain or removed from the storage to avoid storage leaks. For the latter
prefer to use the `poke_unused_validation_code` dispatchable to raw storage manipulation.

This function is mainly meant to be used for upgrading parachains that do not follow
the go-ahead signal while the PVF pre-checking feature is enabled.
#### Attributes
| Name | Type |
| -------- | -------- | 
| validation_code | `ValidationCode` | 

#### Python
```python
call = substrate.compose_call(
    'Paras', 'add_trusted_validation_code', {'validation_code': 'Bytes'}
)
```

---------
### force_note_new_head
Note a new block head for para within the context of the current block.
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 
| new_head | `HeadData` | 

#### Python
```python
call = substrate.compose_call(
    'Paras', 'force_note_new_head', {'new_head': 'Bytes', 'para': 'u32'}
)
```

---------
### force_queue_action
Put a parachain directly into the next session&\#x27;s action queue.
We can&\#x27;t queue it any sooner than this without going into the
initializer...
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'Paras', 'force_queue_action', {'para': 'u32'}
)
```

---------
### force_schedule_code_upgrade
Schedule an upgrade as if it was scheduled in the given relay parent block.
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 
| new_code | `ValidationCode` | 
| relay_parent_number | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Paras', 'force_schedule_code_upgrade', {
    'new_code': 'Bytes',
    'para': 'u32',
    'relay_parent_number': 'u32',
}
)
```

---------
### force_set_current_code
Set the storage for the parachain validation code immediately.
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 
| new_code | `ValidationCode` | 

#### Python
```python
call = substrate.compose_call(
    'Paras', 'force_set_current_code', {'new_code': 'Bytes', 'para': 'u32'}
)
```

---------
### force_set_current_head
Set the storage for the current parachain head data immediately.
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 
| new_head | `HeadData` | 

#### Python
```python
call = substrate.compose_call(
    'Paras', 'force_set_current_head', {'new_head': 'Bytes', 'para': 'u32'}
)
```

---------
### include_pvf_check_statement
Includes a statement for a PVF pre-checking vote. Potentially, finalizes the vote and
enacts the results if that was the last vote before achieving the supermajority.
#### Attributes
| Name | Type |
| -------- | -------- | 
| stmt | `PvfCheckStatement` | 
| signature | `ValidatorSignature` | 

#### Python
```python
call = substrate.compose_call(
    'Paras', 'include_pvf_check_statement', {
    'signature': '[u8; 64]',
    'stmt': {
        'accept': 'bool',
        'session_index': 'u32',
        'subject': '[u8; 32]',
        'validator_index': 'u32',
    },
}
)
```

---------
### poke_unused_validation_code
Remove the validation code from the storage iff the reference count is 0.

This is better than removing the storage directly, because it will not remove the code
that was suddenly got used by some parachain while this dispatchable was pending
dispatching.
#### Attributes
| Name | Type |
| -------- | -------- | 
| validation_code_hash | `ValidationCodeHash` | 

#### Python
```python
call = substrate.compose_call(
    'Paras', 'poke_unused_validation_code', {'validation_code_hash': '[u8; 32]'}
)
```

---------
## Events

---------
### ActionQueued
A para has been queued to execute pending actions. `para_id`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `SessionIndex` | ```u32```

---------
### CodeUpgradeScheduled
A code upgrade has been scheduled for a Para. `para_id`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```

---------
### CurrentCodeUpdated
Current code has been updated for a Para. `para_id`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```

---------
### CurrentHeadUpdated
Current head has been updated for a Para. `para_id`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```

---------
### NewHeadNoted
A new head has been noted for a Para. `para_id`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```

---------
### PvfCheckAccepted
The given validation code was accepted by the PVF pre-checking vote.
`code_hash` `para_id`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ValidationCodeHash` | ```[u8; 32]```
| None | `ParaId` | ```u32```

---------
### PvfCheckRejected
The given validation code was rejected by the PVF pre-checking vote.
`code_hash` `para_id`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ValidationCodeHash` | ```[u8; 32]```
| None | `ParaId` | ```u32```

---------
### PvfCheckStarted
The given para either initiated or subscribed to a PVF check for the given validation
code. `code_hash` `para_id`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ValidationCodeHash` | ```[u8; 32]```
| None | `ParaId` | ```u32```

---------
## Storage functions

---------
### ActionsQueue
 The actions to perform during the start of a specific session index.

#### Python
```python
result = substrate.query(
    'Paras', 'ActionsQueue', ['u32']
)
```

#### Return value
```python
['u32']
```
---------
### CodeByHash
 Validation code stored by its hash.

 This storage is consistent with [`FutureCodeHash`], [`CurrentCodeHash`] and
 [`PastCodeHash`].

#### Python
```python
result = substrate.query(
    'Paras', 'CodeByHash', ['[u8; 32]']
)
```

#### Return value
```python
'Bytes'
```
---------
### CodeByHashRefs
 The number of reference on the validation code in [`CodeByHash`] storage.

#### Python
```python
result = substrate.query(
    'Paras', 'CodeByHashRefs', ['[u8; 32]']
)
```

#### Return value
```python
'u32'
```
---------
### CurrentCodeHash
 The validation code hash of every live para.

 Corresponding code can be retrieved with [`CodeByHash`].

#### Python
```python
result = substrate.query(
    'Paras', 'CurrentCodeHash', ['u32']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### FutureCodeHash
 The actual future code hash of a para.

 Corresponding code can be retrieved with [`CodeByHash`].

#### Python
```python
result = substrate.query(
    'Paras', 'FutureCodeHash', ['u32']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### FutureCodeUpgrades
 The block number at which the planned code change is expected for a para.
 The change will be applied after the first parablock for this ID included which executes
 in the context of a relay chain block with a number &gt;= `expected_at`.

#### Python
```python
result = substrate.query(
    'Paras', 'FutureCodeUpgrades', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### Heads
 The head-data of every registered para.

#### Python
```python
result = substrate.query(
    'Paras', 'Heads', ['u32']
)
```

#### Return value
```python
'Bytes'
```
---------
### ParaLifecycles
 The current lifecycle of a all known Para IDs.

#### Python
```python
result = substrate.query(
    'Paras', 'ParaLifecycles', ['u32']
)
```

#### Return value
```python
(
    'Onboarding',
    'Parathread',
    'Parachain',
    'UpgradingParathread',
    'DowngradingParachain',
    'OffboardingParathread',
    'OffboardingParachain',
)
```
---------
### Parachains
 All parachains. Ordered ascending by `ParaId`. Parathreads are not included.

 Consider using the [`ParachainsCache`] type of modifying.

#### Python
```python
result = substrate.query(
    'Paras', 'Parachains', []
)
```

#### Return value
```python
['u32']
```
---------
### PastCodeHash
 Actual past code hash, indicated by the para id as well as the block number at which it
 became outdated.

 Corresponding code can be retrieved with [`CodeByHash`].

#### Python
```python
result = substrate.query(
    'Paras', 'PastCodeHash', [('u32', 'u32')]
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### PastCodeMeta
 Past code of parachains. The parachains themselves may not be registered anymore,
 but we also keep their code on-chain for the same amount of time as outdated code
 to keep it available for approval checkers.

#### Python
```python
result = substrate.query(
    'Paras', 'PastCodeMeta', ['u32']
)
```

#### Return value
```python
{
    'last_pruned': (None, 'u32'),
    'upgrade_times': [{'activated_at': 'u32', 'expected_at': 'u32'}],
}
```
---------
### PastCodePruning
 Which paras have past code that needs pruning and the relay-chain block at which the code was replaced.
 Note that this is the actual height of the included block, not the expected height at which the
 code upgrade would be applied, although they may be equal.
 This is to ensure the entire acceptance period is covered, not an offset acceptance period starting
 from the time at which the parachain perceives a code upgrade as having occurred.
 Multiple entries for a single para are permitted. Ordered ascending by block number.

#### Python
```python
result = substrate.query(
    'Paras', 'PastCodePruning', []
)
```

#### Return value
```python
[('u32', 'u32')]
```
---------
### PvfActiveVoteList
 The list of all currently active PVF votes. Auxiliary to `PvfActiveVoteMap`.

#### Python
```python
result = substrate.query(
    'Paras', 'PvfActiveVoteList', []
)
```

#### Return value
```python
['[u8; 32]']
```
---------
### PvfActiveVoteMap
 All currently active PVF pre-checking votes.

 Invariant:
 - There are no PVF pre-checking votes that exists in list but not in the set and vice versa.

#### Python
```python
result = substrate.query(
    'Paras', 'PvfActiveVoteMap', ['[u8; 32]']
)
```

#### Return value
```python
{
    'age': 'u32',
    'causes': [
        {
            'Onboarding': 'u32',
            'Upgrade': {'id': 'u32', 'relay_parent_number': 'u32'},
        },
    ],
    'created_at': 'u32',
    'votes_accept': 'BitVec',
    'votes_reject': 'BitVec',
}
```
---------
### UpcomingParasGenesis
 Upcoming paras instantiation arguments.

 NOTE that after PVF pre-checking is enabled the para genesis arg will have it&#x27;s code set
 to empty. Instead, the code will be saved into the storage right away via `CodeByHash`.

#### Python
```python
result = substrate.query(
    'Paras', 'UpcomingParasGenesis', ['u32']
)
```

#### Return value
```python
{'genesis_head': 'Bytes', 'para_kind': 'bool', 'validation_code': 'Bytes'}
```
---------
### UpcomingUpgrades
 The list of upcoming code upgrades. Each item is a pair of which para performs a code
 upgrade and at which relay-chain block it is expected at.

 Ordered ascending by block number.

#### Python
```python
result = substrate.query(
    'Paras', 'UpcomingUpgrades', []
)
```

#### Return value
```python
[('u32', 'u32')]
```
---------
### UpgradeCooldowns
 The list of parachains that are awaiting for their upgrade restriction to cooldown.

 Ordered ascending by block number.

#### Python
```python
result = substrate.query(
    'Paras', 'UpgradeCooldowns', []
)
```

#### Return value
```python
[('u32', 'u32')]
```
---------
### UpgradeGoAheadSignal
 This is used by the relay-chain to communicate to a parachain a go-ahead with in the upgrade procedure.

 This value is absent when there are no upgrades scheduled or during the time the relay chain
 performs the checks. It is set at the first relay-chain block when the corresponding parachain
 can switch its upgrade function. As soon as the parachain&#x27;s block is included, the value
 gets reset to `None`.

 NOTE that this field is used by parachains via merkle storage proofs, therefore changing
 the format will require migration of parachains.

#### Python
```python
result = substrate.query(
    'Paras', 'UpgradeGoAheadSignal', ['u32']
)
```

#### Return value
```python
('Abort', 'GoAhead')
```
---------
### UpgradeRestrictionSignal
 This is used by the relay-chain to communicate that there are restrictions for performing
 an upgrade for this parachain.

 This may be a because the parachain waits for the upgrade cooldown to expire. Another
 potential use case is when we want to perform some maintenance (such as storage migration)
 we could restrict upgrades to make the process simpler.

 NOTE that this field is used by parachains via merkle storage proofs, therefore changing
 the format will require migration of parachains.

#### Python
```python
result = substrate.query(
    'Paras', 'UpgradeRestrictionSignal', ['u32']
)
```

#### Return value
```python
('Present', )
```
---------
## Constants

---------
### UnsignedPriority
#### Value
```python
18446744073709551615
```
#### Python
```python
constant = substrate.get_constant('Paras', 'UnsignedPriority')
```
---------
## Errors

---------
### CannotDowngrade
Para cannot be downgraded to a parathread.

---------
### CannotOffboard
Para cannot be offboarded at this time.

---------
### CannotOnboard
Para cannot be onboarded because it is already tracked by our system.

---------
### CannotUpgrade
Para cannot be upgraded to a parachain.

---------
### CannotUpgradeCode
Parachain cannot currently schedule a code upgrade.

---------
### NotRegistered
Para is not registered in our system.

---------
### PvfCheckDoubleVote
The given validator already has cast a vote.

---------
### PvfCheckInvalidSignature
The signature for the PVF pre-checking is invalid.

---------
### PvfCheckStatementFuture
The statement for PVF pre-checking is for a future session.

---------
### PvfCheckStatementStale
The statement for PVF pre-checking is stale.

---------
### PvfCheckSubjectInvalid
The given PVF does not exist at the moment of process a vote.

---------
### PvfCheckValidatorIndexOutOfBounds
Claimed validator index is out of bounds.

---------