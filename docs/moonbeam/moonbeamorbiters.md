
# MoonbeamOrbiters

---------
## Calls

---------
### add_collator
Add a collator to orbiters program.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collator | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'MoonbeamOrbiters', 'add_collator', {'collator': '[u8; 20]'}
)
```

---------
### collator_add_orbiter
Add an orbiter in a collator pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| orbiter | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'MoonbeamOrbiters', 'collator_add_orbiter', {'orbiter': '[u8; 20]'}
)
```

---------
### collator_remove_orbiter
Remove an orbiter from the caller collator pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| orbiter | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'MoonbeamOrbiters', 'collator_remove_orbiter', {'orbiter': '[u8; 20]'}
)
```

---------
### orbiter_leave_collator_pool
Remove the caller from the specified collator pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| collator | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'MoonbeamOrbiters', 'orbiter_leave_collator_pool', {'collator': '[u8; 20]'}
)
```

---------
### orbiter_register
Registering as an orbiter
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'MoonbeamOrbiters', 'orbiter_register', {}
)
```

---------
### orbiter_unregister
Deregistering from orbiters
#### Attributes
| Name | Type |
| -------- | -------- | 
| collators_pool_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'MoonbeamOrbiters', 'orbiter_unregister', {'collators_pool_count': 'u32'}
)
```

---------
### remove_collator
Remove a collator from orbiters program.
#### Attributes
| Name | Type |
| -------- | -------- | 
| collator | `<T::Lookup as StaticLookup>::Source` | 

#### Python
```python
call = substrate.compose_call(
    'MoonbeamOrbiters', 'remove_collator', {'collator': '[u8; 20]'}
)
```

---------
## Events

---------
### OrbiterJoinCollatorPool
An orbiter join a collator pool
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collator | `T::AccountId` | ```[u8; 20]```
| orbiter | `T::AccountId` | ```[u8; 20]```

---------
### OrbiterLeaveCollatorPool
An orbiter leave a collator pool
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collator | `T::AccountId` | ```[u8; 20]```
| orbiter | `T::AccountId` | ```[u8; 20]```

---------
### OrbiterRegistered
An orbiter has registered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```[u8; 20]```
| deposit | `BalanceOf<T>` | ```u128```

---------
### OrbiterRewarded
Paid the orbiter account the balance as liquid rewards.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```[u8; 20]```
| rewards | `BalanceOf<T>` | ```u128```

---------
### OrbiterRotation
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collator | `T::AccountId` | ```[u8; 20]```
| old_orbiter | `Option<T::AccountId>` | ```(None, '[u8; 20]')```
| new_orbiter | `Option<T::AccountId>` | ```(None, '[u8; 20]')```

---------
### OrbiterUnregistered
An orbiter has unregistered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account | `T::AccountId` | ```[u8; 20]```

---------
## Storage functions

---------
### AccountLookupOverride
 Account lookup override

#### Python
```python
result = substrate.query(
    'MoonbeamOrbiters', 'AccountLookupOverride', ['[u8; 20]']
)
```

#### Return value
```python
(None, '[u8; 20]')
```
---------
### CollatorsPool
 Current orbiters, with their &quot;parent&quot; collator

#### Python
```python
result = substrate.query(
    'MoonbeamOrbiters', 'CollatorsPool', ['[u8; 20]']
)
```

#### Return value
```python
{
    'maybe_current_orbiter': (
        None,
        {'account_id': '[u8; 20]', 'removed': 'bool'},
    ),
    'next_orbiter': 'u32',
    'orbiters': ['[u8; 20]'],
}
```
---------
### CounterForCollatorsPool
Counter for the related counted storage map

#### Python
```python
result = substrate.query(
    'MoonbeamOrbiters', 'CounterForCollatorsPool', []
)
```

#### Return value
```python
'u32'
```
---------
### CurrentRound
 Current round index

#### Python
```python
result = substrate.query(
    'MoonbeamOrbiters', 'CurrentRound', []
)
```

#### Return value
```python
'u32'
```
---------
### ForceRotation
 If true, it forces the rotation at the next round.
 A use case: when changing RotatePeriod, you need a migration code that sets this value to
 true to avoid holes in OrbiterPerRound.

#### Python
```python
result = substrate.query(
    'MoonbeamOrbiters', 'ForceRotation', []
)
```

#### Return value
```python
'bool'
```
---------
### MinOrbiterDeposit
 Minimum deposit required to be registered as an orbiter

#### Python
```python
result = substrate.query(
    'MoonbeamOrbiters', 'MinOrbiterDeposit', []
)
```

#### Return value
```python
'u128'
```
---------
### OrbiterPerRound
 Store active orbiter per round and per parent collator

#### Python
```python
result = substrate.query(
    'MoonbeamOrbiters', 'OrbiterPerRound', ['u32', '[u8; 20]']
)
```

#### Return value
```python
'[u8; 20]'
```
---------
### RegisteredOrbiter
 Check if account is an orbiter

#### Python
```python
result = substrate.query(
    'MoonbeamOrbiters', 'RegisteredOrbiter', ['[u8; 20]']
)
```

#### Return value
```python
'bool'
```
---------
## Constants

---------
### MaxPoolSize
 Maximum number of orbiters per collator.
#### Value
```python
8
```
#### Python
```python
constant = substrate.get_constant('MoonbeamOrbiters', 'MaxPoolSize')
```
---------
### MaxRoundArchive
 Maximum number of round to keep on storage.
#### Value
```python
4
```
#### Python
```python
constant = substrate.get_constant('MoonbeamOrbiters', 'MaxRoundArchive')
```
---------
### RotatePeriod
 Number of rounds before changing the selected orbiter.
 WARNING: when changing `RotatePeriod`, you need a migration code that sets
 `ForceRotation` to true to avoid holes in `OrbiterPerRound`.
#### Value
```python
1
```
#### Python
```python
constant = substrate.get_constant('MoonbeamOrbiters', 'RotatePeriod')
```
---------
## Errors

---------
### CollatorAlreadyAdded
The collator is already added in orbiters program.

---------
### CollatorNotFound
This collator is not in orbiters program.

---------
### CollatorPoolTooLarge
There are already too many orbiters associated with this collator.

---------
### CollatorsPoolCountTooLow
There are more collator pools than the number specified in the parameter.

---------
### MinOrbiterDepositNotSet
The minimum deposit required to register as an orbiter has not yet been included in the
onchain storage

---------
### OrbiterAlreadyInPool
This orbiter is already associated with this collator.

---------
### OrbiterDepositNotFound
This orbiter has not made a deposit

---------
### OrbiterNotFound
This orbiter is not found

---------
### OrbiterStillInAPool
The orbiter is still at least in one pool

---------