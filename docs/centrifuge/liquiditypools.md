
# LiquidityPools

---------
## Calls

---------
### add_currency
Add a currency to the set of known currencies on the domain derived
from the given currency.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityPools', 'add_currency', {
    'currency_id': {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'LocalAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
    },
}
)
```

---------
### add_pool
Add a pool to a given domain
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| domain | `Domain` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityPools', 'add_pool', {
    'domain': {
        'Centrifuge': None,
        'EVM': 'u64',
    },
    'pool_id': 'u64',
}
)
```

---------
### add_tranche
Add a tranche to a given domain
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| tranche_id | `T::TrancheId` | 
| domain | `Domain` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityPools', 'add_tranche', {
    'domain': {
        'Centrifuge': None,
        'EVM': 'u64',
    },
    'pool_id': 'u64',
    'tranche_id': '[u8; 16]',
}
)
```

---------
### allow_investment_currency
Allow a currency to be used as a pool currency and to invest in a
pool on the domain derived from the given currency.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| currency_id | `CurrencyIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityPools', 'allow_investment_currency', {
    'currency_id': {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'LocalAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
        None: None,
    },
    'pool_id': 'u64',
}
)
```

---------
### cancel_upgrade
Schedule an upgrade of an EVM-based liquidity pool contract instance
#### Attributes
| Name | Type |
| -------- | -------- | 
| evm_chain_id | `EVMChainId` | 
| contract | `[u8; 20]` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityPools', 'cancel_upgrade', {
    'contract': '[u8; 20]',
    'evm_chain_id': 'u64',
}
)
```

---------
### disallow_investment_currency
Disallow a currency to be used as a pool currency and to invest in a
pool on the domain derived from the given currency.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| currency_id | `CurrencyIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityPools', 'disallow_investment_currency', {
    'currency_id': {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'LocalAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        None: None,
        'Tranche': ('u64', '[u8; 16]'),
    },
    'pool_id': 'u64',
}
)
```

---------
### schedule_upgrade
Schedule an upgrade of an EVM-based liquidity pool contract instance
#### Attributes
| Name | Type |
| -------- | -------- | 
| evm_chain_id | `EVMChainId` | 
| contract | `[u8; 20]` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityPools', 'schedule_upgrade', {
    'contract': '[u8; 20]',
    'evm_chain_id': 'u64',
}
)
```

---------
### transfer
Transfer non-tranche tokens to a given address.

NOTE: Assumes `OutboundQueue` to check whether destination is local.

NOTE: The transferring account is not kept alive as we allow its
death.
#### Attributes
| Name | Type |
| -------- | -------- | 
| currency_id | `CurrencyIdOf<T>` | 
| receiver | `DomainAddress` | 
| amount | `<T as pallet::Config>::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityPools', 'transfer', {
    'amount': 'u128',
    'currency_id': {
        None: None,
        'AUSD': None,
        'ForeignAsset': 'u32',
        'LocalAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        'Tranche': ('u64', '[u8; 16]'),
    },
    'receiver': {
        'Centrifuge': '[u8; 32]',
        'EVM': ('u64', '[u8; 20]'),
    },
}
)
```

---------
### transfer_tranche_tokens
Transfer tranche tokens to a given address.

NOTE: Assumes `OutboundQueue` to check whether destination is local.

NOTE: The transferring account is not kept alive as we allow its
death.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| tranche_id | `T::TrancheId` | 
| domain_address | `DomainAddress` | 
| amount | `<T as pallet::Config>::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityPools', 'transfer_tranche_tokens', {
    'amount': 'u128',
    'domain_address': {
        'Centrifuge': '[u8; 32]',
        'EVM': ('u64', '[u8; 20]'),
    },
    'pool_id': 'u64',
    'tranche_id': '[u8; 16]',
}
)
```

---------
### update_member
Update a member
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| tranche_id | `T::TrancheId` | 
| domain_address | `DomainAddress` | 
| valid_until | `Seconds` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityPools', 'update_member', {
    'domain_address': {
        'Centrifuge': '[u8; 32]',
        'EVM': ('u64', '[u8; 20]'),
    },
    'pool_id': 'u64',
    'tranche_id': '[u8; 16]',
    'valid_until': 'u64',
}
)
```

---------
### update_token_price
Update the price of a tranche token.

By ensuring that registered currency location matches the specified
domain, this call origin can be permissionless.

The `currency_id` parameter is necessary for the EVM side.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| tranche_id | `T::TrancheId` | 
| currency_id | `CurrencyIdOf<T>` | 
| destination | `Domain` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityPools', 'update_token_price', {
    'currency_id': {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'LocalAsset': 'u32',
        'Native': None,
        'Staking': ('BlockRewards', ),
        None: None,
        'Tranche': ('u64', '[u8; 16]'),
    },
    'destination': {
        'Centrifuge': None,
        'EVM': 'u64',
    },
    'pool_id': 'u64',
    'tranche_id': '[u8; 16]',
}
)
```

---------
### update_tranche_token_metadata
Update the tranche token name and symbol on the specified domain

NOTE: Pulls the metadata from the `AssetRegistry` and thus requires
the pool admin to have updated the tranche tokens metadata there
beforehand.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| tranche_id | `T::TrancheId` | 
| domain | `Domain` | 

#### Python
```python
call = substrate.compose_call(
    'LiquidityPools', 'update_tranche_token_metadata', {
    'domain': {
        'Centrifuge': None,
        'EVM': 'u64',
    },
    'pool_id': 'u64',
    'tranche_id': '[u8; 16]',
}
)
```

---------
## Events

---------
### IncomingMessage
An incoming LP message was
detected and is further processed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| sender | `DomainAddress` | ```{'Centrifuge': '[u8; 32]', 'EVM': ('u64', '[u8; 20]')}```
| message | `MessageOf<T>` | ```{'Invalid': None, 'AddCurrency': {'currency': 'u128', 'evm_address': '[u8; 20]'}, 'AddPool': {'pool_id': 'u64'}, 'AllowInvestmentCurrency': {'pool_id': 'u64', 'currency': 'u128'}, 'AddTranche': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'token_name': '[u8; 128]', 'token_symbol': '[u8; 32]', 'decimals': 'u8', 'restriction_set': 'u8'}, 'UpdateTrancheTokenPrice': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'currency': 'u128', 'price': 'u128', 'computed_at': 'u64'}, 'UpdateMember': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'member': '[u8; 32]', 'valid_until': 'u64'}, 'Transfer': {'currency': 'u128', 'sender': '[u8; 32]', 'receiver': '[u8; 32]', 'amount': 'u128'}, 'TransferTrancheTokens': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'sender': '[u8; 32]', 'domain': {'Centrifuge': None, 'EVM': 'u64'}, 'receiver': '[u8; 32]', 'amount': 'u128'}, 'IncreaseInvestOrder': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128', 'amount': 'u128'}, 'DecreaseInvestOrder': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128', 'amount': 'u128'}, 'IncreaseRedeemOrder': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128', 'amount': 'u128'}, 'DecreaseRedeemOrder': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128', 'amount': 'u128'}, 'CollectInvest': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128'}, 'CollectRedeem': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128'}, 'ExecutedDecreaseInvestOrder': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128', 'currency_payout': 'u128', 'remaining_invest_amount': 'u128'}, 'ExecutedDecreaseRedeemOrder': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128', 'tranche_tokens_payout': 'u128', 'remaining_redeem_amount': 'u128'}, 'ExecutedCollectInvest': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128', 'currency_payout': 'u128', 'tranche_tokens_payout': 'u128', 'remaining_invest_amount': 'u128'}, 'ExecutedCollectRedeem': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128', 'currency_payout': 'u128', 'tranche_tokens_payout': 'u128', 'remaining_redeem_amount': 'u128'}, 'CancelInvestOrder': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128'}, 'CancelRedeemOrder': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'investor': '[u8; 32]', 'currency': 'u128'}, 'ScheduleUpgrade': {'contract': '[u8; 20]'}, 'CancelUpgrade': {'contract': '[u8; 20]'}, 'UpdateTrancheTokenMetadata': {'pool_id': 'u64', 'tranche_id': '[u8; 16]', 'token_name': '[u8; 128]', 'token_symbol': '[u8; 32]'}, 'DisallowInvestmentCurrency': {'pool_id': 'u64', 'currency': 'u128'}}```

---------
## Storage functions

---------
## Constants

---------
### GeneralCurrencyPrefix
 The prefix for currencies added via the LiquidityPools feature.
#### Value
```python
'0xb64fd1c3a60c260188389850'
```
#### Python
```python
constant = substrate.get_constant('LiquidityPools', 'GeneralCurrencyPrefix')
```
---------
### TreasuryAccount
 The type for paying the transaction fees for the dispatch of
 `Executed*` and `ScheduleUpgrade` messages.

 NOTE: We need to make sure to collect the appropriate amount
 beforehand as part of receiving the corresponding investment
 message.
#### Value
```python
'4dpEcgqJRyJK3J8Es6v8ZfVntV7c64Ysgcjd4hYwyGoFPWbg'
```
#### Python
```python
constant = substrate.get_constant('LiquidityPools', 'TreasuryAccount')
```
---------
## Errors

---------
### AssetMetadataNotPoolCurrency
The metadata of the given asset does not declare it as a pool
currency and thus it cannot be used as an investment currency.

---------
### AssetNotFound
Failed to map the asset to the corresponding LiquidityPools&\#x27; General
Index representation and thus cannot be used as an
investment currency.

---------
### AssetNotLiquidityPoolsTransferable
The metadata of the given asset does not declare it as transferable
via LiquidityPools&\#x27;.

---------
### AssetNotLiquidityPoolsWrappedToken
The asset is not a [LiquidityPoolsWrappedToken] and thus cannot be
transferred via liquidity pools.

---------
### BalanceTooLow
Senders balance is insufficient for transfer amount

---------
### InvalidDomain
The destination domain is invalid.

---------
### InvalidIncomingMessage
Failed to decode an incoming message.

---------
### InvalidTrancheInvestorValidity
The validity is in the past.

---------
### InvalidTransferAmount
Transfer amount must be non-zero.

---------
### InvalidTransferCurrency
The currency is not allowed to be transferred via LiquidityPools.

---------
### InvestorDomainAddressNotAMember
The account derived from the [Domain] and [DomainAddress] has not
been whitelisted as a TrancheInvestor.

---------
### MissingTranchePrice
Failed to fetch a tranche token price.
This can occur if `TrancheNotFound` or if effectively
the price for this tranche has not yet been set.

---------
### NotPoolAdmin
Only the PoolAdmin can execute a given operation.

---------
### PoolNotFound
A pool could not be found.

---------
### TrancheMetadataNotFound
Could not find the metadata of a tranche token.

---------
### TrancheNotFound
A tranche could not be found.

---------
### UnauthorizedTransfer
A transfer to a non-whitelisted destination was attempted.

---------