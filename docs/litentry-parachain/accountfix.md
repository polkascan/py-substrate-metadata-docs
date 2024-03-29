
# AccountFix

---------
## Calls

---------
### set_balance
add some balance of an existing account
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdLookupOf<T>` | 
| add_free | `BalanceOf<T>` | 
| add_reserved | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'AccountFix', 'set_balance', {
    'add_free': 'u128',
    'add_reserved': 'u128',
    'who': {
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
### upgrade_accounts
Change the admin account
similar to sudo.set_key, the old account will be supplied in event
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'AccountFix', 'upgrade_accounts', {'who': ['AccountId']}
)
```

---------