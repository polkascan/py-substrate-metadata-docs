
# Staking

---------
## Calls

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
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| controller | `AccountIdLookupOf<T>` | 
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
        'Index': (),
        'Raw': 'Bytes',
    },
    'payee': {
        'Account': 'AccountId',
        'Controller': None,
        'None': None,
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

The dispatch origin for this call must be _Signed_ by the stash, not the controller.

Use this if there are additional funds in your stash account that you wish to bond.
Unlike [`bond`](Self::bond) or [`unbond`](Self::unbond) this function does not impose
any limitation on the amount that can be added.

Emits `Bonded`.

\# &lt;weight&gt;
- Independent of the arguments. Insignificant complexity.
- O(1).
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
### chill
Declare no desire to either validate or nominate.

Effects will be felt at the beginning of the next era.

The dispatch origin for this call must be _Signed_ by the controller, not the stash.

\# &lt;weight&gt;
- Independent of the arguments. Insignificant complexity.
- Contains one read.
- Writes are limited to the `origin` account key.
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
### chill_other
Declare a `controller` to stop participating as either a validator or nominator.

Effects will be felt at the beginning of the next era.

The dispatch origin for this call must be _Signed_, but can be called by anyone.

If the caller is the same as the controller being targeted, then no further checks are
enforced, and this function behaves just like `chill`.

If the caller is different than the controller being targeted, the following conditions
must be met:

* `controller` must belong to a nominator who has become non-decodable,

Or:

* A `ChillThreshold` must be set and checked which defines how close to the max
  nominators or validators we must reach before users can start chilling one-another.
* A `MaxNominatorCount` and `MaxValidatorCount` must be set which is used to determine
  how close we are to the threshold.
* A `MinNominatorBond` and `MinValidatorBond` must be set and checked, which determines
  if this is a person that should be chilled because they have not met the threshold
  bond required.

This can be helpful if bond requirements are updated, and we need to remove old users
who do not satisfy these requirements.
#### Attributes
| Name | Type |
| -------- | -------- | 
| controller | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'chill_other', {'controller': 'AccountId'}
)
```

---------
### force_apply_min_commission
Force a validator to have at least the minimum commission. This will not affect a
validator who already has a commission greater than or equal to the minimum. Any account
can call this.
#### Attributes
| Name | Type |
| -------- | -------- | 
| validator_stash | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'force_apply_min_commission', {'validator_stash': 'AccountId'}
)
```

---------
### force_new_era
Force there to be a new era at the end of the next session. After this, it will be
reset to normal (non-forced) behaviour.

The dispatch origin must be Root.

\# Warning

The election process starts multiple blocks before the end of the era.
If this is called just before a new era is triggered, the election process may not
have enough blocks to get a result.

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

\# Warning

The election process starts multiple blocks before the end of the era.
If this is called just before a new era is triggered, the election process may not
have enough blocks to get a result.
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

\# Warning

The election process starts multiple blocks before the end of the era.
Thus the election process may be ongoing when this is called. In this case the
election will continue until the next era is triggered.

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
Increments the ideal number of validators upto maximum of
`ElectionProviderBase::MaxWinners`.

The dispatch origin must be Root.

\# &lt;weight&gt;
Same as [`Self::set_validator_count`].
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
### kick
Remove the given nominations from the calling validator.

Effects will be felt at the beginning of the next era.

The dispatch origin for this call must be _Signed_ by the controller, not the stash.

- `who`: A list of nominator stash accounts who are nominating this validator which
  should no longer be nominating this validator.

Note: Making this call only makes sense if you first set the validator preferences to
block any further nominations.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `Vec<AccountIdLookupOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'kick', {
    'who': [
        {
            'Address20': '[u8; 20]',
            'Address32': '[u8; 32]',
            'Id': 'AccountId',
            'Index': (),
            'Raw': 'Bytes',
        },
    ],
}
)
```

---------
### nominate
Declare the desire to nominate `targets` for the origin controller.

Effects will be felt at the beginning of the next era.

The dispatch origin for this call must be _Signed_ by the controller, not the stash.

\# &lt;weight&gt;
- The transaction&\#x27;s complexity is proportional to the size of `targets` (N)
which is capped at CompactAssignments::LIMIT (T::MaxNominations).
- Both the reads and writes follow a similar pattern.
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| targets | `Vec<AccountIdLookupOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'nominate', {
    'targets': [
        {
            'Address20': '[u8; 20]',
            'Address32': '[u8; 32]',
            'Id': 'AccountId',
            'Index': (),
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

\# &lt;weight&gt;
- Time complexity: at most O(MaxNominatorRewardedPerValidator).
- Contains a limited number of reads and writes.
-----------
N is the Number of payouts for the validator (including the validator)
Weight:
- Reward Destination Staked: O(N)
- Reward Destination Controller (Creating): O(N)

  NOTE: weights are assuming that payouts are made to alive stash account (Staked).
  Paying even a dead controller is cheaper weight-wise. We don&\#x27;t do any refunds here.
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
### reap_stash
Remove all data structures concerning a staker/stash once it is at a state where it can
be considered `dust` in the staking system. The requirements are:

1. the `total_balance` of the stash is below existential deposit.
2. or, the `ledger.total` of the stash is below existential deposit.

The former can happen in cases like a slash; the latter when a fully unbonded account
is still receiving staking rewards in `RewardDestination::Staked`.

It can be called by anyone, as long as `stash` meets the above requirements.

Refunds the transaction fees upon successful execution.
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

The dispatch origin must be signed by the controller.

\# &lt;weight&gt;
- Time complexity: O(L), where L is unlocking chunks
- Bounded by `MaxUnlockingChunks`.
- Storage changes: Can&\#x27;t increase storage, only decrease it.
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
### scale_validator_count
Scale up the ideal number of validators by a factor upto maximum of
`ElectionProviderBase::MaxWinners`.

The dispatch origin must be Root.

\# &lt;weight&gt;
Same as [`Self::set_validator_count`].
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
### set_controller
(Re-)set the controller of a stash.

Effects will be felt instantly (as soon as this function is completed successfully).

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
| controller | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'set_controller', {
    'controller': {
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
### set_invulnerables
Set the validators who cannot be slashed (if any).

The dispatch origin must be Root.
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
### set_payee
(Re-)set the payment target for a controller.

Effects will be felt instantly (as soon as this function is completed successfully).

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
        'None': None,
        'Staked': None,
        'Stash': None,
    },
}
)
```

---------
### set_staking_configs
Update the various staking configurations .

* `min_nominator_bond`: The minimum active bond needed to be a nominator.
* `min_validator_bond`: The minimum active bond needed to be a validator.
* `max_nominator_count`: The max number of users who can be a nominator at once. When
  set to `None`, no limit is enforced.
* `max_validator_count`: The max number of users who can be a validator at once. When
  set to `None`, no limit is enforced.
* `chill_threshold`: The ratio of `max_nominator_count` or `max_validator_count` which
  should be filled in order for the `chill_other` transaction to work.
* `min_commission`: The minimum amount of commission that each validators must maintain.
  This is checked only upon calling `validate`. Existing validators are not affected.

RuntimeOrigin must be Root to call this function.

NOTE: Existing nominators and validators will not be affected by this update.
to kick people under the new limits, `chill_other` should be called.
#### Attributes
| Name | Type |
| -------- | -------- | 
| min_nominator_bond | `ConfigOp<BalanceOf<T>>` | 
| min_validator_bond | `ConfigOp<BalanceOf<T>>` | 
| max_nominator_count | `ConfigOp<u32>` | 
| max_validator_count | `ConfigOp<u32>` | 
| chill_threshold | `ConfigOp<Percent>` | 
| min_commission | `ConfigOp<Perbill>` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'set_staking_configs', {
    'chill_threshold': {
        'Noop': None,
        'Remove': None,
        'Set': 'u8',
    },
    'max_nominator_count': {
        'Noop': None,
        'Remove': None,
        'Set': 'u32',
    },
    'max_validator_count': {
        'Noop': None,
        'Remove': None,
        'Set': 'u32',
    },
    'min_commission': {
        'Noop': None,
        'Remove': None,
        'Set': 'u32',
    },
    'min_nominator_bond': {
        'Noop': None,
        'Remove': None,
        'Set': 'u128',
    },
    'min_validator_bond': {
        'Noop': None,
        'Remove': None,
        'Set': 'u128',
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
### unbond
Schedule a portion of the stash to be unlocked ready for transfer out after the bond
period ends. If this leaves an amount actively bonded less than
T::Currency::minimum_balance(), then it is increased to the full amount.

The dispatch origin for this call must be _Signed_ by the controller, not the stash.

Once the unlock period is done, you can call `withdraw_unbonded` to actually move
the funds out of management ready for transfer.

No more than a limited number of unlocking chunks (see `MaxUnlockingChunks`)
can co-exists at the same time. If there are no unlocking chunks slots available
[`Call::withdraw_unbonded`] is called to remove some of the chunks (if possible).

If a user encounters the `InsufficientBond` error when calling this extrinsic,
they should call `chill` first in order to free up their bonded funds.

Emits `Unbonded`.

See also [`Call::withdraw_unbonded`].
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
### validate
Declare the desire to validate for the origin controller.

Effects will be felt at the beginning of the next era.

The dispatch origin for this call must be _Signed_ by the controller, not the stash.
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
### withdraw_unbonded
Remove any unlocked chunks from the `unlocking` queue from our management.

This essentially frees up that balance to be used by the stash account to do
whatever it wants.

The dispatch origin for this call must be _Signed_ by the controller.

Emits `Withdrawn`.

See also [`Call::unbond`].

\# &lt;weight&gt;
Complexity O(S) where S is the number of slashing spans to remove
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
An account has bonded this amount. \[stash, amount\]

NOTE: This event is only emitted when funds are bonded via a dispatchable. Notably,
it will not be emitted for staking rewards when they are added to stake.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| stash | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### Chilled
An account has stopped participating as either a validator or nominator.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| stash | `T::AccountId` | ```AccountId```

---------
### EraPaid
The era payout has been set; the first balance is the validator-payout; the second is
the remainder from the maximum amount of reward.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| era_index | `EraIndex` | ```u32```
| validator_payout | `BalanceOf<T>` | ```u128```
| remainder | `BalanceOf<T>` | ```u128```

---------
### Kicked
A nominator has been kicked from a validator.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| nominator | `T::AccountId` | ```AccountId```
| stash | `T::AccountId` | ```AccountId```

---------
### OldSlashingReportDiscarded
An old slashing report from a prior era was discarded because it could
not be processed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| session_index | `SessionIndex` | ```u32```

---------
### PayoutStarted
The stakers&\#x27; rewards are getting paid.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| era_index | `EraIndex` | ```u32```
| validator_stash | `T::AccountId` | ```AccountId```

---------
### Rewarded
The nominator has been rewarded by this amount.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| stash | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### SlashReported
A slash for the given validator, for the given percentage of their stake, at the given
era as been reported.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| validator | `T::AccountId` | ```AccountId```
| fraction | `Perbill` | ```u32```
| slash_era | `EraIndex` | ```u32```

---------
### Slashed
A staker (validator or nominator) has been slashed by the given amount.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| staker | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### StakersElected
A new set of stakers was elected.
#### Attributes
No attributes

---------
### StakingElectionFailed
The election failed. No new era is planned.
#### Attributes
No attributes

---------
### Unbonded
An account has unbonded this amount.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| stash | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### ValidatorPrefsSet
A validator has set their preferences.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| stash | `T::AccountId` | ```AccountId```
| prefs | `ValidatorPrefs` | ```{'commission': 'u32', 'blocked': 'bool'}```

---------
### Withdrawn
An account has called `withdraw_unbonded` and removed unbonding chunks worth `Balance`
from the unlocking queue.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| stash | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

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
### ChillThreshold
 The threshold for when users can start calling `chill_other` for other validators /
 nominators. The threshold is compared to the actual number of validators / nominators
 (`CountFor*`) in the system compared to the configured max (`Max*Count`).

#### Python
```python
result = substrate.query(
    'Staking', 'ChillThreshold', []
)
```

#### Return value
```python
'u8'
```
---------
### CounterForNominators
Counter for the related counted storage map

#### Python
```python
result = substrate.query(
    'Staking', 'CounterForNominators', []
)
```

#### Return value
```python
'u32'
```
---------
### CounterForValidators
Counter for the related counted storage map

#### Python
```python
result = substrate.query(
    'Staking', 'CounterForValidators', []
)
```

#### Return value
```python
'u32'
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
### CurrentPlannedSession
 The last planned session scheduled by the session pallet.

 This is basically in sync with the call to [`pallet_session::SessionManager::new_session`].

#### Python
```python
result = substrate.query(
    'Staking', 'CurrentPlannedSession', []
)
```

#### Return value
```python
'u32'
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
{'individual': 'scale_info::495', 'total': 'u32'}
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
### MaxNominatorsCount
 The maximum nominator count before we stop allowing new validators to join.

 When this value is not set, no limits are enforced.

#### Python
```python
result = substrate.query(
    'Staking', 'MaxNominatorsCount', []
)
```

#### Return value
```python
'u32'
```
---------
### MaxValidatorsCount
 The maximum validator count before we stop allowing new validators to join.

 When this value is not set, no limits are enforced.

#### Python
```python
result = substrate.query(
    'Staking', 'MaxValidatorsCount', []
)
```

#### Return value
```python
'u32'
```
---------
### MinCommission
 The minimum amount of commission that validators can set.

 If set to `0`, no limit exists.

#### Python
```python
result = substrate.query(
    'Staking', 'MinCommission', []
)
```

#### Return value
```python
'u32'
```
---------
### MinNominatorBond
 The minimum active bond to become and maintain the role of a nominator.

#### Python
```python
result = substrate.query(
    'Staking', 'MinNominatorBond', []
)
```

#### Return value
```python
'u128'
```
---------
### MinValidatorBond
 The minimum active bond to become and maintain the role of a validator.

#### Python
```python
result = substrate.query(
    'Staking', 'MinValidatorBond', []
)
```

#### Return value
```python
'u128'
```
---------
### MinimumActiveStake
 The minimum active nominator stake of the last successful election.

#### Python
```python
result = substrate.query(
    'Staking', 'MinimumActiveStake', []
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
 The map from nominator stash key to their nomination preferences, namely the validators that
 they wish to support.

 Note that the keys of this storage map might become non-decodable in case the
 [`Config::MaxNominations`] configuration is decreased. In this rare case, these nominators
 are still existent in storage, their key is correct and retrievable (i.e. `contains_key`
 indicates that they exist), but their value cannot be decoded. Therefore, the non-decodable
 nominators will effectively not-exist, until they re-submit their preferences such that it
 is within the bounds of the newly set `Config::MaxNominations`.

 This implies that `::iter_keys().count()` and `::iter().count()` might return different
 values for this map. Moreover, the main `::count()` is aligned with the former, namely the
 number of keys that exist.

 Lastly, if any of the nominators become non-decodable, they can be chilled immediately via
 [`Call::chill_other`] dispatchable by anyone.

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
{
    'Account': 'AccountId',
    'Controller': None,
    'None': None,
    'Staked': None,
    'Stash': None,
}
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

 This is set to v7.0.0 for new networks.

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
    'V7_0_0',
    'V8_0_0',
    'V9_0_0',
    'V10_0_0',
    'V11_0_0',
    'V12_0_0',
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
### ValidatorCount
 The ideal number of active validators.

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
### HistoryDepth
 Number of eras to keep in history.

 Following information is kept for eras in `[current_era -
 HistoryDepth, current_era]`: `ErasStakers`, `ErasStakersClipped`,
 `ErasValidatorPrefs`, `ErasValidatorReward`, `ErasRewardPoints`,
 `ErasTotalStake`, `ErasStartSessionIndex`,
 `StakingLedger.claimed_rewards`.

 Must be more than the number of eras delayed by session.
 I.e. active era must always be in history. I.e. `active_era &gt;
 current_era - history_depth` must be guaranteed.

 If migrating an existing pallet from storage value to config value,
 this should be set to same value or greater as in storage.

 Note: `HistoryDepth` is used as the upper bound for the `BoundedVec`
 item `StakingLedger.claimed_rewards`. Setting this value lower than
 the existing value can lead to inconsistencies in the
 `StakingLedger` and will need to be handled properly in a migration.
 The test `reducing_history_depth_abrupt` shows this effect.
#### Value
```python
84
```
#### Python
```python
constant = substrate.get_constant('Staking', 'HistoryDepth')
```
---------
### MaxNominations
 Maximum number of nominations per nominator.
#### Value
```python
16
```
#### Python
```python
constant = substrate.get_constant('Staking', 'MaxNominations')
```
---------
### MaxNominatorRewardedPerValidator
 The maximum number of nominators rewarded for each validator.

 For each validator only the `$MaxNominatorRewardedPerValidator` biggest stakers can
 claim their reward. This used to limit the i/o cost for the nominator payout.
#### Value
```python
512
```
#### Python
```python
constant = substrate.get_constant('Staking', 'MaxNominatorRewardedPerValidator')
```
---------
### MaxUnlockingChunks
 The maximum number of `unlocking` chunks a [`StakingLedger`] can
 have. Effectively determines how many unique eras a staker may be
 unbonding in.

 Note: `MaxUnlockingChunks` is used as the upper bound for the
 `BoundedVec` item `StakingLedger.unlocking`. Setting this value
 lower than the existing value can lead to inconsistencies in the
 `StakingLedger` and will need to be handled properly in a runtime
 migration. The test `reducing_max_unlocking_chunks_abrupt` shows
 this effect.
#### Value
```python
32
```
#### Python
```python
constant = substrate.get_constant('Staking', 'MaxUnlockingChunks')
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

 This should be less than the bonding duration. Set to 0 if slashes
 should be applied immediately, without opportunity for intervention.
#### Value
```python
27
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
### AlreadyPaired
Controller is already paired.

---------
### BadState
Internal state has become somehow corrupted and the operation cannot continue.

---------
### BadTarget
A nomination target was supplied that was blocked or otherwise not a validator.

---------
### BoundNotMet
Some bound is not met.

---------
### CannotChillOther
The user has enough bond and thus cannot be chilled forcefully by an external person.

---------
### CommissionTooLow
Commission is too low. Must be at least `MinCommission`.

---------
### DuplicateIndex
Duplicate index.

---------
### EmptyTargets
Targets cannot be empty.

---------
### FundedTarget
Attempting to target a stash that still has funds.

---------
### IncorrectHistoryDepth
Incorrect previous history depth input provided.

---------
### IncorrectSlashingSpans
Incorrect number of slashing spans provided.

---------
### InsufficientBond
Cannot have a validator or nominator role, with value less than the minimum defined by
governance (see `MinValidatorBond` and `MinNominatorBond`). If unbonding is the
intention, `chill` first to remove one&\#x27;s role as validator/nominator.

---------
### InvalidEraToReward
Invalid era to reward.

---------
### InvalidNumberOfNominations
Invalid number of nominations.

---------
### InvalidSlashIndex
Slash record index out of bounds.

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
### NotSortedAndUnique
Items are not sorted and unique.

---------
### NotStash
Not a stash account.

---------
### TooManyNominators
There are too many nominators in the system. Governance needs to adjust the staking
settings to keep things safe for the runtime.

---------
### TooManyTargets
Too many nomination targets supplied.

---------
### TooManyValidators
There are too many validator candidates in the system. Governance needs to adjust the
staking settings to keep things safe for the runtime.

---------