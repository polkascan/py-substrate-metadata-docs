
# Redeem

---------
## Calls

---------
### cancel_redeem
If a redeem request is not completed on time, the redeem request can be cancelled.
The user that initially requested the redeem process calls this function to obtain
the Vault’s collateral as compensation for not transferring the BTC back to their address.

\# Arguments

* `origin` - sender of the transaction
* `redeem_id` - identifier of redeem request as output from request_redeem
* `reimburse` - specifying if the user wishes to be reimbursed in collateral
and slash the Vault, or wishes to keep the tokens (and retry
Redeem with another Vault)
#### Attributes
| Name | Type |
| -------- | -------- | 
| redeem_id | `H256` | 
| reimburse | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Redeem', 'cancel_redeem', {
    'redeem_id': '[u8; 32]',
    'reimburse': 'bool',
}
)
```

---------
### execute_redeem
A Vault calls this function after receiving an RequestRedeem event with their public key.
Before calling the function, the Vault transfers the specific amount of BTC to the BTC address
given in the original redeem request. The Vault completes the redeem with this function.

\# Arguments

* `origin` - anyone executing this redeem request
* `redeem_id` - identifier of redeem request as output from request_redeem
* `tx_id` - transaction hash
* `merkle_proof` - membership proof
* `transaction` - tx containing payment

\#\# Complexity:
- `O(H + I + O + B)` where:
  - `H` is the number of hashes in the merkle tree
  - `I` is the number of transaction inputs
  - `O` is the number of transaction outputs
  - `B` is `transaction` size in bytes (length-fee-bounded)
#### Attributes
| Name | Type |
| -------- | -------- | 
| redeem_id | `H256` | 
| merkle_proof | `MerkleProof` | 
| transaction | `Transaction` | 
| length_bound | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'Redeem', 'execute_redeem', {
    'length_bound': 'u32',
    'merkle_proof': {
        'block_header': {
            'hash': {
                'content': '[u8; 32]',
            },
            'hash_prev_block': {
                'content': '[u8; 32]',
            },
            'merkle_root': {
                'content': '[u8; 32]',
            },
            'nonce': 'u32',
            'target': '[u64; 4]',
            'timestamp': 'u32',
            'version': 'i32',
        },
        'flag_bits': ['bool'],
        'hashes': [
            {'content': '[u8; 32]'},
        ],
        'transactions_count': 'u32',
    },
    'redeem_id': '[u8; 32]',
    'transaction': {
        'inputs': [
            {
                'script': 'Bytes',
                'sequence': 'u32',
                'source': {
                    'Coinbase': (
                        None,
                        'u32',
                    ),
                    'FromOutput': (
                        {
                            'content': '[u8; 32]',
                        },
                        'u32',
                    ),
                },
                'witness': ['Bytes'],
            },
        ],
        'lock_at': {
            'BlockHeight': 'u32',
            'Time': 'u32',
        },
        'outputs': [
            {
                'script': {
                    'bytes': 'Bytes',
                },
                'value': 'i64',
            },
        ],
        'version': 'i32',
    },
}
)
```

---------
### liquidation_redeem
When a Vault is liquidated, its collateral is slashed up to 150% of the liquidated BTC value.
To re-establish the physical 1:1 peg, the bridge allows users to burn issued tokens in return for
collateral at a premium rate.

\# Arguments

* `origin` - sender of the transaction
* `collateral_currency` - currency to be received
* `wrapped_currency` - currency of the wrapped token to burn
* `amount_wrapped` - amount of issued tokens to burn
#### Attributes
| Name | Type |
| -------- | -------- | 
| currencies | `DefaultVaultCurrencyPair<T>` | 
| amount_wrapped | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Redeem', 'liquidation_redeem', {
    'amount_wrapped': 'u128',
    'currencies': {
        'collateral': {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
        'wrapped': {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
    },
}
)
```

---------
### mint_tokens_for_reimbursed_redeem
Mint tokens for a redeem that was cancelled with reimburse=true. This is
only possible if at the time of the cancel_redeem, the vault did not have
sufficient collateral after being slashed to back the tokens that the user
used to hold.

\# Arguments

* `origin` - the dispatch origin of this call (must be _Root_)
* `redeem_id` - identifier of redeem request as output from request_redeem

\# Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_pair | `DefaultVaultCurrencyPair<T>` | 
| redeem_id | `H256` | 

#### Python
```python
call = substrate.compose_call(
    'Redeem', 'mint_tokens_for_reimbursed_redeem', {
    'currency_pair': {
        'collateral': {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
        'wrapped': {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
    },
    'redeem_id': '[u8; 32]',
}
)
```

---------
### request_redeem
Initializes a request to burn issued tokens against a Vault with sufficient tokens. It will
also ensure that the Parachain status is RUNNING.

\# Arguments

* `origin` - sender of the transaction
* `amount` - amount of issued tokens
* `btc_address` - the address to receive BTC
* `vault_id` - address of the vault
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount_wrapped | `BalanceOf<T>` | 
| btc_address | `BtcAddress` | 
| vault_id | `DefaultVaultId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Redeem', 'request_redeem', {
    'amount_wrapped': 'u128',
    'btc_address': {
        'P2PKH': '[u8; 20]',
        'P2SH': '[u8; 20]',
        'P2WPKHv0': '[u8; 20]',
        'P2WSHv0': '[u8; 32]',
    },
    'vault_id': {
        'account_id': 'AccountId',
        'currencies': {
            'collateral': {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'LpToken': (
                    {
                        'ForeignAsset': 'u32',
                        'StableLpToken': 'u32',
                        'Token': (
                            'DOT',
                            'IBTC',
                            'INTR',
                            'KSM',
                            'KBTC',
                            'KINT',
                        ),
                    },
                    {
                        'ForeignAsset': 'u32',
                        'StableLpToken': 'u32',
                        'Token': (
                            'DOT',
                            'IBTC',
                            'INTR',
                            'KSM',
                            'KBTC',
                            'KINT',
                        ),
                    },
                ),
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
            'wrapped': {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'LpToken': (
                    {
                        'ForeignAsset': 'u32',
                        'StableLpToken': 'u32',
                        'Token': (
                            'DOT',
                            'IBTC',
                            'INTR',
                            'KSM',
                            'KBTC',
                            'KINT',
                        ),
                    },
                    {
                        'ForeignAsset': 'u32',
                        'StableLpToken': 'u32',
                        'Token': (
                            'DOT',
                            'IBTC',
                            'INTR',
                            'KSM',
                            'KBTC',
                            'KINT',
                        ),
                    },
                ),
                'StableLpToken': 'u32',
                'Token': (
                    'DOT',
                    'IBTC',
                    'INTR',
                    'KSM',
                    'KBTC',
                    'KINT',
                ),
            },
        },
    },
}
)
```

---------
### self_redeem
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_pair | `DefaultVaultCurrencyPair<T>` | 
| amount_wrapped | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Redeem', 'self_redeem', {
    'amount_wrapped': 'u128',
    'currency_pair': {
        'collateral': {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
        'wrapped': {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
            'LpToken': (
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
                {
                    'ForeignAsset': 'u32',
                    'StableLpToken': 'u32',
                    'Token': (
                        'DOT',
                        'IBTC',
                        'INTR',
                        'KSM',
                        'KBTC',
                        'KINT',
                    ),
                },
            ),
            'StableLpToken': 'u32',
            'Token': (
                'DOT',
                'IBTC',
                'INTR',
                'KSM',
                'KBTC',
                'KINT',
            ),
        },
    },
}
)
```

---------
### set_redeem_period
Set the default redeem period for tx verification.

\# Arguments

* `origin` - the dispatch origin of this call (must be _Root_)
* `period` - default period for new requests

\# Weight: `O(1)`
#### Attributes
| Name | Type |
| -------- | -------- | 
| period | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Redeem', 'set_redeem_period', {'period': 'u32'}
)
```

---------
## Events

---------
### CancelRedeem
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| redeem_id | `H256` | ```[u8; 32]```
| redeemer | `T::AccountId` | ```AccountId```
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}}}```
| slashed_amount | `BalanceOf<T>` | ```u128```
| status | `RedeemRequestStatus` | ```{'Pending': None, 'Completed': None, 'Reimbursed': 'bool', 'Retried': None}```

---------
### ExecuteRedeem
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| redeem_id | `H256` | ```[u8; 32]```
| redeemer | `T::AccountId` | ```AccountId```
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}}}```
| amount | `BalanceOf<T>` | ```u128```
| fee | `BalanceOf<T>` | ```u128```
| transfer_fee | `BalanceOf<T>` | ```u128```

---------
### LiquidationRedeem
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| redeemer | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### MintTokensForReimbursedRedeem
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| redeem_id | `H256` | ```[u8; 32]```
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}}}```
| amount | `BalanceOf<T>` | ```u128```

---------
### RedeemPeriodChange
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| period | `T::BlockNumber` | ```u32```

---------
### RequestRedeem
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| redeem_id | `H256` | ```[u8; 32]```
| redeemer | `T::AccountId` | ```AccountId```
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}}}```
| amount | `BalanceOf<T>` | ```u128```
| fee | `BalanceOf<T>` | ```u128```
| premium | `BalanceOf<T>` | ```u128```
| btc_address | `BtcAddress` | ```{'P2PKH': '[u8; 20]', 'P2SH': '[u8; 20]', 'P2WPKHv0': '[u8; 20]', 'P2WSHv0': '[u8; 32]'}```
| transfer_fee | `BalanceOf<T>` | ```u128```

---------
### SelfRedeem
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::51', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}}}```
| amount | `BalanceOf<T>` | ```u128```
| fee | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### RedeemBtcDustValue
 The minimum amount of btc that is accepted for redeem requests; any lower values would
 risk the bitcoin client to reject the payment

#### Python
```python
result = substrate.query(
    'Redeem', 'RedeemBtcDustValue', []
)
```

#### Return value
```python
'u128'
```
---------
### RedeemPeriod
 The time difference in number of blocks between a redeem request is created and required completion time by a
 vault. The redeem period has an upper limit to ensure the user gets their BTC in time and to potentially
 punish a vault for inactivity or stealing BTC.

#### Python
```python
result = substrate.query(
    'Redeem', 'RedeemPeriod', []
)
```

#### Return value
```python
'u32'
```
---------
### RedeemRequests
 Users create redeem requests to receive BTC in return for their previously issued tokens.
 This mapping provides access from a unique hash redeemId to a Redeem struct.

#### Python
```python
result = substrate.query(
    'Redeem', 'RedeemRequests', ['[u8; 32]']
)
```

#### Return value
```python
{
    'amount_btc': 'u128',
    'btc_address': {
        'P2PKH': '[u8; 20]',
        'P2SH': '[u8; 20]',
        'P2WPKHv0': '[u8; 20]',
        'P2WSHv0': '[u8; 32]',
    },
    'btc_height': 'u32',
    'fee': 'u128',
    'opentime': 'u32',
    'period': 'u32',
    'premium': 'u128',
    'redeemer': 'AccountId',
    'status': {
        'Completed': None,
        'Pending': None,
        'Reimbursed': 'bool',
        'Retried': None,
    },
    'transfer_fee_btc': 'u128',
    'vault': {
        'account_id': 'AccountId',
        'currencies': {
            'collateral': {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'LpToken': ('scale_info::52', 'scale_info::52'),
                'StableLpToken': 'u32',
                'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'),
            },
            'wrapped': {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'LpToken': ('scale_info::52', 'scale_info::52'),
                'StableLpToken': 'u32',
                'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'),
            },
        },
    },
}
```
---------
### RedeemTransactionSize
 the expected size in bytes of the redeem bitcoin transfer

#### Python
```python
result = substrate.query(
    'Redeem', 'RedeemTransactionSize', []
)
```

#### Return value
```python
'u32'
```
---------
### StorageVersion
 Build storage at V1 (requires default 0).

#### Python
```python
result = substrate.query(
    'Redeem', 'StorageVersion', []
)
```

#### Return value
```python
('V0', )
```
---------
## Errors

---------
### AmountBelowDustAmount
Redeem amount is too small.

---------
### AmountExceedsUserBalance
Account has insufficient balance.

---------
### RedeemCancelled
Redeem request already cancelled.

---------
### RedeemCompleted
Redeem request already completed.

---------
### RedeemIdNotFound
Redeem request not found.

---------
### TimeNotExpired
Redeem request has not expired.

---------
### TryIntoIntError
Unable to convert value.

---------
### UnauthorizedRedeemer
Unexpected redeem account.

---------
### UnauthorizedVault
Unexpected vault account.

---------