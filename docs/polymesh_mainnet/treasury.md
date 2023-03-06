
# Treasury

---------
## Calls

---------
### disbursement
It transfers balances from treasury to each of beneficiaries and the specific amount
for each of them.

\# Error
* `BadOrigin`: Only root can execute transaction.
* `InsufficientBalance`: If treasury balances is not enough to cover all beneficiaries.
* `InvalidIdentity`: If one of the beneficiaries has an invalid identity.
#### Attributes
| Name | Type |
| -------- | -------- | 
| beneficiaries | `Vec<Beneficiary<BalanceOf<T>>>` | 

#### Python
```python
call = substrate.compose_call(
    'Treasury', 'disbursement', {
    'beneficiaries': [
        {
            'amount': 'u128',
            'id': '[u8; 32]',
        },
    ],
}
)
```

---------
### reimbursement
It transfers the specific `amount` from `origin` account into treasury.

Only accounts which are associated to an identity can make a donation to treasury.
#### Attributes
| Name | Type |
| -------- | -------- | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Treasury', 'reimbursement', {'amount': 'u128'}
)
```

---------
## Events

---------
### TreasuryDisbursement
Disbursement to a target Identity.

(treasury identity, target identity, target primary key, amount)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### TreasuryDisbursementFailed
Disbursement to a target Identity failed.

(treasury identity, target identity, target primary key, amount)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `Balance` | ```u128```

---------
### TreasuryReimbursement
Treasury reimbursement.

(source identity, amount)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Balance` | ```u128```

---------
## Errors

---------
### InsufficientBalance
Proposer&\#x27;s balance is too low.

---------
### InvalidIdentity
Invalid identity for disbursement.

---------