
# XStaking

---------
## Calls

---------
### bond
Nominate the `target` with `value` of the origin account&\#x27;s balance locked.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `<T::Lookup as StaticLookup>::Source` | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'XStaking', 'bond', {
    'target': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'value': 'u128',
}
)
```

---------
### chill
Declare no desire to validate for the origin account.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'XStaking', 'chill', {}
)
```

---------
### claim
Claim the staking reward given the `target` validator.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'XStaking', 'claim', {
    'target': {
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
### force_reset_staking_lock
#### Attributes
| Name | Type |
| -------- | -------- | 
| accounts | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'XStaking', 'force_reset_staking_lock', {'accounts': ['AccountId']}
)
```

---------
### force_set_lock
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_locks | `Vec<(T::AccountId, BalanceOf<T>)>` | 

#### Python
```python
call = substrate.compose_call(
    'XStaking', 'force_set_lock', {'new_locks': [('AccountId', 'u128')]}
)
```

---------
### force_unlock_bonded_withdrawal
Clear the records in Staking for leaked `BondedWithdrawal` frozen balances.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'XStaking', 'force_unlock_bonded_withdrawal', {'who': 'AccountId'}
)
```

---------
### rebond
Move the `value` of current nomination from one validator to another.
#### Attributes
| Name | Type |
| -------- | -------- | 
| from | `<T::Lookup as StaticLookup>::Source` | 
| to | `<T::Lookup as StaticLookup>::Source` | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'XStaking', 'rebond', {
    'from': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'to': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'value': 'u128',
}
)
```

---------
### register
Register to be a validator for the origin account.

The reason for using `validator_nickname` instead of `referral_id` as
the variable name is when we interact with this interface from outside
we can take this as the nickname of validator, which possibly
can help reduce some misunderstanding for these unfamiliar with
the referral mechanism in Asset Mining. In the context of codebase, we
always use the concept of referral id.
#### Attributes
| Name | Type |
| -------- | -------- | 
| validator_nickname | `ReferralId` | 
| initial_bond | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'XStaking', 'register', {
    'initial_bond': 'u128',
    'validator_nickname': 'Bytes',
}
)
```

---------
### set_bonding_duration
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'XStaking', 'set_bonding_duration', {'new': 'u32'}
)
```

---------
### set_immortals
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'XStaking', 'set_immortals', {'new': ['AccountId']}
)
```

---------
### set_minimum_penalty
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'XStaking', 'set_minimum_penalty', {'new': 'u128'}
)
```

---------
### set_minimum_validator_count
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'XStaking', 'set_minimum_validator_count', {'new': 'u32'}
)
```

---------
### set_sessions_per_era
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `SessionIndex` | 

#### Python
```python
call = substrate.compose_call(
    'XStaking', 'set_sessions_per_era', {'new': 'u32'}
)
```

---------
### set_validator_bonding_duration
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'XStaking', 'set_validator_bonding_duration', {'new': 'u32'}
)
```

---------
### set_validator_count
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'XStaking', 'set_validator_count', {'new': 'u32'}
)
```

---------
### unbond
Unnominate the `value` of bonded balance for validator `target`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `<T::Lookup as StaticLookup>::Source` | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'XStaking', 'unbond', {
    'target': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'value': 'u128',
}
)
```

---------
### unlock_unbonded_withdrawal
Unlock the frozen unbonded balances that are due.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `<T::Lookup as StaticLookup>::Source` | 
| unbonded_index | `UnbondedIndex` | 

#### Python
```python
call = substrate.compose_call(
    'XStaking', 'unlock_unbonded_withdrawal', {
    'target': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'unbonded_index': 'u32',
}
)
```

---------
### validate
Declare the desire to validate for the origin account.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'XStaking', 'validate', {}
)
```

---------
## Events

---------
### Bonded
A nominator bonded to the validator this amount. [nominator, validator, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### Claimed
A nominator claimed the staking dividend. [nominator, validator, dividend]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### ForceAllWithdrawn
Unlock the unbonded withdrawal by force. [account]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### ForceChilled
Offenders were forcibly to be chilled due to insufficient reward pot balance. [session_index, chilled_validators]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `SessionIndex` | ```u32```
| None | `Vec<T::AccountId>` | ```['AccountId']```

---------
### Minted
Issue new balance to this account. [account, reward_amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### MintedForValidator
Issue new balance to validator and pot. [validator, reward_amount, validator_pot, reward_amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### Rebonded
A nominator switched the vote from one validator to another. [nominator, from, to, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### Slashed
A validator (and its reward pot) was slashed. [validator, slashed_amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### Unbonded
A nominator unbonded this amount. [nominator, validator, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### Withdrawn
The nominator withdrew the locked balance from the unlocking queue. [nominator, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### ActiveEra
 The active era information, it holds index and start.

 The active era is the era currently rewarded.
 Validator set of this era must be equal to `SessionInterface::validators`.

#### Python
```python
result = substrate.query(
    'XStaking', 'ActiveEra', []
)
```

#### Return value
```python
{'index': 'u32', 'start': (None, 'u64')}
```
---------
### BondingDuration
 The length of the bonding duration in blocks.

#### Python
```python
result = substrate.query(
    'XStaking', 'BondingDuration', []
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
    'XStaking', 'CurrentEra', []
)
```

#### Return value
```python
'u32'
```
---------
### ErasStartSessionIndex
 The session index at which the era start for the last `HISTORY_DEPTH` eras.

#### Python
```python
result = substrate.query(
    'XStaking', 'ErasStartSessionIndex', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### ForceEra
 Mode of era forcing.

#### Python
```python
result = substrate.query(
    'XStaking', 'ForceEra', []
)
```

#### Return value
```python
('NotForcing', 'ForceNew', 'ForceNone', 'ForceAlways')
```
---------
### GlobalDistributionRatio
 (Treasury, Staking)

#### Python
```python
result = substrate.query(
    'XStaking', 'GlobalDistributionRatio', []
)
```

#### Return value
```python
{'mining': 'u32', 'treasury': 'u32'}
```
---------
### Immortals
 Immortal validators will always be elected if any.

 Immortals will be intialized from the genesis validators.

#### Python
```python
result = substrate.query(
    'XStaking', 'Immortals', []
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
    'XStaking', 'IsCurrentSessionFinal', []
)
```

#### Return value
```python
'bool'
```
---------
### LastRebondOf
 The map from nominator to the block number of last `rebond` operation.

#### Python
```python
result = substrate.query(
    'XStaking', 'LastRebondOf', ['AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### Locks
 All kinds of locked balances of an account in Staking.

#### Python
```python
result = substrate.query(
    'XStaking', 'Locks', ['AccountId']
)
```

#### Return value
```python
'scale_info::413'
```
---------
### MaximumUnbondedChunkSize
 Maximum number of on-going unbonded chunk.

#### Python
```python
result = substrate.query(
    'XStaking', 'MaximumUnbondedChunkSize', []
)
```

#### Return value
```python
'u32'
```
---------
### MaximumValidatorCount
 Maximum number of staking participants before emergency conditions are imposed.

#### Python
```python
result = substrate.query(
    'XStaking', 'MaximumValidatorCount', []
)
```

#### Return value
```python
'u32'
```
---------
### MinimumPenalty
 Minimum penalty for each slash.

#### Python
```python
result = substrate.query(
    'XStaking', 'MinimumPenalty', []
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
    'XStaking', 'MinimumValidatorCount', []
)
```

#### Return value
```python
'u32'
```
---------
### MiningDistributionRatio
 (Staker, Asset Miners)

#### Python
```python
result = substrate.query(
    'XStaking', 'MiningDistributionRatio', []
)
```

#### Return value
```python
{'asset': 'u32', 'staking': 'u32'}
```
---------
### Nominations
 The map from nominator to the vote weight ledger of all nominees.

#### Python
```python
result = substrate.query(
    'XStaking', 'Nominations', ['AccountId', 'AccountId']
)
```

#### Return value
```python
{
    'last_vote_weight': 'u128',
    'last_vote_weight_update': 'u32',
    'nomination': 'u128',
    'unbonded_chunks': [{'locked_until': 'u32', 'value': 'u128'}],
}
```
---------
### SessionOffenders
 Offenders reported in last session.

#### Python
```python
result = substrate.query(
    'XStaking', 'SessionOffenders', []
)
```

#### Return value
```python
'scale_info::419'
```
---------
### SessionsPerEra
 The length of a staking era in sessions.

#### Python
```python
result = substrate.query(
    'XStaking', 'SessionsPerEra', []
)
```

#### Return value
```python
'u32'
```
---------
### UpperBoundFactorOfAcceptableVotes
 Maximum value of total_bonded/self_bonded.

#### Python
```python
result = substrate.query(
    'XStaking', 'UpperBoundFactorOfAcceptableVotes', []
)
```

#### Return value
```python
'u32'
```
---------
### ValidatorBondingDuration
 The length of the bonding duration in blocks for validator.

#### Python
```python
result = substrate.query(
    'XStaking', 'ValidatorBondingDuration', []
)
```

#### Return value
```python
'u32'
```
---------
### ValidatorCandidateRequirement
 Minimum value (self_bonded, total_bonded) to be a candidate of validator election.

#### Python
```python
result = substrate.query(
    'XStaking', 'ValidatorCandidateRequirement', []
)
```

#### Return value
```python
{'self_bonded': 'u128', 'total': 'u128'}
```
---------
### ValidatorCount
 The ideal number of staking participants.

#### Python
```python
result = substrate.query(
    'XStaking', 'ValidatorCount', []
)
```

#### Return value
```python
'u32'
```
---------
### ValidatorFor
 The validator account behind the referral id.

#### Python
```python
result = substrate.query(
    'XStaking', 'ValidatorFor', ['Bytes']
)
```

#### Return value
```python
'AccountId'
```
---------
### ValidatorLedgers
 The map from validator key to the vote weight ledger of that validator.

#### Python
```python
result = substrate.query(
    'XStaking', 'ValidatorLedgers', ['AccountId']
)
```

#### Return value
```python
{
    'last_total_vote_weight': 'u128',
    'last_total_vote_weight_update': 'u32',
    'total_nomination': 'u128',
}
```
---------
### Validators
 The map from (wannabe) validator key to the profile of that validator.

#### Python
```python
result = substrate.query(
    'XStaking', 'Validators', ['AccountId']
)
```

#### Return value
```python
{
    'is_chilled': 'bool',
    'last_chilled': (None, 'u32'),
    'referral_id': 'Bytes',
    'registered_at': 'u32',
}
```
---------
## Constants

---------
### MaximumReferralId
 The maximum byte length of validator referral id.
#### Value
```python
12
```
#### Python
```python
constant = substrate.get_constant('XStaking', 'MaximumReferralId')
```
---------
### MinimumReferralId
 The minimum byte length of validator referral id.
#### Value
```python
2
```
#### Python
```python
constant = substrate.get_constant('XStaking', 'MinimumReferralId')
```
---------
## Errors

---------
### AllocateDividendFailed
Failed to allocate the dividend.

---------
### AlreadyValidator
The account is already registered as a validator.

---------
### EmptyUnbondedChunks
The account has no unbonded entries.

---------
### InsufficientBalance
Free balance can not cover this bond operation.

---------
### InvalidRebondBalance
An account can only rebond the balance that is no more than what it has bonded to the validator.

---------
### InvalidReferralIdentityLength
The length of referral identity is either too long or too short.

---------
### InvalidUnbondBalance
An account can only unbond the balance that is no more than what it has bonded to the validator.

---------
### InvalidUnbondedIndex
Can not find the unbonded entry given the index.

---------
### NoMoreAcceptableVotes
The validator can accept no more votes from other voters.

---------
### NoMoreRebond
Can not rebond due to the restriction of rebond frequency limit.

---------
### NoMoreUnbondChunks
An account can have only `MaximumUnbondedChunkSize` unbonded entries in parallel.

---------
### NotValidator
Invalid validator target.

---------
### OccupiedReferralIdentity
The referral identity has been claimed by someone else.

---------
### RebondSelfBondedNotAllowed
Can not rebond the validator self-bonded votes as it has a much longer bonding duration.

---------
### TooFewActiveValidators
The validator can not (forcedly) be chilled due to the limit of minimal validators count.

---------
### TooManyValidators
The validators count already reaches `MaximumValidatorCount`.

---------
### UnbondedWithdrawalNotYetDue
The unbonded balances are still in the locked state.

---------
### XssCheckFailed
Failed to pass the xss check.

---------
### ZeroBalance
The operation of zero balance in Staking makes no sense.

---------
### ZeroVoteWeight
No rewards when the vote weight is zero.

---------