
# Paras

---------
## Calls

---------
### add_trusted_validation_code
See [`Pallet::add_trusted_validation_code`].
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
See [`Pallet::force_note_new_head`].
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
See [`Pallet::force_queue_action`].
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
See [`Pallet::force_schedule_code_upgrade`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 
| new_code | `ValidationCode` | 
| relay_parent_number | `BlockNumberFor<T>` | 

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
See [`Pallet::force_set_current_code`].
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
See [`Pallet::force_set_current_head`].
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
### force_set_most_recent_context
See [`Pallet::force_set_most_recent_context`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 
| context | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Paras', 'force_set_most_recent_context', {'context': 'u32', 'para': 'u32'}
)
```

---------
### include_pvf_check_statement
See [`Pallet::include_pvf_check_statement`].
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
        'subject': 'scale_info::12',
        'validator_index': 'u32',
    },
}
)
```

---------
### poke_unused_validation_code
See [`Pallet::poke_unused_validation_code`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| validation_code_hash | `ValidationCodeHash` | 

#### Python
```python
call = substrate.compose_call(
    'Paras', 'poke_unused_validation_code', {
    'validation_code_hash': 'scale_info::12',
}
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
| None | `ValidationCodeHash` | ```scale_info::12```
| None | `ParaId` | ```u32```

---------
### PvfCheckRejected
The given validation code was rejected by the PVF pre-checking vote.
`code_hash` `para_id`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ValidationCodeHash` | ```scale_info::12```
| None | `ParaId` | ```u32```

---------
### PvfCheckStarted
The given para either initiated or subscribed to a PVF check for the given validation
code. `code_hash` `para_id`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ValidationCodeHash` | ```scale_info::12```
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
    'Paras', 'CodeByHash', ['scale_info::12']
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
    'Paras', 'CodeByHashRefs', ['scale_info::12']
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
'scale_info::12'
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
'scale_info::12'
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
### MostRecentContext
 The context (relay-chain block number) of the most recent parachain head.

#### Python
```python
result = substrate.query(
    'Paras', 'MostRecentContext', ['u32']
)
```

#### Return value
```python
'u32'
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
 All lease holding parachains. Ordered ascending by `ParaId`. On demand parachains are not
 included.

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
'scale_info::12'
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
 Which paras have past code that needs pruning and the relay-chain block at which the code
 was replaced. Note that this is the actual height of the included block, not the expected
 height at which the code upgrade would be applied, although they may be equal.
 This is to ensure the entire acceptance period is covered, not an offset acceptance period
 starting from the time at which the parachain perceives a code upgrade as having occurred.
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
['scale_info::12']
```
---------
### PvfActiveVoteMap
 All currently active PVF pre-checking votes.

 Invariant:
 - There are no PVF pre-checking votes that exists in list but not in the set and vice versa.

#### Python
```python
result = substrate.query(
    'Paras', 'PvfActiveVoteMap', ['scale_info::12']
)
```

#### Return value
```python
{
    'age': 'u32',
    'causes': [
        {
            'Onboarding': 'u32',
            'Upgrade': {
                'id': 'u32',
                'included_at': 'u32',
                'set_go_ahead': ('Yes', 'No'),
            },
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
 This is used by the relay-chain to communicate to a parachain a go-ahead with in the upgrade
 procedure.

 This value is absent when there are no upgrades scheduled or during the time the relay chain
 performs the checks. It is set at the first relay-chain block when the corresponding
 parachain can switch its upgrade function. As soon as the parachain&#x27;s block is included, the
 value gets reset to `None`.

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
Para cannot be downgraded to an on-demand parachain.

---------
### CannotOffboard
Para cannot be offboarded at this time.

---------
### CannotOnboard
Para cannot be onboarded because it is already tracked by our system.

---------
### CannotUpgrade
Para cannot be upgraded to a lease holding parachain.

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