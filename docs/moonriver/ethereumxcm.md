
# EthereumXcm

---------
## Calls

---------
### resume_ethereum_xcm_execution
Resumes all Ethereum executions from XCM.

- `origin`: Must pass `ControllerOrigin`.
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
Suspends all Ethereum executions from XCM.

- `origin`: Must pass `ControllerOrigin`.
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
Xcm Transact an Ethereum transaction.
Weight: Gas limit plus the db read involving the suspension check
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
                        ['[u8; 32]'],
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
                        '[u64; 4]',
                    ),
                    'max_fee_per_gas': (
                        None,
                        '[u64; 4]',
                    ),
                },
            },
            'gas_limit': '[u64; 4]',
            'input': 'Bytes',
            'value': '[u64; 4]',
        },
        'V2': {
            'access_list': (
                None,
                [
                    (
                        '[u8; 20]',
                        ['[u8; 32]'],
                    ),
                ],
            ),
            'action': {
                'Call': '[u8; 20]',
                'Create': None,
            },
            'gas_limit': '[u64; 4]',
            'input': 'Bytes',
            'value': '[u64; 4]',
        },
    },
}
)
```

---------
### transact_through_proxy
Xcm Transact an Ethereum transaction through proxy.
Weight: Gas limit plus the db reads involving the suspension and proxy checks
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
                        ['[u8; 32]'],
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
                        '[u64; 4]',
                    ),
                    'max_fee_per_gas': (
                        None,
                        '[u64; 4]',
                    ),
                },
            },
            'gas_limit': '[u64; 4]',
            'input': 'Bytes',
            'value': '[u64; 4]',
        },
        'V2': {
            'access_list': (
                None,
                [
                    (
                        '[u8; 20]',
                        ['[u8; 32]'],
                    ),
                ],
            ),
            'action': {
                'Call': '[u8; 20]',
                'Create': None,
            },
            'gas_limit': '[u64; 4]',
            'input': 'Bytes',
            'value': '[u64; 4]',
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
'[u64; 4]'
```
---------
## Errors

---------
### EthereumXcmExecutionSuspended
Xcm to Ethereum execution is suspended

---------