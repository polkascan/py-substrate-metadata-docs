
# EthereumXcm

---------
## Calls

---------
### resume_ethereum_xcm_execution
See `Pallet::resume_ethereum_xcm_execution`.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'EthereumXcm', 'resume_ethereum_xcm_execution', {}
)
```

---------
### suspend_ethereum_xcm_execution
See `Pallet::suspend_ethereum_xcm_execution`.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'EthereumXcm', 'suspend_ethereum_xcm_execution', {}
)
```

---------
### transact
See `Pallet::transact`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| xcm_transaction | `EthereumXcmTransaction` | 

#### Python
```python
call = substrate.compose_call(
    'EthereumXcm', 'transact', {
    'xcm_transaction': {
        'V1': {
            'access_list': (
                None,
                [
                    (
                        '[u8; 20]',
                        [
                            'scale_info::12',
                        ],
                    ),
                ],
            ),
            'action': {
                'Call': '[u8; 20]',
                'Create': None,
            },
            'fee_payment': {
                'Auto': None,
                'Manual': {
                    'gas_price': (
                        None,
                        'scale_info::187',
                    ),
                    'max_fee_per_gas': (
                        None,
                        'scale_info::187',
                    ),
                },
            },
            'gas_limit': 'scale_info::187',
            'input': 'Bytes',
            'value': 'scale_info::187',
        },
        'V2': {
            'access_list': (
                None,
                [
                    (
                        '[u8; 20]',
                        [
                            'scale_info::12',
                        ],
                    ),
                ],
            ),
            'action': {
                'Call': '[u8; 20]',
                'Create': None,
            },
            'gas_limit': 'scale_info::187',
            'input': 'Bytes',
            'value': 'scale_info::187',
        },
    },
}
)
```

---------
### transact_through_proxy
See `Pallet::transact_through_proxy`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| transact_as | `H160` | 
| xcm_transaction | `EthereumXcmTransaction` | 

#### Python
```python
call = substrate.compose_call(
    'EthereumXcm', 'transact_through_proxy', {
    'transact_as': '[u8; 20]',
    'xcm_transaction': {
        'V1': {
            'access_list': (
                None,
                [
                    (
                        '[u8; 20]',
                        [
                            'scale_info::12',
                        ],
                    ),
                ],
            ),
            'action': {
                'Call': '[u8; 20]',
                'Create': None,
            },
            'fee_payment': {
                'Auto': None,
                'Manual': {
                    'gas_price': (
                        None,
                        'scale_info::187',
                    ),
                    'max_fee_per_gas': (
                        None,
                        'scale_info::187',
                    ),
                },
            },
            'gas_limit': 'scale_info::187',
            'input': 'Bytes',
            'value': 'scale_info::187',
        },
        'V2': {
            'access_list': (
                None,
                [
                    (
                        '[u8; 20]',
                        [
                            'scale_info::12',
                        ],
                    ),
                ],
            ),
            'action': {
                'Call': '[u8; 20]',
                'Create': None,
            },
            'gas_limit': 'scale_info::187',
            'input': 'Bytes',
            'value': 'scale_info::187',
        },
    },
}
)
```

---------
## Storage functions

---------
### EthereumXcmSuspended
 Whether or not Ethereum-XCM is suspended from executing

#### Python
```python
result = substrate.query(
    'EthereumXcm', 'EthereumXcmSuspended', []
)
```

#### Return value
```python
'bool'
```
---------
### Nonce
 Global nonce used for building Ethereum transaction payload.

#### Python
```python
result = substrate.query(
    'EthereumXcm', 'Nonce', []
)
```

#### Return value
```python
'scale_info::187'
```
---------
## Errors

---------
### EthereumXcmExecutionSuspended
Xcm to Ethereum execution is suspended

---------