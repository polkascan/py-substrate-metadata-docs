
# Registrar

---------
## Calls

---------
### add_lock
Add a manager lock from a para. This will prevent the manager of a
para to deregister or swap a para.

Can be called by Root, the parachain, or the parachain manager if the parachain is unlocked.
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
Deregister a Para Id, freeing all data and returning any deposit.

The caller must be Root, the `para` owner, or the `para` itself. The para must be a parathread.
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
Force the registration of a Para Id on the relay chain.

This function must be called by a Root origin.

The deposit taken can be specified for this registration. Any `ParaId`
can be registered, including sub-1000 IDs which are System Parachains.
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
Register head data and validation code for a reserved Para Id.

\#\# Arguments
- `origin`: Must be called by a `Signed` origin.
- `id`: The para ID. Must be owned/managed by the `origin` signing account.
- `genesis_head`: The genesis head data of the parachain/thread.
- `validation_code`: The initial validation code of the parachain/thread.

\#\# Deposits/Fees
The origin signed account must reserve a corresponding deposit for the registration. Anything already
reserved previously for this para ID is accounted for.

\#\# Events
The `Registered` event is emitted in case of success.
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
Remove a manager lock from a para. This will allow the manager of a
previously locked para to deregister or swap a para without using governance.

Can only be called by the Root origin or the parachain.
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
Reserve a Para Id on the relay chain.

This function will reserve a new Para Id to be owned/managed by the origin account.
The origin account is able to register head data and validation code using `register` to create
a parathread. Using the Slots pallet, a parathread can then be upgraded to get a parachain slot.

\#\# Arguments
- `origin`: Must be called by a `Signed` origin. Becomes the manager/owner of the new para ID.

\#\# Deposits/Fees
The origin must reserve a deposit of `ParaDeposit` for the registration.

\#\# Events
The `Reserved` event is emitted in case of success, which provides the ID reserved for use.
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
Schedule a parachain upgrade.

Can be called by Root, the parachain, or the parachain manager if the parachain is unlocked.
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
Set the parachain&\#x27;s current head.

Can be called by Root, the parachain, or the parachain manager if the parachain is unlocked.
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
Swap a parachain with another parachain or parathread.

The origin must be Root, the `para` owner, or the `para` itself.

The swap will happen only if there is already an opposite swap pending. If there is not,
the swap will be stored in the pending swaps map, ready for a later confirmatory swap.

The `ParaId`s remain mapped to the same head data and code so external code can rely on
`ParaId` to be a long-term identifier of a notional &quot;parachain&quot;. However, their
scheduling info (i.e. whether they&\#x27;re a parathread or parachain), auction information
and the auction deposit are switched.
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

 The given account ID is responsible for registering the code and initial head data, but may only do
 so if it isn&#x27;t yet registered. (After that, it&#x27;s up to governance to do so.)

#### Python
```python
result = substrate.query(
    'Registrar', 'Paras', ['u32']
)
```

#### Return value
```python
{'deposit': 'u128', 'locked': 'bool', 'manager': 'AccountId'}
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
10000000
```
#### Python
```python
constant = substrate.get_constant('Registrar', 'DataDepositPerByte')
```
---------
### ParaDeposit
 The deposit to be paid to run a parathread.
 This should include the cost for storing the genesis head and validation code.
#### Value
```python
1000000000000
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
Cannot schedule downgrade of parachain to parathread

---------
### CannotSwap
Cannot perform a parachain slot / lifecycle swap. Check that the state of both paras are
correct for the swap to work.

---------
### CannotUpgrade
Cannot schedule upgrade of parathread to parachain

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
Para is not a Parathread.

---------
### NotRegistered
The ID is not registered.

---------
### NotReserved
The ID given for registration has not been reserved.

---------
### ParaLocked
Para is locked from manipulation by the manager. Must use parachain or relay chain governance.

---------