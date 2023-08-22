
# TransactionPause

---------
## Calls

---------
### pause_transaction
#### Attributes
| Name | Type |
| -------- | -------- | 
| pallet_name | `Vec<u8>` | 
| function_name | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'TransactionPause', 'pause_transaction', {
    'function_name': 'Bytes',
    'pallet_name': 'Bytes',
}
)
```

---------
### unpause_transaction
#### Attributes
| Name | Type |
| -------- | -------- | 
| pallet_name | `Vec<u8>` | 
| function_name | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'TransactionPause', 'unpause_transaction', {
    'function_name': 'Bytes',
    'pallet_name': 'Bytes',
}
)
```

---------
## Events

---------
### TransactionPaused
Paused transaction
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pallet_name_bytes | `Vec<u8>` | ```Bytes```
| function_name_bytes | `Vec<u8>` | ```Bytes```

---------
### TransactionUnpaused
Unpaused transaction
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pallet_name_bytes | `Vec<u8>` | ```Bytes```
| function_name_bytes | `Vec<u8>` | ```Bytes```

---------
## Storage functions

---------
### PausedTransactions
 The paused transaction map

 map (PalletNameBytes, FunctionNameBytes) =&gt; Option&lt;()&gt;

#### Python
```python
result = substrate.query(
    'TransactionPause', 'PausedTransactions', [('Bytes', 'Bytes')]
)
```

#### Return value
```python
()
```
---------
## Errors

---------
### CannotPause
can not pause

---------
### InvalidCharacter
invalid character encoding

---------
### NameTooLong
pallet name or function name is too long

---------