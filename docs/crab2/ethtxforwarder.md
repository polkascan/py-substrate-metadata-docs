
# EthTxForwarder

---------
## Calls

---------
### forward_transact
See [`Pallet::forward_transact`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| transaction | `Box<Transaction>` | 

#### Python
```python
call = substrate.compose_call(
    'EthTxForwarder', 'forward_transact', {
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
            'gas_limit': 'scale_info::249',
            'input': 'Bytes',
            'max_fee_per_gas': 'scale_info::249',
            'max_priority_fee_per_gas': 'scale_info::249',
            'nonce': 'scale_info::249',
            'odd_y_parity': 'bool',
            'r': 'scale_info::12',
            's': 'scale_info::12',
            'value': 'scale_info::249',
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
            'gas_limit': 'scale_info::249',
            'gas_price': 'scale_info::249',
            'input': 'Bytes',
            'nonce': 'scale_info::249',
            'odd_y_parity': 'bool',
            'r': 'scale_info::12',
            's': 'scale_info::12',
            'value': 'scale_info::249',
        },
        'Legacy': {
            'action': {
                'Call': '[u8; 20]',
                'Create': None,
            },
            'gas_limit': 'scale_info::249',
            'gas_price': 'scale_info::249',
            'input': 'Bytes',
            'nonce': 'scale_info::249',
            'signature': {
                'r': 'scale_info::12',
                's': 'scale_info::12',
                'v': 'u64',
            },
            'value': 'scale_info::249',
        },
    },
}
)
```

---------
## Errors

---------
### MessageTransactError
EVM validation errors.

---------