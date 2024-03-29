
# Vesting

---------
## Calls

---------
### force_set_cliff
See [`Pallet::force_set_cliff`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `<T::Lookup as StaticLookup>::Source` | 
| cliff_block | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'force_set_cliff', {
    'cliff_block': 'u32',
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
    'source': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
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
### init_vesting_start_at
See [`Pallet::init_vesting_start_at`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| vesting_start_at | `BlockNumberFor<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'init_vesting_start_at', {'vesting_start_at': 'u32'}
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
### set_vesting_per_block
See [`Pallet::set_vesting_per_block`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `<T::Lookup as StaticLookup>::Source` | 
| index | `u32` | 
| per_block | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'set_vesting_per_block', {
    'index': 'u32',
    'per_block': 'u128',
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
    'Vesting', 'vest_other', {
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
## Events

---------
### VestingCompleted
An \[account\] has become fully vested.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```

---------
### VestingUpdated
The amount vested has been updated. This could indicate a change in funds available.
The balance given is the amount which is left unvested (and thus locked).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```AccountId```
| unvested | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### Cliff
 Cliff vesting

#### Python
```python
result = substrate.query(
    'Vesting', 'Cliff', ['AccountId']
)
```

#### Return value
```python
'u32'
```
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
    'Vesting', 'Vesting', ['AccountId']
)
```

#### Return value
```python
[{'locked': 'u128', 'per_block': 'u128', 'starting_block': 'u32'}]
```
---------
### VestingStartAt
 Start at

#### Python
```python
result = substrate.query(
    'Vesting', 'VestingStartAt', []
)
```

#### Return value
```python
'u32'
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
10000000000
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
### SamePerBlock
change to the same per_block param

---------
### ScheduleIndexOutOfBounds
An index was out of bounds of the vesting schedules.

---------
### VestingStartAtNotSet
VestingStartAt storage is not set

---------
### WrongCliffVesting
Wrong vesting during cliff period

---------
### WrongLockedAmount
Wrong amount

---------