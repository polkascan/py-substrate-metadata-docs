
# TransactionPause

---------
## Calls

---------
### pause_evm_precompile
#### Attributes
| Name | Type |
| -------- | -------- | 
| address | `H160` | 

#### Python
```python
call = substrate.compose_call(
    'TransactionPause', 'pause_evm_precompile', {'address': '[u8; 20]'}
)
```

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
### unpause_evm_precompile
#### Attributes
| Name | Type |
| -------- | -------- | 
| address | `H160` | 

#### Python
```python
call = substrate.compose_call(
    'TransactionPause', 'unpause_evm_precompile', {'address': '[u8; 20]'}
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
### EvmPrecompilePaused
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| address | `H160` | ```[u8; 20]```

---------
### EvmPrecompileUnpaused
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| address | `H160` | ```[u8; 20]```

---------
### TransactionPaused
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pallet_name_bytes | `Vec<u8>` | ```Bytes```
| function_name_bytes | `Vec<u8>` | ```Bytes```

---------
### TransactionUnpaused
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pallet_name_bytes | `Vec<u8>` | ```Bytes```
| function_name_bytes | `Vec<u8>` | ```Bytes```

---------
## Storage functions

---------
### PausedEvmPrecompiles

#### Python
```python
result = substrate.query(
    'TransactionPause', 'PausedEvmPrecompiles', ['[u8; 20]']
)
```

#### Return value
```python
()
```
---------
### PausedTransactions

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

---------
### InvalidCharacter

---------