
# Subaccounts

---------
## Calls

---------
### transfer
Transfers `amount` of `currency` from subaccount to &\#x27;destination&\#x27; account. If `subacc_type`
is `Bailsman` and it&\#x27;s total collateral value becomes less than minimal bailsman
collateral value - subaccount will be unregistered as bailsman.
Destination should not be subaccount.
#### Attributes
| Name | Type |
| -------- | -------- | 
| subacc_type | `SubAccType` | 
| destination | `T::AccountId` | 
| asset | `Asset` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Subaccounts', 'transfer', {
    'amount': 'u128',
    'asset': 'u64',
    'destination': 'AccountId',
    'subacc_type': (
        'Bailsman',
        'Trader',
        'Borrower',
    ),
}
)
```

---------
### transfer_from_subaccount
Transfers `amount` of `currency` from subaccount to main account. If `subacc_type`
is `Bailsman` and it&\#x27;s total collateral value becomes less than minimal bailsman
collateral value - subaccount will be unregistered as bailsman.
#### Attributes
| Name | Type |
| -------- | -------- | 
| subacc_type | `SubAccType` | 
| asset | `Asset` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Subaccounts', 'transfer_from_subaccount', {
    'amount': 'u128',
    'asset': 'u64',
    'subacc_type': (
        'Bailsman',
        'Trader',
        'Borrower',
    ),
}
)
```

---------
### transfer_to_subaccount
Transfers `value` amount of `currency` from main account to `subacc_type` subaccount
#### Attributes
| Name | Type |
| -------- | -------- | 
| subacc_type | `SubAccType` | 
| asset | `Asset` | 
| value | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Subaccounts', 'transfer_to_subaccount', {
    'asset': 'u64',
    'subacc_type': (
        'Bailsman',
        'Trader',
        'Borrower',
    ),
    'value': 'u128',
}
)
```

---------
## Events

---------
### RegisterBailsman
Register bailsman subaccount as bailsman
- first element is subaccount owner&\#x27;s `AccountId`
- second element is subaccount of type Bailsman
\[owner, subaccount\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```

---------
### SubaccountCreated
New subaccount created
- first element is subaccount owner&\#x27;s `AccountId`
- second element is `AccountId` of created subaccount
- last element is a type of created subaccount
\[owner, subaccount, type\]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `T::AccountId` | ```AccountId```
| None | `SubAccType` | ```('Bailsman', 'Trader', 'Borrower')```

---------
## Storage functions

---------
### OwnerAccount
 Pallet storage - a map storing a tuple  (`AccountId`, `SubAccType`)
 for each existing subaccount. First element in stored tuple is
 `AccountId` of main user account, owning the subaccount and second
 is `SubAccType` of key subaccount

#### Python
```python
result = substrate.query(
    'Subaccounts', 'OwnerAccount', ['AccountId']
)
```

#### Return value
```python
('AccountId', ('Bailsman', 'Trader', 'Borrower'))
```
---------
### Subaccount
 Pallet storage - double map storing subaccounts as `AccountId` where
 user&#x27;s main `AccountId` and `SubAccType` used as keys

#### Python
```python
result = substrate.query(
    'Subaccounts', 'Subaccount', [
    'AccountId',
    ('Bailsman', 'Trader', 'Borrower'),
]
)
```

#### Return value
```python
'AccountId'
```
---------
## Errors

---------
### AccountInWhiteList
Cannot create a subaccount: account in whitelist

---------
### AccountIsNotMaster
Account is not a master account. Transfers to external subaccounts prohibited.

---------
### AlreadyHasSubaccount
Cannot create a subaccount: user already has subaccount of
this type

---------
### Debt
Debt not allowed to be creating in this operation

---------
### EntropyError
Entropy is not allow to generate subaccount. Try one more time.

---------
### NoSubaccountOfThisType
Cannot delete subaccount or transfer from it: no subaccount of this type

---------
### TransfersAreDisabled
Transfers are disabled

---------