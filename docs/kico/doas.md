
# DoAs

---------
## Calls

---------
### do_as_collective
#### Attributes
| Name | Type |
| -------- | -------- | 
| dao_id | `T::DaoId` | 
| call | `Box<<T as dao::Config>::Call>` | 

#### Python
```python
call = substrate.compose_call(
    'DoAs', 'do_as_collective', {'call': 'Call', 'dao_id': 'u64'}
)
```

---------
## Events

---------
### DoAsDone
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sudo_result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('NoFunds', 'WouldDie', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer')}}```

---------
### SetEnsure
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::DaoId` | ```u64```
| None | `u32` | ```u32```
| None | `DoAsEnsureOrigin<Proportion<MemberCount>, MemberCount>` | ```{'Proportion': {'MoreThan': ('u32', 'u32'), 'AtLeast': ('u32', 'u32')}, 'Member': None, 'Members': 'u32', 'Root': None, 'NoPermission': None}```

---------
## Errors

---------
### BadOrigin

---------
### CallNotSupport

---------
### DaoNotExists

---------
### HaveNoCallId

---------
### InVailCall

---------
### InVailCallId

---------
### InVailDaoId

---------
### NotDaoAccount

---------
### NotDaoId

---------
### ProportionErr

---------