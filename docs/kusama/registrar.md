
# Registrar

---------
## Calls

---------
### add_lock
See [`Pallet::add_lock`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'Registrar', 'add_lock', {'para': 'u32'}
)
```

---------
### deregister
See [`Pallet::deregister`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'Registrar', 'deregister', {'id': 'u32'}
)
```

---------
### force_register
See [`Pallet::force_register`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 
| deposit | `BalanceOf<T>` | 
| id | `ParaId` | 
| genesis_head | `HeadData` | 
| validation_code | `ValidationCode` | 

#### Python
```python
call = substrate.compose_call(
    'Registrar', 'force_register', {
    'deposit': 'u128',
    'genesis_head': 'Bytes',
    'id': 'u32',
    'validation_code': 'Bytes',
    'who': 'AccountId',
}
)
```

---------
### register
See [`Pallet::register`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `ParaId` | 
| genesis_head | `HeadData` | 
| validation_code | `ValidationCode` | 

#### Python
```python
call = substrate.compose_call(
    'Registrar', 'register', {
    'genesis_head': 'Bytes',
    'id': 'u32',
    'validation_code': 'Bytes',
}
)
```

---------
### remove_lock
See [`Pallet::remove_lock`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'Registrar', 'remove_lock', {'para': 'u32'}
)
```

---------
### reserve
See [`Pallet::reserve`].
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Registrar', 'reserve', {}
)
```

---------
### schedule_code_upgrade
See [`Pallet::schedule_code_upgrade`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 
| new_code | `ValidationCode` | 

#### Python
```python
call = substrate.compose_call(
    'Registrar', 'schedule_code_upgrade', {'new_code': 'Bytes', 'para': 'u32'}
)
```

---------
### set_current_head
See [`Pallet::set_current_head`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| para | `ParaId` | 
| new_head | `HeadData` | 

#### Python
```python
call = substrate.compose_call(
    'Registrar', 'set_current_head', {'new_head': 'Bytes', 'para': 'u32'}
)
```

---------
### swap
See [`Pallet::swap`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| id | `ParaId` | 
| other | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'Registrar', 'swap', {'id': 'u32', 'other': 'u32'}
)
```

---------
## Events

---------
### Deregistered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| para_id | `ParaId` | ```u32```

---------
### Registered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| para_id | `ParaId` | ```u32```
| manager | `T::AccountId` | ```AccountId```

---------
### Reserved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| para_id | `ParaId` | ```u32```
| who | `T::AccountId` | ```AccountId```

---------
### Swapped
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| para_id | `ParaId` | ```u32```
| other_id | `ParaId` | ```u32```

---------
## Storage functions

---------
### NextFreeParaId
 The next free `ParaId`.

#### Python
```python
result = substrate.query(
    'Registrar', 'NextFreeParaId', []
)
```

#### Return value
```python
'u32'
```
---------
### Paras
 Amount held on deposit for each para and the original depositor.

 The given account ID is responsible for registering the code and initial head data, but may
 only do so if it isn&#x27;t yet registered. (After that, it&#x27;s up to governance to do so.)

#### Python
```python
result = substrate.query(
    'Registrar', 'Paras', ['u32']
)
```

#### Return value
```python
{'deposit': 'u128', 'locked': (None, 'bool'), 'manager': 'AccountId'}
```
---------
### PendingSwap
 Pending swap operations.

#### Python
```python
result = substrate.query(
    'Registrar', 'PendingSwap', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### DataDepositPerByte
 The deposit to be paid per byte stored on chain.
#### Value
```python
333333333
```
#### Python
```python
constant = substrate.get_constant('Registrar', 'DataDepositPerByte')
```
---------
### ParaDeposit
 The deposit to be paid to run a on-demand parachain.
 This should include the cost for storing the genesis head and validation code.
#### Value
```python
40000000000000
```
#### Python
```python
constant = substrate.get_constant('Registrar', 'ParaDeposit')
```
---------
## Errors

---------
### AlreadyRegistered
The ID is already registered.

---------
### CannotDeregister
Cannot deregister para

---------
### CannotDowngrade
Cannot schedule downgrade of lease holding parachain to on-demand parachain

---------
### CannotSwap
Cannot perform a parachain slot / lifecycle swap. Check that the state of both paras
are correct for the swap to work.

---------
### CannotUpgrade
Cannot schedule upgrade of on-demand parachain to lease holding parachain

---------
### CodeTooLarge
Invalid para code size.

---------
### EmptyCode
Registering parachain with empty code is not allowed.

---------
### HeadDataTooLarge
Invalid para head data size.

---------
### NotOwner
The caller is not the owner of this Id.

---------
### NotParachain
Para is not a Parachain.

---------
### NotParathread
Para is not a Parathread (on-demand parachain).

---------
### NotRegistered
The ID is not registered.

---------
### NotReserved
The ID given for registration has not been reserved.

---------
### ParaLocked
Para is locked from manipulation by the manager. Must use parachain or relay chain
governance.

---------