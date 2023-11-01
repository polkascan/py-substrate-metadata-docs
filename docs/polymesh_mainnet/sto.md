
# Sto

---------
## Calls

---------
### create_fundraiser
Create a new fundraiser.

* `offering_portfolio` - Portfolio containing the `offering_asset`.
* `offering_asset` - Asset being offered.
* `raising_portfolio` - Portfolio containing the `raising_asset`.
* `raising_asset` - Asset being exchanged for `offering_asset` on investment.
* `tiers` - Price tiers to charge investors on investment.
* `venue_id` - Venue to handle settlement.
* `start` - Fundraiser start time, if `None` the fundraiser will start immediately.
* `end` - Fundraiser end time, if `None` the fundraiser will never expire.
* `minimum_investment` - Minimum amount of `raising_asset` that an investor needs to spend to invest in this raise.
* `fundraiser_name` - Fundraiser name, only used in the UIs.

\# Permissions
* Asset
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| offering_portfolio | `PortfolioId` | 
| offering_asset | `Ticker` | 
| raising_portfolio | `PortfolioId` | 
| raising_asset | `Ticker` | 
| tiers | `Vec<PriceTier>` | 
| venue_id | `VenueId` | 
| start | `Option<T::Moment>` | 
| end | `Option<T::Moment>` | 
| minimum_investment | `Balance` | 
| fundraiser_name | `FundraiserName` | 

#### Python
```python
call = substrate.compose_call(
    'Sto', 'create_fundraiser', {
    'end': (None, 'u64'),
    'fundraiser_name': 'Bytes',
    'minimum_investment': 'u128',
    'offering_asset': '[u8; 12]',
    'offering_portfolio': {
        'did': '[u8; 32]',
        'kind': {
            'Default': None,
            'User': 'u64',
        },
    },
    'raising_asset': '[u8; 12]',
    'raising_portfolio': {
        'did': '[u8; 32]',
        'kind': {
            'Default': None,
            'User': 'u64',
        },
    },
    'start': (None, 'u64'),
    'tiers': [
        {
            'price': 'u128',
            'total': 'u128',
        },
    ],
    'venue_id': 'u64',
}
)
```

---------
### freeze_fundraiser
Freeze a fundraiser.

* `offering_asset` - Asset to freeze.
* `id` - ID of the fundraiser to freeze.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| offering_asset | `Ticker` | 
| id | `FundraiserId` | 

#### Python
```python
call = substrate.compose_call(
    'Sto', 'freeze_fundraiser', {
    'id': 'u64',
    'offering_asset': '[u8; 12]',
}
)
```

---------
### invest
Invest in a fundraiser.

* `investment_portfolio` - Portfolio that `offering_asset` will be deposited in.
* `funding_portfolio` - Portfolio that will fund the investment.
* `offering_asset` - Asset to invest in.
* `id` - ID of the fundraiser to invest in.
* `purchase_amount` - Amount of `offering_asset` to purchase.
* `max_price` - Maximum price to pay per unit of `offering_asset`, If `None`there are no constraints on price.
* `receipt` - Off-chain receipt to use instead of on-chain balance in `funding_portfolio`.

\# Permissions
* Portfolio
#### Attributes
| Name | Type |
| -------- | -------- | 
| investment_portfolio | `PortfolioId` | 
| funding_portfolio | `PortfolioId` | 
| offering_asset | `Ticker` | 
| id | `FundraiserId` | 
| purchase_amount | `Balance` | 
| max_price | `Option<Balance>` | 
| receipt | `Option<ReceiptDetails<T::AccountId, T::OffChainSignature>>` | 

#### Python
```python
call = substrate.compose_call(
    'Sto', 'invest', {
    'funding_portfolio': {
        'did': '[u8; 32]',
        'kind': {
            'Default': None,
            'User': 'u64',
        },
    },
    'id': 'u64',
    'investment_portfolio': {
        'did': '[u8; 32]',
        'kind': {
            'Default': None,
            'User': 'u64',
        },
    },
    'max_price': (None, 'u128'),
    'offering_asset': '[u8; 12]',
    'purchase_amount': 'u128',
    'receipt': (
        None,
        {
            'instruction_id': 'u64',
            'leg_id': 'u64',
            'metadata': (
                None,
                '[u8; 32]',
            ),
            'signature': {
                'Ecdsa': '[u8; 65]',
                'Ed25519': '[u8; 64]',
                'Sr25519': '[u8; 64]',
            },
            'signer': 'AccountId',
            'uid': 'u64',
        },
    ),
}
)
```

---------
### modify_fundraiser_window
Modify the time window a fundraiser is active

* `offering_asset` - Asset to modify.
* `id` - ID of the fundraiser to modify.
* `start` - New start of the fundraiser.
* `end` - New end of the fundraiser to modify.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| offering_asset | `Ticker` | 
| id | `FundraiserId` | 
| start | `T::Moment` | 
| end | `Option<T::Moment>` | 

#### Python
```python
call = substrate.compose_call(
    'Sto', 'modify_fundraiser_window', {
    'end': (None, 'u64'),
    'id': 'u64',
    'offering_asset': '[u8; 12]',
    'start': 'u64',
}
)
```

---------
### stop
Stop a fundraiser.

* `offering_asset` - Asset to stop.
* `id` - ID of the fundraiser to stop.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| offering_asset | `Ticker` | 
| id | `FundraiserId` | 

#### Python
```python
call = substrate.compose_call(
    'Sto', 'stop', {
    'id': 'u64',
    'offering_asset': '[u8; 12]',
}
)
```

---------
### unfreeze_fundraiser
Unfreeze a fundraiser.

* `offering_asset` - Asset to unfreeze.
* `id` - ID of the fundraiser to unfreeze.

\# Permissions
* Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| offering_asset | `Ticker` | 
| id | `FundraiserId` | 

#### Python
```python
call = substrate.compose_call(
    'Sto', 'unfreeze_fundraiser', {
    'id': 'u64',
    'offering_asset': '[u8; 12]',
}
)
```

---------
## Events

---------
### FundraiserClosed
A fundraiser has been stopped.
(Agent DID, fundraiser id)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `FundraiserId` | ```u64```

---------
### FundraiserCreated
A new fundraiser has been created.
(Agent DID, fundraiser id, fundraiser name, fundraiser details)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `FundraiserId` | ```u64```
| None | `FundraiserName` | ```Bytes```
| None | `Fundraiser<Moment>` | ```{'creator': '[u8; 32]', 'offering_portfolio': {'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}, 'offering_asset': '[u8; 12]', 'raising_portfolio': {'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}, 'raising_asset': '[u8; 12]', 'tiers': [{'total': 'u128', 'price': 'u128', 'remaining': 'u128'}], 'venue_id': 'u64', 'start': 'u64', 'end': (None, 'u64'), 'status': ('Live', 'Frozen', 'Closed', 'ClosedEarly'), 'minimum_investment': 'u128'}```

---------
### FundraiserFrozen
A fundraiser has been frozen.
(Agent DID, fundraiser id)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `FundraiserId` | ```u64```

---------
### FundraiserUnfrozen
A fundraiser has been unfrozen.
(Agent DID, fundraiser id)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `FundraiserId` | ```u64```

---------
### FundraiserWindowModified
A fundraiser window has been modified.
(Agent DID, fundraiser id, old_start, old_end, new_start, new_end)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EventDid` | ```[u8; 32]```
| None | `FundraiserId` | ```u64```
| None | `Moment` | ```u64```
| None | `Option<Moment>` | ```(None, 'u64')```
| None | `Moment` | ```u64```
| None | `Option<Moment>` | ```(None, 'u64')```

---------
### Invested
An investor invested in the fundraiser.
(Investor, fundraiser_id, offering token, raise token, offering_token_amount, raise_token_amount)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `FundraiserId` | ```u64```
| None | `Ticker` | ```[u8; 12]```
| None | `Ticker` | ```[u8; 12]```
| None | `Balance` | ```u128```
| None | `Balance` | ```u128```

---------
## Storage functions

---------
### FundraiserCount
 Total fundraisers created for a token.

#### Python
```python
result = substrate.query(
    'Sto', 'FundraiserCount', ['[u8; 12]']
)
```

#### Return value
```python
'u64'
```
---------
### FundraiserNames
 Name for the Fundraiser. Only used offchain.
 (ticker, fundraiser_id) -&gt; Fundraiser name

#### Python
```python
result = substrate.query(
    'Sto', 'FundraiserNames', ['[u8; 12]', 'u64']
)
```

#### Return value
```python
'Bytes'
```
---------
### Fundraisers
 All fundraisers that are currently running.
 (ticker, fundraiser_id) -&gt; Fundraiser

#### Python
```python
result = substrate.query(
    'Sto', 'Fundraisers', ['[u8; 12]', 'u64']
)
```

#### Return value
```python
{
    'creator': '[u8; 32]',
    'end': (None, 'u64'),
    'minimum_investment': 'u128',
    'offering_asset': '[u8; 12]',
    'offering_portfolio': {
        'did': '[u8; 32]',
        'kind': {'Default': None, 'User': 'u64'},
    },
    'raising_asset': '[u8; 12]',
    'raising_portfolio': {
        'did': '[u8; 32]',
        'kind': {'Default': None, 'User': 'u64'},
    },
    'start': 'u64',
    'status': ('Live', 'Frozen', 'Closed', 'ClosedEarly'),
    'tiers': [{'price': 'u128', 'remaining': 'u128', 'total': 'u128'}],
    'venue_id': 'u64',
}
```
---------
## Errors

---------
### FundraiserClosed
Fundraiser has been closed/stopped already.

---------
### FundraiserExpired
Interacting with a fundraiser past the end `Moment`.

---------
### FundraiserNotFound
Fundraiser not found.

---------
### FundraiserNotLive
Fundraiser is either frozen or stopped.

---------
### InsufficientTokensRemaining
Not enough tokens left for sale.

---------
### InvalidOfferingWindow
Window (start time, end time) has invalid parameters, e.g start time is after end time.

---------
### InvalidPriceTiers
An individual price tier was invalid or a set of price tiers was invalid.

---------
### InvalidVenue
An invalid venue provided.

---------
### InvestmentAmountTooLow
Investment amount is lower than minimum investment amount.

---------
### MaxPriceExceeded
Price of the investment exceeded the max price.

---------
### Overflow
An arithmetic operation overflowed.

---------
### Unauthorized
Sender does not have required permissions.

---------