
# Vesting

---------
## Calls

---------
### force_vested_transfer
See [`Pallet::force_vested_transfer`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| source | `AccountIdLookupOf<T>` | 
| target | `AccountIdLookupOf<T>` | 
| schedule | `VestingInfo<BalanceOf<T>, BlockNumberFor<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'force_vested_transfer', {
    'schedule': {
        'locked': 'u128',
        'per_block': 'u128',
        'starting_block': 'u32',
    },
    'source': '[u8; 20]',
    'target': '[u8; 20]',
}
)
```

---------
### merge_schedules
See [`Pallet::merge_schedules`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| schedule1_index | `u32` | 
| schedule2_index | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'merge_schedules', {
    'schedule1_index': 'u32',
    'schedule2_index': 'u32',
}
)
```

---------
### vest
See [`Pallet::vest`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'vest', {}
)
```

---------
### vest_other
See [`Pallet::vest_other`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `AccountIdLookupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'vest_other', {'target': '[u8; 20]'}
)
```

---------
### vested_transfer
See [`Pallet::vested_transfer`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `AccountIdLookupOf<T>` | 
| schedule | `VestingInfo<BalanceOf<T>, BlockNumberFor<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'vested_transfer', {
    'schedule': {
        'locked': 'u128',
        'per_block': 'u128',
        'starting_block': 'u32',
    },
    'target': '[u8; 20]',
}
)
```

---------
## Events

---------
### VestingCompleted
An \[account\] has become fully vested.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```[u8; 20]```

---------
### VestingUpdated
The amount vested has been updated. This could indicate a change in funds available.
The balance given is the amount which is left unvested (and thus locked).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```[u8; 20]```
| unvested | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### StorageVersion
 Storage version of the pallet.

 New networks start with latest version, as determined by the genesis build.

#### Python
```python
result = substrate.query(
    'Vesting', 'StorageVersion', []
)
```

#### Return value
```python
('V0', 'V1')
```
---------
### Vesting
 Information regarding the vesting of a given account.

#### Python
```python
result = substrate.query(
    'Vesting', 'Vesting', ['[u8; 20]']
)
```

#### Return value
```python
[{'locked': 'u128', 'per_block': 'u128', 'starting_block': 'u32'}]
```
---------
## Constants

---------
### MaxVestingSchedules
#### Value
```python
28
```
#### Python
```python
constant = substrate.get_constant('Vesting', 'MaxVestingSchedules')
```
---------
### MinVestedTransfer
 The minimum amount transferred to call `vested_transfer`.
#### Value
```python
1000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Vesting', 'MinVestedTransfer')
```
---------
## Errors

---------
### AmountLow
Amount being transferred is too low to create a vesting schedule.

---------
### AtMaxVestingSchedules
The account already has `MaxVestingSchedules` count of schedules and thus
cannot add another one. Consider merging existing schedules in order to add another.

---------
### InvalidScheduleParams
Failed to create a new schedule because some parameter was invalid.

---------
### NotVesting
The account given is not vesting.

---------
### ScheduleIndexOutOfBounds
An index was out of bounds of the vesting schedules.

---------