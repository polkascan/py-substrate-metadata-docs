
# TimeRelease

---------
## Calls

---------
### claim
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'TimeRelease', 'claim', {}
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
    'TimeRelease', 'claim_for', {
    'dest': {
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
### transfer
#### Attributes
| Name | Type |
| -------- | -------- | 
| dest | `<T::Lookup as StaticLookup>::Source` | 
| schedule | `ReleaseScheduleOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'TimeRelease', 'transfer', {
    'dest': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
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
### update_release_schedules
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `<T::Lookup as StaticLookup>::Source` | 
| release_schedules | `Vec<ReleaseScheduleOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'TimeRelease', 'update_release_schedules', {
    'release_schedules': [
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
        'Index': (),
        'Raw': 'Bytes',
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
### ReleaseScheduleAdded
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| release_schedule | `ReleaseScheduleOf<T>` | ```{'start': 'u32', 'period': 'u32', 'period_count': 'u32', 'per_period': 'u128'}```

---------
### ReleaseSchedulesUpdated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### ReleaseSchedules

#### Python
```python
result = substrate.query(
    'TimeRelease', 'ReleaseSchedules', ['AccountId']
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
### MinReleaseTransfer
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('TimeRelease', 'MinReleaseTransfer')
```
---------
## Errors

---------
### AmountLow

---------
### InsufficientBalanceToLock

---------
### MaxReleaseSchedulesExceeded

---------
### TooManyReleaseSchedules

---------
### ZeroReleasePeriod

---------
### ZeroReleasePeriodCount

---------