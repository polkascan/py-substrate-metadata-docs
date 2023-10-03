
# Issue

---------
## Calls

---------
### cancel_issue
Cancel the issuance of tokens if expired

\# Arguments

* `origin` - sender of the transaction
* `issue_id` - identifier of issue request as output from request_issue
#### Attributes
| Name | Type |
| -------- | -------- | 
| issue_id | `H256` | 

#### Python
```python
call = substrate.compose_call(
    'Issue', 'cancel_issue', {'issue_id': '[u8; 32]'}
)
```

---------
### execute_issue
Finalize the issuance of tokens

\# Arguments

* `origin` - sender of the transaction
* `issue_id` - identifier of issue request as output from request_issue
* `tx_block_height` - block number of collateral chain
* `merkle_proof` - raw bytes
* `raw_tx` - raw bytes
#### Attributes
| Name | Type |
| -------- | -------- | 
| issue_id | `H256` | 
| unchecked_transaction | `FullTransactionProof` | 

#### Python
```python
call = substrate.compose_call(
    'Issue', 'execute_issue', {
    'issue_id': '[u8; 32]',
    'unchecked_transaction': {
        'coinbase_proof': {
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
                    {
                        'content': '[u8; 32]',
                    },
                ],
                'transactions_count': 'u32',
            },
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
                                'scale_info::95',
                                'u32',
                            ),
                        },
                        'witness': [
                            'Bytes',
                        ],
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
            'tx_encoded_len': 'u32',
        },
        'user_tx_proof': {
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
                    {
                        'content': '[u8; 32]',
                    },
                ],
                'transactions_count': 'u32',
            },
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
                                'scale_info::95',
                                'u32',
                            ),
                        },
                        'witness': [
                            'Bytes',
                        ],
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
            'tx_encoded_len': 'u32',
        },
    },
}
)
```

---------
### request_issue
Request the issuance of tokens

\# Arguments

* `origin` - sender of the transaction
* `amount` - amount of BTC the user wants to convert to issued tokens. Note that the
amount of issued tokens received will be less, because a fee is subtracted.
* `vault` - address of the vault
* `griefing_collateral` - amount of collateral
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 
| vault_id | `DefaultVaultId<T>` | 
| griefing_currency | `CurrencyId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Issue', 'request_issue', {
    'amount': 'u128',
    'griefing_currency': {
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
### set_issue_period
Set the default issue period for tx verification.

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
    'Issue', 'set_issue_period', {'period': 'u32'}
)
```

---------
## Events

---------
### CancelIssue
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| issue_id | `H256` | ```[u8; 32]```
| requester | `T::AccountId` | ```AccountId```
| griefing_collateral | `BalanceOf<T>` | ```u128```

---------
### ExecuteIssue
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| issue_id | `H256` | ```[u8; 32]```
| requester | `T::AccountId` | ```AccountId```
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::52', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::52', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::52', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::52', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}}}```
| amount | `BalanceOf<T>` | ```u128```
| fee | `BalanceOf<T>` | ```u128```

---------
### IssueAmountChange
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| issue_id | `H256` | ```[u8; 32]```
| amount | `BalanceOf<T>` | ```u128```
| fee | `BalanceOf<T>` | ```u128```
| confiscated_griefing_collateral | `BalanceOf<T>` | ```u128```

---------
### IssuePeriodChange
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| period | `T::BlockNumber` | ```u32```

---------
### RequestIssue
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| issue_id | `H256` | ```[u8; 32]```
| requester | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```
| fee | `BalanceOf<T>` | ```u128```
| griefing_collateral | `BalanceOf<T>` | ```u128```
| griefing_currency | `CurrencyId<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::52', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::52', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': 'scale_info::52', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': 'scale_info::52', 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}}}```
| vault_address | `BtcAddress` | ```{'P2PKH': '[u8; 20]', 'P2SH': '[u8; 20]', 'P2WPKHv0': '[u8; 20]', 'P2WSHv0': '[u8; 32]'}```
| vault_public_key | `BtcPublicKey` | ```[u8; 33]```

---------
## Storage functions

---------
### IssueBtcDustValue
 The minimum amount of btc that is required for issue requests; lower values would
 risk the rejection of payment on Bitcoin.

#### Python
```python
result = substrate.query(
    'Issue', 'IssueBtcDustValue', []
)
```

#### Return value
```python
'u128'
```
---------
### IssuePeriod
 The time difference in number of blocks between an issue request is created
 and required completion time by a user. The issue period has an upper limit
 to prevent griefing of vault collateral.

#### Python
```python
result = substrate.query(
    'Issue', 'IssuePeriod', []
)
```

#### Return value
```python
'u32'
```
---------
### IssueRequests
 Users create issue requests to issue tokens. This mapping provides access
 from a unique hash `IssueId` to an `IssueRequest` struct.

#### Python
```python
result = substrate.query(
    'Issue', 'IssueRequests', ['[u8; 32]']
)
```

#### Return value
```python
{
    'amount': 'u128',
    'btc_address': {
        'P2PKH': '[u8; 20]',
        'P2SH': '[u8; 20]',
        'P2WPKHv0': '[u8; 20]',
        'P2WSHv0': '[u8; 32]',
    },
    'btc_height': 'u32',
    'btc_public_key': '[u8; 33]',
    'fee': 'u128',
    'griefing_collateral': 'u128',
    'griefing_currency': {
        'ForeignAsset': 'u32',
        'LendToken': 'u32',
        'LpToken': (
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'),
            },
            {
                'ForeignAsset': 'u32',
                'StableLpToken': 'u32',
                'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'),
            },
        ),
        'StableLpToken': 'u32',
        'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'),
    },
    'opentime': 'u32',
    'period': 'u32',
    'requester': 'AccountId',
    'status': ('Pending', 'Completed', 'Cancelled'),
    'vault': {
        'account_id': 'AccountId',
        'currencies': {
            'collateral': {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'LpToken': ('scale_info::53', 'scale_info::53'),
                'StableLpToken': 'u32',
                'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'),
            },
            'wrapped': {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'LpToken': ('scale_info::53', 'scale_info::53'),
                'StableLpToken': 'u32',
                'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'),
            },
        },
    },
}
```
---------
### StorageVersion
 Build storage at V1 (requires default 0).

#### Python
```python
result = substrate.query(
    'Issue', 'StorageVersion', []
)
```

#### Return value
```python
('V0', 'V1', 'V2', 'V3', 'V4')
```
---------
## Constants

---------
### TreasuryPalletId
 The treasury pallet account for slashed griefing collateral.
#### Value
```python
'0x6d6f642f74727379'
```
#### Python
```python
constant = substrate.get_constant('Issue', 'TreasuryPalletId')
```
---------
## Errors

---------
### AmountBelowDustAmount
Issue amount is too small.

---------
### CommitPeriodExpired
Issue request has expired.

---------
### InvalidExecutor
Not expected origin.

---------
### IssueCancelled
Issue request already cancelled.

---------
### IssueCompleted
Issue request already completed.

---------
### IssueIdNotFound
Issue request not found.

---------
### TimeNotExpired
Issue request has not expired.

---------
### VaultNotAcceptingNewIssues
Vault is not active.

---------
### WaitingForRelayerInitialization
Relay is not initialized.

---------