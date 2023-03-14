
# Staking

---------
## Calls

---------
### add_permissioned_validator
Governance committee on 2/3 rds majority can introduce a new potential identity
to the pool of permissioned entities who can run validators. Staking module uses `PermissionedIdentity`
to ensure validators have completed KYB compliance and considers them for validation.

\# Arguments
* origin Required origin for adding a potential validator.
* identity Validator&\#x27;s IdentityId.
* intended_count No. of validators given identity intends to run.
#### Attributes
| Name | Type |
| -------- | -------- | 
| identity | `IdentityId` | 
| intended_count | `Option<u32>` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'add_permissioned_validator', {
    'identity': '[u8; 32]',
    'intended_count': (None, 'u32'),
}
)
```

---------
### bond
Take the origin account as a stash and lock up `value` of its balance. `controller` will
be the account that controls it.

`value` must be more than the `minimum_balance` specified by `T::Currency`.

The dispatch origin for this call must be _Signed_ by the stash account.

Emits `Bonded`.

\# &lt;weight&gt;
- Independent of the arguments. Moderate complexity.
- O(1).
- Three extra DB entries.

NOTE: Two of the storage writes (`Self::bonded`, `Self::payee`) are _never_ cleaned
unless the `origin` falls below _existential deposit_ and gets removed as dust.
------------------
Weight: O(1)
DB Weight:
- Read: Bonded, Ledger, [Origin Account], Current Era, History Depth, Locks
- Write: Bonded, Payee, [Origin Account], Locks, Ledger
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| controller | `<T::Lookup as StaticLookup>::Source` | 
| value | `BalanceOf<T>` | 
| payee | `RewardDestination<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'bond', {
    'controller': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'payee': {
        'Account': 'AccountId',
        'Controller': None,
        'Staked': None,
        'Stash': None,
    },
    'value': 'u128',
}
)
```

---------
### bond_extra
Add some extra amount that have appeared in the stash `free_balance` into the balance up
for staking.

Use this if there are additional funds in your stash account that you wish to bond.
Unlike [`bond`] or [`unbond`] this function does not impose any limitation on the amount
that can be added.

The dispatch origin for this call must be _Signed_ by the stash, not the controller and
it can be only called when [`EraElectionStatus`] is `Closed`.

Emits `Bonded`.

\# &lt;weight&gt;
- Independent of the arguments. Insignificant complexity.
- O(1).
- One DB entry.
------------
DB Weight:
- Read: Era Election Status, Bonded, Ledger, [Origin Account], Locks
- Write: [Origin Account], Locks, Ledger
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| max_additional | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'bond_extra', {'max_additional': 'u128'}
)
```

---------
### cancel_deferred_slash
Cancel enactment of a deferred slash.

Can be called by the `T::SlashCancelOrigin`.

Parameters: era and indices of the slashes for that era to kill.

\# &lt;weight&gt;
Complexity: O(U + S)
with U unapplied slashes weighted with U=1000
and S is the number of slash indices to be canceled.
- Read: Unapplied Slashes
- Write: Unapplied Slashes
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| era | `EraIndex` | 
| slash_indices | `Vec<u32>` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'cancel_deferred_slash', {
    'era': 'u32',
    'slash_indices': ['u32'],
}
)
```

---------
### change_slashing_allowed_for
Switch slashing status on the basis of given `SlashingSwitch`. Can only be called by root.

\# Arguments
* origin - AccountId of root.
* slashing_switch - Switch used to set the targets for slashing.
#### Attributes
| Name | Type |
| -------- | -------- | 
| slashing_switch | `SlashingSwitch` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'change_slashing_allowed_for', {
    'slashing_switch': (
        'Validator',
        'ValidatorAndNominator',
        'None',
    ),
}
)
```

---------
### chill
Declare no desire to either validate or nominate.

Effects will be felt at the beginning of the next era.

The dispatch origin for this call must be _Signed_ by the controller, not the stash.
And, it can be only called when [`EraElectionStatus`] is `Closed`.

\# &lt;weight&gt;
- Independent of the arguments. Insignificant complexity.
- Contains one read.
- Writes are limited to the `origin` account key.
--------
Weight: O(1)
DB Weight:
- Read: EraElectionStatus, Ledger
- Write: Validators, Nominators
\# &lt;/weight&gt;
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Staking', 'chill', {}
)
```

---------
### chill_from_governance
GC forcefully chills a validator.
Effects will be felt at the beginning of the next era.
And, it can be only called when [`EraElectionStatus`] is `Closed`.

\# Arguments
* origin which must be a GC.
* identity must be permissioned to run operator/validator nodes.
* stash_keys contains the secondary keys of the permissioned identity

\# Errors
* `BadOrigin` The origin was not a GC member.
* `CallNotAllowed` The call is not allowed at the given time due to restrictions of election period.
* `NotExists` Permissioned validator doesn&\#x27;t exist.
* `NotStash` Not a stash account for the permissioned identity.
#### Attributes
| Name | Type |
| -------- | -------- | 
| identity | `IdentityId` | 
| stash_keys | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'chill_from_governance', {
    'identity': '[u8; 32]',
    'stash_keys': ['AccountId'],
}
)
```

---------
### force_new_era
Force there to be a new era at the end of the next session. After this, it will be
reset to normal (non-forced) behaviour.

The dispatch origin must be Root.

\# &lt;weight&gt;
- No arguments.
- Weight: O(1)
- Write ForceEra
\# &lt;/weight&gt;
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Staking', 'force_new_era', {}
)
```

---------
### force_new_era_always
Force there to be a new era at the end of sessions indefinitely.

The dispatch origin must be Root.

\# &lt;weight&gt;
- Weight: O(1)
- Write: ForceEra
\# &lt;/weight&gt;
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Staking', 'force_new_era_always', {}
)
```

---------
### force_no_eras
Force there to be no new eras indefinitely.

The dispatch origin must be Root.

\# &lt;weight&gt;
- No arguments.
- Weight: O(1)
- Write: ForceEra
\# &lt;/weight&gt;
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Staking', 'force_no_eras', {}
)
```

---------
### force_unstake
Force a current staker to become completely unstaked, immediately.

The dispatch origin must be Root.

\# &lt;weight&gt;
O(S) where S is the number of slashing spans to be removed
Reads: Bonded, Slashing Spans, Account, Locks
Writes: Bonded, Slashing Spans (if S &gt; 0), Ledger, Payee, Validators, Nominators, Account, Locks
Writes Each: SpanSlash * S
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| stash | `T::AccountId` | 
| num_slashing_spans | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'force_unstake', {
    'num_slashing_spans': 'u32',
    'stash': 'AccountId',
}
)
```

---------
### increase_validator_count
Increments the ideal number of validators.

The dispatch origin must be Root.

\# &lt;weight&gt;
Same as [`set_validator_count`].
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| additional | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'increase_validator_count', {'additional': 'u32'}
)
```

---------
### nominate
Declare the desire to nominate `targets` for the origin controller.

Effects will be felt at the beginning of the next era. This can only be called when
[`EraElectionStatus`] is `Closed`.

The dispatch origin for this call must be _Signed_ by the controller, not the stash.
And, it can be only called when [`EraElectionStatus`] is `Closed`.

\# &lt;weight&gt;
- The transaction&\#x27;s complexity is proportional to the size of `targets` (N)
which is capped at CompactAssignments::LIMIT (MAX_NOMINATIONS).
- Both the reads and writes follow a similar pattern.
---------
Weight: O(N)
where N is the number of targets
DB Weight:
- Reads: Era Election Status, Ledger, Current Era
- Writes: Validators, Nominators
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| targets | `Vec<<T::Lookup as StaticLookup>::Source>` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'nominate', {
    'targets': [
        {
            'Address20': '[u8; 20]',
            'Address32': '[u8; 32]',
            'Id': 'AccountId',
            'Index': 'u32',
            'Raw': 'Bytes',
        },
    ],
}
)
```

---------
### payout_stakers
Pay out all the stakers behind a single validator for a single era.

- `validator_stash` is the stash account of the validator. Their nominators, up to
  `T::MaxNominatorRewardedPerValidator`, will also receive their rewards.
- `era` may be any era between `[current_era - history_depth; current_era]`.

The origin of this call must be _Signed_. Any account can call this function, even if
it is not one of the stakers.

This can only be called when [`EraElectionStatus`] is `Closed`.

\# &lt;weight&gt;
- Time complexity: at most O(MaxNominatorRewardedPerValidator).
- Contains a limited number of reads and writes.
-----------
N is the Number of payouts for the validator (including the validator)
Weight:
- Reward Destination Staked: O(N)
- Reward Destination Controller (Creating): O(N)
DB Weight:
- Read: EraElectionStatus, CurrentEra, HistoryDepth, ErasValidatorReward,
        ErasStakersClipped, ErasRewardPoints, ErasValidatorPrefs (8 items)
- Read Each: Bonded, Ledger, Payee, Locks, System Account (5 items)
- Write Each: System Account, Locks, Ledger (3 items)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| validator_stash | `T::AccountId` | 
| era | `EraIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'payout_stakers', {
    'era': 'u32',
    'validator_stash': 'AccountId',
}
)
```

---------
### payout_stakers_by_system
System version of `payout_stakers()`. Only be called by the root origin.
#### Attributes
| Name | Type |
| -------- | -------- | 
| validator_stash | `T::AccountId` | 
| era | `EraIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'payout_stakers_by_system', {
    'era': 'u32',
    'validator_stash': 'AccountId',
}
)
```

---------
### reap_stash
Remove all data structure concerning a staker/stash once its balance is at the minimum.
This is essentially equivalent to `withdraw_unbonded` except it can be called by anyone
and the target `stash` must have no funds left beyond the ED.

This can be called from any origin.

- `stash`: The stash account to reap. Its balance must be zero.

\# &lt;weight&gt;
Complexity: O(S) where S is the number of slashing spans on the account.
DB Weight:
- Reads: Stash Account, Bonded, Slashing Spans, Locks
- Writes: Bonded, Slashing Spans (if S &gt; 0), Ledger, Payee, Validators, Nominators, Stash Account, Locks
- Writes Each: SpanSlash * S
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| stash | `T::AccountId` | 
| num_slashing_spans | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'reap_stash', {
    'num_slashing_spans': 'u32',
    'stash': 'AccountId',
}
)
```

---------
### rebond
Rebond a portion of the stash scheduled to be unlocked.

The dispatch origin must be signed by the controller, and it can be only called when
[`EraElectionStatus`] is `Closed`.

\# &lt;weight&gt;
- Time complexity: O(L), where L is unlocking chunks
- Bounded by `MAX_UNLOCKING_CHUNKS`.
- Storage changes: Can&\#x27;t increase storage, only decrease it.
---------------
- DB Weight:
    - Reads: EraElectionStatus, Ledger, Locks, [Origin Account]
    - Writes: [Origin Account], Locks, Ledger
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'rebond', {'value': 'u128'}
)
```

---------
### remove_permissioned_validator
Remove an identity from the pool of (wannabe) validator identities. Effects are known in the next session.
Staking module checks `PermissionedIdentity` to ensure validators have
completed KYB compliance

\# Arguments
* origin Required origin for removing a potential validator.
* identity Validator&\#x27;s IdentityId.
#### Attributes
| Name | Type |
| -------- | -------- | 
| identity | `IdentityId` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'remove_permissioned_validator', {'identity': '[u8; 32]'}
)
```

---------
### scale_validator_count
Scale up the ideal number of validators by a factor.

The dispatch origin must be Root.

\# &lt;weight&gt;
Same as [`set_validator_count`].
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| factor | `Percent` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'scale_validator_count', {'factor': 'u8'}
)
```

---------
### set_commission_cap
Changes commission rate which applies to all validators. Only Governance
committee is allowed to change this value.

\# Arguments
* `new_cap` the new commission cap.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_cap | `Perbill` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'set_commission_cap', {'new_cap': 'u32'}
)
```

---------
### set_controller
(Re-)set the controller of a stash.

Effects will be felt at the beginning of the next era.

The dispatch origin for this call must be _Signed_ by the stash, not the controller.

\# &lt;weight&gt;
- Independent of the arguments. Insignificant complexity.
- Contains a limited number of reads.
- Writes are limited to the `origin` account key.
----------
Weight: O(1)
DB Weight:
- Read: Bonded, Ledger New Controller, Ledger Old Controller
- Write: Bonded, Ledger New Controller, Ledger Old Controller
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| controller | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'set_controller', {
    'controller': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
}
)
```

---------
### set_history_depth
Set `HistoryDepth` value. This function will delete any history information
when `HistoryDepth` is reduced.

Parameters:
- `new_history_depth`: The new history depth you would like to set.
- `era_items_deleted`: The number of items that will be deleted by this dispatch.
   This should report all the storage items that will be deleted by clearing old
   era history. Needed to report an accurate weight for the dispatch. Trusted by
   `Root` to report an accurate number.

Origin must be root.

\# &lt;weight&gt;
- E: Number of history depths removed, i.e. 10 -&gt; 7 = 3
- Weight: O(E)
- DB Weight:
    - Reads: Current Era, History Depth
    - Writes: History Depth
    - Clear Prefix Each: Era Stakers, EraStakersClipped, ErasValidatorPrefs
    - Writes Each: ErasValidatorReward, ErasRewardPoints, ErasTotalStake, ErasStartSessionIndex
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_history_depth | `EraIndex` | 
| _era_items_deleted | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'set_history_depth', {
    '_era_items_deleted': 'u32',
    'new_history_depth': 'u32',
}
)
```

---------
### set_invulnerables
Set the validators who cannot be slashed (if any).

The dispatch origin must be Root.

\# &lt;weight&gt;
- O(V)
- Write: Invulnerables
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| invulnerables | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'set_invulnerables', {'invulnerables': ['AccountId']}
)
```

---------
### set_min_bond_threshold
Changes min bond value to be used in validate(). Only Governance
committee is allowed to change this value.

\# Arguments
* `new_value` the new minimum
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'set_min_bond_threshold', {'new_value': 'u128'}
)
```

---------
### set_payee
(Re-)set the payment target for a controller.

Effects will be felt at the beginning of the next era.

The dispatch origin for this call must be _Signed_ by the controller, not the stash.

\# &lt;weight&gt;
- Independent of the arguments. Insignificant complexity.
- Contains a limited number of reads.
- Writes are limited to the `origin` account key.
---------
- Weight: O(1)
- DB Weight:
    - Read: Ledger
    - Write: Payee
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| payee | `RewardDestination<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'set_payee', {
    'payee': {
        'Account': 'AccountId',
        'Controller': None,
        'Staked': None,
        'Stash': None,
    },
}
)
```

---------
### set_validator_count
Sets the ideal number of validators.

The dispatch origin must be Root.

\# &lt;weight&gt;
Weight: O(1)
Write: Validator Count
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'set_validator_count', {'new': 'u32'}
)
```

---------
### submit_election_solution
Submit an election result to the chain. If the solution:

1. is valid.
2. has a better score than a potentially existing solution on chain.

then, it will be _put_ on chain.

A solution consists of two pieces of data:

1. `winners`: a flat vector of all the winners of the round.
2. `assignments`: the compact version of an assignment vector that encodes the edge
   weights.

Both of which may be computed using _phragmen_, or any other algorithm.

Additionally, the submitter must provide:

- The `score` that they claim their solution has.

Both validators and nominators will be represented by indices in the solution. The
indices should respect the corresponding types ([`ValidatorIndex`] and
[`NominatorIndex`]). Moreover, they should be valid when used to index into
[`SnapshotValidators`] and [`SnapshotNominators`]. Any invalid index will cause the
solution to be rejected. These two storage items are set during the election window and
may be used to determine the indices.

A solution is valid if:

0. It is submitted when [`EraElectionStatus`] is `Open`.
1. Its claimed score is equal to the score computed on-chain.
2. Presents the correct number of winners.
3. All indexes must be value according to the snapshot vectors. All edge values must
   also be correct and should not overflow the granularity of the ratio type (i.e. 256
   or billion).
4. For each edge, all targets are actually nominated by the voter.
5. Has correct self-votes.

A solutions score is consisted of 3 parameters:

1. `min { support.total }` for each support of a winner. This value should be maximized.
2. `sum { support.total }` for each support of a winner. This value should be minimized.
3. `sum { support.total^2 }` for each support of a winner. This value should be
   minimized (to ensure less variance)

\# &lt;weight&gt;
The transaction is assumed to be the longest path, a better solution.
  - Initial solution is almost the same.
  - Worse solution is retraced in pre-dispatch-checks which sets its own weight.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| winners | `Vec<ValidatorIndex>` | 
| compact | `CompactAssignments` | 
| score | `ElectionScore` | 
| era | `EraIndex` | 
| size | `ElectionSize` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'submit_election_solution', {
    'compact': {
        'votes1': [('u32', 'u16')],
        'votes10': [
            (
                'u32',
                "[('u16', 'u16'); 9]",
                'u16',
            ),
        ],
        'votes11': [
            (
                'u32',
                "[('u16', 'u16'); 10]",
                'u16',
            ),
        ],
        'votes12': [
            (
                'u32',
                "[('u16', 'u16'); 11]",
                'u16',
            ),
        ],
        'votes13': [
            (
                'u32',
                "[('u16', 'u16'); 12]",
                'u16',
            ),
        ],
        'votes14': [
            (
                'u32',
                "[('u16', 'u16'); 13]",
                'u16',
            ),
        ],
        'votes15': [
            (
                'u32',
                "[('u16', 'u16'); 14]",
                'u16',
            ),
        ],
        'votes16': [
            (
                'u32',
                "[('u16', 'u16'); 15]",
                'u16',
            ),
        ],
        'votes2': [
            ('u32', ('u16', 'u16'), 'u16'),
        ],
        'votes3': [
            (
                'u32',
                "[('u16', 'u16'); 2]",
                'u16',
            ),
        ],
        'votes4': [
            (
                'u32',
                "[('u16', 'u16'); 3]",
                'u16',
            ),
        ],
        'votes5': [
            (
                'u32',
                "[('u16', 'u16'); 4]",
                'u16',
            ),
        ],
        'votes6': [
            (
                'u32',
                "[('u16', 'u16'); 5]",
                'u16',
            ),
        ],
        'votes7': [
            (
                'u32',
                "[('u16', 'u16'); 6]",
                'u16',
            ),
        ],
        'votes8': [
            (
                'u32',
                "[('u16', 'u16'); 7]",
                'u16',
            ),
        ],
        'votes9': [
            (
                'u32',
                "[('u16', 'u16'); 8]",
                'u16',
            ),
        ],
    },
    'era': 'u32',
    'score': {
        'minimal_stake': 'u128',
        'sum_stake': 'u128',
        'sum_stake_squared': 'u128',
    },
    'size': {
        'nominators': 'u32',
        'validators': 'u16',
    },
    'winners': ['u16'],
}
)
```

---------
### submit_election_solution_unsigned
Unsigned version of `submit_election_solution`.

Note that this must pass the [`ValidateUnsigned`] check which only allows transactions
from the local node to be included. In other words, only the block author can include a
transaction in the block.

\# &lt;weight&gt;
See [`submit_election_solution`].
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| winners | `Vec<ValidatorIndex>` | 
| compact | `CompactAssignments` | 
| score | `ElectionScore` | 
| era | `EraIndex` | 
| size | `ElectionSize` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'submit_election_solution_unsigned', {
    'compact': {
        'votes1': [('u32', 'u16')],
        'votes10': [
            (
                'u32',
                "[('u16', 'u16'); 9]",
                'u16',
            ),
        ],
        'votes11': [
            (
                'u32',
                "[('u16', 'u16'); 10]",
                'u16',
            ),
        ],
        'votes12': [
            (
                'u32',
                "[('u16', 'u16'); 11]",
                'u16',
            ),
        ],
        'votes13': [
            (
                'u32',
                "[('u16', 'u16'); 12]",
                'u16',
            ),
        ],
        'votes14': [
            (
                'u32',
                "[('u16', 'u16'); 13]",
                'u16',
            ),
        ],
        'votes15': [
            (
                'u32',
                "[('u16', 'u16'); 14]",
                'u16',
            ),
        ],
        'votes16': [
            (
                'u32',
                "[('u16', 'u16'); 15]",
                'u16',
            ),
        ],
        'votes2': [
            ('u32', ('u16', 'u16'), 'u16'),
        ],
        'votes3': [
            (
                'u32',
                "[('u16', 'u16'); 2]",
                'u16',
            ),
        ],
        'votes4': [
            (
                'u32',
                "[('u16', 'u16'); 3]",
                'u16',
            ),
        ],
        'votes5': [
            (
                'u32',
                "[('u16', 'u16'); 4]",
                'u16',
            ),
        ],
        'votes6': [
            (
                'u32',
                "[('u16', 'u16'); 5]",
                'u16',
            ),
        ],
        'votes7': [
            (
                'u32',
                "[('u16', 'u16'); 6]",
                'u16',
            ),
        ],
        'votes8': [
            (
                'u32',
                "[('u16', 'u16'); 7]",
                'u16',
            ),
        ],
        'votes9': [
            (
                'u32',
                "[('u16', 'u16'); 8]",
                'u16',
            ),
        ],
    },
    'era': 'u32',
    'score': {
        'minimal_stake': 'u128',
        'sum_stake': 'u128',
        'sum_stake_squared': 'u128',
    },
    'size': {
        'nominators': 'u32',
        'validators': 'u16',
    },
    'winners': ['u16'],
}
)
```

---------
### unbond
Schedule a portion of the stash to be unlocked ready for transfer out after the bond
period ends. If this leaves an amount actively bonded less than
T::Currency::minimum_balance(), then it is increased to the full amount.

Once the unlock period is done, you can call `withdraw_unbonded` to actually move
the funds out of management ready for transfer.

No more than a limited number of unlocking chunks (see `MAX_UNLOCKING_CHUNKS`)
can co-exists at the same time. In that case, [`Call::withdraw_unbonded`] need
to be called first to remove some of the chunks (if possible).

The dispatch origin for this call must be _Signed_ by the controller, not the stash.
And, it can be only called when [`EraElectionStatus`] is `Closed`.

Emits `Unbonded`.

See also [`Call::withdraw_unbonded`].

\# &lt;weight&gt;
- Independent of the arguments. Limited but potentially exploitable complexity.
- Contains a limited number of reads.
- Each call (requires the remainder of the bonded balance to be above `minimum_balance`)
  will cause a new entry to be inserted into a vector (`Ledger.unlocking`) kept in storage.
  The only way to clean the aforementioned storage item is also user-controlled via
  `withdraw_unbonded`.
- One DB entry.
----------
Weight: O(1)
DB Weight:
- Read: EraElectionStatus, Ledger, CurrentEra, Locks, \[Origin Account\]
- Write: Locks, Ledger, \[Origin Account\]
&lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'unbond', {'value': 'u128'}
)
```

---------
### update_permissioned_validator_intended_count
Update the intended validator count for a given DID.

\# Arguments
* origin which must be the required origin for adding a potential validator.
* identity to add as a validator.
* new_intended_count New value of intended count.
#### Attributes
| Name | Type |
| -------- | -------- | 
| identity | `IdentityId` | 
| new_intended_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'update_permissioned_validator_intended_count', {
    'identity': '[u8; 32]',
    'new_intended_count': 'u32',
}
)
```

---------
### validate
Declare the desire to validate for the origin controller.

Effects will be felt at the beginning of the next era.

The dispatch origin for this call must be _Signed_ by the controller, not the stash.
And, it can be only called when [`EraElectionStatus`] is `Closed`.

\# &lt;weight&gt;
- Independent of the arguments. Insignificant complexity.
- Contains a limited number of reads.
- Writes are limited to the `origin` account key.
-----------
Weight: O(1)
DB Weight:
- Read: Era Election Status, Ledger
- Write: Nominators, Validators
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| prefs | `ValidatorPrefs` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'validate', {
    'prefs': {
        'blocked': 'bool',
        'commission': 'u32',
    },
}
)
```

---------
### validate_cdd_expiry_nominators
Validate the nominators CDD expiry time.

If an account from a given set of address is nominating then
check the CDD expiry time of it and if it is expired
then the account should be unbonded and removed from the nominating process.

\#&lt;weight&gt;
- Depends on passed list of AccountId.
- Depends on the no. of claim issuers an accountId has for the CDD expiry.
\#&lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| targets | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'validate_cdd_expiry_nominators', {'targets': ['AccountId']}
)
```

---------
### withdraw_unbonded
Remove any unlocked chunks from the `unlocking` queue from our management.

This essentially frees up that balance to be used by the stash account to do
whatever it wants.

The dispatch origin for this call must be _Signed_ by the controller, not the stash.
And, it can be only called when [`EraElectionStatus`] is `Closed`.

Emits `Withdrawn`.

See also [`Call::unbond`].

\# &lt;weight&gt;
- Could be dependent on the `origin` argument and how much `unlocking` chunks exist.
 It implies `consolidate_unlocked` which loops over `Ledger.unlocking`, which is
 indirectly user-controlled. See [`unbond`] for more detail.
- Contains a limited number of reads, yet the size of which could be large based on `ledger`.
- Writes are limited to the `origin` account key.
---------------
Complexity O(S) where S is the number of slashing spans to remove
Update:
- Reads: EraElectionStatus, Ledger, Current Era, Locks, [Origin Account]
- Writes: [Origin Account], Locks, Ledger
Kill:
- Reads: EraElectionStatus, Ledger, Current Era, Bonded, Slashing Spans, [Origin
  Account], Locks
- Writes: Bonded, Slashing Spans (if S &gt; 0), Ledger, Payee, Validators, Nominators,
  [Origin Account], Locks
- Writes Each: SpanSlash * S
NOTE: Weight annotation is the kill scenario, we refund otherwise.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| num_slashing_spans | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'withdraw_unbonded', {'num_slashing_spans': 'u32'}
)
```

---------
## Events

---------
### Bonded
An account has bonded this amount. \[did, stash, amount\]

NOTE: This event is only emitted when funds are bonded via a dispatchable. Notably,
it will not be emitted for staking rewards when they are added to stake.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### CommissionCapUpdated
When commission cap get updated.
(old value, new value)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Perbill` | ```u32```
| None | `Perbill` | ```u32```

---------
### EraPayout
The era payout has been set; the first balance is the validator-payout; the second is
the remainder from the maximum amount of reward.
\[era_index, validator_payout, remainder\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EraIndex` | ```u32```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
### InvalidatedNominators
Remove the nominators from the valid nominators when there CDD expired.
Caller, Stash accountId of nominators
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `Vec<AccountId>` | ```['AccountId']```

---------
### MinimumBondThresholdUpdated
Min bond threshold was updated (new value).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Option<IdentityId>` | ```(None, '[u8; 32]')```
| None | `Balance` | ```u128```

---------
### Nominated
User has updated their nominations
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `Vec<AccountId>` | ```['AccountId']```

---------
### OldSlashingReportDiscarded
An old slashing report from a prior era was discarded because it could
not be processed. \[session_index\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `SessionIndex` | ```u32```

---------
### PermissionedIdentityAdded
An DID has issued a candidacy. See the transaction for who.
GC identity , Validator&\#x27;s identity.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `IdentityId` | ```[u8; 32]```

---------
### PermissionedIdentityRemoved
The given member was removed. See the transaction for who.
GC identity , Validator&\#x27;s identity.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `IdentityId` | ```[u8; 32]```

---------
### Reward
The staker has been rewarded by this amount. \[stash_identity, stash, amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### RewardPaymentSchedulingInterrupted
When scheduling of reward payments get interrupted.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId` | ```AccountId```
| None | `EraIndex` | ```u32```
| None | `DispatchError` | ```{'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}```

---------
### Slash
One validator (and its nominators) has been slashed by the given amount.
\[validator, amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### SlashingAllowedForChanged
Update for whom balance get slashed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `SlashingSwitch` | ```('Validator', 'ValidatorAndNominator', 'None')```

---------
### SolutionStored
A new solution for the upcoming election has been stored. \[compute\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ElectionCompute` | ```('OnChain', 'Signed', 'Unsigned')```

---------
### StakingElection
A new set of stakers was elected with the given \[compute\].
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ElectionCompute` | ```('OnChain', 'Signed', 'Unsigned')```

---------
### Unbonded
An account has unbonded this amount. \[did, stash, amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### Withdrawn
An account has called `withdraw_unbonded` and removed unbonding chunks worth `Balance`
from the unlocking queue. \[stash, amount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
## Storage functions

---------
### ActiveEra
 The active era information, it holds index and start.

 The active era is the era being currently rewarded. Validator set of this era must be
 equal to [`SessionInterface::validators`].

#### Python
```python
result = substrate.query(
    'Staking', 'ActiveEra', []
)
```

#### Return value
```python
{'index': 'u32', 'start': (None, 'u64')}
```
---------
### Bonded
 Map from all locked &quot;stash&quot; accounts to the controller account.

#### Python
```python
result = substrate.query(
    'Staking', 'Bonded', ['AccountId']
)
```

#### Return value
```python
'AccountId'
```
---------
### BondedEras
 A mapping from still-bonded eras to the first session index of that era.

 Must contains information for eras for the range:
 `[active_era - bounding_duration; active_era]`

#### Python
```python
result = substrate.query(
    'Staking', 'BondedEras', []
)
```

#### Return value
```python
[('u32', 'u32')]
```
---------
### CanceledSlashPayout
 The amount of currency given to reporters of a slash event which was
 canceled by extraordinary circumstances (e.g. governance).

#### Python
```python
result = substrate.query(
    'Staking', 'CanceledSlashPayout', []
)
```

#### Return value
```python
'u128'
```
---------
### CurrentEra
 The current era index.

 This is the latest planned era, depending on how the Session pallet queues the validator
 set, it might be active or not.

#### Python
```python
result = substrate.query(
    'Staking', 'CurrentEra', []
)
```

#### Return value
```python
'u32'
```
---------
### EarliestUnappliedSlash
 The earliest era for which we have a pending, unapplied slash.

#### Python
```python
result = substrate.query(
    'Staking', 'EarliestUnappliedSlash', []
)
```

#### Return value
```python
'u32'
```
---------
### EraElectionStatus
 Flag to control the execution of the offchain election. When `Open(_)`, we accept
 solutions to be submitted.

#### Python
```python
result = substrate.query(
    'Staking', 'EraElectionStatus', []
)
```

#### Return value
```python
{'Closed': None, 'Open': 'u32'}
```
---------
### ErasRewardPoints
 Rewards for the last `HISTORY_DEPTH` eras.
 If reward hasn&#x27;t been set or has been removed then 0 reward is returned.

#### Python
```python
result = substrate.query(
    'Staking', 'ErasRewardPoints', ['u32']
)
```

#### Return value
```python
{'individual': 'scale_info::561', 'total': 'u32'}
```
---------
### ErasStakers
 Exposure of validator at era.

 This is keyed first by the era index to allow bulk deletion and then the stash account.

 Is it removed after `HISTORY_DEPTH` eras.
 If stakers hasn&#x27;t been set or has been removed then empty exposure is returned.

#### Python
```python
result = substrate.query(
    'Staking', 'ErasStakers', ['u32', 'AccountId']
)
```

#### Return value
```python
{'others': [{'value': 'u128', 'who': 'AccountId'}], 'own': 'u128', 'total': 'u128'}
```
---------
### ErasStakersClipped
 Clipped Exposure of validator at era.

 This is similar to [`ErasStakers`] but number of nominators exposed is reduced to the
 `T::MaxNominatorRewardedPerValidator` biggest stakers.
 (Note: the field `total` and `own` of the exposure remains unchanged).
 This is used to limit the i/o cost for the nominator payout.

 This is keyed fist by the era index to allow bulk deletion and then the stash account.

 Is it removed after `HISTORY_DEPTH` eras.
 If stakers hasn&#x27;t been set or has been removed then empty exposure is returned.

#### Python
```python
result = substrate.query(
    'Staking', 'ErasStakersClipped', ['u32', 'AccountId']
)
```

#### Return value
```python
{'others': [{'value': 'u128', 'who': 'AccountId'}], 'own': 'u128', 'total': 'u128'}
```
---------
### ErasStartSessionIndex
 The session index at which the era start for the last `HISTORY_DEPTH` eras.

 Note: This tracks the starting session (i.e. session index when era start being active)
 for the eras in `[CurrentEra - HISTORY_DEPTH, CurrentEra]`.

#### Python
```python
result = substrate.query(
    'Staking', 'ErasStartSessionIndex', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### ErasTotalStake
 The total amount staked for the last `HISTORY_DEPTH` eras.
 If total hasn&#x27;t been set or has been removed then 0 stake is returned.

#### Python
```python
result = substrate.query(
    'Staking', 'ErasTotalStake', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### ErasValidatorPrefs
 Similar to `ErasStakers`, this holds the preferences of validators.

 This is keyed first by the era index to allow bulk deletion and then the stash account.

 Is it removed after `HISTORY_DEPTH` eras.

#### Python
```python
result = substrate.query(
    'Staking', 'ErasValidatorPrefs', ['u32', 'AccountId']
)
```

#### Return value
```python
{'blocked': 'bool', 'commission': 'u32'}
```
---------
### ErasValidatorReward
 The total validator era payout for the last `HISTORY_DEPTH` eras.

 Eras that haven&#x27;t finished yet or has been removed doesn&#x27;t have reward.

#### Python
```python
result = substrate.query(
    'Staking', 'ErasValidatorReward', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### ForceEra
 Mode of era forcing.

#### Python
```python
result = substrate.query(
    'Staking', 'ForceEra', []
)
```

#### Return value
```python
('NotForcing', 'ForceNew', 'ForceNone', 'ForceAlways')
```
---------
### HistoryDepth
 Number of eras to keep in history.

 Information is kept for eras in `[current_era - history_depth; current_era]`.

 Must be more than the number of eras delayed by session otherwise. I.e. active era must
 always be in history. I.e. `active_era &gt; current_era - history_depth` must be
 guaranteed.

#### Python
```python
result = substrate.query(
    'Staking', 'HistoryDepth', []
)
```

#### Return value
```python
'u32'
```
---------
### Invulnerables
 Any validators that may never be slashed or forcibly kicked. It&#x27;s a Vec since they&#x27;re
 easy to initialize and the performance hit is minimal (we expect no more than four
 invulnerables) and restricted to testnets.

#### Python
```python
result = substrate.query(
    'Staking', 'Invulnerables', []
)
```

#### Return value
```python
['AccountId']
```
---------
### IsCurrentSessionFinal
 True if the current **planned** session is final. Note that this does not take era
 forcing into account.

#### Python
```python
result = substrate.query(
    'Staking', 'IsCurrentSessionFinal', []
)
```

#### Return value
```python
'bool'
```
---------
### Ledger
 Map from all (unlocked) &quot;controller&quot; accounts to the info regarding the staking.

#### Python
```python
result = substrate.query(
    'Staking', 'Ledger', ['AccountId']
)
```

#### Return value
```python
{
    'active': 'u128',
    'claimed_rewards': ['u32'],
    'stash': 'AccountId',
    'total': 'u128',
    'unlocking': [{'era': 'u32', 'value': 'u128'}],
}
```
---------
### MinimumBondThreshold
 The minimum amount with which a validator can bond.

#### Python
```python
result = substrate.query(
    'Staking', 'MinimumBondThreshold', []
)
```

#### Return value
```python
'u128'
```
---------
### MinimumValidatorCount
 Minimum number of staking participants before emergency conditions are imposed.

#### Python
```python
result = substrate.query(
    'Staking', 'MinimumValidatorCount', []
)
```

#### Return value
```python
'u32'
```
---------
### NominatorSlashInEra
 All slashing events on nominators, mapped by era to the highest slash value of the era.

#### Python
```python
result = substrate.query(
    'Staking', 'NominatorSlashInEra', ['u32', 'AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### Nominators
 The map from nominator stash key to the set of stash keys of all validators to nominate.

#### Python
```python
result = substrate.query(
    'Staking', 'Nominators', ['AccountId']
)
```

#### Return value
```python
{'submitted_in': 'u32', 'suppressed': 'bool', 'targets': ['AccountId']}
```
---------
### OffendingValidators
 Indices of validators that have offended in the active era and whether they are currently
 disabled.

 This value should be a superset of disabled validators since not all offences lead to the
 validator being disabled (if there was no slash). This is needed to track the percentage of
 validators that have offended in the current era, ensuring a new era is forced if
 `OffendingValidatorsThreshold` is reached. The vec is always kept sorted so that we can find
 whether a given validator has previously offended using binary search. It gets cleared when
 the era ends.

#### Python
```python
result = substrate.query(
    'Staking', 'OffendingValidators', []
)
```

#### Return value
```python
[('u32', 'bool')]
```
---------
### Payee
 Where the reward payment should be made. Keyed by stash.

#### Python
```python
result = substrate.query(
    'Staking', 'Payee', ['AccountId']
)
```

#### Return value
```python
{'Account': 'AccountId', 'Controller': None, 'Staked': None, 'Stash': None}
```
---------
### PermissionedIdentity
 Entities that are allowed to run operator/validator nodes.

#### Python
```python
result = substrate.query(
    'Staking', 'PermissionedIdentity', ['[u8; 32]']
)
```

#### Return value
```python
{'intended_count': 'u32', 'running_count': 'u32'}
```
---------
### PolymeshStorageVersion
 Polymesh Storage version.

#### Python
```python
result = substrate.query(
    'Staking', 'PolymeshStorageVersion', []
)
```

#### Return value
```python
'u8'
```
---------
### QueuedElected
 The next validator set. At the end of an era, if this is available (potentially from the
 result of an offchain worker), it is immediately used. Otherwise, the on-chain election
 is executed.

#### Python
```python
result = substrate.query(
    'Staking', 'QueuedElected', []
)
```

#### Return value
```python
{
    'compute': ('OnChain', 'Signed', 'Unsigned'),
    'elected_stashes': ['AccountId'],
    'exposures': [
        (
            'AccountId',
            {'others': ['scale_info::118'], 'own': 'u128', 'total': 'u128'},
        ),
    ],
}
```
---------
### QueuedScore
 The score of the current [`QueuedElected`].

#### Python
```python
result = substrate.query(
    'Staking', 'QueuedScore', []
)
```

#### Return value
```python
{'minimal_stake': 'u128', 'sum_stake': 'u128', 'sum_stake_squared': 'u128'}
```
---------
### SlashRewardFraction
 The percentage of the slash that is distributed to reporters.

 The rest of the slashed value is handled by the `Slash`.

#### Python
```python
result = substrate.query(
    'Staking', 'SlashRewardFraction', []
)
```

#### Return value
```python
'u32'
```
---------
### SlashingAllowedFor

#### Python
```python
result = substrate.query(
    'Staking', 'SlashingAllowedFor', []
)
```

#### Return value
```python
('Validator', 'ValidatorAndNominator', 'None')
```
---------
### SlashingSpans
 Slashing spans for stash accounts.

#### Python
```python
result = substrate.query(
    'Staking', 'SlashingSpans', ['AccountId']
)
```

#### Return value
```python
{
    'last_nonzero_slash': 'u32',
    'last_start': 'u32',
    'prior': ['u32'],
    'span_index': 'u32',
}
```
---------
### SnapshotNominators
 Snapshot of nominators at the beginning of the current election window. This should only
 have a value when [`EraElectionStatus`] == `ElectionStatus::Open(_)`.

#### Python
```python
result = substrate.query(
    'Staking', 'SnapshotNominators', []
)
```

#### Return value
```python
['AccountId']
```
---------
### SnapshotValidators
 Snapshot of validators at the beginning of the current election window. This should only
 have a value when [`EraElectionStatus`] == `ElectionStatus::Open(_)`.

#### Python
```python
result = substrate.query(
    'Staking', 'SnapshotValidators', []
)
```

#### Return value
```python
['AccountId']
```
---------
### SpanSlash
 Records information about the maximum slash of a stash within a slashing span,
 as well as how much reward has been paid out.

#### Python
```python
result = substrate.query(
    'Staking', 'SpanSlash', [('AccountId', 'u32')]
)
```

#### Return value
```python
{'paid_out': 'u128', 'slashed': 'u128'}
```
---------
### StorageVersion
 True if network has been upgraded to this version.
 Storage version of the pallet.

 This is set to v6.0.1 for new networks.

#### Python
```python
result = substrate.query(
    'Staking', 'StorageVersion', []
)
```

#### Return value
```python
(
    'V1_0_0Ancient',
    'V2_0_0',
    'V3_0_0',
    'V4_0_0',
    'V5_0_0',
    'V6_0_0',
    'V6_0_1',
    'V7_0_0',
)
```
---------
### UnappliedSlashes
 All unapplied slashes that are queued for later.

#### Python
```python
result = substrate.query(
    'Staking', 'UnappliedSlashes', ['u32']
)
```

#### Return value
```python
[
    {
        'others': [('AccountId', 'u128')],
        'own': 'u128',
        'payout': 'u128',
        'reporters': ['AccountId'],
        'validator': 'AccountId',
    },
]
```
---------
### ValidatorCommissionCap
 Every validator has commission that should be in the range [0, Cap].

#### Python
```python
result = substrate.query(
    'Staking', 'ValidatorCommissionCap', []
)
```

#### Return value
```python
'u32'
```
---------
### ValidatorCount
 The ideal number of staking participants.

#### Python
```python
result = substrate.query(
    'Staking', 'ValidatorCount', []
)
```

#### Return value
```python
'u32'
```
---------
### ValidatorSlashInEra
 All slashing events on validators, mapped by era to the highest slash proportion
 and slash value of the era.

#### Python
```python
result = substrate.query(
    'Staking', 'ValidatorSlashInEra', ['u32', 'AccountId']
)
```

#### Return value
```python
('u32', 'u128')
```
---------
### Validators
 The map from (wannabe) validator stash key to the preferences of that validator.

#### Python
```python
result = substrate.query(
    'Staking', 'Validators', ['AccountId']
)
```

#### Return value
```python
{'blocked': 'bool', 'commission': 'u32'}
```
---------
## Constants

---------
### BondingDuration
 Number of eras that staked funds must remain bonded for.
#### Value
```python
28
```
#### Python
```python
constant = substrate.get_constant('Staking', 'BondingDuration')
```
---------
### ElectionLookahead
 The number of blocks before the end of the era from which election submissions are allowed.

 Setting this to zero will disable the offchain compute and only on-chain seq-phragmen will
 be used.

 This is bounded by being within the last session. Hence, setting it to a value more than the
 length of a session will be pointless.
#### Value
```python
600
```
#### Python
```python
constant = substrate.get_constant('Staking', 'ElectionLookahead')
```
---------
### FixedYearlyReward
 Total year rewards that gets paid during fixed reward schedule.
#### Value
```python
140000000000000
```
#### Python
```python
constant = substrate.get_constant('Staking', 'FixedYearlyReward')
```
---------
### MaxIterations
 Maximum number of balancing iterations to run in the offchain submission.

 If set to 0, balance_solution will not be executed at all.
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Staking', 'MaxIterations')
```
---------
### MaxNominatorRewardedPerValidator
 The maximum number of nominators rewarded for each validator.

 For each validator only the `$MaxNominatorRewardedPerValidator` biggest stakers can claim
 their reward. This used to limit the i/o cost for the nominator payout.
#### Value
```python
2048
```
#### Python
```python
constant = substrate.get_constant('Staking', 'MaxNominatorRewardedPerValidator')
```
---------
### MaxValidatorPerIdentity
 Maximum number of validators for each permissioned identity.

 Max number of validators count = `MaxValidatorPerIdentity * Self::validator_count()`.
#### Value
```python
330000
```
#### Python
```python
constant = substrate.get_constant('Staking', 'MaxValidatorPerIdentity')
```
---------
### MaxVariableInflationTotalIssuance
 Maximum amount of `T::currency::total_issuance()` after that non-inflated rewards get paid.
#### Value
```python
1000000000000000
```
#### Python
```python
constant = substrate.get_constant('Staking', 'MaxVariableInflationTotalIssuance')
```
---------
### MinSolutionScoreBump
 The threshold of improvement that should be provided for a new solution to be accepted.
#### Value
```python
500000
```
#### Python
```python
constant = substrate.get_constant('Staking', 'MinSolutionScoreBump')
```
---------
### MinimumBond
 Minimum amount of POLYX that must be bonded for a new bond.
#### Value
```python
1000000
```
#### Python
```python
constant = substrate.get_constant('Staking', 'MinimumBond')
```
---------
### SessionsPerEra
 Number of sessions per era.
#### Value
```python
6
```
#### Python
```python
constant = substrate.get_constant('Staking', 'SessionsPerEra')
```
---------
### SlashDeferDuration
 Number of eras that slashes are deferred by, after computation.

 This should be less than the bonding duration.
 Set to 0 if slashes should be applied immediately, without opportunity for
 intervention.
#### Value
```python
14
```
#### Python
```python
constant = substrate.get_constant('Staking', 'SlashDeferDuration')
```
---------
## Errors

---------
### AlreadyBonded
Stash is already bonded.

---------
### AlreadyClaimed
Rewards for this era have already been claimed for this validator.

---------
### AlreadyExists
Permissioned validator already exists.

---------
### AlreadyPaired
Controller is already paired.

---------
### BadState
Internal state has become somehow corrupted and the operation cannot continue.

---------
### BadTarget
A nomination target was supplied that was blocked or otherwise not a validator.

---------
### BondTooSmall
When the amount to be bonded is less than `MinimumBond`

---------
### CallNotAllowed
The call is not allowed at the given time due to restrictions of election period.

---------
### EmptyTargets
Targets cannot be empty.

---------
### FundedTarget
Attempting to target a stash that still has funds.

---------
### HitIntendedValidatorCount
Running validator count hit the intended count.

---------
### IncorrectSlashingSpans
Incorrect number of slashing spans provided.

---------
### InsufficientValue
Can not bond with value less than minimum balance.

---------
### IntendedCountIsExceedingConsensusLimit
When the intended number of validators to run is &gt;= 2/3 of `validator_count`.

---------
### InvalidEraToReward
Invalid era to reward.

---------
### InvalidSlashIndex
Slash record index out of bounds.

---------
### InvalidValidatorCommission
Validator prefs are not in valid range.

---------
### InvalidValidatorIdentity
Given potential validator identity is invalid.

---------
### InvalidValidatorUnbondAmount
Validator should have minimum 50k POLYX bonded.

---------
### NoChange
Updates with same value.

---------
### NoMoreChunks
Can not schedule more unlock chunks.

---------
### NoUnlockChunk
Can not rebond without unlocking chunks.

---------
### NotController
Not a controller account.

---------
### NotExists
Permissioned validator not exists.

---------
### NotSortedAndUnique
Items are not sorted and unique.

---------
### NotStash
Not a stash account.

---------
### OffchainElectionBogusCompact
Error while building the assignment type from the compact. This can happen if an index
is invalid, or if the weights _overflow_.

---------
### OffchainElectionBogusEdge
The submitted result has unknown edges that are not among the presented winners.

---------
### OffchainElectionBogusElectionSize
The election size is invalid.

---------
### OffchainElectionBogusNomination
One of the submitted nominators has an edge to which they have not voted on chain.

---------
### OffchainElectionBogusNominator
One of the submitted nominators is not an active nominator on chain.

---------
### OffchainElectionBogusScore
The claimed score does not match with the one computed from the data.

---------
### OffchainElectionBogusSelfVote
A self vote must only be originated from a validator to ONLY themselves.

---------
### OffchainElectionBogusWinner
One of the submitted winners is not an active candidate on chain (index is out of range
in snapshot).

---------
### OffchainElectionBogusWinnerCount
Incorrect number of winners were presented.

---------
### OffchainElectionEarlySubmission
The submitted result is received out of the open window.

---------
### OffchainElectionSlashedNomination
One of the submitted nominators has an edge which is submitted before the last non-zero
slash of the target.

---------
### OffchainElectionWeakSubmission
The submitted result is not as good as the one stored on chain.

---------
### SnapshotUnavailable
The snapshot data of the current window is missing.

---------
### StashIdentityDoesNotExist
Validator or nominator stash identity does not exist.

---------
### StashIdentityNotCDDed
Nominator stash was not CDDed.

---------
### StashIdentityNotPermissioned
Validator stash identity was not permissioned.

---------
### TooManyTargets
Too many nomination targets supplied.

---------