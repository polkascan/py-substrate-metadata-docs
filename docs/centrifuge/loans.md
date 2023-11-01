
# Loans

---------
## Calls

---------
### admin_write_off
Writes off a loan from admin origin.

Forces a writing off of a loan if the `percentage` and `penalty`
parameters respecting the policy values as the maximum.
This action can write down/up the current write off status of the
loan. If there is no active policy, an admin write off action can
write up the write off status. But if there is a policy applied, the
admin can only write up until the policy. Write down more than the
policy is always allowed. The portfolio valuation of the pool is
updated to reflect the new present value of the loan.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| loan_id | `T::LoanId` | 
| percentage | `T::Rate` | 
| penalty | `T::Rate` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'admin_write_off', {
    'loan_id': 'u64',
    'penalty': 'u128',
    'percentage': 'u128',
    'pool_id': 'u64',
}
)
```

---------
### apply_loan_mutation
Apply a proposed change identified by a change id.
It will only perform the change if the requirements for it
are fulfilled.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| change_id | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'apply_loan_mutation', {
    'change_id': '[u8; 32]',
    'pool_id': 'u64',
}
)
```

---------
### apply_transfer_debt
Transfer debt from one loan to another loan,
repaying from the first loan and borrowing the same amount from the
second loan. `from_loan_id` is the loan used to repay.
`to_loan_id` is the loan used to borrow.
The repaid and borrow amount must match.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| change_id | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'apply_transfer_debt', {
    'change_id': '[u8; 32]',
    'pool_id': 'u64',
}
)
```

---------
### apply_write_off_policy
Apply a proposed change identified by a change id.
It will only perform the change if the requirements for it
are fulfilled.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| change_id | `T::Hash` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'apply_write_off_policy', {
    'change_id': '[u8; 32]',
    'pool_id': 'u64',
}
)
```

---------
### borrow
Transfers borrow amount to the borrower.

The origin must be the borrower of the loan.
The borrow action should fulfill the borrow restrictions configured
at [`types::LoanRestrictions`]. The `amount` will be transferred
from pool reserve to borrower. The portfolio valuation of the pool
is updated to reflect the new present value of the loan.
Rate accumulation will start after the first borrow.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| loan_id | `T::LoanId` | 
| amount | `PrincipalInput<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'borrow', {
    'amount': {
        'External': {
            'quantity': 'u128',
            'settlement_price': 'u128',
        },
        'Internal': 'u128',
    },
    'loan_id': 'u64',
    'pool_id': 'u64',
}
)
```

---------
### close
Closes a given loan

A loan only can be closed if it&\#x27;s fully repaid by the loan borrower.
Closing a loan gives back the collateral used for the loan to the
borrower .
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| loan_id | `T::LoanId` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'close', {'loan_id': 'u64', 'pool_id': 'u64'}
)
```

---------
### create
Creates a new loan against the collateral provided

The origin must be the owner of the collateral.
This collateral will be transferred to the existing pool.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| info | `LoanInfo<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'create', {
    'info': {
        'collateral': ('u64', 'u128'),
        'interest_rate': {
            'Fixed': {
                'compounding': (
                    'Secondly',
                ),
                'rate_per_year': 'u128',
            },
        },
        'pricing': {
            'External': {
                'max_borrow_amount': {
                    'NoLimit': None,
                    'Quantity': 'u128',
                },
                'max_price_variation': 'u128',
                'notional': 'u128',
                'price_id': {
                    'Isin': '[u8; 12]',
                },
            },
            'Internal': {
                'collateral_value': 'u128',
                'max_borrow_amount': {
                    'UpToOutstandingDebt': {
                        'advance_rate': 'u128',
                    },
                    'UpToTotalBorrowed': {
                        'advance_rate': 'u128',
                    },
                },
                'valuation_method': {
                    'DiscountedCashFlow': {
                        'discount_rate': {
                            'Fixed': 'InnerStruct',
                        },
                        'loss_given_default': 'u128',
                        'probability_of_default': 'u128',
                    },
                    'OutstandingDebt': None,
                },
            },
        },
        'restrictions': {
            'borrows': (
                'NotWrittenOff',
                'FullOnce',
                'OraclePriceRequired',
            ),
            'repayments': (
                'None',
                'Full',
            ),
        },
        'schedule': {
            'interest_payments': (
                'None',
            ),
            'maturity': {
                'Fixed': {
                    'date': 'u64',
                    'extension': 'u64',
                },
            },
            'pay_down_schedule': (
                'None',
            ),
        },
    },
    'pool_id': 'u64',
}
)
```

---------
### propose_loan_mutation
Propose a change.
The change is not performed until you call
[`Pallet::apply_loan_mutation()`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| loan_id | `T::LoanId` | 
| mutation | `LoanMutation<T::Rate>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'propose_loan_mutation', {
    'loan_id': 'u64',
    'mutation': {
        'InterestPayments': ('None', ),
        'InterestRate': {
            'Fixed': {
                'compounding': (
                    'Secondly',
                ),
                'rate_per_year': 'u128',
            },
        },
        'Internal': {
            'DiscountRate': {
                'Fixed': {
                    'compounding': (
                        'Secondly',
                    ),
                    'rate_per_year': 'u128',
                },
            },
            'LossGivenDefault': 'u128',
            'ProbabilityOfDefault': 'u128',
            'ValuationMethod': {
                'DiscountedCashFlow': {
                    'discount_rate': {
                        'Fixed': {
                            'compounding': 'scale_info::248',
                            'rate_per_year': 'u128',
                        },
                    },
                    'loss_given_default': 'u128',
                    'probability_of_default': 'u128',
                },
                'OutstandingDebt': None,
            },
        },
        'Maturity': {
            'Fixed': {
                'date': 'u64',
                'extension': 'u64',
            },
        },
        'MaturityExtension': 'u64',
        'PayDownSchedule': ('None', ),
    },
    'pool_id': 'u64',
}
)
```

---------
### propose_transfer_debt
Transfer debt from one loan to another loan,
repaying from the first loan and borrowing the same amount from the
second loan. `from_loan_id` is the loan used to repay.
`to_loan_id` is the loan used to borrow.
The repaid and borrow amount must match.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| from_loan_id | `T::LoanId` | 
| to_loan_id | `T::LoanId` | 
| repaid_amount | `RepaidInput<T>` | 
| borrow_amount | `PrincipalInput<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'propose_transfer_debt', {
    'borrow_amount': {
        'External': {
            'quantity': 'u128',
            'settlement_price': 'u128',
        },
        'Internal': 'u128',
    },
    'from_loan_id': 'u64',
    'pool_id': 'u64',
    'repaid_amount': {
        'interest': 'u128',
        'principal': {
            'External': {
                'quantity': 'u128',
                'settlement_price': 'u128',
            },
            'Internal': 'u128',
        },
        'unscheduled': 'u128',
    },
    'to_loan_id': 'u64',
}
)
```

---------
### propose_write_off_policy
Updates the write off policy with write off rules.

The write off policy is used to automatically set a write off
minimum value to the loan.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| policy | `BoundedVec<WriteOffRule<T::Rate>, T::MaxWriteOffPolicySize>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'propose_write_off_policy', {
    'policy': [
        {
            'status': {
                'penalty': 'u128',
                'percentage': 'u128',
            },
            'triggers': 'scale_info::259',
        },
    ],
    'pool_id': 'u64',
}
)
```

---------
### repay
Transfers amount borrowed to the pool reserve.

The origin must be the borrower of the loan.
The repay action should fulfill the repay restrictions
configured at [`types::RepayRestrictions`].
If the repaying `amount` is more than current debt, only current
debt is transferred. This does not apply to `unscheduled_amount`,
which can be used to repay more than the outstanding debt.
The portfolio  valuation of the pool is updated to reflect the new
present value of the loan.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| loan_id | `T::LoanId` | 
| amount | `RepaidInput<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'repay', {
    'amount': {
        'interest': 'u128',
        'principal': {
            'External': {
                'quantity': 'u128',
                'settlement_price': 'u128',
            },
            'Internal': 'u128',
        },
        'unscheduled': 'u128',
    },
    'loan_id': 'u64',
    'pool_id': 'u64',
}
)
```

---------
### update_portfolio_valuation
Updates the porfolio valuation for the given pool
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'update_portfolio_valuation', {'pool_id': 'u64'}
)
```

---------
### write_off
Writes off an overdue loan.

This action will write off based on the configured write off policy.
The write off action will only take effect if it writes down more
(percentage or penalty) than the current write off status of the
loan. This action will never writes up. i.e:
- Write off by admin with percentage 0.5 and penalty 0.2
- Time passes and the policy can be applied.
- Write of with a policy that says: percentage 0.3, penaly 0.4
- The loan is written off with the maximum between the policy and
  the current rule: percentage 0.5, penalty 0.4

No special permisions are required to this call.
The portfolio valuation of the pool is updated to reflect the new
present value of the loan.
#### Attributes
| Name | Type |
| -------- | -------- | 
| pool_id | `T::PoolId` | 
| loan_id | `T::LoanId` | 

#### Python
```python
call = substrate.compose_call(
    'Loans', 'write_off', {'loan_id': 'u64', 'pool_id': 'u64'}
)
```

---------
## Events

---------
### Borrowed
An amount was borrowed for a loan
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u64```
| loan_id | `T::LoanId` | ```u64```
| amount | `PrincipalInput<T>` | ```{'Internal': 'u128', 'External': {'quantity': 'u128', 'settlement_price': 'u128'}}```

---------
### Closed
A loan was closed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u64```
| loan_id | `T::LoanId` | ```u64```
| collateral | `AssetOf<T>` | ```('u64', 'u128')```

---------
### Created
A loan was created
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u64```
| loan_id | `T::LoanId` | ```u64```
| loan_info | `LoanInfo<T>` | ```{'schedule': {'maturity': {'Fixed': {'date': 'u64', 'extension': 'u64'}}, 'interest_payments': ('None',), 'pay_down_schedule': ('None',)}, 'collateral': ('u64', 'u128'), 'interest_rate': {'Fixed': {'rate_per_year': 'u128', 'compounding': ('Secondly',)}}, 'pricing': {'Internal': {'collateral_value': 'u128', 'valuation_method': {'DiscountedCashFlow': {'probability_of_default': 'u128', 'loss_given_default': 'u128', 'discount_rate': 'scale_info::247'}, 'OutstandingDebt': None}, 'max_borrow_amount': {'UpToTotalBorrowed': {'advance_rate': 'u128'}, 'UpToOutstandingDebt': {'advance_rate': 'u128'}}}, 'External': {'price_id': {'Isin': '[u8; 12]'}, 'max_borrow_amount': {'NoLimit': None, 'Quantity': 'u128'}, 'notional': 'u128', 'max_price_variation': 'u128'}}, 'restrictions': {'borrows': ('NotWrittenOff', 'FullOnce', 'OraclePriceRequired'), 'repayments': ('None', 'Full')}}```

---------
### DebtTransferred
Debt has been transfered between loans
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u64```
| from_loan_id | `T::LoanId` | ```u64```
| to_loan_id | `T::LoanId` | ```u64```
| amount | `T::Balance` | ```u128```

---------
### Mutated
An active loan was mutated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u64```
| loan_id | `T::LoanId` | ```u64```
| mutation | `LoanMutation<T::Rate>` | ```{'Maturity': {'Fixed': {'date': 'u64', 'extension': 'u64'}}, 'MaturityExtension': 'u64', 'InterestRate': {'Fixed': {'rate_per_year': 'u128', 'compounding': ('Secondly',)}}, 'InterestPayments': ('None',), 'PayDownSchedule': ('None',), 'Internal': {'ValuationMethod': {'DiscountedCashFlow': {'probability_of_default': 'u128', 'loss_given_default': 'u128', 'discount_rate': {'Fixed': 'InnerStruct'}}, 'OutstandingDebt': None}, 'ProbabilityOfDefault': 'u128', 'LossGivenDefault': 'u128', 'DiscountRate': {'Fixed': {'rate_per_year': 'u128', 'compounding': ('Secondly',)}}}}```

---------
### PortfolioValuationUpdated
The portfolio valuation for a pool was updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u64```
| valuation | `T::Balance` | ```u128```
| update_type | `PortfolioValuationUpdateType` | ```('Exact', 'Inexact')```

---------
### Repaid
An amount was repaid for a loan
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u64```
| loan_id | `T::LoanId` | ```u64```
| amount | `RepaidInput<T>` | ```{'principal': {'Internal': 'u128', 'External': {'quantity': 'u128', 'settlement_price': 'u128'}}, 'interest': 'u128', 'unscheduled': 'u128'}```

---------
### WriteOffPolicyUpdated
The write off policy for a pool was updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u64```
| policy | `BoundedVec<WriteOffRule<T::Rate>, T::MaxWriteOffPolicySize>` | ```[{'triggers': 'scale_info::259', 'status': {'percentage': 'u128', 'penalty': 'u128'}}]```

---------
### WrittenOff
A loan was written off
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| pool_id | `T::PoolId` | ```u64```
| loan_id | `T::LoanId` | ```u64```
| status | `WriteOffStatus<T::Rate>` | ```{'percentage': 'u128', 'penalty': 'u128'}```

---------
## Storage functions

---------
### ActiveLoans
 Storage for active loans.
 The indexation of this storage differs from `CreatedLoan` or
 `ClosedLoan` because here we try to minimize the iteration speed over
 all active loans in a pool. `Moment` value along with the `ActiveLoan`
 correspond to the last moment the active loan was used to compute the
 portfolio valuation in an inexact way.

#### Python
```python
result = substrate.query(
    'Loans', 'ActiveLoans', ['u64']
)
```

#### Return value
```python
[
    (
        'u64',
        {
            'borrower': 'AccountId',
            'collateral': ('u64', 'u128'),
            'origination_date': 'u64',
            'pricing': {
                'External': {
                    'info': 'scale_info::295',
                    'interest': 'scale_info::838',
                    'latest_settlement_price': 'u128',
                    'outstanding_quantity': 'u128',
                },
                'Internal': {
                    'info': 'scale_info::293',
                    'interest': 'scale_info::838',
                },
            },
            'repayments_on_schedule_until': 'u64',
            'restrictions': {
                'borrows': (
                    'NotWrittenOff',
                    'FullOnce',
                    'OraclePriceRequired',
                ),
                'repayments': ('None', 'Full'),
            },
            'schedule': {
                'interest_payments': ('None', ),
                'maturity': {'Fixed': 'InnerStruct'},
                'pay_down_schedule': ('None', ),
            },
            'total_borrowed': 'u128',
            'total_repaid': {
                'interest': 'u128',
                'principal': 'u128',
                'unscheduled': 'u128',
            },
            'write_off_percentage': 'u128',
        },
    ),
]
```
---------
### ClosedLoan
 Storage for closed loans.
 No mutations are expected in this storage.
 Loans are stored here for historical purposes.

#### Python
```python
result = substrate.query(
    'Loans', 'ClosedLoan', ['u64', 'u64']
)
```

#### Return value
```python
{
    'closed_at': 'u32',
    'info': {
        'collateral': ('u64', 'u128'),
        'interest_rate': {
            'Fixed': {'compounding': ('Secondly', ), 'rate_per_year': 'u128'},
        },
        'pricing': {
            'External': {
                'max_borrow_amount': {'NoLimit': None, 'Quantity': 'u128'},
                'max_price_variation': 'u128',
                'notional': 'u128',
                'price_id': {'Isin': '[u8; 12]'},
            },
            'Internal': {
                'collateral_value': 'u128',
                'max_borrow_amount': {
                    'UpToOutstandingDebt': 'InnerStruct',
                    'UpToTotalBorrowed': 'InnerStruct',
                },
                'valuation_method': {
                    'DiscountedCashFlow': 'scale_info::253',
                    'OutstandingDebt': None,
                },
            },
        },
        'restrictions': {
            'borrows': ('NotWrittenOff', 'FullOnce', 'OraclePriceRequired'),
            'repayments': ('None', 'Full'),
        },
        'schedule': {
            'interest_payments': ('None', ),
            'maturity': {'Fixed': {'date': 'u64', 'extension': 'u64'}},
            'pay_down_schedule': ('None', ),
        },
    },
    'total_borrowed': 'u128',
    'total_repaid': {
        'interest': 'u128',
        'principal': 'u128',
        'unscheduled': 'u128',
    },
}
```
---------
### CreatedLoan
 Storage for loans that has been created but are not still active.

#### Python
```python
result = substrate.query(
    'Loans', 'CreatedLoan', ['u64', 'u64']
)
```

#### Return value
```python
{
    'borrower': 'AccountId',
    'info': {
        'collateral': ('u64', 'u128'),
        'interest_rate': {
            'Fixed': {'compounding': ('Secondly', ), 'rate_per_year': 'u128'},
        },
        'pricing': {
            'External': {
                'max_borrow_amount': {'NoLimit': None, 'Quantity': 'u128'},
                'max_price_variation': 'u128',
                'notional': 'u128',
                'price_id': {'Isin': '[u8; 12]'},
            },
            'Internal': {
                'collateral_value': 'u128',
                'max_borrow_amount': {
                    'UpToOutstandingDebt': 'InnerStruct',
                    'UpToTotalBorrowed': 'InnerStruct',
                },
                'valuation_method': {
                    'DiscountedCashFlow': 'scale_info::253',
                    'OutstandingDebt': None,
                },
            },
        },
        'restrictions': {
            'borrows': ('NotWrittenOff', 'FullOnce', 'OraclePriceRequired'),
            'repayments': ('None', 'Full'),
        },
        'schedule': {
            'interest_payments': ('None', ),
            'maturity': {'Fixed': {'date': 'u64', 'extension': 'u64'}},
            'pay_down_schedule': ('None', ),
        },
    },
}
```
---------
### LastLoanId
 Contains the last loan id generated

#### Python
```python
result = substrate.query(
    'Loans', 'LastLoanId', ['u64']
)
```

#### Return value
```python
'u64'
```
---------
### PortfolioValuation
 Stores the portfolio valuation associated to each pool

#### Python
```python
result = substrate.query(
    'Loans', 'PortfolioValuation', ['u64']
)
```

#### Return value
```python
{'last_updated': 'u64', 'value': 'u128', 'values': [('u64', 'u128')]}
```
---------
### WriteOffPolicy
 Stores write off policy used in each pool

#### Python
```python
result = substrate.query(
    'Loans', 'WriteOffPolicy', ['u64']
)
```

#### Return value
```python
[
    {'status': {'penalty': 'u128', 'percentage': 'u128'}, 'triggers': 'scale_info::259'},
]
```
---------
## Constants

---------
### MaxActiveLoansPerPool
 Max number of active loans per pool.
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('Loans', 'MaxActiveLoansPerPool')
```
---------
### MaxWriteOffPolicySize
 Max number of write-off groups per pool.
#### Value
```python
100
```
#### Python
```python
constant = substrate.get_constant('Loans', 'MaxWriteOffPolicySize')
```
---------
## Errors

---------
### BorrowLoanError
Emits when the loan can not be borrowed from

---------
### CloseLoanError
Emits when the loan can not be closed

---------
### CreateLoanError
Emits when the loan is incorrectly specified and can not be created

---------
### LoanNotActiveOrNotFound
Emits when loan doesn&\#x27;t exist or it&\#x27;s not active yet.

---------
### MaxActiveLoansReached
Emits when the max number of active loans was reached

---------
### MismatchedPricingMethod
Emits when the pricing method is not compatible with the input

---------
### MutationError
Emits when the loan can not be mutated

---------
### NFTOwnerNotFound
Emits when the NFT owner is not found

---------
### NoLoanChangeId
The Change Id does not belong to a loan change

---------
### NoValidWriteOffRule
Emits when a write-off rule is not found in a policy for a specific
loan. It happens when there is no policy or the loan is not overdue.

---------
### NotLoanBorrower
Emits when the applicant account is not the borrower of the loan

---------
### NotNFTOwner
Emits when NFT owner doesn&\#x27;t match the expected owner

---------
### PoolNotFound
Emits when pool doesn&\#x27;t exist

---------
### RepayLoanError
Emits when the loan can not be repaid from

---------
### SettlementPriceExceedsVariation
Emits when settlement price is exceeds the configured variation.

---------
### TransferDebtAmountMismatched
Emits when debt is transfered with different repaid/borrow amounts

---------
### TransferDebtToSameLoan
Emits when debt is transfered to the same loan

---------
### UnrelatedChangeId
The Change Id exists but it&\#x27;s not releated with the expected change

---------
### WrittenOffError
Emits when the loan can not be written off

---------