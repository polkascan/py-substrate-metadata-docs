
# ImbueBriefs

---------
## Calls

---------
### cancel_brief
Extrinsic to cancel a brief
#### Attributes
| Name | Type |
| -------- | -------- | 
| brief_id | `BriefHash` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueBriefs', 'cancel_brief', {'brief_id': '[u8; 32]'}
)
```

---------
### commence_work
Once the freelancer is happy with both the milestones and the offering this can be called.
#### Attributes
| Name | Type |
| -------- | -------- | 
| brief_id | `BriefHash` | 

#### Python
```python
call = substrate.compose_call(
    'ImbueBriefs', 'commence_work', {'brief_id': '[u8; 32]'}
)
```

---------
### contribute_to_brief
Add a bounty to a brief.
A bounty must be fully contributed to before a piece of work is started.

TODO: runtime api to return how much bounty exactly is left on a brief.
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
    'brief_id': '[u8; 32]',
}
)
```

---------
### create_brief
Create a brief to be funded or amended.
In the current state the applicant must be approved.
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

#### Python
```python
call = substrate.compose_call(
    'ImbueBriefs', 'create_brief', {
    'applicant': 'AccountId',
    'brief_id': '[u8; 32]',
    'brief_owners': ['AccountId'],
    'budget': 'u128',
    'currency_id': {
        'AUSD': None,
        'ForeignAsset': 'u32',
        'KAR': None,
        'KSM': None,
        'MGX': None,
        'Native': None,
    },
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
| None | `BriefHash` | ```[u8; 32]```

---------
### BriefContribution
A brief has been contributed to.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BriefHash` | ```[u8; 32]```

---------
### BriefEvolution
A brief has been converted to milestones.
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `BriefHash` | ```[u8; 32]```

---------
### BriefSubmitted
A brief has been successfully submitted!
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```
| None | `BriefHash` | ```[u8; 32]```

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
    'ImbueBriefs', 'BriefContributions', ['[u8; 32]']
)
```

#### Return value
```python
'scale_info::459'
```
---------
### Briefs

#### Python
```python
result = substrate.query(
    'ImbueBriefs', 'Briefs', ['[u8; 32]']
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
        'ForeignAsset': 'u32',
        'KAR': None,
        'KSM': None,
        'MGX': None,
        'Native': None,
    },
    'deposit_id': 'u64',
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
### StorageVersion

#### Python
```python
result = substrate.query(
    'ImbueBriefs', 'StorageVersion', []
)
```

#### Return value
```python
('V0', 'V1')
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
### DepositBelowMinimum
The deposit you have sent is below the minimum requirement.

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