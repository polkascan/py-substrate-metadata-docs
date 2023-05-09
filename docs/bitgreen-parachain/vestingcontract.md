
# VestingContract

---------
## Calls

---------
### add_new_contract
Add a new contract on chain
A contract is considered valid if the following conditions are satisfied
- the recipient does not already have a contract
- The expiry block is in the future
- If the pallet has balance to payout this contract
#### Attributes
| Name | Type |
| -------- | -------- | 
| recipient | `T::AccountId` | 
| expiry | `T::BlockNumber` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'VestingContract', 'add_new_contract', {
    'amount': 'u128',
    'expiry': 'u32',
    'recipient': 'AccountId',
}
)
```

---------
### bulk_add_new_contracts
Same as add_contract but take multiple accounts as input
If any of the contracts fail to be processed all inputs are rejected
#### Attributes
| Name | Type |
| -------- | -------- | 
| recipients | `BulkContractInputs<T>` | 

#### Python
```python
call = substrate.compose_call(
    'VestingContract', 'bulk_add_new_contracts', {
    'recipients': [
        {
            'amount': 'u128',
            'expiry': 'u32',
            'recipient': 'AccountId',
        },
    ],
}
)
```

---------
### bulk_remove_contracts
Same as remove_contract but take multiple accounts as input
If any of the contracts fail to be processed all inputs are rejected
#### Attributes
| Name | Type |
| -------- | -------- | 
| recipients | `BulkContractRemove<T>` | 

#### Python
```python
call = substrate.compose_call(
    'VestingContract', 'bulk_remove_contracts', {'recipients': ['AccountId']}
)
```

---------
### force_add_authorized_account
Add a new account to the list of authorised Accounts
The caller must be from a permitted origin
#### Attributes
| Name | Type |
| -------- | -------- | 
| account_id | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'VestingContract', 'force_add_authorized_account', {'account_id': 'AccountId'}
)
```

---------
### force_remove_authorized_account
Remove an account from the list of authorised accounts
#### Attributes
| Name | Type |
| -------- | -------- | 
| account_id | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'VestingContract', 'force_remove_authorized_account', {'account_id': 'AccountId'}
)
```

---------
### force_withdraw_vested
Call withdraw_vested for any account with a valid contract
#### Attributes
| Name | Type |
| -------- | -------- | 
| recipient | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'VestingContract', 'force_withdraw_vested', {'recipient': 'AccountId'}
)
```

---------
### remove_contract
Remove a contract from storage
#### Attributes
| Name | Type |
| -------- | -------- | 
| recipient | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'VestingContract', 'remove_contract', {'recipient': 'AccountId'}
)
```

---------
### withdraw_vested
Withdraw amount from a vested (expired) contract

WARNING: Insecure unless the chain includes `PrevalidateVestingWithdraw` as a
`SignedExtension`.

Unsigned Validation:
A call to withdraw vested is deemed valid if the sender has an existing contract
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'VestingContract', 'withdraw_vested', {}
)
```

---------
## Events

---------
### AuthorizedAccountAdded
A new authorized account has been added to storage
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```

---------
### AuthorizedAccountRemoved
An authorized account has been removed from storage
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```

---------
### ContractAdded
A new contract has been added to storage
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| recipient | `T::AccountId` | ```AccountId```
| expiry | `T::BlockNumber` | ```u32```
| amount | `BalanceOf<T>` | ```u128```

---------
### ContractRemoved
Contract removed from storage
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| recipient | `T::AccountId` | ```AccountId```

---------
### ContractWithdrawn
An existing contract has been completed/withdrawn
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| recipient | `T::AccountId` | ```AccountId```
| expiry | `T::BlockNumber` | ```u32```
| amount | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### AuthorizedAccounts

#### Python
```python
result = substrate.query(
    'VestingContract', 'AuthorizedAccounts', []
)
```

#### Return value
```python
['AccountId']
```
---------
### VestingBalance

#### Python
```python
result = substrate.query(
    'VestingContract', 'VestingBalance', []
)
```

#### Return value
```python
'u128'
```
---------
### VestingContracts

#### Python
```python
result = substrate.query(
    'VestingContract', 'VestingContracts', ['AccountId']
)
```

#### Return value
```python
{'amount': 'u128', 'expiry': 'u32'}
```
---------
## Constants

---------
### PalletId
 The Vesting Contract pallet id
#### Value
```python
'0x626974672f766370'
```
#### Python
```python
constant = substrate.get_constant('VestingContract', 'PalletId')
```
---------
## Errors

---------
### AuthorizedAccountAlreadyExists
Authorized account already exists

---------
### ContractAlreadyExists
Contract already exists, remove old contract before adding new

---------
### ContractNotExpired
The contract has not expired

---------
### ContractNotFound
Contract not found in storage

---------
### ExpiryInThePast
The contract expiry has already passed

---------
### NotAuthorised
Not authorized to perform this operation

---------
### PalletOutOfFunds
The pallet account does not have funds to pay contract

---------
### StorageOverflow
Errors should have helpful documentation associated with them.

---------
### TooManyAuthorizedAccounts
Too many authorized accounts

---------