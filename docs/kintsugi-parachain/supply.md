
# Supply

---------
## Calls

---------
### set_start_height_and_inflation
#### Attributes
| Name | Type |
| -------- | -------- | 
| start_height | `T::BlockNumber` | 
| inflation | `T::UnsignedFixedPoint` | 

#### Python
```python
call = substrate.compose_call(
    'Supply', 'set_start_height_and_inflation', {
    'inflation': 'u128',
    'start_height': 'u32',
}
)
```

---------
## Events

---------
### Inflation
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| total_inflation | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### Inflation

#### Python
```python
result = substrate.query(
    'Supply', 'Inflation', []
)
```

#### Return value
```python
'u128'
```
---------
### LastEmission

#### Python
```python
result = substrate.query(
    'Supply', 'LastEmission', []
)
```

#### Return value
```python
'u128'
```
---------
### StartHeight

#### Python
```python
result = substrate.query(
    'Supply', 'StartHeight', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### InflationPeriod
 The period between inflation updates.
#### Value
```python
2628000
```
#### Python
```python
constant = substrate.get_constant('Supply', 'InflationPeriod')
```
---------
### SupplyPalletId
 The supply module id, used for deriving its sovereign account ID.
#### Value
```python
'0x6d6f642f7375706c'
```
#### Python
```python
constant = substrate.get_constant('Supply', 'SupplyPalletId')
```
---------