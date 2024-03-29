
# Ethereum

---------
## Calls

---------
### transact
See [`Pallet::transact`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| transaction | `Transaction` | 

#### Python
```python
call = substrate.compose_call(
    'Ethereum', 'transact', {
    'transaction': {
        'EIP1559': {
            'access_list': [
                {
                    'address': '[u8; 20]',
                    'storage_keys': [
                        'scale_info::12',
                    ],
                },
            ],
            'action': {
                'Call': '[u8; 20]',
                'Create': None,
            },
            'chain_id': 'u64',
            'gas_limit': 'scale_info::135',
            'input': 'Bytes',
            'max_fee_per_gas': 'scale_info::135',
            'max_priority_fee_per_gas': 'scale_info::135',
            'nonce': 'scale_info::135',
            'odd_y_parity': 'bool',
            'r': 'scale_info::12',
            's': 'scale_info::12',
            'value': 'scale_info::135',
        },
        'EIP2930': {
            'access_list': [
                {
                    'address': '[u8; 20]',
                    'storage_keys': [
                        'scale_info::12',
                    ],
                },
            ],
            'action': {
                'Call': '[u8; 20]',
                'Create': None,
            },
            'chain_id': 'u64',
            'gas_limit': 'scale_info::135',
            'gas_price': 'scale_info::135',
            'input': 'Bytes',
            'nonce': 'scale_info::135',
            'odd_y_parity': 'bool',
            'r': 'scale_info::12',
            's': 'scale_info::12',
            'value': 'scale_info::135',
        },
        'Legacy': {
            'action': {
                'Call': '[u8; 20]',
                'Create': None,
            },
            'gas_limit': 'scale_info::135',
            'gas_price': 'scale_info::135',
            'input': 'Bytes',
            'nonce': 'scale_info::135',
            'signature': {
                'r': 'scale_info::12',
                's': 'scale_info::12',
                'v': 'u64',
            },
            'value': 'scale_info::135',
        },
    },
}
)
```

---------
## Events

---------
### Executed
An ethereum transaction was successfully executed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `H160` | ```[u8; 20]```
| to | `H160` | ```[u8; 20]```
| transaction_hash | `H256` | ```scale_info::12```
| exit_reason | `ExitReason` | ```{'Succeed': ('Stopped', 'Returned', 'Suicided'), 'Error': {'StackUnderflow': None, 'StackOverflow': None, 'InvalidJump': None, 'InvalidRange': None, 'DesignatedInvalid': None, 'CallTooDeep': None, 'CreateCollision': None, 'CreateContractLimit': None, 'OutOfOffset': None, 'OutOfGas': None, 'OutOfFund': None, 'PCUnderflow': None, 'CreateEmpty': None, 'Other': 'Str', 'MaxNonce': None, 'InvalidCode': 'u8'}, 'Revert': ('Reverted',), 'Fatal': {'NotSupported': None, 'UnhandledInterrupt': None, 'CallErrorAsFatal': {'StackUnderflow': None, 'StackOverflow': None, 'InvalidJump': None, 'InvalidRange': None, 'DesignatedInvalid': None, 'CallTooDeep': None, 'CreateCollision': None, 'CreateContractLimit': None, 'OutOfOffset': None, 'OutOfGas': None, 'OutOfFund': None, 'PCUnderflow': None, 'CreateEmpty': None, 'Other': 'Str', 'MaxNonce': None, 'InvalidCode': 'u8'}, 'Other': 'Str'}}```
| extra_data | `Vec<u8>` | ```Bytes```

---------
## Storage functions

---------
### BlockHash

#### Python
```python
result = substrate.query(
    'Ethereum', 'BlockHash', ['scale_info::135']
)
```

#### Return value
```python
'scale_info::12'
```
---------
### CurrentBlock
 The current Ethereum block.

#### Python
```python
result = substrate.query(
    'Ethereum', 'CurrentBlock', []
)
```

#### Return value
```python
{
    'header': {
        'beneficiary': '[u8; 20]',
        'difficulty': 'scale_info::135',
        'extra_data': 'Bytes',
        'gas_limit': 'scale_info::135',
        'gas_used': 'scale_info::135',
        'logs_bloom': '[u8; 256]',
        'mix_hash': 'scale_info::12',
        'nonce': '[u8; 8]',
        'number': 'scale_info::135',
        'ommers_hash': 'scale_info::12',
        'parent_hash': 'scale_info::12',
        'receipts_root': 'scale_info::12',
        'state_root': 'scale_info::12',
        'timestamp': 'u64',
        'transactions_root': 'scale_info::12',
    },
    'ommers': [
        {
            'beneficiary': '[u8; 20]',
            'difficulty': 'scale_info::135',
            'extra_data': 'Bytes',
            'gas_limit': 'scale_info::135',
            'gas_used': 'scale_info::135',
            'logs_bloom': '[u8; 256]',
            'mix_hash': 'scale_info::12',
            'nonce': '[u8; 8]',
            'number': 'scale_info::135',
            'ommers_hash': 'scale_info::12',
            'parent_hash': 'scale_info::12',
            'receipts_root': 'scale_info::12',
            'state_root': 'scale_info::12',
            'timestamp': 'u64',
            'transactions_root': 'scale_info::12',
        },
    ],
    'transactions': [
        {
            'EIP1559': {
                'access_list': ['scale_info::282'],
                'action': {'Call': '[u8; 20]', 'Create': None},
                'chain_id': 'u64',
                'gas_limit': 'scale_info::135',
                'input': 'Bytes',
                'max_fee_per_gas': 'scale_info::135',
                'max_priority_fee_per_gas': 'scale_info::135',
                'nonce': 'scale_info::135',
                'odd_y_parity': 'bool',
                'r': 'scale_info::12',
                's': 'scale_info::12',
                'value': 'scale_info::135',
            },
            'EIP2930': {
                'access_list': ['scale_info::282'],
                'action': {'Call': '[u8; 20]', 'Create': None},
                'chain_id': 'u64',
                'gas_limit': 'scale_info::135',
                'gas_price': 'scale_info::135',
                'input': 'Bytes',
                'nonce': 'scale_info::135',
                'odd_y_parity': 'bool',
                'r': 'scale_info::12',
                's': 'scale_info::12',
                'value': 'scale_info::135',
            },
            'Legacy': {
                'action': {'Call': '[u8; 20]', 'Create': None},
                'gas_limit': 'scale_info::135',
                'gas_price': 'scale_info::135',
                'input': 'Bytes',
                'nonce': 'scale_info::135',
                'signature': {
                    'r': 'scale_info::12',
                    's': 'scale_info::12',
                    'v': 'u64',
                },
                'value': 'scale_info::135',
            },
        },
    ],
}
```
---------
### CurrentReceipts
 The current Ethereum receipts.

#### Python
```python
result = substrate.query(
    'Ethereum', 'CurrentReceipts', []
)
```

#### Return value
```python
[
    {
        'EIP1559': {
            'logs': [
                {
                    'address': '[u8; 20]',
                    'data': 'Bytes',
                    'topics': ['scale_info::12'],
                },
            ],
            'logs_bloom': '[u8; 256]',
            'status_code': 'u8',
            'used_gas': 'scale_info::135',
        },
        'EIP2930': {
            'logs': [
                {
                    'address': '[u8; 20]',
                    'data': 'Bytes',
                    'topics': ['scale_info::12'],
                },
            ],
            'logs_bloom': '[u8; 256]',
            'status_code': 'u8',
            'used_gas': 'scale_info::135',
        },
        'Legacy': {
            'logs': [
                {
                    'address': '[u8; 20]',
                    'data': 'Bytes',
                    'topics': ['scale_info::12'],
                },
            ],
            'logs_bloom': '[u8; 256]',
            'status_code': 'u8',
            'used_gas': 'scale_info::135',
        },
    },
]
```
---------
### CurrentTransactionStatuses
 The current transaction statuses.

#### Python
```python
result = substrate.query(
    'Ethereum', 'CurrentTransactionStatuses', []
)
```

#### Return value
```python
[
    {
        'contract_address': (None, '[u8; 20]'),
        'from': '[u8; 20]',
        'logs': [
            {
                'address': '[u8; 20]',
                'data': 'Bytes',
                'topics': ['scale_info::12'],
            },
        ],
        'logs_bloom': '[u8; 256]',
        'to': (None, '[u8; 20]'),
        'transaction_hash': 'scale_info::12',
        'transaction_index': 'u32',
    },
]
```
---------
### Pending
 Current building block&#x27;s transactions and receipts.

#### Python
```python
result = substrate.query(
    'Ethereum', 'Pending', []
)
```

#### Return value
```python
[
    (
        {
            'EIP1559': {
                'access_list': ['scale_info::282'],
                'action': {'Call': '[u8; 20]', 'Create': None},
                'chain_id': 'u64',
                'gas_limit': 'scale_info::135',
                'input': 'Bytes',
                'max_fee_per_gas': 'scale_info::135',
                'max_priority_fee_per_gas': 'scale_info::135',
                'nonce': 'scale_info::135',
                'odd_y_parity': 'bool',
                'r': 'scale_info::12',
                's': 'scale_info::12',
                'value': 'scale_info::135',
            },
            'EIP2930': {
                'access_list': ['scale_info::282'],
                'action': {'Call': '[u8; 20]', 'Create': None},
                'chain_id': 'u64',
                'gas_limit': 'scale_info::135',
                'gas_price': 'scale_info::135',
                'input': 'Bytes',
                'nonce': 'scale_info::135',
                'odd_y_parity': 'bool',
                'r': 'scale_info::12',
                's': 'scale_info::12',
                'value': 'scale_info::135',
            },
            'Legacy': {
                'action': {'Call': '[u8; 20]', 'Create': None},
                'gas_limit': 'scale_info::135',
                'gas_price': 'scale_info::135',
                'input': 'Bytes',
                'nonce': 'scale_info::135',
                'signature': {
                    'r': 'scale_info::12',
                    's': 'scale_info::12',
                    'v': 'u64',
                },
                'value': 'scale_info::135',
            },
        },
        {
            'contract_address': (None, '[u8; 20]'),
            'from': '[u8; 20]',
            'logs': [
                {
                    'address': '[u8; 20]',
                    'data': 'Bytes',
                    'topics': ['scale_info::12'],
                },
            ],
            'logs_bloom': '[u8; 256]',
            'to': (None, '[u8; 20]'),
            'transaction_hash': 'scale_info::12',
            'transaction_index': 'u32',
        },
        {
            'EIP1559': {
                'logs': ['scale_info::123'],
                'logs_bloom': '[u8; 256]',
                'status_code': 'u8',
                'used_gas': 'scale_info::135',
            },
            'EIP2930': {
                'logs': ['scale_info::123'],
                'logs_bloom': '[u8; 256]',
                'status_code': 'u8',
                'used_gas': 'scale_info::135',
            },
            'Legacy': {
                'logs': ['scale_info::123'],
                'logs_bloom': '[u8; 256]',
                'status_code': 'u8',
                'used_gas': 'scale_info::135',
            },
        },
    ),
]
```
---------
## Errors

---------
### InvalidSignature
Signature is invalid.

---------
### PreLogExists
Pre-log is present, therefore transact is not allowed.

---------