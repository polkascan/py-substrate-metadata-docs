
# Parameters

---------
## Calls

---------
### set_parameter
#### Attributes
| Name | Type |
| -------- | -------- | 
| key_value | `T::AggregratedKeyValue` | 

#### Python
```python
call = substrate.compose_call(
    'Parameters', 'set_parameter', {
    'key_value': {
        'Earning': {
            'InstantUnstakeFee': (
                {},
                (None, 'u32'),
            ),
        },
    },
}
)
```

---------
## Events

---------
### Updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| key_value | `T::AggregratedKeyValue` | ```{'Earning': {'InstantUnstakeFee': ({}, (None, 'u32'))}}```

---------
## Storage functions

---------
### Parameters

#### Python
```python
result = substrate.query(
    'Parameters', 'Parameters', [{'Earning': {'InstantUnstakeFee': {}}}]
)
```

#### Return value
```python
{'Earning': {'InstantUnstakeFee': 'u32'}}
```
---------