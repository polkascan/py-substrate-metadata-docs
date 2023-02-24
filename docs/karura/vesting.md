
# Vesting

---------
## Calls

---------
### claim
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'claim', {}
)
```

---------
### claim_for
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'claim_for', {
    'dest': {
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
### update_vesting_schedules
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `<T::Lookup as StaticLookup>::Source` | 
| vesting_schedules | `Vec<VestingScheduleOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'update_vesting_schedules', {
    'vesting_schedules': [
        {
            'per_period': 'u128',
            'period': 'u32',
            'period_count': 'u32',
            'start': 'u32',
        },
    ],
    'who': {
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
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| schedule | `VestingScheduleOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Vesting', 'vested_transfer', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': 'u32',
        'Raw': 'Bytes',
    },
    'schedule': {
        'per_period': 'u128',
        'period': 'u32',
        'period_count': 'u32',
        'start': 'u32',
    },
}
)
```

---------
## Events

---------
### Claimed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### VestingScheduleAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| vesting_schedule | `VestingScheduleOf<T>` | ```{'start': 'u32', 'period': 'u32', 'period_count': 'u32', 'per_period': 'u128'}```

---------
### VestingSchedulesUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### VestingSchedules

#### Python
```python
result = substrate.query(
    'Vesting', 'VestingSchedules', ['AccountId']
)
```

#### Return value
```python
[
    {
        'per_period': 'u128',
        'period': 'u32',
        'period_count': 'u32',
        'start': 'u32',
    },
]
```
---------
## Constants

---------
### MinVestedTransfer
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Vesting', 'MinVestedTransfer')
```
---------
## Errors

---------
### AmountLow

---------
### InsufficientBalanceToLock

---------
### MaxVestingSchedulesExceeded

---------
### TooManyVestingSchedules

---------
### ZeroVestingPeriod

---------
### ZeroVestingPeriodCount

---------