
# DoraRewards

---------
## Calls

---------
### claim_rewards
contributors claim their rewards by this call
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'DoraRewards', 'claim_rewards', {}
)
```

---------
### complete_initialization
Update the ending lease block
#### Attributes
| Name | Type |
| -------- | -------- | 
| lease_ending_block | `T::VestingBlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'DoraRewards', 'complete_initialization', {'lease_ending_block': 'u32'}
)
```

---------
### initialize_contributors_list
 Initialize contributor&\#x27;s rewards info which is a contributors vec
 this operation should be execute by sudo user
#### Attributes
| Name | Type |
| -------- | -------- | 
| contributor_list | `Vec<(T::AccountId, BalanceOf<T>)>` | 

#### Python
```python
call = substrate.compose_call(
    'DoraRewards', 'initialize_contributors_list', {
    'contributor_list': [
        ('AccountId', 'u128'),
    ],
}
)
```

---------
## Events

---------
### DistributeReward
distribute reward (source account, destination account, amount)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### EndleasingBlock
set the ending lease block
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::VestingBlockNumber` | ```u32```

---------
### UpdateContributorsInfo
update contributor&\#x27;s reward info (accountId, total reward, claimed reward)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### ContributorsInfo
 Record contributor&#x27;s info (total reward, claimed reward, track block number)

#### Python
```python
result = substrate.query(
    'DoraRewards', 'ContributorsInfo', ['AccountId']
)
```

#### Return value
```python
{
    'claimed_reward': 'u128',
    'total_reward': 'u128',
    'track_block_number': 'u32',
}
```
---------
### EndBlock
 Vesting block height at the initialization of the pallet

#### Python
```python
result = substrate.query(
    'DoraRewards', 'EndBlock', []
)
```

#### Return value
```python
'u32'
```
---------
### InitBlock
 Vesting block height at the initialization of the pallet

#### Python
```python
result = substrate.query(
    'DoraRewards', 'InitBlock', []
)
```

#### Return value
```python
'u32'
```
---------
### Initialized

#### Python
```python
result = substrate.query(
    'DoraRewards', 'Initialized', []
)
```

#### Return value
```python
'bool'
```
---------
### TotalContributors
 store total number of contributors

#### Python
```python
result = substrate.query(
    'DoraRewards', 'TotalContributors', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### MaxContributorsNumber
 this parameter control the max contributor list length
#### Value
```python
400
```
#### Python
```python
constant = substrate.get_constant('DoraRewards', 'MaxContributorsNumber')
```
---------
## Errors

---------
### InitializationIsCompleted
complete the initialized

---------
### InvalidEndingLeaseBlock
Ending lease block setting invalid (should higher than the init block)

---------
### NoLeftRewards
current account claimed all the reward, no reward left

---------
### NotCompleteInitialization
Not set the Ending lease block

---------
### NotInContributorList
Invalid contributor account (not exist in contributor list)

---------
### TooManyContributors
too many contributors when put the contributor list into the storage

---------