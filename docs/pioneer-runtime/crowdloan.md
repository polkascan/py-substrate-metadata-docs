
# Crowdloan

---------
## Calls

---------
### remove_distributor_origin
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Crowdloan', 'remove_distributor_origin', {'to': 'AccountId'}
)
```

---------
### remove_vested_reward
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `T::AccountId` | 
| schedule_index | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Crowdloan', 'remove_vested_reward', {
    'schedule_index': 'u32',
    'to': 'AccountId',
}
)
```

---------
### set_distributor_origin
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Crowdloan', 'set_distributor_origin', {'to': 'AccountId'}
)
```

---------
### transfer_unlocked_reward
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `T::AccountId` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Crowdloan', 'transfer_unlocked_reward', {'amount': 'u128', 'to': 'AccountId'}
)
```

---------
### transfer_vested_reward
#### Attributes
| Name | Type |
| -------- | -------- | 
| to | `<T::Lookup as StaticLookup>::Source` | 
| schedule | `VestingInfo<VestingBalanceOf<T>, T::BlockNumber>` | 

#### Python
```python
call = substrate.compose_call(
    'Crowdloan', 'transfer_vested_reward', {
    'schedule': {
        'locked': 'u128',
        'per_block': 'u128',
        'starting_block': 'u32',
    },
    'to': {
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
## Events

---------
### AddedDistributorOrigin
Distributor AccountId
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### RemovedDistributorOrigin
Distributor AccountId
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### RemovedRewardVestingSchedule
AccountId, Schedule Index
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `u32` | ```u32```

---------
### TokenTransferred
Beneficial Account Id, Amount
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### VestedTokenTransferred
Beneficial AccountId, Amount
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `VestingInfo<BalanceOf<T>, T::BlockNumber>` | ```{'locked': 'u128', 'per_block': 'u128', 'starting_block': 'u32'}```

---------
## Storage functions

---------
### CrowdloanDistributorOrigins
 allowed origins

#### Python
```python
result = substrate.query(
    'Crowdloan', 'CrowdloanDistributorOrigins', ['AccountId']
)
```

#### Return value
```python
()
```
---------
## Errors

---------
### AlreadySetAsDistributorOrigin
Already set as distributor origin

---------
### DistributorOriginDoesNotExist
Distributor origin does not exist

---------
### NoPermission
No permission

---------
### UserAlreadyGotExistingVestingInfo
Already got existing vesting info

---------