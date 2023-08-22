
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
* `transaction_envelope_xdr_encoded` - the XDR representation of the transaction
  envelope
* `externalized_envelopes_encoded` - the XDR representation of the externalized
  envelopes
* `transaction_set_encoded` - the XDR representation of the transaction set
#### Attributes
| Name | Type |
| -------- | -------- | 
| issue_id | `H256` | 
| transaction_envelope_xdr_encoded | `Vec<u8>` | 
| externalized_envelopes_encoded | `Vec<u8>` | 
| transaction_set_encoded | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Issue', 'execute_issue', {
    'externalized_envelopes_encoded': 'Bytes',
    'issue_id': '[u8; 32]',
    'transaction_envelope_xdr_encoded': 'Bytes',
    'transaction_set_encoded': 'Bytes',
}
)
```

---------
### minimum_transfer_amount_update
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_minimum_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Issue', 'minimum_transfer_amount_update', {'new_minimum_amount': 'u128'}
)
```

---------
### rate_limit_update
#### Attributes
| Name | Type |
| -------- | -------- | 
| limit_volume_amount | `Option<BalanceOf<T>>` | 
| limit_volume_currency_id | `T::CurrencyId` | 
| interval_length | `T::BlockNumber` | 

#### Python
```python
call = substrate.compose_call(
    'Issue', 'rate_limit_update', {
    'interval_length': 'u32',
    'limit_volume_amount': (
        None,
        'u128',
    ),
    'limit_volume_currency_id': {
        'Native': None,
        'Stellar': {
            'AlphaNum12': {
                'code': '[u8; 12]',
                'issuer': '[u8; 32]',
            },
            'AlphaNum4': {
                'code': '[u8; 4]',
                'issuer': '[u8; 32]',
            },
            'StellarNative': None,
        },
        'XCM': 'u8',
        'ZenlinkLPToken': (
            'u8',
            'u8',
            'u8',
            'u8',
        ),
    },
}
)
```

---------
### request_issue
Request the issuance of tokens

\# Arguments

* `origin` - sender of the transaction
* `amount` - amount of a stellar asset the user wants to convert to issued tokens. Note
  that the
amount of issued tokens received will be less, because a fee is subtracted.
* `asset` - the currency id of the stellar asset the user wants to convert to issued
  tokens
* `vault` - address of the vault
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 
| vault_id | `DefaultVaultId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Issue', 'request_issue', {
    'amount': 'u128',
    'vault_id': {
        'account_id': 'AccountId',
        'currencies': {
            'collateral': {
                'Native': None,
                'Stellar': {
                    'AlphaNum12': {
                        'code': '[u8; 12]',
                        'issuer': '[u8; 32]',
                    },
                    'AlphaNum4': {
                        'code': '[u8; 4]',
                        'issuer': '[u8; 32]',
                    },
                    'StellarNative': None,
                },
                'XCM': 'u8',
                'ZenlinkLPToken': (
                    'u8',
                    'u8',
                    'u8',
                    'u8',
                ),
            },
            'wrapped': {
                'Native': None,
                'Stellar': {
                    'AlphaNum12': {
                        'code': '[u8; 12]',
                        'issuer': '[u8; 32]',
                    },
                    'AlphaNum4': {
                        'code': '[u8; 4]',
                        'issuer': '[u8; 32]',
                    },
                    'StellarNative': None,
                },
                'XCM': 'u8',
                'ZenlinkLPToken': (
                    'u8',
                    'u8',
                    'u8',
                    'u8',
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
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}}}```
| amount | `BalanceOf<T>` | ```u128```
| asset | `CurrencyId<T>` | ```{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}```
| fee | `BalanceOf<T>` | ```u128```

---------
### IssueAmountChange
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| issue_id | `H256` | ```[u8; 32]```
| amount | `BalanceOf<T>` | ```u128```
| asset | `CurrencyId<T>` | ```{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}```
| fee | `BalanceOf<T>` | ```u128```
| confiscated_griefing_collateral | `BalanceOf<T>` | ```u128```

---------
### IssueMinimumTransferAmountUpdate
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| new_minimum_amount | `BalanceOf<T>` | ```u128```

---------
### IssuePeriodChange
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| period | `T::BlockNumber` | ```u32```

---------
### RateLimitUpdate
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| limit_volume_amount | `Option<BalanceOf<T>>` | ```(None, 'u128')```
| limit_volume_currency_id | `T::CurrencyId` | ```{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}```
| interval_length | `T::BlockNumber` | ```u32```

---------
### RequestIssue
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| issue_id | `H256` | ```[u8; 32]```
| requester | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```
| asset | `CurrencyId<T>` | ```{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}```
| fee | `BalanceOf<T>` | ```u128```
| griefing_collateral | `BalanceOf<T>` | ```u128```
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}, 'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8')}}}```
| vault_stellar_public_key | `StellarPublicKeyRaw` | ```[u8; 32]```

---------
## Storage functions

---------
### CurrentVolumeAmount

#### Python
```python
result = substrate.query(
    'Issue', 'CurrentVolumeAmount', []
)
```

#### Return value
```python
'u128'
```
---------
### IntervalLength
 Represent interval define regular 24 hour intervals (every 24 * 3600 / 12 blocks)

#### Python
```python
result = substrate.query(
    'Issue', 'IntervalLength', []
)
```

#### Return value
```python
'u32'
```
---------
### IssueMinimumTransferAmount
 The minimum amount of wrapped assets that is required for issue requests

#### Python
```python
result = substrate.query(
    'Issue', 'IssueMinimumTransferAmount', []
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
    'asset': {
        'Native': None,
        'Stellar': {
            'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'},
            'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'},
            'StellarNative': None,
        },
        'XCM': 'u8',
        'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'),
    },
    'fee': 'u128',
    'griefing_collateral': 'u128',
    'opentime': 'u32',
    'period': 'u32',
    'requester': 'AccountId',
    'status': ('Pending', 'Completed', 'Cancelled'),
    'stellar_address': '[u8; 32]',
    'vault': {
        'account_id': 'AccountId',
        'currencies': {
            'collateral': {
                'Native': None,
                'Stellar': {
                    'AlphaNum12': 'InnerStruct',
                    'AlphaNum4': 'InnerStruct',
                    'StellarNative': None,
                },
                'XCM': 'u8',
                'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'),
            },
            'wrapped': {
                'Native': None,
                'Stellar': {
                    'AlphaNum12': 'InnerStruct',
                    'AlphaNum4': 'InnerStruct',
                    'StellarNative': None,
                },
                'XCM': 'u8',
                'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'),
            },
        },
    },
}
```
---------
### LastIntervalIndex
 Represent current interval current_block_number / IntervalLength

#### Python
```python
result = substrate.query(
    'Issue', 'LastIntervalIndex', []
)
```

#### Return value
```python
'u32'
```
---------
### LimitVolumeAmount

#### Python
```python
result = substrate.query(
    'Issue', 'LimitVolumeAmount', []
)
```

#### Return value
```python
(None, 'u128')
```
---------
### LimitVolumeCurrencyId
 CurrencyID that represents the currency in which the volume limit is measured, eg DOT, USDC
 or PEN

#### Python
```python
result = substrate.query(
    'Issue', 'LimitVolumeCurrencyId', []
)
```

#### Return value
```python
{
    'Native': None,
    'Stellar': {
        'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'},
        'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'},
        'StellarNative': None,
    },
    'XCM': 'u8',
    'ZenlinkLPToken': ('u8', 'u8', 'u8', 'u8'),
}
```
---------
## Errors

---------
### AmountBelowMinimumTransferAmount
Issue amount is too small.

---------
### ExceedLimitVolumeForIssueRequest
Exceeds the volume limit for an issue request.

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