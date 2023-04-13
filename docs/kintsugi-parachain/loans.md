
# Loans

---------
## Calls

---------
### activate_market
Activates a market. Returns `Err` if the market does not exist.

If the market is already active, does nothing.

- `asset_id`: Currency to enable lending and borrowing for.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `CurrencyId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'activate_market', {
    'asset_id': {
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
}
)
```

---------
### add_market
Creates a new lending market for a given currency. Returns `Err` if a market already
exists for the given currency.

All provided market states must be `Pending`, otherwise an error will be returned.

The lend_token id specified in the Market struct has to be unique, and cannot be later reused
when creating a new market.

- `asset_id`: Currency to enable lending and borrowing for.
- `market`: Configuration of the new lending market
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `CurrencyId<T>` | 
| market | `Market<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'add_market', {
    'asset_id': {
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
    'market': {
        'borrow_cap': 'u128',
        'close_factor': 'u32',
        'collateral_factor': 'u32',
        'lend_token_id': {
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
        'liquidate_incentive': 'u128',
        'liquidate_incentive_reserved_factor': 'u32',
        'liquidation_threshold': 'u32',
        'rate_model': {
            'Curve': {
                'base_rate': 'u128',
            },
            'Jump': {
                'base_rate': 'u128',
                'full_rate': 'u128',
                'jump_rate': 'u128',
                'jump_utilization': 'u32',
            },
        },
        'reserve_factor': 'u32',
        'state': (
            'Active',
            'Pending',
            'Supervision',
        ),
        'supply_cap': 'u128',
    },
}
)
```

---------
### add_reserves
Add reserves by transferring from payer.
TODO: This extrinsic currently does nothing useful. See the TODO comment
of the `ensure_enough_cash` function for more details. Based on that
TODO, decide whether this extrinsic should be kept.

May only be called from `T::ReserveOrigin`.

- `payer`: the payer account.
- `asset_id`: the assets to be added.
- `add_amount`: the amount to be added.
#### Attributes
| Name | Type |
| -------- | -------- | 
| payer | `<T::Lookup as StaticLookup>::Source` | 
| asset_id | `CurrencyId<T>` | 
| add_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'add_reserves', {
    'add_amount': 'u128',
    'asset_id': {
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
    'payer': 'AccountId',
}
)
```

---------
### add_reward
Deposit incentive reward currency into the pallet account.

- `amount`: Reward amount added
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'add_reward', {'amount': 'u128'}
)
```

---------
### borrow
The caller borrows `borrow_amount` of `asset_id` from the protocol, using their
supplied assets as collateral.

- `asset_id`: the asset to be borrowed.
- `borrow_amount`: the amount to be borrowed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `CurrencyId<T>` | 
| borrow_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'borrow', {
    'asset_id': {
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
    'borrow_amount': 'u128',
}
)
```

---------
### claim_reward
Claim incentive rewards for all markets.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Loans', 'claim_reward', {}
)
```

---------
### claim_reward_for_market
Claim inceitve reward for the specified market.

- `asset_id`: Market related currency
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `CurrencyId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'claim_reward_for_market', {
    'asset_id': {
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
}
)
```

---------
### deposit_all_collateral
Caller enables their lend token balance as borrow collateral. This operation locks
the lend tokens, so they are no longer transferrable.
Any incoming lend tokens into the caller&\#x27;s account (either by direct transfer or minting)
are automatically locked as well, such that locking and unlocking borrow collateral is
an atomic state (a &quot;collateral toggle&quot;).
If any of the caller&\#x27;s lend token balance is locked elsewhere (for instance, as bridge vault
collateral), this operation will fail.
If this operation is successful, the caller&\#x27;s maximum allowed debt increases.

- `asset_id`: the underlying asset denoting the market whose lend tokens are to be
enabled as collateral.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `CurrencyId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'deposit_all_collateral', {
    'asset_id': {
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
}
)
```

---------
### force_update_market
Force updates a stored market. Returns `Err` if the market currency
does not exist.

- `asset_id`: market related currency
- `market`: Configuration of the new lending market
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `CurrencyId<T>` | 
| market | `Market<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'force_update_market', {
    'asset_id': {
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
    'market': {
        'borrow_cap': 'u128',
        'close_factor': 'u32',
        'collateral_factor': 'u32',
        'lend_token_id': {
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
        'liquidate_incentive': 'u128',
        'liquidate_incentive_reserved_factor': 'u32',
        'liquidation_threshold': 'u32',
        'rate_model': {
            'Curve': {
                'base_rate': 'u128',
            },
            'Jump': {
                'base_rate': 'u128',
                'full_rate': 'u128',
                'jump_rate': 'u128',
                'jump_utilization': 'u32',
            },
        },
        'reserve_factor': 'u32',
        'state': (
            'Active',
            'Pending',
            'Supervision',
        ),
        'supply_cap': 'u128',
    },
}
)
```

---------
### liquidate_borrow
The caller liquidates the borrower&\#x27;s collateral. This extrinsic may need to be called multiple
times to completely clear the borrower&\#x27;s bad debt, because of the `close_factor` parameter in
the market. See the `close_factor_may_require_multiple_liquidations_to_clear_bad_debt` unit
test for an example of this.

- `borrower`: the borrower to be liquidated.
- `liquidation_asset_id`: the underlying asset to be liquidated.
- `repay_amount`: the amount of `liquidation_asset_id` to be repaid. This parameter can only
be as large as the `close_factor` market parameter allows
(`close_factor * borrower_debt_in_liquidation_asset`).
- `collateral_asset_id`: The underlying currency whose lend tokens to seize from the borrower.
Note that the liquidator has to redeem the received lend tokens from the market to convert them
to `collateral_asset_id`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| borrower | `T::AccountId` | 
| liquidation_asset_id | `CurrencyId<T>` | 
| repay_amount | `BalanceOf<T>` | 
| collateral_asset_id | `CurrencyId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'liquidate_borrow', {
    'borrower': 'AccountId',
    'collateral_asset_id': {
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
    'liquidation_asset_id': {
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
    'repay_amount': 'u128',
}
)
```

---------
### mint
The caller supplies (lends) assets into the market and receives a corresponding amount
of lend tokens, at the current internal exchange rate.

- `asset_id`: the asset to be deposited.
- `mint_amount`: the amount to be deposited.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `CurrencyId<T>` | 
| mint_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'mint', {
    'asset_id': {
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
    'mint_amount': 'u128',
}
)
```

---------
### redeem
The caller redeems lend tokens for the underlying asset, at the current
internal exchange rate.

- `asset_id`: the asset to be redeemed
- `redeem_amount`: the amount to be redeemed, expressed in the underyling currency (`asset_id`)
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `CurrencyId<T>` | 
| redeem_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'redeem', {
    'asset_id': {
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
    'redeem_amount': 'u128',
}
)
```

---------
### redeem_all
The caller redeems their entire lend token balance in exchange for the underlying asset.
Note: this will fail if the account needs some of the collateral for backing open borrows,
or if any of the lend tokens are used by other pallets (e.g. used as vault collateral)

- `asset_id`: the asset to be redeemed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `CurrencyId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'redeem_all', {
    'asset_id': {
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
}
)
```

---------
### reduce_incentive_reserves
Sender redeems some of internal supplies in exchange for the underlying asset.

- `asset_id`: the asset to be redeemed.
- `redeem_amount`: the amount to be redeemed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| receiver | `<T::Lookup as StaticLookup>::Source` | 
| asset_id | `CurrencyId<T>` | 
| redeem_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'reduce_incentive_reserves', {
    'asset_id': {
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
    'receiver': 'AccountId',
    'redeem_amount': 'u128',
}
)
```

---------
### reduce_reserves
Reduces reserves (treasury&\#x27;s share of accrued interest) by transferring to receiver.

May only be called from `T::ReserveOrigin`.

- `receiver`: the receiver account.
- `asset_id`: the assets to be reduced.
- `reduce_amount`: the amount to be reduced.
#### Attributes
| Name | Type |
| -------- | -------- | 
| receiver | `<T::Lookup as StaticLookup>::Source` | 
| asset_id | `CurrencyId<T>` | 
| reduce_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'reduce_reserves', {
    'asset_id': {
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
    'receiver': 'AccountId',
    'reduce_amount': 'u128',
}
)
```

---------
### repay_borrow
The caller repays some of their debts.

- `asset_id`: the asset to be repaid.
- `repay_amount`: the amount to be repaid, in the underlying currency (`asset_id`).
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `CurrencyId<T>` | 
| repay_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'repay_borrow', {
    'asset_id': {
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
    'repay_amount': 'u128',
}
)
```

---------
### repay_borrow_all
The caller repays all of their debts.

- `asset_id`: the asset to be repaid.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `CurrencyId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'repay_borrow_all', {
    'asset_id': {
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
}
)
```

---------
### update_market
Updates a stored market. Returns `Err` if the market currency does not exist.

- `asset_id`: market related currency
- `collateral_factor`: the collateral utilization ratio
- `liquidation_threshold`: The collateral ratio when a borrower can be liquidated
- `reserve_factor`: fraction of interest set aside for reserves
- `close_factor`: max percentage of debt that can be liquidated in a single transaction
- `liquidate_incentive_reserved_factor`: liquidation share set aside for reserves
- `liquidate_incentive`: liquidation incentive ratio
- `supply_cap`: Upper bound of supplying
- `borrow_cap`: Upper bound of borrowing
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `CurrencyId<T>` | 
| collateral_factor | `Option<Ratio>` | 
| liquidation_threshold | `Option<Ratio>` | 
| reserve_factor | `Option<Ratio>` | 
| close_factor | `Option<Ratio>` | 
| liquidate_incentive_reserved_factor | `Option<Ratio>` | 
| liquidate_incentive | `Option<Rate>` | 
| supply_cap | `Option<BalanceOf<T>>` | 
| borrow_cap | `Option<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'update_market', {
    'asset_id': {
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
    'borrow_cap': (None, 'u128'),
    'close_factor': (None, 'u32'),
    'collateral_factor': (None, 'u32'),
    'liquidate_incentive': (
        None,
        'u128',
    ),
    'liquidate_incentive_reserved_factor': (
        None,
        'u32',
    ),
    'liquidation_threshold': (
        None,
        'u32',
    ),
    'reserve_factor': (None, 'u32'),
    'supply_cap': (None, 'u128'),
}
)
```

---------
### update_market_reward_speed
Updates reward speed for the specified market

The origin must conform to `UpdateOrigin`.

- `asset_id`: Market related currency
- `supply_reward_per_block`: supply reward amount per block.
- `borrow_reward_per_block`: borrow reward amount per block.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `CurrencyId<T>` | 
| supply_reward_per_block | `Option<BalanceOf<T>>` | 
| borrow_reward_per_block | `Option<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'update_market_reward_speed', {
    'asset_id': {
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
    'borrow_reward_per_block': (
        None,
        'u128',
    ),
    'supply_reward_per_block': (
        None,
        'u128',
    ),
}
)
```

---------
### update_rate_model
Updates the rate model of a stored market. Returns `Err` if the market
currency does not exist or the rate model is invalid.

- `asset_id`: Market currency
- `rate_model`: The new rate model to set
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `CurrencyId<T>` | 
| rate_model | `InterestRateModel` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'update_rate_model', {
    'asset_id': {
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
    'rate_model': {
        'Curve': {'base_rate': 'u128'},
        'Jump': {
            'base_rate': 'u128',
            'full_rate': 'u128',
            'jump_rate': 'u128',
            'jump_utilization': 'u32',
        },
    },
}
)
```

---------
### withdraw_all_collateral
Caller disables their lend token balance as borrow collateral. This operation unlocks
the lend tokens, so they become transferrable.
This operation can only succeed if the caller&\#x27;s debt is backed by sufficient collateral
excluding this currency.

- `asset_id`: the underlying asset denoting the market whose lend tokens are to be
disabled as collateral.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `CurrencyId<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'withdraw_all_collateral', {
    'asset_id': {
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
}
)
```

---------
## Events

---------
### ActivatedMarket
Event emitted when a market is activated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| underlying_currency_id | `CurrencyId<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```

---------
### Borrowed
Event emitted when cash is borrowed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| currency_id | `CurrencyId<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| amount | `BalanceOf<T>` | ```u128```

---------
### DepositCollateral
Enable collateral for certain asset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| currency_id | `CurrencyId<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| amount | `BalanceOf<T>` | ```u128```

---------
### Deposited
Event emitted when assets are deposited
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| currency_id | `CurrencyId<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| amount | `BalanceOf<T>` | ```u128```

---------
### DistributedBorrowerReward
Deposited when Reward is distributed to a borrower
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| underlying_currency_id | `CurrencyId<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| borrower | `T::AccountId` | ```AccountId```
| reward_delta | `BalanceOf<T>` | ```u128```
| borrow_reward_index | `BalanceOf<T>` | ```u128```

---------
### DistributedSupplierReward
Deposited when Reward is distributed to a supplier
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| underlying_currency_id | `CurrencyId<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| supplier | `T::AccountId` | ```AccountId```
| reward_delta | `BalanceOf<T>` | ```u128```
| supply_reward_index | `BalanceOf<T>` | ```u128```

---------
### IncentiveReservesReduced
Event emitted when the incentive reserves are redeemed and transfer to receiver&\#x27;s account
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| receiver | `T::AccountId` | ```AccountId```
| currency_id | `CurrencyId<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| amount | `BalanceOf<T>` | ```u128```

---------
### InterestAccrued
Event emitted when interest has been accrued for a market
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| underlying_currency_id | `CurrencyId<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| total_borrows | `BalanceOf<T>` | ```u128```
| total_reserves | `BalanceOf<T>` | ```u128```
| borrow_index | `FixedU128` | ```u128```
| utilization_ratio | `Ratio` | ```u32```
| borrow_rate | `Rate` | ```u128```
| supply_rate | `Rate` | ```u128```
| exchange_rate | `Rate` | ```u128```

---------
### LiquidatedBorrow
Event emitted when a borrow is liquidated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| liquidator | `T::AccountId` | ```AccountId```
| borrower | `T::AccountId` | ```AccountId```
| liquidation_currency_id | `CurrencyId<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| collateral_currency_id | `CurrencyId<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| repay_amount | `BalanceOf<T>` | ```u128```
| collateral_underlying_amount | `BalanceOf<T>` | ```u128```

---------
### MarketRewardSpeedUpdated
Event emitted when market reward speed updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| underlying_currency_id | `CurrencyId<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| supply_reward_per_block | `BalanceOf<T>` | ```u128```
| borrow_reward_per_block | `BalanceOf<T>` | ```u128```

---------
### NewMarket
New market is set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| underlying_currency_id | `CurrencyId<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| market | `Market<BalanceOf<T>>` | ```{'collateral_factor': 'u32', 'liquidation_threshold': 'u32', 'reserve_factor': 'u32', 'close_factor': 'u32', 'liquidate_incentive': 'u128', 'liquidate_incentive_reserved_factor': 'u32', 'rate_model': {'Jump': {'base_rate': 'u128', 'jump_rate': 'u128', 'full_rate': 'u128', 'jump_utilization': 'u32'}, 'Curve': {'base_rate': 'u128'}}, 'state': ('Active', 'Pending', 'Supervision'), 'supply_cap': 'u128', 'borrow_cap': 'u128', 'lend_token_id': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}}```

---------
### Redeemed
Event emitted when assets are redeemed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| currency_id | `CurrencyId<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| amount | `BalanceOf<T>` | ```u128```

---------
### RepaidBorrow
Event emitted when a borrow is repaid
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| currency_id | `CurrencyId<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| amount | `BalanceOf<T>` | ```u128```

---------
### ReservesAdded
Event emitted when the reserves are added
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| payer | `T::AccountId` | ```AccountId```
| currency_id | `CurrencyId<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| amount | `BalanceOf<T>` | ```u128```
| new_reserve_amount | `BalanceOf<T>` | ```u128```

---------
### ReservesReduced
Event emitted when the reserves are reduced
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| receiver | `T::AccountId` | ```AccountId```
| currency_id | `CurrencyId<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| amount | `BalanceOf<T>` | ```u128```
| new_reserve_amount | `BalanceOf<T>` | ```u128```

---------
### RewardAdded
Reward added
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| payer | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### RewardPaid
Reward Paid for user
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| receiver | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### RewardWithdrawn
Reward withdrawed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| receiver | `T::AccountId` | ```AccountId```
| amount | `BalanceOf<T>` | ```u128```

---------
### UpdatedMarket
New market parameters is updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| underlying_currency_id | `CurrencyId<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| market | `Market<BalanceOf<T>>` | ```{'collateral_factor': 'u32', 'liquidation_threshold': 'u32', 'reserve_factor': 'u32', 'close_factor': 'u32', 'liquidate_incentive': 'u128', 'liquidate_incentive_reserved_factor': 'u32', 'rate_model': {'Jump': {'base_rate': 'u128', 'jump_rate': 'u128', 'full_rate': 'u128', 'jump_utilization': 'u32'}, 'Curve': {'base_rate': 'u128'}}, 'state': ('Active', 'Pending', 'Supervision'), 'supply_cap': 'u128', 'borrow_cap': 'u128', 'lend_token_id': {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}}```

---------
### WithdrawCollateral
Disable collateral for certain asset
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```
| currency_id | `CurrencyId<T>` | ```{'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'LendToken': 'u32', 'LpToken': ({'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}, {'Token': ('DOT', 'IBTC', 'INTR', 'KSM', 'KBTC', 'KINT'), 'ForeignAsset': 'u32', 'StableLpToken': 'u32'}), 'StableLpToken': 'u32'}```
| amount | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### AccountBorrows
 Mapping of account addresses to outstanding borrow balances
 CurrencyId -&gt; Owner -&gt; BorrowSnapshot

#### Python
```python
result = substrate.query(
    'Loans', 'AccountBorrows', [
    {
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
    'AccountId',
]
)
```

#### Return value
```python
{'borrow_index': 'u128', 'principal': 'u128'}
```
---------
### AccountDeposits
 Mapping of account addresses to collateral deposit details
 CollateralType -&gt; Owner -&gt; Collateral Deposits

 \# Remarks

 Differently from Parallel Finance&#x27;s implementation of lending, `AccountDeposits` only
 represents Lend Tokens locked as collateral rather than the entire Lend Token balance of an account.
 If an account minted without also locking their balance as collateral, their corresponding entry
 in this map will be zero.

#### Python
```python
result = substrate.query(
    'Loans', 'AccountDeposits', [
    {
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
    'AccountId',
]
)
```

#### Return value
```python
'u128'
```
---------
### BorrowIndex
 Accumulator of the total earned interest rate since the opening of the market
 CurrencyId -&gt; u128

#### Python
```python
result = substrate.query(
    'Loans', 'BorrowIndex', [
    {
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
]
)
```

#### Return value
```python
'u128'
```
---------
### BorrowRate
 Mapping of borrow rate to currency type

#### Python
```python
result = substrate.query(
    'Loans', 'BorrowRate', [
    {
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
]
)
```

#### Return value
```python
'u128'
```
---------
### ExchangeRate
 The internal exchange rate from the associated lend token to the underlying currency.

#### Python
```python
result = substrate.query(
    'Loans', 'ExchangeRate', [
    {
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
]
)
```

#### Return value
```python
'u128'
```
---------
### LastAccruedInterestTime
 The timestamp of the last calculation of accrued interest

#### Python
```python
result = substrate.query(
    'Loans', 'LastAccruedInterestTime', [
    {
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
]
)
```

#### Return value
```python
'u64'
```
---------
### Markets
 Mapping of underlying currency id to its market

#### Python
```python
result = substrate.query(
    'Loans', 'Markets', [
    {
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
]
)
```

#### Return value
```python
{
    'borrow_cap': 'u128',
    'close_factor': 'u32',
    'collateral_factor': 'u32',
    'lend_token_id': {
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
    'liquidate_incentive': 'u128',
    'liquidate_incentive_reserved_factor': 'u32',
    'liquidation_threshold': 'u32',
    'rate_model': {
        'Curve': {'base_rate': 'u128'},
        'Jump': {
            'base_rate': 'u128',
            'full_rate': 'u128',
            'jump_rate': 'u128',
            'jump_utilization': 'u32',
        },
    },
    'reserve_factor': 'u32',
    'state': ('Active', 'Pending', 'Supervision'),
    'supply_cap': 'u128',
}
```
---------
### MaxExchangeRate
 The maximum allowed exchange rate for a market.

#### Python
```python
result = substrate.query(
    'Loans', 'MaxExchangeRate', []
)
```

#### Return value
```python
'u128'
```
---------
### MinExchangeRate
 The minimum allowed exchange rate for a market. This is the starting rate when a market is first set up.

#### Python
```python
result = substrate.query(
    'Loans', 'MinExchangeRate', []
)
```

#### Return value
```python
'u128'
```
---------
### RewardAccrued
 The incentive reward accrued but not yet transferred to each user.

#### Python
```python
result = substrate.query(
    'Loans', 'RewardAccrued', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### RewardBorrowSpeed
 Mapping of underlying currency id to borrow reward speed

#### Python
```python
result = substrate.query(
    'Loans', 'RewardBorrowSpeed', [
    {
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
]
)
```

#### Return value
```python
'u128'
```
---------
### RewardBorrowState
 The Reward market borrow state for each market

#### Python
```python
result = substrate.query(
    'Loans', 'RewardBorrowState', [
    {
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
]
)
```

#### Return value
```python
{'block': 'u32', 'index': 'u128'}
```
---------
### RewardBorrowerIndex
 The incentive reward index for each market for each borrower as of the last time they accrued Reward

#### Python
```python
result = substrate.query(
    'Loans', 'RewardBorrowerIndex', [
    {
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
    'AccountId',
]
)
```

#### Return value
```python
'u128'
```
---------
### RewardSupplierIndex
 The incentive reward index for each market for each supplier as of the last time they accrued Reward

#### Python
```python
result = substrate.query(
    'Loans', 'RewardSupplierIndex', [
    {
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
    'AccountId',
]
)
```

#### Return value
```python
'u128'
```
---------
### RewardSupplySpeed
 Mapping of underlying currency id to supply reward speed

#### Python
```python
result = substrate.query(
    'Loans', 'RewardSupplySpeed', [
    {
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
]
)
```

#### Return value
```python
'u128'
```
---------
### RewardSupplyState
 The Reward market supply state for each market

#### Python
```python
result = substrate.query(
    'Loans', 'RewardSupplyState', [
    {
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
]
)
```

#### Return value
```python
{'block': 'u32', 'index': 'u128'}
```
---------
### StorageVersion
 Storage version of the pallet.

#### Python
```python
result = substrate.query(
    'Loans', 'StorageVersion', []
)
```

#### Return value
```python
('V0', )
```
---------
### SupplyRate
 Mapping of supply rate to currency type

#### Python
```python
result = substrate.query(
    'Loans', 'SupplyRate', [
    {
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
]
)
```

#### Return value
```python
'u128'
```
---------
### TotalBorrows
 Total amount of outstanding borrows of the underlying in this market
 CurrencyId -&gt; Balance

#### Python
```python
result = substrate.query(
    'Loans', 'TotalBorrows', [
    {
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
]
)
```

#### Return value
```python
'u128'
```
---------
### TotalReserves
 Total amount of reserves of the underlying held in this market
 CurrencyId -&gt; Balance

#### Python
```python
result = substrate.query(
    'Loans', 'TotalReserves', [
    {
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
]
)
```

#### Return value
```python
'u128'
```
---------
### UnderlyingAssetId
 Mapping of lend_token id to underlying currency id
 `lend_token id`: voucher token id
 `asset id`: underlying token id

#### Python
```python
result = substrate.query(
    'Loans', 'UnderlyingAssetId', [
    {
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
]
)
```

#### Return value
```python
{
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
}
```
---------
### UtilizationRatio
 Borrow utilization ratio

#### Python
```python
result = substrate.query(
    'Loans', 'UtilizationRatio', [
    {
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
]
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### PalletId
 The loan&#x27;s module id, used to derive the account that holds the liquidity in all markets.
#### Value
```python
'0x6d6f642f6c6f616e'
```
#### Python
```python
constant = substrate.get_constant('Loans', 'PalletId')
```
---------
### ReferenceAssetId
 Reference currency for expressing asset prices. Example: USD, IBTC.
#### Value
```python
{'Token': 'KBTC'}
```
#### Python
```python
constant = substrate.get_constant('Loans', 'ReferenceAssetId')
```
---------
### RewardAssetId
 Incentive reward asset id.
#### Value
```python
{'Token': 'KINT'}
```
#### Python
```python
constant = substrate.get_constant('Loans', 'RewardAssetId')
```
---------
## Errors

---------
### BorrowCapacityExceeded
Upper bound of borrowing is exceeded

---------
### DepositAllCollateralFailed
Locking collateral failed. The account has no `free` tokens.

---------
### DepositsAreNotCollateral
Deposits are not used as a collateral

---------
### InsufficientCash
Insufficient cash in the pool

---------
### InsufficientCollateral
Repay amount more than collateral amount

---------
### InsufficientDeposit
Insufficient deposit to redeem

---------
### InsufficientLiquidity
Insufficient liquidity to borrow more or disable collateral

---------
### InsufficientReserves
Insufficient reserves

---------
### InsufficientShortfall
Insufficient shortfall to repay

---------
### InvalidAmount
Amount cannot be zero

---------
### InvalidExchangeRate
The exchange rate should be a value between `MinExchangeRate` and `MaxExchangeRate`

---------
### InvalidFactor
The factor should be greater than 0% and less than 100%

---------
### InvalidLendTokenId
Invalid lend_token id

---------
### InvalidRateModelParam
Invalid rate model params

---------
### InvalidSupplyCap
The supply cap cannot be zero

---------
### LiquidatorIsBorrower
Liquidator is same as borrower

---------
### LockedTokensCannotBeRedeemed
Only free lend tokens are redeemable

---------
### MarketAlreadyExists
Market already exists

---------
### MarketDoesNotExist
Market does not exist

---------
### MarketNotActivated
Market not activated

---------
### NewMarketMustHavePendingState
New markets must have a pending state

---------
### SupplyCapacityExceeded
Upper bound of supplying is exceeded

---------
### TokensAlreadyLocked
Tokens already locked for a different purpose than borrow collateral

---------
### TooMuchRepay
Repay amount greater than allowed (either repays more than the existing debt, or
exceeds the close factor)

---------
### WithdrawAllCollateralFailed
Unlocking collateral failed. The account has no `reserved` tokens.

---------