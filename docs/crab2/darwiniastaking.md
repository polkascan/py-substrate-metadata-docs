
# DarwiniaStaking

---------
## Calls

---------
### chill
See [`Pallet::chill`].
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
See [`Pallet::claim`].
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
See [`Pallet::collect`].
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
See [`Pallet::nominate`].
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
### payout
See [`Pallet::payout`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'DarwiniaStaking', 'payout', {'who': '[u8; 20]'}
)
```

---------
### restake
See [`Pallet::restake`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| ring_amount | `Balance` | 
| deposits | `Vec<DepositId<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'DarwiniaStaking', 'restake', {
    'deposits': ['u16'],
    'ring_amount': 'u128',
}
)
```

---------
### set_collator_count
See [`Pallet::set_collator_count`].
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
See [`Pallet::stake`].
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
See [`Pallet::unstake`].
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
| amount | `Balance` | ```u128```

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
### Unpaid
Unable to pay the staker&\#x27;s reward.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| staker | `T::AccountId` | ```[u8; 20]```
| amount | `Balance` | ```u128```

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
### AuthoredBlocksCount
 Number of blocks authored by the collator within current session.

#### Python
```python
result = substrate.query(
    'DarwiniaStaking', 'AuthoredBlocksCount', []
)
```

#### Return value
```python
('u32', 'scale_info::387')
```
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
### ExposureCache0
 Exposure cache 0.

#### Python
```python
result = substrate.query(
    'DarwiniaStaking', 'ExposureCache0', ['[u8; 20]']
)
```

#### Return value
```python
{'commission': 'u32', 'nominators': [{'vote': 'u32', 'who': '[u8; 20]'}], 'vote': 'u32'}
```
---------
### ExposureCache1
 Exposure cache 1.

#### Python
```python
result = substrate.query(
    'DarwiniaStaking', 'ExposureCache1', ['[u8; 20]']
)
```

#### Return value
```python
{'commission': 'u32', 'nominators': [{'vote': 'u32', 'who': '[u8; 20]'}], 'vote': 'u32'}
```
---------
### ExposureCache2
 Exposure cache 2.

#### Python
```python
result = substrate.query(
    'DarwiniaStaking', 'ExposureCache2', ['[u8; 20]']
)
```

#### Return value
```python
{'commission': 'u32', 'nominators': [{'vote': 'u32', 'who': '[u8; 20]'}], 'vote': 'u32'}
```
---------
### ExposureCacheStates
 Exposure cache states.

 To avoid extra DB RWs during new session, such as:
 ```nocompile
 previous = current;
 current = next;
 next = elect();
 ```

 Now, with data:
 ```nocompile
 cache1 == previous;
 cache2 == current;
 cache3 == next;
 ```
 Just need to shift the marker and write the storage map once:
 ```nocompile
 mark(cache3, current);
 mark(cache2, previous);
 mark(cache1, next);
 cache1 = elect();
 ```

#### Python
```python
result = substrate.query(
    'DarwiniaStaking', 'ExposureCacheStates', []
)
```

#### Return value
```python
(
    ('Previous', 'Current', 'Next'),
    ('Previous', 'Current', 'Next'),
    ('Previous', 'Current', 'Next'),
)
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
### MigrationStartBlock
 Migration starting block.

#### Python
```python
result = substrate.query(
    'DarwiniaStaking', 'MigrationStartBlock', []
)
```

#### Return value
```python
'u32'
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
### PendingRewards
 All outstanding rewards since the last payment.

#### Python
```python
result = substrate.query(
    'DarwiniaStaking', 'PendingRewards', ['[u8; 20]']
)
```

#### Return value
```python
'u128'
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
### KtonRewardDistributionContract
 The address of KTON reward distribution contract.
#### Value
```python
'0x000000000ae5db7bdaf8d071e680452e33d91dd5'
```
#### Python
```python
constant = substrate.get_constant('DarwiniaStaking', 'KtonRewardDistributionContract')
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
### MigrationCurve
 The curve of migration.
#### Value
```python
582296296296296297
```
#### Python
```python
constant = substrate.get_constant('DarwiniaStaking', 'MigrationCurve')
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
## Errors

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
### NoReward
No reward to pay for this collator.

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