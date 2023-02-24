
# CurrencyFactory

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