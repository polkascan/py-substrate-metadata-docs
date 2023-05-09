
# Ethereum

---------
## Calls

---------
### transact
Transact an Ethereum transaction.
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
                        '[u8; 32]',
                    ],
                },
            ],
            'action': {
                'Call': '[u8; 20]',
                'Create': None,
            },
            'chain_id': 'u64',
            'gas_limit': '[u64; 4]',
            'input': 'Bytes',
            'max_fee_per_gas': '[u64; 4]',
            'max_priority_fee_per_gas': '[u64; 4]',
            'nonce': '[u64; 4]',
            'odd_y_parity': 'bool',
            'r': '[u8; 32]',
            's': '[u8; 32]',
            'value': '[u64; 4]',
        },
        'EIP2930': {
            'access_list': [
                {
                    'address': '[u8; 20]',
                    'storage_keys': [
                        '[u8; 32]',
                    ],
                },
            ],
            'action': {
                'Call': '[u8; 20]',
                'Create': None,
            },
            'chain_id': 'u64',
            'gas_limit': '[u64; 4]',
            'gas_price': '[u64; 4]',
            'input': 'Bytes',
            'nonce': '[u64; 4]',
            'odd_y_parity': 'bool',
            'r': '[u8; 32]',
            's': '[u8; 32]',
            'value': '[u64; 4]',
        },
        'Legacy': {
            'action': {
                'Call': '[u8; 20]',
                'Create': None,
            },
            'gas_limit': '[u64; 4]',
            'gas_price': '[u64; 4]',
            'input': 'Bytes',
            'nonce': '[u64; 4]',
            'signature': {
                'r': '[u8; 32]',
                's': '[u8; 32]',
                'v': 'u64',
            },
            'value': '[u64; 4]',
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
| transaction_hash | `H256` | ```[u8; 32]```
| exit_reason | `ExitReason` | ```{'Succeed': ('Stopped', 'Returned', 'Suicided'), 'Error': {'StackUnderflow': None, 'StackOverflow': None, 'InvalidJump': None, 'InvalidRange': None, 'DesignatedInvalid': None, 'CallTooDeep': None, 'CreateCollision': None, 'CreateContractLimit': None, 'OutOfOffset': None, 'OutOfGas': None, 'OutOfFund': None, 'PCUnderflow': None, 'CreateEmpty': None, 'Other': 'Str', None: None, 'InvalidCode': 'u8'}, 'Revert': ('Reverted',), 'Fatal': {'NotSupported': None, 'UnhandledInterrupt': None, 'CallErrorAsFatal': {'StackUnderflow': None, 'StackOverflow': None, 'InvalidJump': None, 'InvalidRange': None, 'DesignatedInvalid': None, 'CallTooDeep': None, 'CreateCollision': None, 'CreateContractLimit': None, 'OutOfOffset': None, 'OutOfGas': None, 'OutOfFund': None, 'PCUnderflow': None, 'CreateEmpty': None, 'Other': 'Str', None: None, 'InvalidCode': 'u8'}, 'Other': 'Str'}}```

---------
## Storage functions

---------
### BlockHash

#### Python
```python
result = substrate.query(
    'Ethereum', 'BlockHash', ['[u64; 4]']
)
```

#### Return value
```python
'[u8; 32]'
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
        'difficulty': '[u64; 4]',
        'extra_data': 'Bytes',
        'gas_limit': '[u64; 4]',
        'gas_used': '[u64; 4]',
        'logs_bloom': '[u8; 256]',
        'mix_hash': '[u8; 32]',
        'nonce': '[u8; 8]',
        'number': '[u64; 4]',
        'ommers_hash': '[u8; 32]',
        'parent_hash': '[u8; 32]',
        'receipts_root': '[u8; 32]',
        'state_root': '[u8; 32]',
        'timestamp': 'u64',
        'transactions_root': '[u8; 32]',
    },
    'ommers': [
        {
            'beneficiary': '[u8; 20]',
            'difficulty': '[u64; 4]',
            'extra_data': 'Bytes',
            'gas_limit': '[u64; 4]',
            'gas_used': '[u64; 4]',
            'logs_bloom': '[u8; 256]',
            'mix_hash': '[u8; 32]',
            'nonce': '[u8; 8]',
            'number': '[u64; 4]',
            'ommers_hash': '[u8; 32]',
            'parent_hash': '[u8; 32]',
            'receipts_root': '[u8; 32]',
            'state_root': '[u8; 32]',
            'timestamp': 'u64',
            'transactions_root': '[u8; 32]',
        },
    ],
    'transactions': [
        {
            'EIP1559': {
                'access_list': ['scale_info::319'],
                'action': {'Call': '[u8; 20]', 'Create': None},
                'chain_id': 'u64',
                'gas_limit': '[u64; 4]',
                'input': 'Bytes',
                'max_fee_per_gas': '[u64; 4]',
                'max_priority_fee_per_gas': '[u64; 4]',
                'nonce': '[u64; 4]',
                'odd_y_parity': 'bool',
                'r': '[u8; 32]',
                's': '[u8; 32]',
                'value': '[u64; 4]',
            },
            'EIP2930': {
                'access_list': ['scale_info::319'],
                'action': {'Call': '[u8; 20]', 'Create': None},
                'chain_id': 'u64',
                'gas_limit': '[u64; 4]',
                'gas_price': '[u64; 4]',
                'input': 'Bytes',
                'nonce': '[u64; 4]',
                'odd_y_parity': 'bool',
                'r': '[u8; 32]',
                's': '[u8; 32]',
                'value': '[u64; 4]',
            },
            'Legacy': {
                'action': {'Call': '[u8; 20]', 'Create': None},
                'gas_limit': '[u64; 4]',
                'gas_price': '[u64; 4]',
                'input': 'Bytes',
                'nonce': '[u64; 4]',
                'signature': {'r': '[u8; 32]', 's': '[u8; 32]', 'v': 'u64'},
                'value': '[u64; 4]',
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
                    'topics': ['[u8; 32]'],
                },
            ],
            'logs_bloom': '[u8; 256]',
            'status_code': 'u8',
            'used_gas': '[u64; 4]',
        },
        'EIP2930': {
            'logs': [
                {
                    'address': '[u8; 20]',
                    'data': 'Bytes',
                    'topics': ['[u8; 32]'],
                },
            ],
            'logs_bloom': '[u8; 256]',
            'status_code': 'u8',
            'used_gas': '[u64; 4]',
        },
        'Legacy': {
            'logs': [
                {
                    'address': '[u8; 20]',
                    'data': 'Bytes',
                    'topics': ['[u8; 32]'],
                },
            ],
            'logs_bloom': '[u8; 256]',
            'status_code': 'u8',
            'used_gas': '[u64; 4]',
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
            {'address': '[u8; 20]', 'data': 'Bytes', 'topics': ['[u8; 32]']},
        ],
        'logs_bloom': '[u8; 256]',
        'to': (None, '[u8; 20]'),
        'transaction_hash': '[u8; 32]',
        'transaction_index': 'u32',
    },
]
```
---------
### InjectedNonce
 Injected transactions should have unique nonce, here we store current

#### Python
```python
result = substrate.query(
    'Ethereum', 'InjectedNonce', []
)
```

#### Return value
```python
'[u64; 4]'
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
                'access_list': ['scale_info::319'],
                'action': {'Call': '[u8; 20]', 'Create': None},
                'chain_id': 'u64',
                'gas_limit': '[u64; 4]',
                'input': 'Bytes',
                'max_fee_per_gas': '[u64; 4]',
                'max_priority_fee_per_gas': '[u64; 4]',
                'nonce': '[u64; 4]',
                'odd_y_parity': 'bool',
                'r': '[u8; 32]',
                's': '[u8; 32]',
                'value': '[u64; 4]',
            },
            'EIP2930': {
                'access_list': ['scale_info::319'],
                'action': {'Call': '[u8; 20]', 'Create': None},
                'chain_id': 'u64',
                'gas_limit': '[u64; 4]',
                'gas_price': '[u64; 4]',
                'input': 'Bytes',
                'nonce': '[u64; 4]',
                'odd_y_parity': 'bool',
                'r': '[u8; 32]',
                's': '[u8; 32]',
                'value': '[u64; 4]',
            },
            'Legacy': {
                'action': {'Call': '[u8; 20]', 'Create': None},
                'gas_limit': '[u64; 4]',
                'gas_price': '[u64; 4]',
                'input': 'Bytes',
                'nonce': '[u64; 4]',
                'signature': {'r': '[u8; 32]', 's': '[u8; 32]', 'v': 'u64'},
                'value': '[u64; 4]',
            },
        },
        {
            'contract_address': (None, '[u8; 20]'),
            'from': '[u8; 20]',
            'logs': [
                {
                    'address': '[u8; 20]',
                    'data': 'Bytes',
                    'topics': ['[u8; 32]'],
                },
            ],
            'logs_bloom': '[u8; 256]',
            'to': (None, '[u8; 20]'),
            'transaction_hash': '[u8; 32]',
            'transaction_index': 'u32',
        },
        {
            'EIP1559': {
                'logs': ['scale_info::122'],
                'logs_bloom': '[u8; 256]',
                'status_code': 'u8',
                'used_gas': '[u64; 4]',
            },
            'EIP2930': {
                'logs': ['scale_info::122'],
                'logs_bloom': '[u8; 256]',
                'status_code': 'u8',
                'used_gas': '[u64; 4]',
            },
            'Legacy': {
                'logs': ['scale_info::122'],
                'logs_bloom': '[u8; 256]',
                'status_code': 'u8',
                'used_gas': '[u64; 4]',
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