
# DarwiniaStaking

---------
## Calls

---------
### chill
Declare no desire to either collect or nominate.

Effects will be felt at the beginning of the next era.

If the target is a collator, its nominators need to re-nominate.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'DarwiniaStaking', 'chill', {}
)
```

---------
### claim
Claim the stakes from the pallet/contract account.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'DarwiniaStaking', 'claim', {}
)
```

---------
### collect
Declare the desire to collect.

Effects will be felt at the beginning of the next session.
#### Attributes
| Name | Type |
| -------- | -------- | 
| commission | `Perbill` | 

#### Python
```python
call = substrate.compose_call(
    'DarwiniaStaking', 'collect', {'commission': 'u32'}
)
```

---------
### nominate
Declare the desire to nominate a collator.

Effects will be felt at the beginning of the next session.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'DarwiniaStaking', 'nominate', {'target': '[u8; 20]'}
)
```

---------
### restake
Cancel the `unstake` operation.

Re-stake the unstaking assets immediately.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ring_amount | `Balance` | 
| kton_amount | `Balance` | 
| deposits | `Vec<DepositId<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'DarwiniaStaking', 'restake', {
    'deposits': ['u16'],
    'kton_amount': 'u128',
    'ring_amount': 'u128',
}
)
```

---------
### set_collator_count
Set collator count.

This will apply to the incoming session.

Require root origin.
#### Attributes
| Name | Type |
| -------- | -------- | 
| count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'DarwiniaStaking', 'set_collator_count', {'count': 'u32'}
)
```

---------
### stake
Add stakes to the staking pool.

This will transfer the stakes to a pallet/contact account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ring_amount | `Balance` | 
| kton_amount | `Balance` | 
| deposits | `Vec<DepositId<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'DarwiniaStaking', 'stake', {
    'deposits': ['u16'],
    'kton_amount': 'u128',
    'ring_amount': 'u128',
}
)
```

---------
### unstake
Withdraw stakes from the staking pool.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ring_amount | `Balance` | 
| kton_amount | `Balance` | 
| deposits | `Vec<DepositId<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'DarwiniaStaking', 'unstake', {
    'deposits': ['u16'],
    'kton_amount': 'u128',
    'ring_amount': 'u128',
}
)
```

---------
## Events

---------
### CommissionUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```[u8; 20]```
| commission | `Perbill` | ```u32```

---------
### Elected
A new collator set has been elected.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collators | `Vec<T::AccountId>` | ```['[u8; 20]']```

---------
### Payout
A payout has been made for the staker.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| staker | `T::AccountId` | ```[u8; 20]```
| ring_amount | `Balance` | ```u128```

---------
### Staked
An account has staked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| staker | `T::AccountId` | ```[u8; 20]```
| ring_amount | `Balance` | ```u128```
| kton_amount | `Balance` | ```u128```
| deposits | `Vec<DepositId<T>>` | ```['u16']```

---------
### Unstaked
An account has unstaked.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| staker | `T::AccountId` | ```[u8; 20]```
| ring_amount | `Balance` | ```u128```
| kton_amount | `Balance` | ```u128```
| deposits | `Vec<DepositId<T>>` | ```['u16']```

---------
## Storage functions

---------
### CollatorCount
 The ideal number of active collators.

#### Python
```python
result = substrate.query(
    'DarwiniaStaking', 'CollatorCount', []
)
```

#### Return value
```python
'u32'
```
---------
### Collators
 The map from (wannabe) collator to the preferences of that collator.

#### Python
```python
result = substrate.query(
    'DarwiniaStaking', 'Collators', ['[u8; 20]']
)
```

#### Return value
```python
'u32'
```
---------
### ElapsedTime
 Elapsed time.

#### Python
```python
result = substrate.query(
    'DarwiniaStaking', 'ElapsedTime', []
)
```

#### Return value
```python
'u128'
```
---------
### Exposures
 Current stakers&#x27; exposure.

#### Python
```python
result = substrate.query(
    'DarwiniaStaking', 'Exposures', ['[u8; 20]']
)
```

#### Return value
```python
{'nominators': [{'value': 'u32', 'who': '[u8; 20]'}], 'total': 'u32'}
```
---------
### KtonPool
 Total staked KTON.

#### Python
```python
result = substrate.query(
    'DarwiniaStaking', 'KtonPool', []
)
```

#### Return value
```python
'u128'
```
---------
### Ledgers
 All staking ledgers.

#### Python
```python
result = substrate.query(
    'DarwiniaStaking', 'Ledgers', ['[u8; 20]']
)
```

#### Return value
```python
{
    'staked_deposits': ['u16'],
    'staked_kton': 'u128',
    'staked_ring': 'u128',
    'unstaking_deposits': [('u16', 'u32')],
    'unstaking_kton': [('u128', 'u32')],
    'unstaking_ring': [('u128', 'u32')],
}
```
---------
### NextExposures
 Next stakers&#x27; exposure.

#### Python
```python
result = substrate.query(
    'DarwiniaStaking', 'NextExposures', ['[u8; 20]']
)
```

#### Return value
```python
{'nominators': [{'value': 'u32', 'who': '[u8; 20]'}], 'total': 'u32'}
```
---------
### Nominators
 The map from nominator to their nomination preferences, namely the collator that
 they wish to support.

#### Python
```python
result = substrate.query(
    'DarwiniaStaking', 'Nominators', ['[u8; 20]']
)
```

#### Return value
```python
'[u8; 20]'
```
---------
### RewardPoints
 Collator&#x27;s reward points.

#### Python
```python
result = substrate.query(
    'DarwiniaStaking', 'RewardPoints', []
)
```

#### Return value
```python
('u32', 'scale_info::324')
```
---------
### RingPool
 Total staked RING.

 This will count RING + deposit(locking RING).

#### Python
```python
result = substrate.query(
    'DarwiniaStaking', 'RingPool', []
)
```

#### Return value
```python
'u128'
```
---------
### SessionStartTime
 Active session&#x27;s start-time.

#### Python
```python
result = substrate.query(
    'DarwiniaStaking', 'SessionStartTime', []
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### MaxCommission
 Maximum commission rate.
#### Value
```python
300000000
```
#### Python
```python
constant = substrate.get_constant('DarwiniaStaking', 'MaxCommission')
```
---------
### MaxDeposits
 Maximum deposit count.
#### Value
```python
512
```
#### Python
```python
constant = substrate.get_constant('DarwiniaStaking', 'MaxDeposits')
```
---------
### MaxUnstakings
 Maximum unstaking/unbonding count.
#### Value
```python
16
```
#### Python
```python
constant = substrate.get_constant('DarwiniaStaking', 'MaxUnstakings')
```
---------
### MinStakingDuration
 Minimum time to stake at least.
#### Value
```python
100800
```
#### Python
```python
constant = substrate.get_constant('DarwiniaStaking', 'MinStakingDuration')
```
---------
### PayoutFraction
 The percentage of the total payout that is distributed to stakers.

 Usually, the rest goes to the treasury.
#### Value
```python
400000000
```
#### Python
```python
constant = substrate.get_constant('DarwiniaStaking', 'PayoutFraction')
```
---------
## Errors

---------
### CommissionTooHigh
Commission rate must be less than maximum commission rate.

---------
### DepositNotFound
Deposit not found.

---------
### ExceedMaxDeposits
Exceed maximum deposit count.

---------
### ExceedMaxUnstakings
Exceed maximum unstaking/unbonding count.

---------
### NotStaker
You are not a staker.

---------
### TargetNotCollator
Target is not a collator.

---------
### ZeroCollatorCount
Collator count mustn&\#x27;t be zero.

---------