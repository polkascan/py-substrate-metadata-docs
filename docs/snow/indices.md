
# Indices

---------
## Calls

---------
### claim
Assign an previously unassigned index.

Payment: `Deposit` is reserved from the sender account.

The dispatch origin for this call must be _Signed_.

- `index`: the index to be claimed. This must not be in use.

Emits `IndexAssigned` if successful.

\# &lt;weight&gt;
- `O(1)`.
- One storage mutation (codec `O(1)`).
- One reserve operation.
- One event.
-------------------
- DB Weight: 1 Read/Write (Accounts)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `T::AccountIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Indices', 'claim', {'index': 'u32'}
)
```

---------
### force_transfer
Force an index to an account. This doesn&\#x27;t require a deposit. If the index is already
held, then any deposit is reimbursed to its current owner.

The dispatch origin for this call must be _Root_.

- `index`: the index to be (re-)assigned.
- `new`: the new owner of the index. This function is a no-op if it is equal to sender.
- `freeze`: if set to `true`, will freeze the index so it cannot be transferred.

Emits `IndexAssigned` if successful.

\# &lt;weight&gt;
- `O(1)`.
- One storage mutation (codec `O(1)`).
- Up to one reserve operation.
- One event.
-------------------
- DB Weight:
   - Reads: Indices Accounts, System Account (original owner)
   - Writes: Indices Accounts, System Account (original owner)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `AccountIdLookupOf<T>` | 
| index | `T::AccountIndex` | 
| freeze | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Indices', 'force_transfer', {
    'freeze': 'bool',
    'index': 'u32',
    'new': {
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
### free
Free up an index owned by the sender.

Payment: Any previous deposit placed for the index is unreserved in the sender account.

The dispatch origin for this call must be _Signed_ and the sender must own the index.

- `index`: the index to be freed. This must be owned by the sender.

Emits `IndexFreed` if successful.

\# &lt;weight&gt;
- `O(1)`.
- One storage mutation (codec `O(1)`).
- One reserve operation.
- One event.
-------------------
- DB Weight: 1 Read/Write (Accounts)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `T::AccountIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Indices', 'free', {'index': 'u32'}
)
```

---------
### freeze
Freeze an index so it will always point to the sender account. This consumes the
deposit.

The dispatch origin for this call must be _Signed_ and the signing account must have a
non-frozen account `index`.

- `index`: the index to be frozen in place.

Emits `IndexFrozen` if successful.

\# &lt;weight&gt;
- `O(1)`.
- One storage mutation (codec `O(1)`).
- Up to one slash operation.
- One event.
-------------------
- DB Weight: 1 Read/Write (Accounts)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `T::AccountIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Indices', 'freeze', {'index': 'u32'}
)
```

---------
### transfer
Assign an index already owned by the sender to another account. The balance reservation
is effectively transferred to the new account.

The dispatch origin for this call must be _Signed_.

- `index`: the index to be re-assigned. This must be owned by the sender.
- `new`: the new owner of the index. This function is a no-op if it is equal to sender.

Emits `IndexAssigned` if successful.

\# &lt;weight&gt;
- `O(1)`.
- One storage mutation (codec `O(1)`).
- One transfer operation.
- One event.
-------------------
- DB Weight:
   - Reads: Indices Accounts, System Account (recipient)
   - Writes: Indices Accounts, System Account (recipient)
\# &lt;/weight&gt;
#### Attributes
| Name | Type |
| -------- | -------- | 
| new | `AccountIdLookupOf<T>` | 
| index | `T::AccountIndex` | 

#### Python
```python
call = substrate.compose_call(
    'Indices', 'transfer', {
    'index': 'u32',
    'new': {
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
### IndexAssigned
A account index was assigned.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| index | `T::AccountIndex` | ```u32```

---------
### IndexFreed
A account index has been freed up (unassigned).
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `T::AccountIndex` | ```u32```

---------
### IndexFrozen
A account index has been frozen to its current account ID.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| index | `T::AccountIndex` | ```u32```
| who | `T::AccountId` | ```AccountId```

---------
## Storage functions

---------
### Accounts
 The lookup from index to account.

#### Python
```python
result = substrate.query(
    'Indices', 'Accounts', ['u32']
)
```

#### Return value
```python
('AccountId', 'u128', 'bool')
```
---------
## Constants

---------
### Deposit
 The deposit needed for reserving an index.
#### Value
```python
1000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Indices', 'Deposit')
```
---------
## Errors

---------
### InUse
The index was not available.

---------
### NotAssigned
The index was not already assigned.

---------
### NotOwner
The index is assigned to another account.

---------
### NotTransfer
The source and destination accounts are identical.

---------
### Permanent
The index is permanent and may not be freed/changed.

---------