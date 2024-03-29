
# Staking

---------
## Calls

---------
### bond
See [`Pallet::bond`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| value | `BalanceOf<T>` | 
| payee | `RewardDestination<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'bond', {
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
See [`Pallet::bond_extra`].
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
See [`Pallet::cancel_deferred_slash`].
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
See [`Pallet::chill`].
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
See [`Pallet::chill_other`].
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
See [`Pallet::force_apply_min_commission`].
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
See [`Pallet::force_new_era`].
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
See [`Pallet::force_new_era_always`].
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
See [`Pallet::force_no_eras`].
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
See [`Pallet::force_unstake`].
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
See [`Pallet::increase_validator_count`].
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
See [`Pallet::kick`].
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
See [`Pallet::nominate`].
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
See [`Pallet::payout_stakers`].
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
See [`Pallet::reap_stash`].
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
See [`Pallet::rebond`].
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
See [`Pallet::scale_validator_count`].
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
See [`Pallet::set_controller`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Staking', 'set_controller', {}
)
```

---------
### set_invulnerables
See [`Pallet::set_invulnerables`].
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
### set_min_commission
See [`Pallet::set_min_commission`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Perbill` | 

#### Python
```python
call = substrate.compose_call(
    'Staking', 'set_min_commission', {'new': 'u32'}
)
```

---------
### set_payee
See [`Pallet::set_payee`].
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
See [`Pallet::set_staking_configs`].
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
See [`Pallet::set_validator_count`].
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
See [`Pallet::unbond`].
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
See [`Pallet::validate`].
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
See [`Pallet::withdraw_unbonded`].
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
### ForceEra
A new force era mode was set.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| mode | `Forcing` | ```('NotForcing', 'ForceNew', 'ForceNone', 'ForceAlways')```

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
The nominator has been rewarded by this amount to this destination.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| stash | `T::AccountId` | ```AccountId```
| dest | `RewardDestination<T::AccountId>` | ```{'Staked': None, 'Stash': None, 'Controller': None, 'Account': 'AccountId', 'None': None}```
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
### SnapshotTargetsSizeExceeded
Targets size limit reached.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| size | `u32` | ```u32```

---------
### SnapshotVotersSizeExceeded
Voters size limit reached.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| size | `u32` | ```u32```

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

 TWOX-NOTE: SAFE since `AccountId` is a secure hash.

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
{'individual': 'scale_info::583', 'total': 'u32'}
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

 Note: All the reads and mutations to this storage *MUST* be done through the methods exposed
 by [`StakingLedger`] to ensure data and lock consistency.

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
 account&#x27;s [`NominationsQuota::MaxNominations`] configuration is decreased.
 In this rare case, these nominators
 are still existent in storage, their key is correct and retrievable (i.e. `contains_key`
 indicates that they exist), but their value cannot be decoded. Therefore, the non-decodable
 nominators will effectively not-exist, until they re-submit their preferences such that it
 is within the bounds of the newly set `Config::MaxNominations`.

 This implies that `::iter_keys().count()` and `::iter().count()` might return different
 values for this map. Moreover, the main `::count()` is aligned with the former, namely the
 number of keys that exist.

 Lastly, if any of the nominators become non-decodable, they can be chilled immediately via
 [`Call::chill_other`] dispatchable by anyone.

 TWOX-NOTE: SAFE since `AccountId` is a secure hash.

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

 TWOX-NOTE: SAFE since `AccountId` is a secure hash.

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

 TWOX-NOTE: SAFE since `AccountId` is a secure hash.

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