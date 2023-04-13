
# Fee

---------
## Calls

---------
### set_commission
todo: proper weight
#### Attributes
| Name | Type |
| -------- | -------- | 
| currencies | `DefaultVaultCurrencyPair<T>` | 
| commission | `UnsignedFixedPoint<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Fee', 'set_commission', {
    'commission': 'u128',
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
### set_issue_fee
Changes the issue fee percentage (only executable by the Root account)

\# Arguments

* `origin` - signing account
* `fee` - the new fee
#### Attributes
| Name | Type |
| -------- | -------- | 
| fee | `UnsignedFixedPoint<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Fee', 'set_issue_fee', {'fee': 'u128'}
)
```

---------
### set_issue_griefing_collateral
Changes the issue griefing collateral percentage (only executable by the Root account)

\# Arguments

* `origin` - signing account
* `griefing_collateral` - the new griefing collateral
#### Attributes
| Name | Type |
| -------- | -------- | 
| griefing_collateral | `UnsignedFixedPoint<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Fee', 'set_issue_griefing_collateral', {'griefing_collateral': 'u128'}
)
```

---------
### set_premium_redeem_fee
Changes the premium redeem fee percentage (only executable by the Root account)

\# Arguments

* `origin` - signing account
* `fee` - the new fee
#### Attributes
| Name | Type |
| -------- | -------- | 
| fee | `UnsignedFixedPoint<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Fee', 'set_premium_redeem_fee', {'fee': 'u128'}
)
```

---------
### set_punishment_fee
Changes the punishment fee percentage (only executable by the Root account)

\# Arguments

* `origin` - signing account
* `fee` - the new fee
#### Attributes
| Name | Type |
| -------- | -------- | 
| fee | `UnsignedFixedPoint<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Fee', 'set_punishment_fee', {'fee': 'u128'}
)
```

---------
### set_redeem_fee
Changes the redeem fee percentage (only executable by the Root account)

\# Arguments

* `origin` - signing account
* `fee` - the new fee
#### Attributes
| Name | Type |
| -------- | -------- | 
| fee | `UnsignedFixedPoint<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Fee', 'set_redeem_fee', {'fee': 'u128'}
)
```

---------
### set_replace_griefing_collateral
Changes the replace griefing collateral percentage (only executable by the Root account)

\# Arguments

* `origin` - signing account
* `griefing_collateral` - the new griefing collateral
#### Attributes
| Name | Type |
| -------- | -------- | 
| griefing_collateral | `UnsignedFixedPoint<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Fee', 'set_replace_griefing_collateral', {'griefing_collateral': 'u128'}
)
```

---------
### withdraw_rewards
Withdraw all rewards from the `origin` account in the `vault_id` staking pool.

\# Arguments

* `origin` - signing account
#### Attributes
| Name | Type |
| -------- | -------- | 
| vault_id | `DefaultVaultId<T>` | 
| index | `Option<T::Index>` | 

#### Python
```python
call = substrate.compose_call(
    'Fee', 'withdraw_rewards', {
    'index': (None, 'u32'),
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
## Storage functions

---------
### Commission
 The fraction up rewards going straight to the vault operator. The rest goes to the vault&#x27;s pool.

#### Python
```python
result = substrate.query(
    'Fee', 'Commission', [
    {
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
]
)
```

#### Return value
```python
'u128'
```
---------
### IssueFee
 \# Issue
 Fee share that users need to pay to issue tokens.

#### Python
```python
result = substrate.query(
    'Fee', 'IssueFee', []
)
```

#### Return value
```python
'u128'
```
---------
### IssueGriefingCollateral
 Default griefing collateral (e.g. DOT/KSM) as a percentage of the locked
 collateral of a Vault a user has to lock to issue tokens.

#### Python
```python
result = substrate.query(
    'Fee', 'IssueGriefingCollateral', []
)
```

#### Return value
```python
'u128'
```
---------
### PremiumRedeemFee
 \# Vault Registry
 If users execute a redeem with a Vault flagged for premium redeem,
 they can earn a collateral premium, slashed from the Vault.

#### Python
```python
result = substrate.query(
    'Fee', 'PremiumRedeemFee', []
)
```

#### Return value
```python
'u128'
```
---------
### PunishmentFee
 Fee that a Vault has to pay if it fails to execute redeem or replace requests
 (for redeem, on top of the slashed value of the request). The fee is
 paid in collateral based on the token amount at the current exchange rate.

#### Python
```python
result = substrate.query(
    'Fee', 'PunishmentFee', []
)
```

#### Return value
```python
'u128'
```
---------
### RedeemFee
 \# Redeem
 Fee share that users need to pay to redeem tokens.

#### Python
```python
result = substrate.query(
    'Fee', 'RedeemFee', []
)
```

#### Return value
```python
'u128'
```
---------
### ReplaceGriefingCollateral
 \# Replace
 Default griefing collateral (e.g. DOT/KSM) as a percentage of the to-be-locked collateral
 of the new Vault. This collateral will be slashed and allocated to the replacing Vault
 if the to-be-replaced Vault does not transfer BTC on time.

#### Python
```python
result = substrate.query(
    'Fee', 'ReplaceGriefingCollateral', []
)
```

#### Return value
```python
'u128'
```
---------
### StorageVersion
 Build storage at V1 (requires default 0).

#### Python
```python
result = substrate.query(
    'Fee', 'StorageVersion', []
)
```

#### Return value
```python
('V0', )
```
---------
## Constants

---------
### FeePalletId
 The fee module id, used for deriving its sovereign account ID.
#### Value
```python
'0x6d6f642f66656573'
```
#### Python
```python
constant = substrate.get_constant('Fee', 'FeePalletId')
```
---------
### MaxExpectedValue
 Maximum expected value to set the storage fields to.
#### Value
```python
1000000000000000000
```
#### Python
```python
constant = substrate.get_constant('Fee', 'MaxExpectedValue')
```
---------
## Errors

---------
### AboveMaxExpectedValue
Value exceeds the expected upper bound for storage fields in this pallet.

---------
### TryIntoIntError
Unable to convert value.

---------