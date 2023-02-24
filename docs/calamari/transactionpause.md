
# TransactionPause

---------
## Calls

---------
### pause_transaction
Pause an extrinsic by passing the extrinsic and corresponding pallet names.
Use names as they are written in the source code of the pallet.
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
Unpause an extrinsic by passing the extrinsic and corresponding pallet names.
Use names as they are written in the source code of the pallet.
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
Paused transaction . \[pallet_name_bytes, function_name_bytes\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<u8>` | ```Bytes```
| None | `Vec<u8>` | ```Bytes```

---------
### TransactionUnpaused
Unpaused transaction . \[pallet_name_bytes, function_name_bytes\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<u8>` | ```Bytes```
| None | `Vec<u8>` | ```Bytes```

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