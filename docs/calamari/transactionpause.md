
# TransactionPause

---------
## Calls

---------
### pause_pallets
Pause all the calls of the listed pallets in `pallet_names`.
This logic is in its own extrinsic in order to not have to pause calls 1 by 1.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pallet_names | `Vec<Vec<u8>>` | 

#### Python
```python
call = substrate.compose_call(
    'TransactionPause', 'pause_pallets', {'pallet_names': ['Bytes']}
)
```

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
### pause_transactions
Pause extrinsics by passing the extrinsic and corresponding pallet names.
Use names as they are written in the source code of the pallet.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pallet_and_funcs | `Vec<(Vec<u8>, Vec<Vec<u8>>)>` | 

#### Python
```python
call = substrate.compose_call(
    'TransactionPause', 'pause_transactions', {
    'pallet_and_funcs': [
        ('Bytes', ['Bytes']),
    ],
}
)
```

---------
### unpause_pallets
Unpause all the calls of the listed pallets in `pallet_names`.
This logic is in its own extrinsic in order to not have to pause calls 1 by 1.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pallet_names | `Vec<Vec<u8>>` | 

#### Python
```python
call = substrate.compose_call(
    'TransactionPause', 'unpause_pallets', {'pallet_names': ['Bytes']}
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
### unpause_transactions
Unpause extrinsics by passing the extrinsic and corresponding pallet names.
Use names as they are written in the source code of the pallet.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pallet_and_funcs | `Vec<(Vec<u8>, Vec<Vec<u8>>)>` | 

#### Python
```python
call = substrate.compose_call(
    'TransactionPause', 'unpause_transactions', {
    'pallet_and_funcs': [
        ('Bytes', ['Bytes']),
    ],
}
)
```

---------
## Events

---------
### PalletPaused
Paused pallet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<u8>` | ```Bytes```

---------
### PalletUnpaused
Unpaused pallet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<u8>` | ```Bytes```

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
### TooManyCalls
call of pallet too many

---------