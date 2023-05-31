
# Crowdloan

---------
## Calls

---------
### add_memo
Add an optional memo to an existing crowdloan contribution.

Origin must be Signed, and the user must have contributed to the crowdloan.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ParaId` | 
| memo | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Crowdloan', 'add_memo', {'index': 'u32', 'memo': 'Bytes'}
)
```

---------
### contribute
Contribute to a crowd sale. This will transfer some balance over to fund a parachain
slot. It will be withdrawable when the crowdloan has ended and the funds are unused.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ParaId` | 
| value | `BalanceOf<T>` | 
| signature | `Option<MultiSignature>` | 

#### Python
```python
call = substrate.compose_call(
    'Crowdloan', 'contribute', {
    'index': 'u32',
    'signature': (
        None,
        {
            'Ecdsa': '[u8; 65]',
            'Ed25519': '[u8; 64]',
            'Sr25519': '[u8; 64]',
        },
    ),
    'value': 'u128',
}
)
```

---------
### contribute_all
Contribute your entire balance to a crowd sale. This will transfer the entire balance of a user over to fund a parachain
slot. It will be withdrawable when the crowdloan has ended and the funds are unused.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ParaId` | 
| signature | `Option<MultiSignature>` | 

#### Python
```python
call = substrate.compose_call(
    'Crowdloan', 'contribute_all', {
    'index': 'u32',
    'signature': (
        None,
        {
            'Ecdsa': '[u8; 65]',
            'Ed25519': '[u8; 64]',
            'Sr25519': '[u8; 64]',
        },
    ),
}
)
```

---------
### create
Create a new crowdloaning campaign for a parachain slot with the given lease period range.

This applies a lock to your parachain configuration, ensuring that it cannot be changed
by the parachain manager.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ParaId` | 
| cap | `BalanceOf<T>` | 
| first_period | `LeasePeriodOf<T>` | 
| last_period | `LeasePeriodOf<T>` | 
| end | `T::BlockNumber` | 
| verifier | `Option<MultiSigner>` | 

#### Python
```python
call = substrate.compose_call(
    'Crowdloan', 'create', {
    'cap': 'u128',
    'end': 'u32',
    'first_period': 'u32',
    'index': 'u32',
    'last_period': 'u32',
    'verifier': (
        None,
        {
            'Ecdsa': '[u8; 33]',
            'Ed25519': '[u8; 32]',
            'Sr25519': '[u8; 32]',
        },
    ),
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
    'Crowdloan', 'dissolve', {'index': 'u32'}
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
| first_period | `LeasePeriodOf<T>` | 
| last_period | `LeasePeriodOf<T>` | 
| end | `T::BlockNumber` | 
| verifier | `Option<MultiSigner>` | 

#### Python
```python
call = substrate.compose_call(
    'Crowdloan', 'edit', {
    'cap': 'u128',
    'end': 'u32',
    'first_period': 'u32',
    'index': 'u32',
    'last_period': 'u32',
    'verifier': (
        None,
        {
            'Ecdsa': '[u8; 33]',
            'Ed25519': '[u8; 32]',
            'Sr25519': '[u8; 32]',
        },
    ),
}
)
```

---------
### poke
Poke the fund into `NewRaise`

Origin must be Signed, and the fund has non-zero raise.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'Crowdloan', 'poke', {'index': 'u32'}
)
```

---------
### refund
Automatically refund contributors of an ended crowdloan.
Due to weight restrictions, this function may need to be called multiple
times to fully refund all users. We will refund `RemoveKeysLimit` users at a time.

Origin must be signed, but can come from anyone.
#### Attributes
| Name | Type |
| -------- | -------- | 
| index | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'Crowdloan', 'refund', {'index': 'u32'}
)
```

---------
### withdraw
Withdraw full balance of a specific contributor.

Origin must be signed, but can come from anyone.

The fund must be either in, or ready for, retirement. For a fund to be *in* retirement, then the retirement
flag must be set. For a fund to be ready for retirement, then:
- it must not already be in retirement;
- the amount of raised funds must be bigger than the _free_ balance of the account;
- and either:
  - the block number must be at least `end`; or
  - the current lease period must be greater than the fund&\#x27;s `last_period`.

In this case, the fund&\#x27;s retirement flag is set and its `end` is reset to the current block
number.

- `who`: The account whose contribution should be withdrawn.
- `index`: The parachain to whose crowdloan the contribution was made.
#### Attributes
| Name | Type |
| -------- | -------- | 
| who | `T::AccountId` | 
| index | `ParaId` | 

#### Python
```python
call = substrate.compose_call(
    'Crowdloan', 'withdraw', {'index': 'u32', 'who': 'AccountId'}
)
```

---------
## Events

---------
### AddedToNewRaise
A parachain has been moved to `NewRaise`
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| para_id | `ParaId` | ```u32```

---------
### AllRefunded
All loans in a fund have been refunded.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| para_id | `ParaId` | ```u32```

---------
### Contributed
Contributed to a crowd sale.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| fund_index | `ParaId` | ```u32```
| amount | `BalanceOf<T>` | ```u128```

---------
### Created
Create a new crowdloaning campaign.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| para_id | `ParaId` | ```u32```

---------
### Dissolved
Fund is dissolved.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| para_id | `ParaId` | ```u32```

---------
### Edited
The configuration to a crowdloan has been edited.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| para_id | `ParaId` | ```u32```

---------
### HandleBidResult
The result of trying to submit a new bid to the Slots pallet.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| para_id | `ParaId` | ```u32```
| result | `DispatchResult` | ```{'Ok': (), 'Err': {'Other': None, 'CannotLookup': None, 'BadOrigin': None, 'Module': {'index': 'u8', 'error': '[u8; 4]'}, 'ConsumerRemaining': None, 'NoProviders': None, 'TooManyConsumers': None, 'Token': ('FundsUnavailable', 'OnlyProvider', 'BelowMinimum', 'CannotCreate', 'UnknownAsset', 'Frozen', 'Unsupported', 'CannotCreateHold', 'NotExpendable'), 'Arithmetic': ('Underflow', 'Overflow', 'DivisionByZero'), 'Transactional': ('LimitReached', 'NoLayer'), 'Exhausted': None, 'Corruption': None, 'Unavailable': None}}```

---------
### MemoUpdated
A memo has been updated.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| para_id | `ParaId` | ```u32```
| memo | `Vec<u8>` | ```Bytes```

---------
### PartiallyRefunded
The loans in a fund have been partially dissolved, i.e. there are some left
over child keys that still need to be killed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| para_id | `ParaId` | ```u32```

---------
### Withdrew
Withdrew full balance of a contributor.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| who | `T::AccountId` | ```AccountId```
| fund_index | `ParaId` | ```u32```
| amount | `BalanceOf<T>` | ```u128```

---------
## Storage functions

---------
### EndingsCount
 The number of auctions that have entered into their ending period so far.

#### Python
```python
result = substrate.query(
    'Crowdloan', 'EndingsCount', []
)
```

#### Return value
```python
'u32'
```
---------
### Funds
 Info on all of the funds.

#### Python
```python
result = substrate.query(
    'Crowdloan', 'Funds', ['u32']
)
```

#### Return value
```python
{
    'cap': 'u128',
    'deposit': 'u128',
    'depositor': 'AccountId',
    'end': 'u32',
    'first_period': 'u32',
    'fund_index': 'u32',
    'last_contribution': {'Ending': 'u32', 'Never': None, 'PreEnding': 'u32'},
    'last_period': 'u32',
    'raised': 'u128',
    'verifier': (
        None,
        {'Ecdsa': '[u8; 33]', 'Ed25519': '[u8; 32]', 'Sr25519': '[u8; 32]'},
    ),
}
```
---------
### NewRaise
 The funds that have had additional contributions during the last block. This is used
 in order to determine which funds should submit new or updated bids.

#### Python
```python
result = substrate.query(
    'Crowdloan', 'NewRaise', []
)
```

#### Return value
```python
['u32']
```
---------
### NextFundIndex
 Tracker for the next available fund index

#### Python
```python
result = substrate.query(
    'Crowdloan', 'NextFundIndex', []
)
```

#### Return value
```python
'u32'
```
---------
## Constants

---------
### MinContribution
 The minimum amount that may be contributed into a crowdloan. Should almost certainly be at
 least `ExistentialDeposit`.
#### Value
```python
999999999000
```
#### Python
```python
constant = substrate.get_constant('Crowdloan', 'MinContribution')
```
---------
### PalletId
 `PalletId` for the crowdloan pallet. An appropriate value could be `PalletId(*b&quot;py/cfund&quot;)`
#### Value
```python
'0x70792f6366756e64'
```
#### Python
```python
constant = substrate.get_constant('Crowdloan', 'PalletId')
```
---------
### RemoveKeysLimit
 Max number of storage keys to remove per extrinsic call.
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('Crowdloan', 'RemoveKeysLimit')
```
---------
## Errors

---------
### AlreadyInNewRaise
The fund is already in `NewRaise`

---------
### BidOrLeaseActive
This parachain&\#x27;s bid or lease is still active and withdraw cannot yet begin.

---------
### CannotEndInPast
The campaign ends before the current block number. The end must be in the future.

---------
### CapExceeded
Contributions exceed maximum amount.

---------
### ContributionPeriodOver
The contribution period has already ended.

---------
### ContributionTooSmall
The contribution was below the minimum, `MinContribution`.

---------
### EndTooFarInFuture
The end date for this crowdloan is not sensible.

---------
### FirstPeriodInPast
The current lease period is more than the first lease period.

---------
### FirstPeriodTooFarInFuture
The first lease period needs to at least be less than 3 `max_value`.

---------
### FundNotEnded
The crowdloan has not yet ended.

---------
### InvalidOrigin
The origin of this call is invalid.

---------
### InvalidParaId
Invalid fund index.

---------
### InvalidSignature
Invalid signature.

---------
### LastPeriodBeforeFirstPeriod
Last lease period must be greater than first lease period.

---------
### LastPeriodTooFarInFuture
The last lease period cannot be more than 3 periods after the first period.

---------
### LeaseActive
This parachain lease is still active and retirement cannot yet begin.

---------
### MemoTooLarge
The provided memo is too large.

---------
### NoContributions
There are no contributions stored in this crowdloan.

---------
### NoLeasePeriod
A lease period has not started yet, due to an offset in the starting block.

---------
### NotParachain
This crowdloan does not correspond to a parachain.

---------
### NotReadyToDissolve
The crowdloan is not ready to dissolve. Potentially still has a slot or in retirement period.

---------
### Overflow
There was an overflow.

---------
### VrfDelayInProgress
No contributions allowed during the VRF delay

---------