
# VestingManager

---------
## Calls

---------
### remove_vesting_schedule
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 
| schedule_index | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'VestingManager', 'remove_vesting_schedule', {
    'schedule_index': 'u32',
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
### VestingScheduleRemoved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| schedule_index | `u32` | ```u32```

---------