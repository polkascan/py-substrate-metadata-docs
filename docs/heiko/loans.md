
# Loans

---------
## Calls

---------
### activate_market
Activates a market. Returns `Err` if the market currency does not exist.

If the market is already activated, does nothing.

- `asset_id`: Market related currency
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'activate_market', {'asset_id': 'u32'}
)
```

---------
### add_market
Stores a new market and its related currency. Returns `Err` if a currency
is not attached to an existent market.

All provided market states must be `Pending`, otherwise an error will be returned.

If a currency is already attached to a market, then the market will be replaced
by the new provided value.

The ptoken id and asset id are bound, the ptoken id of new provided market cannot
be duplicated with the existing one, otherwise it will return `InvalidPtokenId`.

- `asset_id`: Market related currency
- `market`: The market that is going to be stored
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetIdOf<T>` | 
| market | `Market<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'add_market', {
    'asset_id': 'u32',
    'market': {
        'borrow_cap': 'u128',
        'close_factor': 'u32',
        'collateral_factor': 'u32',
        'liquidate_incentive': 'u128',
        'liquidate_incentive_reserved_factor': 'u32',
        'liquidation_threshold': 'u32',
        'ptoken_id': 'u32',
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

May only be called from `T::ReserveOrigin`.

- `payer`: the payer account.
- `asset_id`: the assets to be added.
- `add_amount`: the amount to be added.
#### Attributes
| Name | Type |
| -------- | -------- | 
| payer | `<T::Lookup as StaticLookup>::Source` | 
| asset_id | `AssetIdOf<T>` | 
| add_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'add_reserves', {
    'add_amount': 'u128',
    'asset_id': 'u32',
    'payer': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
### add_reward
Add reward for the pallet account.

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
Sender borrows assets from the protocol to their own address.

- `asset_id`: the asset to be borrowed.
- `borrow_amount`: the amount to be borrowed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetIdOf<T>` | 
| borrow_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'borrow', {
    'asset_id': 'u32',
    'borrow_amount': 'u128',
}
)
```

---------
### claim_reward
Claim reward from all market.
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
Claim reward from the specified market.

- `asset_id`: Market related currency
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'claim_reward_for_market', {'asset_id': 'u32'}
)
```

---------
### collateral_asset
Set the collateral asset.

- `asset_id`: the asset to be set.
- `enable`: turn on/off the collateral option.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetIdOf<T>` | 
| enable | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'collateral_asset', {'asset_id': 'u32', 'enable': 'bool'}
)
```

---------
### force_update_market
Force updates a stored market. Returns `Err` if the market currency
does not exist.

- `asset_id`: market related currency
- `market`: the new market parameters
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetIdOf<T>` | 
| market | `Market<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'force_update_market', {
    'asset_id': 'u32',
    'market': {
        'borrow_cap': 'u128',
        'close_factor': 'u32',
        'collateral_factor': 'u32',
        'liquidate_incentive': 'u128',
        'liquidate_incentive_reserved_factor': 'u32',
        'liquidation_threshold': 'u32',
        'ptoken_id': 'u32',
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
The sender liquidates the borrower&\#x27;s collateral.

- `borrower`: the borrower to be liquidated.
- `liquidation_asset_id`: the assert to be liquidated.
- `repay_amount`: the amount to be repaid borrow.
- `collateral_asset_id`: The collateral to seize from the borrower.
#### Attributes
| Name | Type |
| -------- | -------- | 
| borrower | `T::AccountId` | 
| liquidation_asset_id | `AssetIdOf<T>` | 
| repay_amount | `BalanceOf<T>` | 
| collateral_asset_id | `AssetIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'liquidate_borrow', {
    'borrower': 'AccountId',
    'collateral_asset_id': 'u32',
    'liquidation_asset_id': 'u32',
    'repay_amount': 'u128',
}
)
```

---------
### mint
Sender supplies assets into the market and receives internal supplies in exchange.

- `asset_id`: the asset to be deposited.
- `mint_amount`: the amount to be deposited.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetIdOf<T>` | 
| mint_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'mint', {
    'asset_id': 'u32',
    'mint_amount': 'u128',
}
)
```

---------
### redeem
Sender redeems some of internal supplies in exchange for the underlying asset.

- `asset_id`: the asset to be redeemed.
- `redeem_amount`: the amount to be redeemed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetIdOf<T>` | 
| redeem_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'redeem', {
    'asset_id': 'u32',
    'redeem_amount': 'u128',
}
)
```

---------
### redeem_all
Sender redeems all of internal supplies in exchange for the underlying asset.

- `asset_id`: the asset to be redeemed.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'redeem_all', {'asset_id': 'u32'}
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
| asset_id | `AssetIdOf<T>` | 
| redeem_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'reduce_incentive_reserves', {
    'asset_id': 'u32',
    'receiver': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'redeem_amount': 'u128',
}
)
```

---------
### reduce_reserves
Reduces reserves by transferring to receiver.

May only be called from `T::ReserveOrigin`.

- `receiver`: the receiver account.
- `asset_id`: the assets to be reduced.
- `reduce_amount`: the amount to be reduced.
#### Attributes
| Name | Type |
| -------- | -------- | 
| receiver | `<T::Lookup as StaticLookup>::Source` | 
| asset_id | `AssetIdOf<T>` | 
| reduce_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'reduce_reserves', {
    'asset_id': 'u32',
    'receiver': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
    'reduce_amount': 'u128',
}
)
```

---------
### repay_borrow
Sender repays some of their debts.

- `asset_id`: the asset to be repaid.
- `repay_amount`: the amount to be repaid.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetIdOf<T>` | 
| repay_amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'repay_borrow', {
    'asset_id': 'u32',
    'repay_amount': 'u128',
}
)
```

---------
### repay_borrow_all
Sender repays all of their debts.

- `asset_id`: the asset to be repaid.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'repay_borrow_all', {'asset_id': 'u32'}
)
```

---------
### update_liquidation_free_collateral
Update liquidation free collateral.

The `assets` won&\#x27;t be counted when do general
#### Attributes
| Name | Type |
| -------- | -------- | 
| collaterals | `Vec<AssetIdOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'update_liquidation_free_collateral', {'collaterals': ['u32']}
)
```

---------
### update_market
Updates a stored market. Returns `Err` if the market currency does not exist.

- `asset_id`: market related currency
- `collateral_factor`: the collateral utilization ratio
- `reserve_factor`: fraction of interest currently set aside for reserves
- `close_factor`: maximum liquidation ratio at one time
- `liquidate_incentive`: liquidation incentive ratio
- `cap`: market capacity
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetIdOf<T>` | 
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
    'asset_id': 'u32',
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
- `reward_per_block`: reward amount per block.
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetIdOf<T>` | 
| supply_reward_per_block | `Option<BalanceOf<T>>` | 
| borrow_reward_per_block | `Option<BalanceOf<T>>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'update_market_reward_speed', {
    'asset_id': 'u32',
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

- `asset_id`: Market related currency
- `rate_model`: The new rate model to be updated
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `AssetIdOf<T>` | 
| rate_model | `InterestRateModel` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'update_rate_model', {
    'asset_id': 'u32',
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
### withdraw_missing_reward
Withdraw reward token from pallet account.

The origin must conform to `UpdateOrigin`.

- `target_account`: account receive reward token.
- `amount`: Withdraw amount
#### Attributes
| Name | Type |
| -------- | -------- | 
| target_account | `<T::Lookup as StaticLookup>::Source` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'withdraw_missing_reward', {
    'amount': 'u128',
    'target_account': {
        'Address20': '[u8; 20]',
        'Address32': '[u8; 32]',
        'Id': 'AccountId',
        'Index': (),
        'Raw': 'Bytes',
    },
}
)
```

---------
## Events

---------
### ActivatedMarket
Event emitted when a market is activated
[admin, asset_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetIdOf<T>` | ```u32```

---------
### Borrowed
Event emitted when cash is borrowed
[sender, asset_id, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetIdOf<T>` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### CollateralAssetAdded
Enable collateral for certain asset
[sender, asset_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetIdOf<T>` | ```u32```

---------
### CollateralAssetRemoved
Disable collateral for certain asset
[sender, asset_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetIdOf<T>` | ```u32```

---------
### Deposited
Event emitted when assets are deposited
[sender, asset_id, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetIdOf<T>` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### DistributedBorrowerReward
Deposited when Reward is distributed to a borrower
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetIdOf<T>` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### DistributedSupplierReward
Deposited when Reward is distributed to a supplier
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetIdOf<T>` | ```u32```
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### IncentiveReservesReduced
Event emitted when the incentive reserves are redeemed and transfer to receiver&\#x27;s account
[receive_account_id, asset_id, reduced_amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetIdOf<T>` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### LiquidatedBorrow
Event emitted when a borrow is liquidated
[liquidator, borrower, liquidation_asset_id, collateral_asset_id, repay_amount, collateral_amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `AssetIdOf<T>` | ```u32```
| None | `AssetIdOf<T>` | ```u32```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### LiquidationFreeCollateralsUpdated
Liquidation free collaterals has been updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Vec<AssetIdOf<T>>` | ```['u32']```

---------
### MarketRewardSpeedUpdated
Event emitted when market reward speed updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetIdOf<T>` | ```u32```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### NewMarket
New market is set
[new_interest_rate_model]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetIdOf<T>` | ```u32```
| None | `Market<BalanceOf<T>>` | ```{'collateral_factor': 'u32', 'liquidation_threshold': 'u32', 'reserve_factor': 'u32', 'close_factor': 'u32', 'liquidate_incentive': 'u128', 'liquidate_incentive_reserved_factor': 'u32', 'rate_model': {'Jump': {'base_rate': 'u128', 'jump_rate': 'u128', 'full_rate': 'u128', 'jump_utilization': 'u32'}, 'Curve': {'base_rate': 'u128'}}, 'state': ('Active', 'Pending', 'Supervision'), 'supply_cap': 'u128', 'borrow_cap': 'u128', 'ptoken_id': 'u32'}```

---------
### Redeemed
Event emitted when assets are redeemed
[sender, asset_id, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetIdOf<T>` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### RepaidBorrow
Event emitted when a borrow is repaid
[sender, asset_id, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetIdOf<T>` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### ReservesAdded
Event emitted when the reserves are added
[admin, asset_id, added_amount, total_reserves]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetIdOf<T>` | ```u32```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### ReservesReduced
Event emitted when the reserves are reduced
[admin, asset_id, reduced_amount, total_reserves]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `AssetIdOf<T>` | ```u32```
| None | `BalanceOf<T>` | ```u128```
| None | `BalanceOf<T>` | ```u128```

---------
### RewardAdded
Reward added
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### RewardPaid
Reward Paid for user
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### RewardWithdrawn
Reward withdrawed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BalanceOf<T>` | ```u128```

---------
### UpdatedMarket
New market parameters is updated
[admin, asset_id]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AssetIdOf<T>` | ```u32```
| None | `Market<BalanceOf<T>>` | ```{'collateral_factor': 'u32', 'liquidation_threshold': 'u32', 'reserve_factor': 'u32', 'close_factor': 'u32', 'liquidate_incentive': 'u128', 'liquidate_incentive_reserved_factor': 'u32', 'rate_model': {'Jump': {'base_rate': 'u128', 'jump_rate': 'u128', 'full_rate': 'u128', 'jump_utilization': 'u32'}, 'Curve': {'base_rate': 'u128'}}, 'state': ('Active', 'Pending', 'Supervision'), 'supply_cap': 'u128', 'borrow_cap': 'u128', 'ptoken_id': 'u32'}```

---------
## Storage functions

---------
### AccountBorrows
 Mapping of account addresses to outstanding borrow balances
 CurrencyId -&gt; Owner -&gt; BorrowSnapshot

#### Python
```python
result = substrate.query(
    'Loans', 'AccountBorrows', ['u32', 'AccountId']
)
```

#### Return value
```python
{'borrow_index': 'u128', 'principal': 'u128'}
```
---------
### AccountDeposits
 Mapping of account addresses to deposit details
 CollateralType -&gt; Owner -&gt; Deposits

#### Python
```python
result = substrate.query(
    'Loans', 'AccountDeposits', ['u32', 'AccountId']
)
```

#### Return value
```python
{'is_collateral': 'bool', 'voucher_balance': 'u128'}
```
---------
### AccountEarned
 Mapping of account addresses to total deposit interest accrual
 CurrencyId -&gt; Owner -&gt; EarnedSnapshot

#### Python
```python
result = substrate.query(
    'Loans', 'AccountEarned', ['u32', 'AccountId']
)
```

#### Return value
```python
{'exchange_rate_prior': 'u128', 'total_earned_prior': 'u128'}
```
---------
### BorrowIndex
 Accumulator of the total earned interest rate since the opening of the market
 CurrencyId -&gt; u128

#### Python
```python
result = substrate.query(
    'Loans', 'BorrowIndex', ['u32']
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
    'Loans', 'BorrowRate', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### ExchangeRate
 The exchange rate from the underlying to the internal collateral

#### Python
```python
result = substrate.query(
    'Loans', 'ExchangeRate', ['u32']
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
    'Loans', 'LastAccruedInterestTime', ['u32']
)
```

#### Return value
```python
'u64'
```
---------
### LiquidationFreeCollaterals
 Liquidation free collateral.

#### Python
```python
result = substrate.query(
    'Loans', 'LiquidationFreeCollaterals', []
)
```

#### Return value
```python
['u32']
```
---------
### Markets
 Mapping of asset id to its market

#### Python
```python
result = substrate.query(
    'Loans', 'Markets', ['u32']
)
```

#### Return value
```python
{
    'borrow_cap': 'u128',
    'close_factor': 'u32',
    'collateral_factor': 'u32',
    'liquidate_incentive': 'u128',
    'liquidate_incentive_reserved_factor': 'u32',
    'liquidation_threshold': 'u32',
    'ptoken_id': 'u32',
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
### RewardAccured
 The reward accrued but not yet transferred to each user.

#### Python
```python
result = substrate.query(
    'Loans', 'RewardAccured', ['AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### RewardBorrowSpeed
 Mapping of token id to borrow reward speed

#### Python
```python
result = substrate.query(
    'Loans', 'RewardBorrowSpeed', ['u32']
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
    'Loans', 'RewardBorrowState', ['u32']
)
```

#### Return value
```python
{'block': 'u32', 'index': 'u128'}
```
---------
### RewardBorrowerIndex
  The Reward index for each market for each borrower as of the last time they accrued Reward

#### Python
```python
result = substrate.query(
    'Loans', 'RewardBorrowerIndex', ['u32', 'AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### RewardSupplierIndex
  The Reward index for each market for each supplier as of the last time they accrued Reward

#### Python
```python
result = substrate.query(
    'Loans', 'RewardSupplierIndex', ['u32', 'AccountId']
)
```

#### Return value
```python
'u128'
```
---------
### RewardSupplySpeed
 Mapping of token id to supply reward speed

#### Python
```python
result = substrate.query(
    'Loans', 'RewardSupplySpeed', ['u32']
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
    'Loans', 'RewardSupplyState', ['u32']
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
('V1', 'V2', 'V3', 'V4', 'V5', 'V6')
```
---------
### SupplyRate
 Mapping of supply rate to currency type

#### Python
```python
result = substrate.query(
    'Loans', 'SupplyRate', ['u32']
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
    'Loans', 'TotalBorrows', ['u32']
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
    'Loans', 'TotalReserves', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### TotalSupply
 Total number of collateral tokens in circulation
 CollateralType -&gt; Balance

#### Python
```python
result = substrate.query(
    'Loans', 'TotalSupply', ['u32']
)
```

#### Return value
```python
'u128'
```
---------
### UnderlyingAssetId
 Mapping of ptoken id to asset id
 `ptoken id`: voucher token id
 `asset id`: underlying token id

#### Python
```python
result = substrate.query(
    'Loans', 'UnderlyingAssetId', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### UtilizationRatio
 Borrow utilization ratio

#### Python
```python
result = substrate.query(
    'Loans', 'UtilizationRatio', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### LiquidationFreeAssetId
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Loans', 'LiquidationFreeAssetId')
```
---------
### PalletId
 The loan&#x27;s module id, keep all collaterals of CDPs.
#### Value
```python
'0x7061722f6c6f616e'
```
#### Python
```python
constant = substrate.get_constant('Loans', 'PalletId')
```
---------
### RewardAssetId
 Reward asset id.
#### Value
```python
0
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
### CodecError
Codec error

---------
### CollateralReserved
Collateral is reserved and cannot be liquidated

---------
### DepositsAreNotCollateral
Deposits are not used as a collateral

---------
### DuplicateOperation
Asset already enabled/disabled collateral

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
### InvalidCurrencyId
Invalid asset id

---------
### InvalidExchangeRate
The exchange rate should be greater than 0.02 and less than 1

---------
### InvalidFactor
The factor should be greater than 0% and less than 100%

---------
### InvalidPtokenId
Invalid ptoken id

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
### NoDeposit
No deposit asset

---------
### PayerIsSigner
Payer cannot be signer

---------
### PriceIsZero
Oracle price is zero

---------
### PriceOracleNotReady
Oracle price not ready

---------
### SupplyCapacityExceeded
Upper bound of supplying is exceeded

---------
### TooMuchRepay
Repay amount greater than allowed

---------