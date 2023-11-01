
# Permissions

---------
## Calls

---------
### add
#### Attributes
| Name | Type |
| -------- | -------- | 
| with_role | `T::Role` | 
| to | `T::AccountId` | 
| scope | `T::Scope` | 
| role | `T::Role` | 

#### Python
```python
call = substrate.compose_call(
    'Permissions', 'add', {
    'role': {
        'PermissionedCurrencyRole': {
            'Holder': 'u64',
            'Issuer': None,
            'Manager': None,
        },
        'PoolRole': {
            'Borrower': None,
            'InvestorAdmin': None,
            'LiquidityAdmin': None,
            'LoanAdmin': None,
            'PODReadAccess': None,
            'PoolAdmin': None,
            'PricingAdmin': None,
            'TrancheInvestor': (
                '[u8; 16]',
                'u64',
            ),
        },
    },
    'scope': {
        'Currency': {
            'AUSD': None,
            'ForeignAsset': 'u32',
            'Native': None,
            'Staking': (
                'BlockRewards',
            ),
            'Tranche': (
                'u64',
                '[u8; 16]',
            ),
            None: None,
        },
        'Pool': 'u64',
    },
    'to': 'AccountId',
    'with_role': {
        'PermissionedCurrencyRole': {
            'Holder': 'u64',
            'Issuer': None,
            'Manager': None,
        },
        'PoolRole': {
            'Borrower': None,
            'InvestorAdmin': None,
            'LiquidityAdmin': None,
            'LoanAdmin': None,
            'PODReadAccess': None,
            'PoolAdmin': None,
            'PricingAdmin': None,
            'TrancheInvestor': (
                '[u8; 16]',
                'u64',
            ),
        },
    },
}
)
```

---------
### admin_purge
#### Attributes
| Name | Type |
| -------- | -------- | 
| from | `T::AccountId` | 
| scope | `T::Scope` | 

#### Python
```python
call = substrate.compose_call(
    'Permissions', 'admin_purge', {
    'from': 'AccountId',
    'scope': {
        'Currency': {
            'Native': None,
            None: None,
            'AUSD': None,
            'ForeignAsset': 'u32',
            'Staking': (
                'BlockRewards',
            ),
            'Tranche': (
                'u64',
                '[u8; 16]',
            ),
        },
        'Pool': 'u64',
    },
}
)
```

---------
### purge
#### Attributes
| Name | Type |
| -------- | -------- | 
| scope | `T::Scope` | 

#### Python
```python
call = substrate.compose_call(
    'Permissions', 'purge', {
    'scope': {
        'Currency': {
            None: None,
            'AUSD': None,
            'ForeignAsset': 'u32',
            'Native': None,
            'Staking': (
                'BlockRewards',
            ),
            'Tranche': (
                'u64',
                '[u8; 16]',
            ),
        },
        'Pool': 'u64',
    },
}
)
```

---------
### remove
#### Attributes
| Name | Type |
| -------- | -------- | 
| with_role | `T::Role` | 
| from | `T::AccountId` | 
| scope | `T::Scope` | 
| role | `T::Role` | 

#### Python
```python
call = substrate.compose_call(
    'Permissions', 'remove', {
    'from': 'AccountId',
    'role': {
        'PermissionedCurrencyRole': {
            'Holder': 'u64',
            'Issuer': None,
            'Manager': None,
        },
        'PoolRole': {
            'Borrower': None,
            'InvestorAdmin': None,
            'LiquidityAdmin': None,
            'LoanAdmin': None,
            'PODReadAccess': None,
            'PoolAdmin': None,
            'PricingAdmin': None,
            'TrancheInvestor': (
                '[u8; 16]',
                'u64',
            ),
        },
    },
    'scope': {
        'Currency': {
            'AUSD': None,
            'ForeignAsset': 'u32',
            'Native': None,
            'Staking': (
                'BlockRewards',
            ),
            'Tranche': (
                'u64',
                '[u8; 16]',
            ),
            None: None,
        },
        'Pool': 'u64',
    },
    'with_role': {
        'PermissionedCurrencyRole': {
            'Holder': 'u64',
            'Issuer': None,
            'Manager': None,
        },
        'PoolRole': {
            'Borrower': None,
            'InvestorAdmin': None,
            'LiquidityAdmin': None,
            'LoanAdmin': None,
            'PODReadAccess': None,
            'PoolAdmin': None,
            'PricingAdmin': None,
            'TrancheInvestor': (
                '[u8; 16]',
                'u64',
            ),
        },
    },
}
)
```

---------
## Events

---------
### Added
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| to | `T::AccountId` | ```AccountId```
| scope | `T::Scope` | ```{'Pool': 'u64', 'Currency': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}}```
| role | `T::Role` | ```{'PoolRole': {'PoolAdmin': None, 'Borrower': None, 'PricingAdmin': None, 'LiquidityAdmin': None, 'InvestorAdmin': None, 'LoanAdmin': None, 'TrancheInvestor': ('[u8; 16]', 'u64'), 'PODReadAccess': None}, 'PermissionedCurrencyRole': {'Holder': 'u64', 'Manager': None, 'Issuer': None}}```

---------
### Purged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| scope | `T::Scope` | ```{'Pool': 'u64', 'Currency': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}}```

---------
### Removed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| from | `T::AccountId` | ```AccountId```
| scope | `T::Scope` | ```{'Pool': 'u64', 'Currency': {'Native': None, 'Tranche': ('u64', '[u8; 16]'), None: None, 'AUSD': None, 'ForeignAsset': 'u32', 'Staking': ('BlockRewards',)}}```
| role | `T::Role` | ```{'PoolRole': {'PoolAdmin': None, 'Borrower': None, 'PricingAdmin': None, 'LiquidityAdmin': None, 'InvestorAdmin': None, 'LoanAdmin': None, 'TrancheInvestor': ('[u8; 16]', 'u64'), 'PODReadAccess': None}, 'PermissionedCurrencyRole': {'Holder': 'u64', 'Manager': None, 'Issuer': None}}```

---------
## Storage functions

---------
### Permission

#### Python
```python
result = substrate.query(
    'Permissions', 'Permission', [
    'AccountId',
    {
        'Currency': {
            'AUSD': None,
            'ForeignAsset': 'u32',
            'Native': None,
            'Staking': (
                'BlockRewards',
            ),
            'Tranche': (
                'u64',
                '[u8; 16]',
            ),
            None: None,
        },
        'Pool': 'u64',
    },
]
)
```

#### Return value
```python
{
    'currency_admin': {'bits': 'u32'},
    'permissioned_asset_holder': {'info': (None, {'permissioned_till': 'u64'})},
    'pool_admin': {'bits': 'u32'},
    'tranche_investor': {
        'info': [{'permissioned_till': 'u64', 'tranche_id': '[u8; 16]'}],
    },
}
```
---------
### PermissionCount

#### Python
```python
result = substrate.query(
    'Permissions', 'PermissionCount', [
    {
        'Currency': {
            'Native': None,
            'Tranche': (
                'u64',
                '[u8; 16]',
            ),
            None: None,
            'AUSD': None,
            'ForeignAsset': 'u32',
            'Staking': (
                'BlockRewards',
            ),
        },
        'Pool': 'u64',
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
### MaxRolesPerScope
#### Value
```python
10000
```
#### Python
```python
constant = substrate.get_constant('Permissions', 'MaxRolesPerScope')
```
---------
## Errors

---------
### NoEditor

---------
### NoRoles

---------
### RoleAlreadyGiven

---------
### RoleNotGiven

---------
### TooManyRoles

---------
### WrongParameters

---------