
# Redeem

---------
## Calls

---------
### cancel_redeem
If a redeem request is not completed on time, the redeem request can be cancelled.
The user that initially requested the redeem process calls this function to obtain
the Vault’s collateral as compensation for not transferring the Stellar assets back to
their address.

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
A Vault calls this function after receiving an RequestRedeem event with their public
key. Before calling the function, the Vault transfers the specific amount of Stellar
assets to the Stellar address given in the original redeem request. The Vault completes
the redeem with this function.

\# Arguments

* `origin` - anyone executing this redeem request
* `redeem_id` - identifier of redeem request as output from request_redeem
* `transaction_envelope_xdr_encoded` - the XDR representation of the transaction
  envelope
* `externalized_envelopes_encoded` - the XDR representation of the externalized
  envelopes
* `transaction_set_encoded` - the XDR representation of the transaction set
#### Attributes
| Name | Type |
| -------- | -------- | 
| redeem_id | `H256` | 
| transaction_envelope_xdr_encoded | `Vec<u8>` | 
| externalized_envelopes_encoded | `Vec<u8>` | 
| transaction_set_encoded | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Redeem', 'execute_redeem', {
    'externalized_envelopes_encoded': 'Bytes',
    'redeem_id': '[u8; 32]',
    'transaction_envelope_xdr_encoded': 'Bytes',
    'transaction_set_encoded': 'Bytes',
}
)
```

---------
### liquidation_redeem
When a Vault is liquidated, its collateral is slashed up to 150% of the liquidated
value. To re-establish the physical 1:1 peg, the bridge allows users to burn issued
tokens in return for collateral at a premium rate.

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
        },
    },
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
    'Redeem', 'minimum_transfer_amount_update', {'new_minimum_amount': 'u128'}
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
        },
    },
    'redeem_id': '[u8; 32]',
}
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
    'Redeem', 'rate_limit_update', {
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
    },
}
)
```

---------
### request_redeem
Initializes a request to burn issued tokens against a Vault with sufficient tokens. It
will also ensure that the Parachain status is RUNNING.

\# Arguments

* `origin` - sender of the transaction
* `amount_wrapped` - amount of tokens to redeem
* `asset` - the asset to redeem
* `stellar_address` - the address to receive assets on Stellar
* `vault_id` - address of the vault
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount_wrapped | `BalanceOf<T>` | 
| stellar_address | `StellarPublicKeyRaw` | 
| vault_id | `DefaultVaultId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Redeem', 'request_redeem', {
    'amount_wrapped': 'u128',
    'stellar_address': '[u8; 32]',
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
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}}}```
| slashed_amount | `BalanceOf<T>` | ```u128```
| status | `RedeemRequestStatus` | ```{'Pending': None, 'Completed': None, 'Reimbursed': 'bool', 'Retried': None}```

---------
### ExecuteRedeem
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| redeem_id | `H256` | ```[u8; 32]```
| redeemer | `T::AccountId` | ```AccountId```
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}}}```
| amount | `BalanceOf<T>` | ```u128```
| asset | `CurrencyId<T>` | ```{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}```
| fee | `BalanceOf<T>` | ```u128```
| transfer_fee | `BalanceOf<T>` | ```u128```

---------
### LiquidationRedeem
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| redeemer | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```
| asset | `CurrencyId<T>` | ```{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}```

---------
### MintTokensForReimbursedRedeem
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| redeem_id | `H256` | ```[u8; 32]```
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}}}```
| amount | `BalanceOf<T>` | ```u128```

---------
### RateLimitUpdate
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| limit_volume_amount | `Option<BalanceOf<T>>` | ```(None, 'u128')```
| limit_volume_currency_id | `T::CurrencyId` | ```{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}```
| interval_length | `T::BlockNumber` | ```u32```

---------
### RedeemMinimumTransferAmountUpdate
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| new_minimum_amount | `BalanceOf<T>` | ```u128```

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
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}}}```
| amount | `BalanceOf<T>` | ```u128```
| asset | `CurrencyId<T>` | ```{'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}```
| fee | `BalanceOf<T>` | ```u128```
| premium | `BalanceOf<T>` | ```u128```
| stellar_address | `StellarPublicKeyRaw` | ```[u8; 32]```
| transfer_fee | `BalanceOf<T>` | ```u128```

---------
### SelfRedeem
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| vault_id | `DefaultVaultId<T>` | ```{'account_id': 'AccountId', 'currencies': {'collateral': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}, 'wrapped': {'Native': None, 'XCM': 'u8', 'Stellar': {'StellarNative': None, 'AlphaNum4': {'code': '[u8; 4]', 'issuer': '[u8; 32]'}, 'AlphaNum12': {'code': '[u8; 12]', 'issuer': '[u8; 32]'}}}}}```
| amount | `BalanceOf<T>` | ```u128```
| fee | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### CurrentVolumeAmount

#### Python
```python
result = substrate.query(
    'Redeem', 'CurrentVolumeAmount', []
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
    'Redeem', 'IntervalLength', []
)
```

#### Return value
```python
'u32'
```
---------
### LastIntervalIndex
 Represent current interval current_block_number / IntervalLength

#### Python
```python
result = substrate.query(
    'Redeem', 'LastIntervalIndex', []
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
    'Redeem', 'LimitVolumeAmount', []
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
    'Redeem', 'LimitVolumeCurrencyId', []
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
}
```
---------
### RedeemMinimumTransferAmount
 The minimum amount of wrapped assets that is accepted for redeem requests

#### Python
```python
result = substrate.query(
    'Redeem', 'RedeemMinimumTransferAmount', []
)
```

#### Return value
```python
'u128'
```
---------
### RedeemPeriod
 The time difference in number of blocks between a redeem request is created and required
 completion time by a vault. The redeem period has an upper limit to ensure the user gets
 their Stellar assets in time and to potentially punish a vault for inactivity or stealing
 Stellar assets.

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
 Users create redeem requests to receive stellar assets in return for their previously issued
 tokens. This mapping provides access from a unique hash redeemId to a Redeem struct.

#### Python
```python
result = substrate.query(
    'Redeem', 'RedeemRequests', ['[u8; 32]']
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
    },
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
    'stellar_address': '[u8; 32]',
    'transfer_fee': 'u128',
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
            },
            'wrapped': {
                'Native': None,
                'Stellar': {
                    'AlphaNum12': 'InnerStruct',
                    'AlphaNum4': 'InnerStruct',
                    'StellarNative': None,
                },
                'XCM': 'u8',
            },
        },
    },
}
```
---------
## Errors

---------
### AmountBelowMinimumTransferAmount
Redeem amount is too small.

---------
### AmountExceedsUserBalance
Account has insufficient balance.

---------
### ExceedLimitVolumeForIssueRequest
Exceeds the volume limit for an issue request.

---------
### InvalidPaymentAmount
Invalid payment amount

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