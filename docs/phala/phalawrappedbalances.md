
# PhalaWrappedBalances

---------
## Calls

---------
### unlock
See [`Pallet::unlock`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| vote_id | `ReferendumIndex` | 
| max_iterations | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaWrappedBalances', 'unlock', {
    'max_iterations': 'u32',
    'vote_id': 'u32',
}
)
```

---------
### unwrap
See [`Pallet::unwrap`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaWrappedBalances', 'unwrap', {'amount': 'u128'}
)
```

---------
### unwrap_all
See [`Pallet::unwrap_all`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'PhalaWrappedBalances', 'unwrap_all', {}
)
```

---------
### vote
See [`Pallet::vote`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| aye_amount | `BalanceOf<T>` | 
| nay_amount | `BalanceOf<T>` | 
| vote_id | `ReferendumIndex` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaWrappedBalances', 'vote', {
    'aye_amount': 'u128',
    'nay_amount': 'u128',
    'vote_id': 'u32',
}
)
```

---------
### wrap
See [`Pallet::wrap`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PhalaWrappedBalances', 'wrap', {'amount': 'u128'}
)
```

---------
## Events

---------
### DustRemoved
Some dust stake is removed

Triggered when the remaining stake of a user is too small after withdrawal or slash.

Affected states:
- the balance of the locking ledger of the contributor at [`StakeLedger`] is set to 0
- the user&\#x27;s dust stake is moved to treasury
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| user | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### Unwrapped
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| user | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### Voted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| user | `T::AccountId` | ```AccountId```
| vote_id | `ReferendumIndex` | ```u32```
| aye_amount | `BalanceOf<T>` | ```u128```
| nay_amount | `BalanceOf<T>` | ```u128```

---------
### Wrapped
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| user | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### AccountVoteMap
 Mapping from the accounts and vote ids to the amounts of W-PHA used to approve or oppose to the vote

#### Python
```python
result = substrate.query(
    'PhalaWrappedBalances', 'AccountVoteMap', ['AccountId', 'u32']
)
```

#### Return value
```python
()
```
---------
### StakerAccounts
 Mapping for users to their asset status proxys

#### Python
```python
result = substrate.query(
    'PhalaWrappedBalances', 'StakerAccounts', ['AccountId']
)
```

#### Return value
```python
{'invest_pools': [('u64', 'u32')], 'locked': 'u128'}
```
---------
### UnmintableDust
 Collect the unmintable dust

#### Python
```python
result = substrate.query(
    'PhalaWrappedBalances', 'UnmintableDust', []
)
```

#### Return value
```python
'u128'
```
---------
### VoteAccountMap
 Mapping from the vote ids and accounts to the amounts of W-PHA used to approve or oppose to the vote

#### Python
```python
result = substrate.query(
    'PhalaWrappedBalances', 'VoteAccountMap', ['u32', 'AccountId']
)
```

#### Return value
```python
('u128', 'u128')
```
---------
## Constants

---------
### WPhaAssetId
 W-PHA&#x27;s asset id
#### Value
```python
10000
```
#### Python
```python
constant = substrate.get_constant('PhalaWrappedBalances', 'WPhaAssetId')
```
---------
### WrappedBalancesAccountId
 Pha&#x27;s global fund pool
#### Value
```python
'43KPr1BjWx1D8RWKAcWU6U4Ye6H6ip7Up1PM4prCWseC425G'
```
#### Python
```python
constant = substrate.get_constant('PhalaWrappedBalances', 'WrappedBalancesAccountId')
```
---------
## Errors

---------
### IterationsIsNotVaild
The Iteration exceed the max limitaion

---------
### ReferendumInvalid
The vote is not currently on going

---------
### ReferendumOngoing
The vote is now on going and the W-PHA used in voting can not be unlocked

---------
### StakerAccountNotFound
user&\#x27;s `FinanceAccount` does not exist in storage: `StakerAccounts`

---------
### UnwrapAmountExceedsAvaliableStake
Trying to unwrap more than the available balance

---------
### VoteAmountLargerThanTotalStakes
Trying to vote more than the available balance

---------