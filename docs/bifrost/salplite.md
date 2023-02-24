
# SalpLite

---------
## Calls

---------
### continue_fund
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ParaId` | 
| first_slot | `LeasePeriod` | 
| last_slot | `LeasePeriod` | 

#### Python
```python
call = substrate.compose_call(
    'SalpLite', 'continue_fund', {
    'first_slot': 'u32',
    'index': 'u32',
    'last_slot': 'u32',
}
)
```

---------
### create
Create a new crowdloaning campaign for a parachain slot deposit for the current auction.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ParaId` | 
| cap | `BalanceOf<T>` | 
| first_slot | `LeasePeriod` | 
| last_slot | `LeasePeriod` | 

#### Python
```python
call = substrate.compose_call(
    'SalpLite', 'create', {
    'cap': 'u128',
    'first_slot': 'u32',
    'index': 'u32',
    'last_slot': 'u32',
}
)
```

---------
### dissolve
Remove a fund after the retirement period has ended and all funds have been returned.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'SalpLite', 'dissolve', {'index': 'u32'}
)
```

---------
### dissolve_refunded
Remove a fund after the retirement period has ended and all funds have been returned.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ParaId` | 
| first_slot | `LeasePeriod` | 
| last_slot | `LeasePeriod` | 

#### Python
```python
call = substrate.compose_call(
    'SalpLite', 'dissolve_refunded', {
    'first_slot': 'u32',
    'index': 'u32',
    'last_slot': 'u32',
}
)
```

---------
### edit
Edit the configuration for an in-progress crowdloan.

Can only be called by Root origin.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ParaId` | 
| cap | `BalanceOf<T>` | 
| raised | `BalanceOf<T>` | 
| first_slot | `LeasePeriod` | 
| last_slot | `LeasePeriod` | 
| fund_status | `Option<FundStatus>` | 

#### Python
```python
call = substrate.compose_call(
    'SalpLite', 'edit', {
    'cap': 'u128',
    'first_slot': 'u32',
    'fund_status': (
        None,
        (
            'Ongoing',
            'Retired',
            'Success',
            'Failed',
            'RefundWithdrew',
            'RedeemWithdrew',
            'FailedToContinue',
        ),
    ),
    'index': 'u32',
    'last_slot': 'u32',
    'raised': 'u128',
}
)
```

---------
### fund_fail
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'SalpLite', 'fund_fail', {'index': 'u32'}
)
```

---------
### fund_retire
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'SalpLite', 'fund_retire', {'index': 'u32'}
)
```

---------
### fund_success
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'SalpLite', 'fund_success', {'index': 'u32'}
)
```

---------
### issue
Contribute to a crowd sale. This will transfer some balance over to fund a parachain
slot. It will be withdrawable in two instances: the parachain becomes retired; or the
slot is unable to be purchased and the timeout expires.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdOf<T>` | 
| index | `ParaId` | 
| value | `BalanceOf<T>` | 
| message_id | `MessageId` | 

#### Python
```python
call = substrate.compose_call(
    'SalpLite', 'issue', {
    'index': 'u32',
    'message_id': '[u8; 32]',
    'value': 'u128',
    'who': 'AccountId',
}
)
```

---------
### redeem
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ParaId` | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'SalpLite', 'redeem', {'index': 'u32', 'value': 'u128'}
)
```

---------
### refund
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ParaId` | 
| first_slot | `LeasePeriod` | 
| last_slot | `LeasePeriod` | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'SalpLite', 'refund', {
    'first_slot': 'u32',
    'index': 'u32',
    'last_slot': 'u32',
    'value': 'u128',
}
)
```

---------
### set_multisig_confirm_account
#### Attributes
| Name | Type |
| -------- | -------- | 
| account | `AccountIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'SalpLite', 'set_multisig_confirm_account', {'account': 'AccountId'}
)
```

---------
### withdraw
Withdraw full balance of the parachain.
- `index`: The parachain to whose crowdloan the contribution was made.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'SalpLite', 'withdraw', {'index': 'u32'}
)
```

---------
## Events

---------
### AllUnlocked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```

---------
### Continued
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `LeasePeriod` | ```u32```
| None | `LeasePeriod` | ```u32```

---------
### Created
Create a new crowdloaning campaign. [fund_index]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```

---------
### Dissolved
Fund is dissolved. [fund_index]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```

---------
### Edited
Fund is edited. [fund_index]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```

---------
### Failed
Fund status change
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```

---------
### Issued
Contributed to a crowd sale. [who, fund_index, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `ParaId` | ```u32```
| None | `BalanceOf<T>` | ```u128```
| None | `MessageId` | ```[u8; 32]```

---------
### Redeemed
redeem to account. [who, fund_index, first_slot, last_slot, value]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `ParaId` | ```u32```
| None | `LeasePeriod` | ```u32```
| None | `LeasePeriod` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### Refunded
refund to account. [who, fund_index,value]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `ParaId` | ```u32```
| None | `LeasePeriod` | ```u32```
| None | `LeasePeriod` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### RefundedDissolved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `LeasePeriod` | ```u32```
| None | `LeasePeriod` | ```u32```

---------
### Retired
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```

---------
### Success
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```

---------
### Unlocked
The vsToken/vsBond was be unlocked. [who, fund_index, value]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `ParaId` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
### Withdrew
Withdrew full balance of a contributor. [who, fund_index, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### CurrentTrieIndex
 Tracker for the next available fund index

#### Python
```python
result = substrate.query(
    'SalpLite', 'CurrentTrieIndex', []
)
```

#### Return value
```python
'u32'
```
---------
### FailedFundsToRefund
 Info on all of the fail-to-continue funds.

#### Python
```python
result = substrate.query(
    'SalpLite', 'FailedFundsToRefund', ['u32', 'u32', 'u32']
)
```

#### Return value
```python
(
    None,
    {
        'cap': 'u128',
        'first_slot': 'u32',
        'last_slot': 'u32',
        'raised': 'u128',
        'status': (
            'Ongoing',
            'Retired',
            'Success',
            'Failed',
            'RefundWithdrew',
            'RedeemWithdrew',
            'FailedToContinue',
        ),
        'trie_index': 'u32',
    },
)
```
---------
### Funds
 Info on all of the funds.

#### Python
```python
result = substrate.query(
    'SalpLite', 'Funds', ['u32']
)
```

#### Return value
```python
(
    None,
    {
        'cap': 'u128',
        'first_slot': 'u32',
        'last_slot': 'u32',
        'raised': 'u128',
        'status': (
            'Ongoing',
            'Retired',
            'Success',
            'Failed',
            'RefundWithdrew',
            'RedeemWithdrew',
            'FailedToContinue',
        ),
        'trie_index': 'u32',
    },
)
```
---------
### MultisigConfirmAccount
 Multisig confirm account

#### Python
```python
result = substrate.query(
    'SalpLite', 'MultisigConfirmAccount', []
)
```

#### Return value
```python
'AccountId'
```
---------
### RedeemPool
 The balance can be redeemed to users.

#### Python
```python
result = substrate.query(
    'SalpLite', 'RedeemPool', []
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### BatchKeysLimit
#### Value
```python
500
```
#### Python
```python
constant = substrate.get_constant('SalpLite', 'BatchKeysLimit')
```
---------
### LeasePeriod
 The number of blocks over which a single period lasts.
#### Value
```python
604800
```
#### Python
```python
constant = substrate.get_constant('SalpLite', 'LeasePeriod')
```
---------
### MinContribution
 The minimum amount that may be contributed into a crowdloan. Should almost certainly be
 at least ExistentialDeposit.
#### Value
```python
50000000000
```
#### Python
```python
constant = substrate.get_constant('SalpLite', 'MinContribution')
```
---------
### PalletId
 ModuleID for the crowdloan module. An appropriate value could be
 ```ModuleId(*b&quot;py/cfund&quot;)```
#### Value
```python
'0x62662f73616c706c'
```
#### Python
```python
constant = substrate.get_constant('SalpLite', 'PalletId')
```
---------
### RelayChainToken
#### Value
```python
{'Token': 'DOT'}
```
#### Python
```python
constant = substrate.get_constant('SalpLite', 'RelayChainToken')
```
---------
### ReleaseCycle
 The time interval from 1:1 redeem-pool to bancor-pool to release.
#### Value
```python
7200
```
#### Python
```python
constant = substrate.get_constant('SalpLite', 'ReleaseCycle')
```
---------
### ReleaseRatio
 The release ratio from the 1:1 redeem-pool to the bancor-pool per cycle.
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('SalpLite', 'ReleaseRatio')
```
---------
### SlotLength
#### Value
```python
8
```
#### Python
```python
constant = substrate.get_constant('SalpLite', 'SlotLength')
```
---------
## Errors

---------
### CapExceeded
Contributions exceed maximum amount.

---------
### ContributionTooSmall
The contribution was below the minimum, `MinContribution`.

---------
### FirstSlotTooFarInFuture
The first slot needs to at least be less than 3 `max_value`.

---------
### FundAlreadyCreated
The fund has been registered.

---------
### InvalidContributionStatus
Invalid contribution status.

---------
### InvalidFundNotExist

---------
### InvalidFundSameSlot

---------
### InvalidFundStatus
Invalid fund status.

---------
### InvalidParaId
Invalid fund index.

---------
### InvalidRefund

---------
### LastSlotBeforeFirstSlot
Last slot must be greater than first slot.

---------
### LastSlotTooFarInFuture
The last slot cannot be more then 3 slots after the first slot.

---------
### MigrateSlotBeforeFirstSlot
Migrate slot must be greater than first slot

---------
### NotEnoughBalanceInFund
Invalid Fund when refund/redeem

---------
### NotEnoughBalanceInRedeemPool
Don&\#x27;t have enough token to redeem by users

---------
### NotEnoughBalanceInRefundPool
Don&\#x27;t have enough token to refund by users

---------
### NotEnoughBalanceToUnlock
Don&\#x27;t have enough vsToken/vsBond to unlock

---------
### NotEnoughFreeAssetsToRedeem
Dont have enough vsToken/vsBond to redeem

---------
### NotEnoughReservedAssetsToRefund
Don&\#x27;t have enough vsToken/vsBond to refund

---------
### Overflow
There was an overflow.

---------
### ZeroContribution
The account doesn&\#x27;t have any contribution to the fund.

---------