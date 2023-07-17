
# ParachainStaking

---------
## Calls

---------
### candidate_withdraw_unbonded
Withdraw deposit and complete candidate exit
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'candidate_withdraw_unbonded', {'candidate': 'AccountId'}
)
```

---------
### delegate
Delegate to an existing candidate, delegators stake a bond amount to support the
selected candidate
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate_id | `T::AccountId` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'delegate', {
    'amount': 'u128',
    'candidate_id': 'AccountId',
}
)
```

---------
### delegate_more
Increase the amount of stake delegated
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate_id | `T::AccountId` | 
| amount_to_add | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'delegate_more', {
    'amount_to_add': 'u128',
    'candidate_id': 'AccountId',
}
)
```

---------
### leave_intent
Deregister `origin` as a collator candidate. Note that the collator can only leave on
session change. The `CandidacyBond` will be unreserved immediately.

This call will fail if the total number of candidates would drop below `MinCandidates`.

This call is not available to `Invulnerable` collators.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'leave_intent', {}
)
```

---------
### register_as_candidate
Register this account as a collator candidate. The account must (a) already have
registered session keys and (b) be able to reserve the `CandidacyBond`.

This call is not available to `Invulnerable` collators.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'register_as_candidate', {}
)
```

---------
### set_block_inflation_reward
Undelegate and remove stake from an existing delegation
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'set_block_inflation_reward', {'amount': 'u128'}
)
```

---------
### set_candidacy_bond
Set the candidacy bond amount.
#### Attributes
| Name | Type |
| -------- | -------- | 
| bond | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'set_candidacy_bond', {'bond': 'u128'}
)
```

---------
### set_desired_candidates
Set the ideal number of collators (not including the invulnerables).
If lowering this number, then the number of running collators could be higher than this
figure. Aside from that edge case, there should be no other way to have more collators
than the desired number.
#### Attributes
| Name | Type |
| -------- | -------- | 
| max | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'set_desired_candidates', {'max': 'u32'}
)
```

---------
### set_invulnerables
Set the list of invulnerable (fixed) collators.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `Vec<CandidateInfoOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'set_invulnerables', {
    'new': [
        {
            'delegators': [
                {
                    'deposit': 'u128',
                    'who': 'AccountId',
                },
            ],
            'deposit': 'u128',
            'total_stake': 'u128',
            'who': 'AccountId',
        },
    ],
}
)
```

---------
### undelegate
Undelegate and remove stake from an existing delegation
#### Attributes
| Name | Type |
| -------- | -------- | 
| candidate_id | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'undelegate', {'candidate_id': 'AccountId'}
)
```

---------
### withdraw_unbonded
Withdraw unbonded delegation after unbonding delay
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'ParachainStaking', 'withdraw_unbonded', {}
)
```

---------
## Events

---------
### CandidateAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| deposit | `BalanceOf<T>` | ```u128```

---------
### CandidateRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```

---------
### CollatorRewardsTransferred
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### DelegatedMore
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| candidate | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### DelegationRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| candidate | `T::AccountId` | ```AccountId```

---------
### DelegatorRewardsTransferred
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### InflationAmountSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| amount | `BalanceOf<T>` | ```u128```

---------
### NewCandidacyBond
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| bond_amount | `BalanceOf<T>` | ```u128```

---------
### NewDelegation
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| candidate | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### NewDesiredCandidates
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| desired_candidates | `u32` | ```u32```

---------
### NewInvulnerables
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| invulnerables | `Vec<CandidateInfoOf<T>>` | ```[{'who': 'AccountId', 'deposit': 'u128', 'delegators': [{'who': 'AccountId', 'deposit': 'u128'}], 'total_stake': 'u128'}]```

---------
### UnbondedWithdrawn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### CandidacyBond
 Fixed amount to deposit to become a collator.

 When a collator calls `leave_intent` they immediately receive the deposit back.

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'CandidacyBond', []
)
```

#### Return value
```python
'u128'
```
---------
### Candidates
 The (community, limited) collation candidates.

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'Candidates', []
)
```

#### Return value
```python
[
    {
        'delegators': [{'deposit': 'u128', 'who': 'AccountId'}],
        'deposit': 'u128',
        'total_stake': 'u128',
        'who': 'AccountId',
    },
]
```
---------
### DesiredCandidates
 Desired number of candidates.

 This should ideally always be less than [`Config::MaxCandidates`] for weights to be correct.

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'DesiredCandidates', []
)
```

#### Return value
```python
'u32'
```
---------
### InflationAmountPerBlock
 Fixed amount to reward to collator

 This amount is rewarded to collators and stakers every block

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'InflationAmountPerBlock', []
)
```

#### Return value
```python
'u128'
```
---------
### Invulnerables
 The invulnerable, fixed collators.

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'Invulnerables', []
)
```

#### Return value
```python
[
    {
        'delegators': [{'deposit': 'u128', 'who': 'AccountId'}],
        'deposit': 'u128',
        'total_stake': 'u128',
        'who': 'AccountId',
    },
]
```
---------
### LastAuthoredBlock
 Last block authored by collator.

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'LastAuthoredBlock', ['AccountId']
)
```

#### Return value
```python
'u32'
```
---------
### UnbondedCandidates
 The delegates that have been removed

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'UnbondedCandidates', ['AccountId']
)
```

#### Return value
```python
{
    'delegators': [{'deposit': 'u128', 'who': 'AccountId'}],
    'deposit': 'u128',
    'total_stake': 'u128',
    'unbonded_at': 'u32',
}
```
---------
### UnbondedDelegates
 The delegates that have unbounded

#### Python
```python
result = substrate.query(
    'ParachainStaking', 'UnbondedDelegates', ['AccountId']
)
```

#### Return value
```python
{'deposit': 'u128', 'unbonded_at': 'u32'}
```
---------
## Errors

---------
### AlreadyCandidate
User is already a candidate

---------
### AlreadyDelegated
Already delegated

---------
### ArithmeticOverflow
Arithmetic overflow

---------
### DelegatorAccountSameAsCandidateAccount
The account is already a candidate

---------
### LessThanMinimumDelegation
Below Minimum delegation amount

---------
### NoAssociatedValidatorId
Account has no associated validator ID

---------
### NoUnbondingDelegation
No unbonding delegation found for user

---------
### NotCandidate
User is not a candidate

---------
### NotDelegator
Not a delegator

---------
### Permission
Permission issue

---------
### TooFewCandidates
Too few candidates

---------
### TooManyCandidates
Too many candidates

---------
### TooManyDelegations
Deledation limit is reached

---------
### TooManyInvulnerables
Too many invulnerables

---------
### UnbondingDelayNotPassed
The unbonding delay has not been reached

---------
### UnbondingInProgress
User already has another unbonding in progress

---------
### Unknown
Unknown error

---------
### ValidatorNotRegistered
Validator ID is not yet registered

---------