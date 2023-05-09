
# Ics20Fee

---------
## Calls

---------
### set_charge
#### Attributes
| Name | Type |
| -------- | -------- | 
| charge | `Perbill` | 

#### Python
```python
call = substrate.compose_call(
    'Ics20Fee', 'set_charge', {'charge': 'u32'}
)
```

---------
## Events

---------
### IbcTransferFeeCollected
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| amount | `T::Balance` | ```u128```

---------
## Storage functions

---------
### ServiceCharge

#### Python
```python
result = substrate.query(
    'Ics20Fee', 'ServiceCharge', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### PalletId
#### Value
```python
'0x6963733230666565'
```
#### Python
```python
constant = substrate.get_constant('Ics20Fee', 'PalletId')
```
---------
### ServiceCharge
#### Value
```python
4000000
```
#### Python
```python
constant = substrate.get_constant('Ics20Fee', 'ServiceCharge')
```
---------