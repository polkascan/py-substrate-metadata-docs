
# CurrencyFactory

---------
## Calls

---------
### add_range
#### Attributes
| Name | Type |
| -------- | -------- | 
| length | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'CurrencyFactory', 'add_range', {'length': 'u64'}
)
```

---------
### set_metadata
Sets metadata
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| metadata | `BasicAssetMetadata` | 

#### Python
```python
call = substrate.compose_call(
    'CurrencyFactory', 'set_metadata', {
    'asset_id': 'u128',
    'metadata': {
        'name': {'inner': 'Bytes'},
        'symbol': {'inner': 'Bytes'},
    },
}
)
```

---------
## Events

---------
### RangeCreated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| range | `Range<T::AssetId>` | ```{'current': 'u128', 'end': 'u128'}```

---------
## Storage functions

---------
### AssetEd

#### Python
```python
result = substrate.query(
    'CurrencyFactory', 'AssetEd', ['u128']
)
```

#### Return value
```python
'u128'
```
---------
### AssetIdRanges

#### Python
```python
result = substrate.query(
    'CurrencyFactory', 'AssetIdRanges', []
)
```

#### Return value
```python
{'ranges': [{'current': 'u128', 'end': 'u128'}]}
```
---------
### AssetMetadata

#### Python
```python
result = substrate.query(
    'CurrencyFactory', 'AssetMetadata', ['u128']
)
```

#### Return value
```python
{'name': {'inner': 'Bytes'}, 'symbol': {'inner': 'Bytes'}}
```
---------
## Errors

---------
### AssetNotFound

---------