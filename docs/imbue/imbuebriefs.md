
# ImbueBriefs

---------
## Calls

---------
### cancel_brief
See [`Pallet::cancel_brief`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| brief_id | `BriefHash` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueBriefs', 'cancel_brief', {'brief_id': 'scale_info::12'}
)
```

---------
### commence_work
See [`Pallet::commence_work`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| brief_id | `BriefHash` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueBriefs', 'commence_work', {'brief_id': 'scale_info::12'}
)
```

---------
### contribute_to_brief
See [`Pallet::contribute_to_brief`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| brief_id | `BriefHash` | 
| amount | `BalanceOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueBriefs', 'contribute_to_brief', {
    'amount': 'u128',
    'brief_id': 'scale_info::12',
}
)
```

---------
### create_brief
See [`Pallet::create_brief`].
#### Attributes
| Name | Type |
| -------- | -------- | 
| brief_owners | `BoundedBriefOwners<T>` | 
| applicant | `AccountIdOf<T>` | 
| budget | `BalanceOf<T>` | 
| initial_contribution | `BalanceOf<T>` | 
| brief_id | `BriefHash` | 
| currency_id | `CurrencyId` | 
| milestones | `BoundedProposedMilestones<T>` | 
| external_owned_address | `Option<common_types::ForeignOwnedAccount>` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueBriefs', 'create_brief', {
    'applicant': 'AccountId',
    'brief_id': 'scale_info::12',
    'brief_owners': ['AccountId'],
    'budget': 'u128',
    'currency_id': {
        'AUSD': None,
        'ForeignAsset': (
            'ETH',
            'USDT',
        ),
        'KAR': None,
        'KSM': None,
        'MGX': None,
        'Native': None,
    },
    'external_owned_address': (
        None,
        {
            'ETH': '[u8; 20]',
            'TRON': '[u8; 22]',
        },
    ),
    'initial_contribution': 'u128',
    'milestones': [
        {'percentage_to_unlock': 'u8'},
    ],
}
)
```

---------
## Events

---------
### AccountApproved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `AccountIdOf<T>` | ```AccountId```

---------
### BriefCanceled
A brief has been cancelled.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BriefHash` | ```scale_info::12```

---------
### BriefContribution
A brief has been contributed to.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BriefHash` | ```scale_info::12```

---------
### BriefEvolution
A brief has been converted to milestones.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BriefHash` | ```scale_info::12```

---------
### BriefSubmitted
A brief has been successfully submitted!
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BriefHash` | ```scale_info::12```

---------
## Storage functions

---------
### BriefContributions
 The contributions to a brief, in a single currency.
 It&#x27;s in a BTree to reduce storage call when we have to inevitably iterate the keys.
 Key 1: BriefHash
 Key 2: AccountIdOf&lt;T&gt;
 Value: Balance

#### Python
```python
result = substrate.query(
    'ImbueBriefs', 'BriefContributions', ['scale_info::12']
)
```

#### Return value
```python
'scale_info::491'
```
---------
### Briefs

#### Python
```python
result = substrate.query(
    'ImbueBriefs', 'Briefs', ['scale_info::12']
)
```

#### Return value
```python
{
    'applicant': 'AccountId',
    'brief_owners': ['AccountId'],
    'budget': 'u128',
    'created_at': 'u32',
    'currency_id': {
        'AUSD': None,
        'ForeignAsset': ('ETH', 'USDT'),
        'KAR': None,
        'KSM': None,
        'MGX': None,
        'Native': None,
    },
    'deposit_id': 'u64',
    'eoa': (None, {'ETH': '[u8; 20]', 'TRON': '[u8; 22]'}),
    'milestones': [{'percentage_to_unlock': 'u8'}],
}
```
---------
### CounterForBriefs
Counter for the related counted storage map

#### Python
```python
result = substrate.query(
    'ImbueBriefs', 'CounterForBriefs', []
)
```

#### Return value
```python
'u32'
```
---------
## Errors

---------
### BountyBelowMinimum
The bounty you have set is below the minimum requirement.

---------
### BountyTotalNotMet
The bounty required for this brief has not been met.

---------
### BriefAlreadyExists
Brief already exists in the block, please don&\#x27;t submit duplicates.

---------
### BriefCurrencyNotSet
Currency must be set to add to a bounty.

---------
### BriefHashingFailed
The BriefId generation failed.

---------
### BriefLimitReached
There are too many briefs open for this block, try again later.

---------
### BriefNotFound
Brief not found.

---------
### ContributionMoreThanBounty
The contribution you have sent is more than the bounty total.

---------
### CurrencyAccountComboNotSupported
Currency is not supported for this external address.

---------
### DepositBelowMinimum
The deposit you have sent is below the minimum requirement.

---------
### EoaRequiredForForeignCurrencies
If youre using a foreign currency then you need an external_owned_address.

---------
### FreelancerApprovalRequired
The brief has not yet been approved to commence by the freelancer.

---------
### MilestonesTotalPercentageMustEqual100
Milestones total do not add up to 100%.

---------
### MustBeApplicant
You must be the brief applicant to do this.

---------
### MustBeBriefOwner
You must be a brief owner to do this.

---------
### OnlyApprovedAccountPermitted
Only approved account can apply for briefs.

---------
### TooManyBriefOwners
Too many brief owners.

---------
### TooManyMilestones
too many milestones here mate fixed with https://github.com/ImbueNetwork/imbue/issues/267

---------