
# LiquidityPoolsAxelarGateway

---------
## Calls

---------
### set_converter
#### Attributes
| Name | Type |
| -------- | -------- | 
| id_hash | `H256` | 
| converter | `SourceConverter` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityPoolsAxelarGateway', 'set_converter', {
    'converter': {
        'domain': {
            'Centrifuge': None,
            'EVM': 'u64',
        },
    },
    'id_hash': '[u8; 32]',
}
)
```

---------
### set_gateway
#### Attributes
| Name | Type |
| -------- | -------- | 
| address | `H160` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityPoolsAxelarGateway', 'set_gateway', {'address': '[u8; 20]'}
)
```

---------
## Events

---------
### ConverterSet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| id_hash | `H256` | ```[u8; 32]```
| converter | `SourceConverter` | ```{'domain': {'Centrifuge': None, 'EVM': 'u64'}}```

---------
### GatewaySet
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| address | `H160` | ```[u8; 20]```

---------
## Storage functions

---------
### GatewayContract

#### Python
```python
result = substrate.query(
    'LiquidityPoolsAxelarGateway', 'GatewayContract', []
)
```

#### Return value
```python
'[u8; 20]'
```
---------
### SourceConversion
 `SourceConversion` is a `hash_of(Vec&lt;u8&gt;)` where the `Vec&lt;u8&gt;` is the
 blake256-hash of the source-chain identifier used by the Axelar network.

#### Python
```python
result = substrate.query(
    'LiquidityPoolsAxelarGateway', 'SourceConversion', ['[u8; 32]']
)
```

#### Return value
```python
{'domain': {'Centrifuge': None, 'EVM': 'u64'}}
```
---------
## Errors

---------
### AccountBytesMismatchForDomain
A given domain expects a given structure for account bytes and it
was not given here.

---------
### NoConverterForSource
The given domain is not yet allowlisted, as we have no converter yet

---------