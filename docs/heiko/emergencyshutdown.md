
# EmergencyShutdown

---------
## Calls

---------
### toggle_call
#### Attributes
| Name | Type |
| -------- | -------- | 
| pallet_idx | `u8` | 
| call_idx | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'EmergencyShutdown', 'toggle_call', {'call_idx': 'u8', 'pallet_idx': 'u8'}
)
```

---------
### toggle_pallet
Toggle the shutdown flag
#### Attributes
| Name | Type |
| -------- | -------- | 
| pallet_idx | `u8` | 

#### Python
```python
call = substrate.compose_call(
    'EmergencyShutdown', 'toggle_pallet', {'pallet_idx': 'u8'}
)
```

---------
## Events

---------
### ToggledCall
Toggled Call
[flag]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `bool` | ```bool```

---------
### ToggledPallet
Toggled Pallet
[flag]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `bool` | ```bool```

---------
## Storage functions

---------
### DisabledCalls

#### Python
```python
result = substrate.query(
    'EmergencyShutdown', 'DisabledCalls', ['u8', 'u8']
)
```

#### Return value
```python
'bool'
```
---------
### DisabledPallets

#### Python
```python
result = substrate.query(
    'EmergencyShutdown', 'DisabledPallets', ['u8']
)
```

#### Return value
```python
'bool'
```
---------