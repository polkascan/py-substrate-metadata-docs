
# Replace

---------
## Calls

---------
### accept_replace
Accept request of vault replacement

\# Arguments

* `origin` - the initiator of the transaction: the new vault
* `old_vault` - id of the old vault that we are (possibly partially) replacing
* `collateral` - the collateral for replacement
* `btc_address` - the address that old-vault should transfer the btc to
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_pair | `DefaultVaultCurrencyPair<T>` | 
| old_vault | `DefaultVaultId<T>` | 
| amount_btc | `BalanceOf<T>` | 
| collateral | `BalanceOf<T>` | 
| btc_address | `BtcAddress` | 

#### Python
```python
call = substrate.compose_call(
    'Replace', 'accept_replace', {
    'amount_btc': 'u128',
    'btc_address': {
        'P2PKH': '[u8; 20]',
        'P2SH': '[u8; 20]',
        'P2WPKHv0': '[u8; 20]',
        'P2WSHv0': '[u8; 32]',
    },
    'collateral': 'u128',
    'currency_pair': {
        'collateral': {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
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
    'old_vault': {
        'account_id': 'AccountId',
        'currencies': {
            'collateral': {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
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
### cancel_replace
Cancel vault replacement

\# Arguments

* `origin` - sender of the transaction: anyone
* `replace_id` - the ID of the replacement request
#### Attributes
| Name | Type |
| -------- | -------- | 
| replace_id | `H256` | 

#### Python
```python
call = substrate.compose_call(
    'Replace', 'cancel_replace', {'replace_id': '[u8; 32]'}
)
```

---------
### execute_replace
Execute vault replacement

\# Arguments

* `origin` - sender of the transaction: the new vault
* `replace_id` - the ID of the replacement request
* &\#x27;merkle_proof&\#x27; - the merkle root of the block
* `raw_tx` - the transaction id in bytes
#### Attributes
| Name | Type |
| -------- | -------- | 
| replace_id | `H256` | 
| merkle_proof | `Vec<u8>` | 
| raw_tx | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Replace', 'execute_replace', {
    'merkle_proof': 'Bytes',
    'raw_tx': 'Bytes',
    'replace_id': '[u8; 32]',
}
)
```

---------
### request_replace
Request the replacement of a new vault ownership

\# Arguments

* `origin` - sender of the transaction
* `amount` - amount of issued tokens
* `griefing_collateral` - amount of collateral
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_pair | `DefaultVaultCurrencyPair<T>` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Replace', 'request_replace', {
    'amount': 'u128',
    'currency_pair': {
        'collateral': {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
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
### set_replace_period
Set the default replace period for tx verification.

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
    'Replace', 'set_replace_period', {'period': 'u32'}
)
```

---------
### withdraw_replace
Withdraw a request of vault replacement

\# Arguments

* `origin` - sender of the transaction: the old vault
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_pair | `DefaultVaultCurrencyPair<T>` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Replace', 'withdraw_replace', {
    'amount': 'u128',
    'currency_pair': {
        'collateral': {
            'ForeignAsset': 'u32',
            'LendToken': 'u32',
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
## Events

---------
### AcceptReplace
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| replace_id | `H256` | ```[u8; 32]```
| old_vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}}}```
| new_vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}}}```
| amount | `BalanceOf<T>` | ```u128```
| collateral | `BalanceOf<T>` | ```u128```
| btc_address | `BtcAddress` | ```{'P2PKH': '[u8; 20]', 'P2SH': '[u8; 20]', 'P2WPKHv0': '[u8; 20]', 'P2WSHv0': '[u8; 32]'}```

---------
### CancelReplace
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| replace_id | `H256` | ```[u8; 32]```
| new_vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}}}```
| old_vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}}}```
| griefing_collateral | `BalanceOf<T>` | ```u128```

---------
### ExecuteReplace
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| replace_id | `H256` | ```[u8; 32]```
| old_vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}}}```
| new_vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}}}```

---------
### ReplacePeriodChange
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| period | `T::BlockNumber` | ```u32```

---------
### RequestReplace
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}}}```
| amount | `BalanceOf<T>` | ```u128```
| griefing_collateral | `BalanceOf<T>` | ```u128```

---------
### WithdrawReplace
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}, 'wrapped': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32'}}}```
| withdrawn_tokens | `BalanceOf<T>` | ```u128```
| withdrawn_griefing_collateral | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### ReplaceBtcDustValue
 The minimum amount of btc that is accepted for replace requests; any lower values would
 risk the bitcoin client to reject the payment

#### Python
```python
result = substrate.query(
    'Replace', 'ReplaceBtcDustValue', []
)
```

#### Return value
```python
'u128'
```
---------
### ReplacePeriod
 The time difference in number of blocks between when a replace request is created
 and required completion time by a vault. The replace period has an upper limit
 to prevent griefing of vault collateral.

#### Python
```python
result = substrate.query(
    'Replace', 'ReplacePeriod', []
)
```

#### Return value
```python
'u32'
```
---------
### ReplaceRequests
 Vaults create replace requests to transfer locked collateral.
 This mapping provides access from a unique hash to a `ReplaceRequest`.

#### Python
```python
result = substrate.query(
    'Replace', 'ReplaceRequests', ['[u8; 32]']
)
```

#### Return value
```python
{
    'accept_time': 'u32',
    'amount': 'u128',
    'btc_address': {
        'P2PKH': '[u8; 20]',
        'P2SH': '[u8; 20]',
        'P2WPKHv0': '[u8; 20]',
        'P2WSHv0': '[u8; 32]',
    },
    'btc_height': 'u32',
    'collateral': 'u128',
    'griefing_collateral': 'u128',
    'new_vault': {
        'account_id': 'AccountId',
        'currencies': {
            'collateral': {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'),
            },
            'wrapped': {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'),
            },
        },
    },
    'old_vault': {
        'account_id': 'AccountId',
        'currencies': {
            'collateral': {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'),
            },
            'wrapped': {
                'ForeignAsset': 'u32',
                'LendToken': 'u32',
                'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'),
            },
        },
    },
    'period': 'u32',
    'status': ('Pending', 'Completed', 'Cancelled'),
}
```
---------
### StorageVersion
 Build storage at V1 (requires default 0).

#### Python
```python
result = substrate.query(
    'Replace', 'StorageVersion', []
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
Replace amount is too small.

---------
### InvalidWrappedCurrency
Vault cannot replace different currency.

---------
### NoPendingRequest
No replace request found.

---------
### ReplaceAmountZero
Replace requires non-zero increase.

---------
### ReplaceCancelled
Replace request already cancelled.

---------
### ReplaceCompleted
Replace request already completed.

---------
### ReplaceIdNotFound
Replace request not found.

---------
### ReplacePeriodNotExpired
Replace request has not expired.

---------
### ReplaceSelfNotAllowed
Cannot replace self.

---------
### UnauthorizedVault
Unexpected vault account.

---------
### VaultHasEnabledNomination
Cannot replace with nominated collateral.

---------