
# BondedFinance

---------
## Calls

---------
### bond
Bond to an offer.

The issuer should provide the number of contracts they are willing to buy.
Once there are no more contracts available on the offer, the `stake` put by the
offer creator is refunded.

The dispatch origin for this call must be _Signed_ and the sender must have the
appropriate funds to buy the desired number of contracts.

Allows the issuer to ask for their account to be kept alive using the `keep_alive`
parameter.

Emits a `NewBond`.
Possibly Emits a `OfferCompleted`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| offer_id | `T::BondOfferId` | 
| nb_of_bonds | `BalanceOf<T>` | 
| keep_alive | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'BondedFinance', 'bond', {
    'keep_alive': 'bool',
    'nb_of_bonds': 'u128',
    'offer_id': 'u128',
}
)
```

---------
### cancel
Cancel a running offer.

Blocking further bonds but not cancelling the currently vested rewards. The `stake` put
by the offer creator is refunded.

The dispatch origin for this call must be _Signed_ and the sender must be `AdminOrigin`

Emits a `OfferCancelled`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| offer_id | `T::BondOfferId` | 

#### Python
```python
call = substrate.compose_call(
    'BondedFinance', 'cancel', {'offer_id': 'u128'}
)
```

---------
### offer
Create a new bond offer. To be `bond` to later.

The dispatch origin for this call must be _Signed_ and the sender must have the
appropriate funds to stake the offer.

Allows the issuer to ask for their account to be kept alive using the `keep_alive`
parameter.

Emits a `NewOffer`.
#### Attributes
| Name | Type |
| -------- | -------- | 
| offer | `Validated<BondOfferOf<T>, ValidBondOffer<T::MinReward,<T::Vesting
as VestedTransfer>::MinVestedTransfer>,>` | 
| keep_alive | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'BondedFinance', 'offer', {
    'keep_alive': 'bool',
    'offer': {
        'asset': 'u128',
        'beneficiary': 'AccountId',
        'bond_price': 'u128',
        'maturity': {
            'Finite': {
                'return_in': 'u32',
            },
            'Infinite': None,
        },
        'nb_of_bonds': 'u128',
        'reward': {
            'amount': 'u128',
            'asset': 'u128',
            'maturity': 'u32',
        },
    },
}
)
```

---------
## Events

---------
### NewBond
A new bond has been registered.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| offer_id | `T::BondOfferId` | ```u128```
| who | `AccountIdOf<T>` | ```AccountId```
| nb_of_bonds | `BalanceOf<T>` | ```u128```

---------
### NewOffer
A new offer has been created.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| offer_id | `T::BondOfferId` | ```u128```
| beneficiary | `AccountIdOf<T>` | ```AccountId```

---------
### OfferCancelled
An offer has been cancelled by the `AdminOrigin`.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| offer_id | `T::BondOfferId` | ```u128```

---------
### OfferCompleted
An offer has been completed.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| offer_id | `T::BondOfferId` | ```u128```

---------
## Storage functions

---------
### BondOfferCount
 The counter used to uniquely identify bond offers within this pallet.

#### Python
```python
result = substrate.query(
    'BondedFinance', 'BondOfferCount', []
)
```

#### Return value
```python
'u128'
```
---------
### BondOffers
 A mapping from offer ID to the pair: (issuer, offer)

#### Python
```python
result = substrate.query(
    'BondedFinance', 'BondOffers', ['u128']
)
```

#### Return value
```python
(
    'AccountId',
    {
        'asset': 'u128',
        'beneficiary': 'AccountId',
        'bond_price': 'u128',
        'maturity': {'Finite': {'return_in': 'u32'}, 'Infinite': None},
        'nb_of_bonds': 'u128',
        'reward': {'amount': 'u128', 'asset': 'u128', 'maturity': 'u32'},
    },
)
```
---------
## Constants

---------
### MinReward
 The minimum reward for an offer.

 Must be &gt; T::Vesting::MinVestedTransfer.
#### Value
```python
10000000000000
```
#### Python
```python
constant = substrate.get_constant('BondedFinance', 'MinReward')
```
---------
### PalletId
 The pallet ID, required to create sub-accounts used by offers.
#### Value
```python
'0x626f6e6465646669'
```
#### Python
```python
constant = substrate.get_constant('BondedFinance', 'PalletId')
```
---------
### Stake
 The stake a user has to put to create an offer.
#### Value
```python
10000000000000
```
#### Python
```python
constant = substrate.get_constant('BondedFinance', 'Stake')
```
---------
## Errors

---------
### BondOfferNotFound
The offer could not be found.

---------
### InvalidBondOffer
Someone tried  to submit an invalid offer.

---------
### InvalidNumberOfBonds
Someone tried to bond with an invalid number of nb_of_bonds.

---------
### OfferCompleted
Someone tried to bond an already completed offer.

---------