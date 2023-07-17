
# Deposits

---------
## Events

---------
### DepositIgnored
A deposit has been ignored due to u32::MAX being passed.
#### Attributes
No attributes

---------
### DepositReturned
A deposit has been reinstated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::DepositId` | ```u64```
| None | `BalanceOf<T>` | ```u128```

---------
### DepositSlashed
A deposit has been slashed and sent to the slash account.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::DepositId` | ```u64```
| None | `BalanceOf<T>` | ```u128```

---------
### DepositTaken
A deposit has been taken.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::DepositId` | ```u64```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### CurrentDeposits
 A list of current deposits and the amount taken for the deposit.

#### Python
```python
result = substrate.query(
    'Deposits', 'CurrentDeposits', ['u64']
)
```

#### Return value
```python
{
    'amount': 'u128',
    'currency_id': {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'KAR': None,
        'KSM': None,
        'MGX': None,
        'Native': None,
    },
    'who': 'AccountId',
}
```
---------
### TicketId
 A counter for generating DepositIds;

#### Python
```python
result = substrate.query(
    'Deposits', 'TicketId', []
)
```

#### Return value
```python
'u64'
```
---------
## Errors

---------
### DepositDoesntExist
The deposit doesnt exist.

---------
### NotEnoughFundsForStorageDeposit
You need more funds to cover the storage deposit.

---------
### UnsupportedCurrencyType
The currency type is not supported.

---------
### UnsupportedStorageType
The storage type is not supported.

---------