
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
    'Vesting', 'claim_for', {'dest': 'AccountId'}
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
    'who': 'AccountId',
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
    'dest': 'AccountId',
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
Claimed vesting.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### VestingScheduleAdded
Added new vesting schedule.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| to | `T::AccountId` | ```AccountId```
| vesting_schedule | `VestingScheduleOf<T>` | ```{'start': 'u32', 'period': 'u32', 'period_count': 'u32', 'per_period': 'u128'}```

---------
### VestingSchedulesUpdated
Updated vesting schedules.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### VestingSchedules
 Vesting schedules of an account.

 VestingSchedules: map AccountId =&gt; Vec&lt;VestingSchedule&gt;

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
 The minimum amount transferred to call `vested_transfer`.
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
The vested transfer amount is too low

---------
### InsufficientBalanceToLock
Insufficient amount of balance to lock

---------
### MaxVestingSchedulesExceeded
Failed because the maximum vesting schedules was exceeded

---------
### TooManyVestingSchedules
This account have too many vesting schedules

---------
### ZeroVestingPeriod
Vesting period is zero

---------
### ZeroVestingPeriodCount
Number of vests is zero

---------