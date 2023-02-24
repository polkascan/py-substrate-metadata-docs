
# Prices

---------
## Calls

---------
### reset_price
Reset emergency price
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `CurrencyId` | 

#### Python
```python
call = substrate.compose_call(
    'Prices', 'reset_price', {'asset_id': 'u32'}
)
```

---------
### set_foreign_asset
Set foreign vault token mapping
#### Attributes
| Name | Type |
| -------- | -------- | 
| foreign_asset_id | `CurrencyId` | 
| asset_id | `CurrencyId` | 

#### Python
```python
call = substrate.compose_call(
    'Prices', 'set_foreign_asset', {
    'asset_id': 'u32',
    'foreign_asset_id': 'u32',
}
)
```

---------
### set_price
Set emergency price
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `CurrencyId` | 
| price | `Price` | 

#### Python
```python
call = substrate.compose_call(
    'Prices', 'set_price', {'asset_id': 'u32', 'price': 'u128'}
)
```

---------
## Events

---------
### ResetPrice
Reset emergency price. \[asset_id\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CurrencyId` | ```u32```

---------
### SetPrice
Set emergency price. \[asset_id, price_detail\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `CurrencyId` | ```u32```
| None | `Price` | ```u128```

---------
## Storage functions

---------
### EmergencyPrice
 Mapping from currency id to it&#x27;s emergency price

#### Python
```python
result = substrate.query(
    'Prices', 'EmergencyPrice', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### ForeignToNativeAsset
 Mapping from foreign vault token to our&#x27;s vault token

#### Python
```python
result = substrate.query(
    'Prices', 'ForeignToNativeAsset', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### RelayCurrency
 Relay currency
#### Value
```python
101
```
#### Python
```python
constant = substrate.get_constant('Prices', 'RelayCurrency')
```
---------