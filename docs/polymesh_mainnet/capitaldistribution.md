
# CapitalDistribution

---------
## Calls

---------
### claim
Claim a benefit of the capital distribution attached to `ca_id`.

Taxes are withheld as specified by the CA.
Post-tax earnings are then transferred to the default portfolio of the `origin`&\#x27;s DID.

All benefits are rounded by truncation, down to first integer below.
Moreover, before post-tax earnings, in indivisible currencies are transferred,
they are rounded down to a whole unit.

\#\# Arguments
- `origin` which must be a holder of the asset and eligible for the distribution.
- `ca_id` identifies the CA to start a capital distribution for.

\# Errors
- `HolderAlreadyPaid` if `origin`&\#x27;s DID has already received its benefit.
- `NoSuchDistribution` if there&\#x27;s no capital distribution for `ca_id`.
- `CannotClaimBeforeStart` if `now &lt; payment_at`.
- `CannotClaimAfterExpiry` if `now &gt; expiry_at.unwrap()`.
- `NoSuchCA` if `ca_id` does not identify an existing CA.
- `NotTargetedByCA` if the CA does not target `origin`&\#x27;s DID.
- `BalanceAmountProductOverflowed` if `ba = balance * amount` would overflow.
- `BalanceAmountProductSupplyDivisionFailed` if `ba * supply` would overflow.
- Other errors can occur if the compliance manager rejects the transfer.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ca_id | `CAId` | 

#### Python
```python
call = substrate.compose_call(
    'CapitalDistribution', 'claim', {
    'ca_id': {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
}
)
```

---------
### distribute
Start and attach a capital distribution, to the CA identified by `ca_id`,
with `amount` funds in `currency` withdrawn from `portfolio` belonging to `origin`&\#x27;s DID.

The distribution will commence at `payment_at` and expire at `expires_at`,
if provided, or if `None`, then there&\#x27;s no expiry.

The funds will be locked in `portfolio` from when `distribute` is called.
When there&\#x27;s no expiry, some funds may be locked indefinitely in `portfolio`,
due to claimants not withdrawing or no benefits being pushed to them.
For indivisible currencies, unlocked amounts, of less than one whole unit,
will not be transferable from `portfolio`.
However, if we imagine that users `Alice` and `Bob` both are entitled to 1.5 units,
and only receive `1` units each, then `0.5 + 0.5 = 1` units are left in `portfolio`,
which is now transferrable.

\#\# Arguments
- `origin` is a signer that has permissions to act as an agent of `ca_id.ticker`.
- `ca_id` identifies the CA to start a capital distribution for.
- `portfolio` specifies the portfolio number of the agent to distribute `amount` from.
- `currency` to withdraw and distribute from the `portfolio`.
- `per_share` amount of `currency` to withdraw and distribute.
   Specified as a per-million, i.e. `1 / 10^6`th of one `currency` token.
- `amount` of `currency` to withdraw and distribute at most.
- `payment_at` specifies when benefits may first be pushed or claimed.
- `expires_at` specifies, if provided, when remaining benefits are forfeit
   and may be reclaimed by `origin`.

\# Errors
- `UnauthorizedAgent` if `origin` is not agent-permissioned for `ticker`.
- `ExpiryBeforePayment` if `expires_at.unwrap() &lt;= payment_at`.
- `NoSuchCA` if `ca_id` does not identify an existing CA.
- `NoRecordDate` if CA has no record date.
- `RecordDateAfterStart` if CA&\#x27;s record date &gt; payment_at.
- `UnauthorizedCustodian` if the caller is not the custodian of `portfolio`.
- `InsufficientPortfolioBalance` if `portfolio` has less than `amount` of `currency`.
- `InsufficientBalance` if the protocol fee couldn&\#x27;t be charged.
- `CANotBenefit` if the CA is not of kind PredictableBenefit/UnpredictableBenefit
- `DistributionAmountIsZero` if the `amount` is zero.
- `DistributionPerShareIsZero` if the `per_share` is zero.

\# Permissions
* Asset
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| ca_id | `CAId` | 
| portfolio | `Option<PortfolioNumber>` | 
| currency | `Ticker` | 
| per_share | `Balance` | 
| amount | `Balance` | 
| payment_at | `Moment` | 
| expires_at | `Option<Moment>` | 

#### Python
```python
call = substrate.compose_call(
    'CapitalDistribution', 'distribute', {
    'amount': 'u128',
    'ca_id': {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
    'currency': '[u8; 12]',
    'expires_at': (None, 'u64'),
    'payment_at': 'u64',
    'per_share': 'u128',
    'portfolio': (None, 'u64'),
}
)
```

---------
### push_benefit
Push benefit of an ongoing distribution to the given `holder`.

Taxes are withheld as specified by the CA.
Post-tax earnings are then transferred to the default portfolio of the `origin`&\#x27;s DID.

All benefits are rounded by truncation, down to first integer below.
Moreover, before post-tax earnings, in indivisible currencies are transferred,
they are rounded down to a whole unit.

\#\# Arguments
- `origin` is a signer that has permissions to act as an agent of `ca_id.ticker`.
- `ca_id` identifies the CA with a capital distributions to push benefits for.
- `holder` to push benefits to.

\# Errors
- `UnauthorizedAgent` if `origin` is not agent-permissioned for `ticker`.
- `NoSuchDistribution` if there&\#x27;s no capital distribution for `ca_id`.
- `CannotClaimBeforeStart` if `now &lt; payment_at`.
- `CannotClaimAfterExpiry` if `now &gt; expiry_at.unwrap()`.
- `NoSuchCA` if `ca_id` does not identify an existing CA.
- `NotTargetedByCA` if the CA does not target `holder`.
- `BalanceAmountProductOverflowed` if `ba = balance * amount` would overflow.
- `BalanceAmountProductSupplyDivisionFailed` if `ba * supply` would overflow.
- Other errors can occur if the compliance manager rejects the transfer.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ca_id | `CAId` | 
| holder | `IdentityId` | 

#### Python
```python
call = substrate.compose_call(
    'CapitalDistribution', 'push_benefit', {
    'ca_id': {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
    'holder': '[u8; 32]',
}
)
```

---------
### reclaim
Assuming a distribution has expired,
unlock the remaining amount in the distributor portfolio.

\#\# Arguments
- `origin` which must be the creator of the capital distribution tied to `ca_id`.
- `ca_id` identifies the CA with a capital distribution to reclaim for.

\# Errors
- `NoSuchDistribution` if there&\#x27;s no capital distribution for `ca_id`.
- `AlreadyReclaimed` if this function has already been called successfully.
- `NotExpired` if `now &lt; expiry`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ca_id | `CAId` | 

#### Python
```python
call = substrate.compose_call(
    'CapitalDistribution', 'reclaim', {
    'ca_id': {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
}
)
```

---------
### remove_distribution
Removes a distribution that hasn&\#x27;t started yet,
unlocking the full amount in the distributor portfolio.

\#\# Arguments
- `origin` is a signer that has permissions to act as an agent of `ca_id.ticker`.
- `ca_id` identifies the CA with a not-yet-started capital distribution to remove.

\# Errors
- `UnauthorizedAgent` if `origin` is not agent-permissioned for `ticker`.
- `NoSuchDistribution` if there&\#x27;s no capital distribution for `ca_id`.
- `DistributionStarted` if `payment_at &lt;= now`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ca_id | `CAId` | 

#### Python
```python
call = substrate.compose_call(
    'CapitalDistribution', 'remove_distribution', {
    'ca_id': {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
}
)
```

---------
## Events

---------
### BenefitClaimed
A token holder&\#x27;s benefit of a capital distribution for the given `CAId` was claimed.

(Caller DID, Holder/Claimant DID, CA&\#x27;s ID, updated distribution details, DID&\#x27;s benefit, DID&\#x27;s tax %)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventDid` | ```[u8; 32]```
| None | `EventDid` | ```[u8; 32]```
| None | `CAId` | ```{'ticker': '[u8; 12]', 'local_id': 'u32'}```
| None | `Distribution` | ```{'from': {'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}, 'currency': '[u8; 12]', 'per_share': 'u128', 'amount': 'u128', 'remaining': 'u128', 'reclaimed': 'bool', 'payment_at': 'u64', 'expires_at': (None, 'u64')}```
| None | `Balance` | ```u128```
| None | `Tax` | ```u32```

---------
### Created
A capital distribution, with details included,
was created by the DID (permissioned agent) for the CA identified by `CAId`.

(Agent DID, CA&\#x27;s ID, distribution details)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventDid` | ```[u8; 32]```
| None | `CAId` | ```{'ticker': '[u8; 12]', 'local_id': 'u32'}```
| None | `Distribution` | ```{'from': {'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}, 'currency': '[u8; 12]', 'per_share': 'u128', 'amount': 'u128', 'remaining': 'u128', 'reclaimed': 'bool', 'payment_at': 'u64', 'expires_at': (None, 'u64')}```

---------
### Reclaimed
Stats from `push_benefit` was emitted.

(Agent DID, CA&\#x27;s ID, max requested DIDs, processed DIDs, failed DIDs)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventDid` | ```[u8; 32]```
| None | `CAId` | ```{'ticker': '[u8; 12]', 'local_id': 'u32'}```
| None | `Balance` | ```u128```

---------
### Removed
A capital distribution was removed.

(Agent DID, CA&\#x27;s ID)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventDid` | ```[u8; 32]```
| None | `CAId` | ```{'ticker': '[u8; 12]', 'local_id': 'u32'}```

---------
## Storage functions

---------
### Distributions
 All capital distributions, tied to their respective corporate actions (CAs).

 (CAId) =&gt; Distribution

#### Python
```python
result = substrate.query(
    'CapitalDistribution', 'Distributions', [
    {
        'local_id': 'u32',
        'ticker': '[u8; 12]',
    },
]
)
```

#### Return value
```python
{
    'amount': 'u128',
    'currency': '[u8; 12]',
    'expires_at': (None, 'u64'),
    'from': {'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}},
    'payment_at': 'u64',
    'per_share': 'u128',
    'reclaimed': 'bool',
    'remaining': 'u128',
}
```
---------
### HolderPaid
 Has an asset holder been paid yet?

 (CAId, DID) -&gt; Was DID paid in the CAId?

#### Python
```python
result = substrate.query(
    'CapitalDistribution', 'HolderPaid', [
    (
        {
            'local_id': 'u32',
            'ticker': '[u8; 12]',
        },
        '[u8; 32]',
    ),
]
)
```

#### Return value
```python
'bool'
```
---------
### StorageVersion
 Storage version.

#### Python
```python
result = substrate.query(
    'CapitalDistribution', 'StorageVersion', []
)
```

#### Return value
```python
'u8'
```
---------
## Errors

---------
### AlreadyExists
A distribution already exists for this CA.

---------
### AlreadyReclaimed
DID who created the distribution already did reclaim.

---------
### BalancePerShareProductOverflowed
Multiplication of the balance with the per share payout amount overflowed.

---------
### CANotBenefit
A capital distribution was made for a non-benefit CA.

---------
### CannotClaimAfterExpiry
Distribution&\#x27;s expiry has passed. DID cannot claim anymore and has forfeited the benefits.

---------
### CannotClaimBeforeStart
Distribution allotment cannot be claimed as the current time is before start-of-payment.

---------
### DistributionAmountIsZero
Distribution `amount` cannot be zero.

---------
### DistributionPerShareIsZero
Distribution `per_share` cannot be zero.

---------
### DistributionStarted
A distribution has been activated, as `payment_at &lt;= now` holds.

---------
### ExpiryBeforePayment
A distributions provided expiry date was strictly before its payment date.
In other words, everything to distribute would immediately be forfeited.

---------
### HolderAlreadyPaid
The token holder has already been paid their benefit.

---------
### InsufficientRemainingAmount
A distribution has insufficient remaining amount of currency to distribute.

---------
### NoSuchDistribution
A capital distribution doesn&\#x27;t exist for this CA.

---------
### NotDistributionCreator
DID is not the one who created the distribution.

---------
### NotExpired
Distribution had not expired yet, or there&\#x27;s no expiry date.

---------