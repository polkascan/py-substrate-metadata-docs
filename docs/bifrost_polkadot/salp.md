
# Salp

---------
## Calls

---------
### batch_unlock
Unlock the reserved vsToken/vsBond after fund success
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'Salp', 'batch_unlock', {'index': 'u32'}
)
```

---------
### buyback
#### Attributes
| Name | Type |
| -------- | -------- | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Salp', 'buyback', {'value': 'u128'}
)
```

---------
### confirm_contribute
Confirm contribute
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdOf<T>` | 
| index | `ParaId` | 
| is_success | `bool` | 
| message_id | `MessageId` | 

#### Python
```python
call = substrate.compose_call(
    'Salp', 'confirm_contribute', {
    'index': 'u32',
    'is_success': 'bool',
    'message_id': '[u8; 32]',
    'who': 'AccountId',
}
)
```

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
    'Salp', 'continue_fund', {
    'first_slot': 'u32',
    'index': 'u32',
    'last_slot': 'u32',
}
)
```

---------
### contribute
Contribute to a crowd sale. This will transfer some balance over to fund a parachain
slot. It will be withdrawable in two instances: the parachain becomes retired; or the
slot is unable to be purchased and the timeout expires.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ParaId` | 
| value | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Salp', 'contribute', {'index': 'u32', 'value': 'u128'}
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
    'Salp', 'create', {
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
    'Salp', 'dissolve', {'index': 'u32'}
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
    'Salp', 'dissolve_refunded', {
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
    'Salp', 'edit', {
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
            'End',
        ),
    ),
    'index': 'u32',
    'last_slot': 'u32',
    'raised': 'u128',
}
)
```

---------
### fund_end
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'Salp', 'fund_end', {'index': 'u32'}
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
    'Salp', 'fund_fail', {'index': 'u32'}
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
    'Salp', 'fund_retire', {'index': 'u32'}
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
    'Salp', 'fund_success', {'index': 'u32'}
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
    'Salp', 'redeem', {'index': 'u32', 'value': 'u128'}
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
    'Salp', 'refund', {
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
    'Salp', 'set_multisig_confirm_account', {'account': 'AccountId'}
)
```

---------
### unlock
Unlock the reserved vsToken/vsBond after fund success
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdOf<T>` | 
| index | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'Salp', 'unlock', {'index': 'u32', 'who': 'AccountId'}
)
```

---------
### unlock_by_vsbond
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdOf<T>` | 
| vsbond | `CurrencyId` | 

#### Python
```python
call = substrate.compose_call(
    'Salp', 'unlock_by_vsbond', {
    'vsbond': {
        'ForeignAsset': 'u32',
        'LPToken': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u8',
        ),
        'Native': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Stable': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'StableLpToken': 'u32',
        'Token': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'Token2': 'u8',
        'VSBond': (
            (
                'ASG',
                'BNC',
                'KUSD',
                'DOT',
                'KSM',
                'ETH',
                'KAR',
                'ZLK',
                'PHA',
                'RMRK',
                'MOVR',
            ),
            'u32',
            'u32',
            'u32',
        ),
        'VSBond2': (
            'u8',
            'u32',
            'u32',
            'u32',
        ),
        'VSToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VSToken2': 'u8',
        'VToken': (
            'ASG',
            'BNC',
            'KUSD',
            'DOT',
            'KSM',
            'ETH',
            'KAR',
            'ZLK',
            'PHA',
            'RMRK',
            'MOVR',
        ),
        'VToken2': 'u8',
    },
    'who': 'AccountId',
}
)
```

---------
### unlock_vstoken
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `AccountIdOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'Salp', 'unlock_vstoken', {'who': 'AccountId'}
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
    'Salp', 'withdraw', {'index': 'u32'}
)
```

---------
## Events

---------
### AllRefunded
all refund
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```

---------
### AllUnlocked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```

---------
### Buyback
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BalanceOf<T>` | ```u128```

---------
### Continued
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `ParaId` | ```u32```
| None | `LeasePeriod` | ```u32```
| None | `LeasePeriod` | ```u32```

---------
### ContributeFailed
Fail on contribute to crowd sale. [who, fund_index, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `ParaId` | ```u32```
| None | `BalanceOf<T>` | ```u128```
| None | `MessageId` | ```[u8; 32]```

---------
### Contributed
Contributed to a crowd sale. [who, fund_index, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `ParaId` | ```u32```
| None | `BalanceOf<T>` | ```u128```
| None | `MessageId` | ```[u8; 32]```

---------
### Contributing
Contributing to a crowd sale. [who, fund_index, amount]
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```
| None | `ParaId` | ```u32```
| None | `BalanceOf<T>` | ```u128```
| None | `MessageId` | ```[u8; 32]```

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
### End
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
### VstokenUnlocked
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```

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
### CurrentNonce
 Tracker for the next nonce index

#### Python
```python
result = substrate.query(
    'Salp', 'CurrentNonce', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### CurrentTrieIndex
 Tracker for the next available fund index

#### Python
```python
result = substrate.query(
    'Salp', 'CurrentTrieIndex', []
)
```

#### Return value
```python
'u32'
```
---------
### FailedFundsToRefund

#### Python
```python
result = substrate.query(
    'Salp', 'FailedFundsToRefund', ['u32', 'u32', 'u32']
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
            'End',
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
    'Salp', 'Funds', ['u32']
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
            'End',
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
    'Salp', 'MultisigConfirmAccount', []
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
    'Salp', 'RedeemPool', []
)
```

#### Return value
```python
'u128'
```
---------
## Constants

---------
### BuybackPalletId
#### Value
```python
'0x62662f73616c7063'
```
#### Python
```python
constant = substrate.get_constant('Salp', 'BuybackPalletId')
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
constant = substrate.get_constant('Salp', 'LeasePeriod')
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
constant = substrate.get_constant('Salp', 'MinContribution')
```
---------
### PalletId
 ModuleID for the crowdloan module. An appropriate value could be
 ```ModuleId(*b&quot;py/cfund&quot;)```
#### Value
```python
'0x62662f73616c7023'
```
#### Python
```python
constant = substrate.get_constant('Salp', 'PalletId')
```
---------
### RelayChainToken
#### Value
```python
{'Token2': 0}
```
#### Python
```python
constant = substrate.get_constant('Salp', 'RelayChainToken')
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
constant = substrate.get_constant('Salp', 'ReleaseCycle')
```
---------
### ReleaseRatio
 The release ratio from the 1:1 redeem-pool to the bancor-pool per cycle.

 **NOTE: THE RELEASE RATIO MUST BE IN [0, 1].**
#### Value
```python
50
```
#### Python
```python
constant = substrate.get_constant('Salp', 'ReleaseRatio')
```
---------
### RemoveKeysLimit
#### Value
```python
500
```
#### Python
```python
constant = substrate.get_constant('Salp', 'RemoveKeysLimit')
```
---------
### SlotLength
#### Value
```python
8
```
#### Python
```python
constant = substrate.get_constant('Salp', 'SlotLength')
```
---------
### TreasuryAccount
#### Value
```python
'eCSrvbA5gGNYdM3UjBNxcBNBqGxtz3SEEfydKragtL4pJ4F'
```
#### Python
```python
constant = substrate.get_constant('Salp', 'TreasuryAccount')
```
---------
### VSBondValidPeriod
#### Value
```python
216000
```
#### Python
```python
constant = substrate.get_constant('Salp', 'VSBondValidPeriod')
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
### NotEnoughBalanceInFund

---------
### NotEnoughBalanceInRedeemPool
Don&\#x27;t have enough token to redeem by users

---------
### NotEnoughBalanceInRefundPool
Don&\#x27;t have enough token to refund by users

---------
### NotEnoughBalanceToContribute

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
### NotSupportTokenType

---------
### Overflow
There was an overflow.

---------
### UnRedeemableNow
The vsBond cannot be redeemed by now

---------
### VSBondExpired
The vsBond is expired now

---------
### XcmFailed
Crosschain xcm failed

---------
### ZeroContribution
The account doesn&\#x27;t have any contribution to the fund.

---------