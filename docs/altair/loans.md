
# Loans

---------
## Calls

---------
### add_write_off_group
Appends a new write off group to the Pool

`group.penalty_interest_rate_per_year` is a yearly
rate, in the same format as used for pricing
loans.

Since written off loans keep written off group index,
we only allow adding new write off groups.
Overdue days doesn&\#x27;t need to be in the sorted order.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolIdOf<T>` | 
| group | `WriteOffGroupInput<T::Rate>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'add_write_off_group', {
    'group': {
        'overdue_days': 'u64',
        'penalty_interest_rate_per_year': 'u128',
        'percentage': 'u128',
    },
    'pool_id': 'u64',
}
)
```

---------
### admin_write_off
Write off an loan from admin origin

`admin_write_off_loan` will write off a loan with write off group associated with index passed.
Loan is accrued, NAV is update accordingly, and updates the Loan with new write off index.
AdminOrigin can write off a healthy loan as well.
Once admin writes off a loan, permission less `write_off_loan` wont be allowed after.
Admin can write off loan with any index potentially going up the index or down.

`penalty_interest_rate_per_year` is specified in the same format as used for pricing loans.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolIdOf<T>` | 
| loan_id | `T::LoanId` | 
| percentage | `T::Rate` | 
| penalty_interest_rate_per_year | `T::Rate` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'admin_write_off', {
    'loan_id': 'u128',
    'penalty_interest_rate_per_year': 'u128',
    'percentage': 'u128',
    'pool_id': 'u64',
}
)
```

---------
### borrow
Transfers borrow amount to the loan owner.

LoanStatus must be active.
Borrow amount should not exceed max_borrow_amount set for the loan.
Loan should still be healthy. If loan type supports maturity, then maturity date should not have passed.
Loan should not be written off.
Rate accumulation will start after the first borrow
Loan is accrued upto the current time.
Pool NAV is updated to reflect new present value of the loan.
Amount of tokens of an Asset will be transferred from pool reserve to loan owner.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolIdOf<T>` | 
| loan_id | `T::LoanId` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'borrow', {
    'amount': 'u128',
    'loan_id': 'u128',
    'pool_id': 'u64',
}
)
```

---------
### close
Closes a given loan

Loan can be closed on two scenarios
1. When the outstanding is fully paid off
2. When loan is written off 100%
Loan status is moved to Closed
Collateral NFT is transferred back to the loan owner.
Loan NFT is transferred back to LoanAccount.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolIdOf<T>` | 
| loan_id | `T::LoanId` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'close', {'loan_id': 'u128', 'pool_id': 'u64'}
)
```

---------
### create
Create a new loan against the collateral provided

`create_loan` transfers the collateral nft from the owner to self and issues a new loan nft to the owner
caller *must* be the owner of the collateral.
LoanStatus is set to created and needs to be priced by an admin origin to start borrowing.
Loan cannot be closed until the status has changed to Priced.
Collateral NFT class cannot be another Loan NFT class. Means, you cannot collateralise a Loan.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolIdOf<T>` | 
| collateral | `AssetOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'create', {'collateral': ('u64', 'u128'), 'pool_id': 'u64'}
)
```

---------
### initialise_pool
Initialises a new pool

`initialise_pool` checks if pool is not initialised yet and then adds the loan nft class id.
All the Loan NFTs will be created into this Class. So loan account *should* be able to mint new NFTs into the class.
Adding LoanAccount as admin to the NFT class will be enough to mint new NFTs.
The origin must be an Admin origin
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolIdOf<T>` | 
| loan_nft_class_id | `T::ClassId` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'initialise_pool', {
    'loan_nft_class_id': 'u64',
    'pool_id': 'u64',
}
)
```

---------
### price
Set pricing for the loan with loan specific details like Rate, Loan type

LoanStatus must be in Created or Active state.
Once activated, loan owner can start loan related functions like Borrow, Repay, Close
`interset_rate_per_year` is the anual interest rate, in the form 0.XXXX,
    such that an APR of XX.YY% becomes 0.XXYY. Valid values are 0.0001
    through 0.9999, with no more than four significant figures.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolIdOf<T>` | 
| loan_id | `T::LoanId` | 
| interest_rate_per_year | `T::Rate` | 
| loan_type | `LoanType<T::Rate, T::Balance>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'price', {
    'interest_rate_per_year': 'u128',
    'loan_id': 'u128',
    'loan_type': {
        'BulletLoan': {
            'advance_rate': 'u128',
            'discount_rate': 'u128',
            'loss_given_default': 'u128',
            'maturity_date': 'u64',
            'probability_of_default': 'u128',
            'value': 'u128',
        },
        'CreditLine': {
            'advance_rate': 'u128',
            'value': 'u128',
        },
        'CreditLineWithMaturity': {
            'advance_rate': 'u128',
            'discount_rate': 'u128',
            'loss_given_default': 'u128',
            'maturity_date': 'u64',
            'probability_of_default': 'u128',
            'value': 'u128',
        },
    },
    'pool_id': 'u64',
}
)
```

---------
### repay
Transfers amount borrowed to the pool reserve.

LoanStatus must be Active.
Loan is accrued before transferring the amount to reserve.
If the repaying amount is more than current debt, only current debt is transferred.
Amount of token will be transferred from owner to Pool reserve.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolIdOf<T>` | 
| loan_id | `T::LoanId` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'repay', {
    'amount': 'u128',
    'loan_id': 'u128',
    'pool_id': 'u64',
}
)
```

---------
### update_nav
Updates the NAV for a given pool

Iterate through each loan and calculate the present value of each active loan.
The loan is accrued and updated.

Weight for the update nav is not straightforward since there could n loans in a pool
So instead, we calculate weight for one loan. We assume a maximum of 200 loans and deposit that weight
Once the NAV calculation is done, we check how many loans we have updated and return the actual weight so that
transaction payment can return the deposit.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'update_nav', {'pool_id': 'u64'}
)
```

---------
### write_off
Write off an unhealthy loan

`write_off_loan` will find the best write off group available based on the overdue days since maturity.
Loan is accrued, NAV is update accordingly, and updates the Loan with new write off index.
Cannot update a loan that was written off by admin.
Cannot write off a healthy loan or loan type that do not have maturity date.


Weight is calculated for one group. Since there is no extra read or writes for groups more than 1,
We need to ensure we are charging the reads and write only once but the actual compute to be equal to number of groups processed
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `PoolIdOf<T>` | 
| loan_id | `T::LoanId` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'write_off', {'loan_id': 'u128', 'pool_id': 'u64'}
)
```

---------
## Events

---------
### Borrowed
An amount was borrowed for a loan.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `PoolIdOf<T>` | ```u64```
| loan_id | `T::LoanId` | ```u128```
| amount | `T::Balance` | ```u128```

---------
### Closed
A loan was closed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `PoolIdOf<T>` | ```u64```
| loan_id | `T::LoanId` | ```u128```
| collateral | `AssetOf<T>` | ```('u64', 'u128')```

---------
### Created
A loan was created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `PoolIdOf<T>` | ```u64```
| loan_id | `T::LoanId` | ```u128```
| collateral | `AssetOf<T>` | ```('u64', 'u128')```

---------
### NAVUpdated
The NAV for a pool was updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `PoolIdOf<T>` | ```u64```
| nav | `T::Balance` | ```u128```
| update_type | `NAVUpdateType` | ```('Exact', 'Inexact')```

---------
### PoolInitialised
A pool was initialised.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `PoolIdOf<T>` | ```u64```

---------
### Priced
A loan was priced.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `PoolIdOf<T>` | ```u64```
| loan_id | `T::LoanId` | ```u128```
| interest_rate_per_sec | `T::Rate` | ```u128```
| loan_type | `LoanType<T::Rate, T::Balance>` | ```{'BulletLoan': {'advance_rate': 'u128', 'probability_of_default': 'u128', 'loss_given_default': 'u128', 'value': 'u128', 'discount_rate': 'u128', 'maturity_date': 'u64'}, 'CreditLine': {'advance_rate': 'u128', 'value': 'u128'}, 'CreditLineWithMaturity': {'advance_rate': 'u128', 'probability_of_default': 'u128', 'loss_given_default': 'u128', 'value': 'u128', 'discount_rate': 'u128', 'maturity_date': 'u64'}}```

---------
### Repaid
An amount was repaid for a loan.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `PoolIdOf<T>` | ```u64```
| loan_id | `T::LoanId` | ```u128```
| amount | `T::Balance` | ```u128```

---------
### WriteOffGroupAdded
A write-off group was added to a pool.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `PoolIdOf<T>` | ```u64```
| write_off_group_index | `u32` | ```u32```

---------
### WrittenOff
A loan was written off. [pool, loan, percentage, penalty_interest_rate_per_sec, write_off_group_index]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `PoolIdOf<T>` | ```u64```
| loan_id | `T::LoanId` | ```u128```
| percentage | `T::Rate` | ```u128```
| penalty_interest_rate_per_sec | `T::Rate` | ```u128```
| write_off_group_index | `Option<u32>` | ```(None, 'u32')```

---------
## Storage functions

---------
### ActiveLoans

#### Python
```python
result = substrate.query(
    'Loans', 'ActiveLoans', ['u64']
)
```

#### Return value
```python
[
    {
        'interest_rate_per_sec': 'u128',
        'last_updated': 'u64',
        'loan_id': 'u128',
        'loan_type': {
            'BulletLoan': {
                'advance_rate': 'u128',
                'discount_rate': 'u128',
                'loss_given_default': 'u128',
                'maturity_date': 'u64',
                'probability_of_default': 'u128',
                'value': 'u128',
            },
            'CreditLine': {'advance_rate': 'u128', 'value': 'u128'},
            'CreditLineWithMaturity': {
                'advance_rate': 'u128',
                'discount_rate': 'u128',
                'loss_given_default': 'u128',
                'maturity_date': 'u64',
                'probability_of_default': 'u128',
                'value': 'u128',
            },
        },
        'normalized_debt': 'u128',
        'origination_date': (None, 'u64'),
        'total_borrowed': 'u128',
        'total_repaid': 'u128',
        'write_off_status': {
            'None': None,
            'WrittenOff': {'write_off_index': 'u32'},
            'WrittenOffByAdmin': {
                'penalty_interest_rate_per_sec': 'u128',
                'percentage': 'u128',
            },
        },
    },
]
```
---------
### ClosedLoans

#### Python
```python
result = substrate.query(
    'Loans', 'ClosedLoans', ['u64', 'u128']
)
```

#### Return value
```python
{
    'interest_rate_per_sec': 'u128',
    'last_updated': 'u64',
    'loan_id': 'u128',
    'loan_type': {
        'BulletLoan': {
            'advance_rate': 'u128',
            'discount_rate': 'u128',
            'loss_given_default': 'u128',
            'maturity_date': 'u64',
            'probability_of_default': 'u128',
            'value': 'u128',
        },
        'CreditLine': {'advance_rate': 'u128', 'value': 'u128'},
        'CreditLineWithMaturity': {
            'advance_rate': 'u128',
            'discount_rate': 'u128',
            'loss_given_default': 'u128',
            'maturity_date': 'u64',
            'probability_of_default': 'u128',
            'value': 'u128',
        },
    },
    'normalized_debt': 'u128',
    'origination_date': (None, 'u64'),
    'total_borrowed': 'u128',
    'total_repaid': 'u128',
    'write_off_status': {
        'None': None,
        'WrittenOff': {'write_off_index': 'u32'},
        'WrittenOffByAdmin': {
            'penalty_interest_rate_per_sec': 'u128',
            'percentage': 'u128',
        },
    },
}
```
---------
### Loan
 Stores the loan info for given pool and loan id

#### Python
```python
result = substrate.query(
    'Loans', 'Loan', ['u64', 'u128']
)
```

#### Return value
```python
{
    'collateral': ('u64', 'u128'),
    'status': {'Active': None, 'Closed': {'closed_at': 'u32'}, 'Created': None},
}
```
---------
### LoanNftClassToPool
 Stores the poolID against ClassId as a key
 this is a reverse lookup used to ensure the collateral itself is not a Loan Nft

#### Python
```python
result = substrate.query(
    'Loans', 'LoanNftClassToPool', ['u64']
)
```

#### Return value
```python
'u64'
```
---------
### NextLoanId
 Stores the next loan tokenID to be created

#### Python
```python
result = substrate.query(
    'Loans', 'NextLoanId', ['u64']
)
```

#### Return value
```python
'u128'
```
---------
### PoolNAV
 Stores the pool nav against poolId

#### Python
```python
result = substrate.query(
    'Loans', 'PoolNAV', ['u64']
)
```

#### Return value
```python
{'last_updated': 'u64', 'latest': 'u128'}
```
---------
### PoolToLoanNftClass
 Stores the loan nft class ID against a given pool

#### Python
```python
result = substrate.query(
    'Loans', 'PoolToLoanNftClass', ['u64']
)
```

#### Return value
```python
'u64'
```
---------
### PoolWriteOffGroups
 Stores the pool associated with the its write off groups

#### Python
```python
result = substrate.query(
    'Loans', 'PoolWriteOffGroups', ['u64']
)
```

#### Return value
```python
[
    {
        'overdue_days': 'u64',
        'penalty_interest_rate_per_sec': 'u128',
        'percentage': 'u128',
    },
]
```
---------
## Constants

---------
### LoansPalletId
 PalletID of this loan module
#### Value
```python
'0x726f632f6c6f616e'
```
#### Python
```python
constant = substrate.get_constant('Loans', 'LoansPalletId')
```
---------
### MaxActiveLoansPerPool
 Max number of active loans per pool.
#### Value
```python
300
```
#### Python
```python
constant = substrate.get_constant('Loans', 'MaxActiveLoansPerPool')
```
---------
### MaxWriteOffGroups
 Max number of write-off groups per pool.
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Loans', 'MaxWriteOffGroups')
```
---------
## Errors

---------
### InvalidWriteOffGroup
Emits when new write off group is invalid

---------
### InvalidWriteOffGroupIndex
Emits when there is no valid write off groups associated with given index

---------
### LoanAccrueFailed
Emits when loan accrue calculation failed

---------
### LoanHealthy
Emits when trying to write off of a healthy loan

---------
### LoanIsClosed
Emits when tries to price a closed loan

---------
### LoanMaturityDatePassed
Emits when maturity has passed and borrower tried to borrow more

---------
### LoanNotActive
Emits when operation is done on an inactive loan

---------
### LoanNotRepaid
Emits when loan amount not repaid but trying to close loan

---------
### LoanPresentValueFailed
Emits when loan present value calculation failed

---------
### LoanTypeInvalid
Emits when loan type given is not valid

---------
### LoanValueInvalid
Emits when a loan data value is invalid

---------
### MaxBorrowAmountExceeded
Emits when the borrowed amount is more than max_borrow_amount

---------
### MissingLoan
Emits when loan doesn&\#x27;t exist.

---------
### NFTOwnerNotFound
Emits when the NFT owner is not found

---------
### NftTokenNonceOverflowed
Emits when the nft token nonce is overflowed

---------
### NoValidWriteOffGroup
Emits when there is no valid write off group available for unhealthy loan

---------
### NormalizedDebtOverflow
Emits when principal debt calculation failed due to overflow

---------
### NotAValidAsset
Emits when the nft is not an acceptable asset

---------
### NotAssetOwner
Emits when nft owner doesn&\#x27;t match the expected owner

---------
### PoolAlreadyInitialised
Emits when pool is already initialised

---------
### PoolMissing
Emits when pool doesn&\#x27;t exist

---------
### PoolNotInitialised
Emits when pool is not initialised

---------
### RepayTooEarly
Emits when borrow and repay happens in the same block

---------
### TooManyActiveLoans
Emits when the max number of active loans was reached

---------
### TooManyWriteOffGroups
Emits when the max number of write off groups was reached

---------
### ValueOverflow
Emits when an operation lead to the number overflow

---------
### WrittenOffByAdmin
Emits when trying to write off loan that was written off by admin already

---------