
# VestingRegistrar

---------
## Calls

---------
### claim_batch
Batch claim for vested accounts
#### Attributes
| Name | Type |
| -------- | -------- | 
| accounts | `VestedAccounts<T>` | 

#### Python
```python
call = substrate.compose_call(
    'VestingRegistrar', 'claim_batch', {
    'accounts': [
        {
            'account_id': 'AccountId',
            'amount': 'u128',
        },
    ],
}
)
```

---------
### force_vest_all_schedules
For all registered accounts, it sets the vesting schedule expiration to the next block
number.

This is a privileged call and can only be called by the root origin.

It simply updates each schedule registered for `account` to expire in the next block.
#### Attributes
| Name | Type |
| -------- | -------- | 
| accounts | `VestedAccounts<T>` | 

#### Python
```python
call = substrate.compose_call(
    'VestingRegistrar', 'force_vest_all_schedules', {
    'accounts': [
        {
            'account_id': 'AccountId',
            'amount': 'u128',
        },
    ],
}
)
```

---------
### register_batch
Register a batch of accounts and their vesting amounts.

\# Errors

- [`Error::InvalidVestedAmount`]: If the vested amount is invalid.
- [`Error::InvalidPeriodCount`]: If the period count is invalid.
#### Attributes
| Name | Type |
| -------- | -------- | 
| accounts | `VestedAccounts<T>` | 
| start_block_number | `BlockNumberFor<T>` | 
| period | `BlockNumberFor<T>` | 
| period_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'VestingRegistrar', 'register_batch', {
    'accounts': [
        {
            'account_id': 'AccountId',
            'amount': 'u128',
        },
    ],
    'period': 'u32',
    'period_count': 'u32',
    'start_block_number': 'u32',
}
)
```

---------
## Errors

---------
### EmptyAccountList
empty list supplied for vesting

---------
### InvalidPeriodCount
Period count is invalid.

---------
### InvalidVestedAmount
Vested amount is invalid..

---------