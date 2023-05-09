
# CarbonCredits

---------
## Calls

---------
### add_batch_group
Add a new batch group to the project
Can only be called by the ProjectOwner
#### Attributes
| Name | Type |
| -------- | -------- | 
| project_id | `T::ProjectId` | 
| batch_group | `BatchGroupOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CarbonCredits', 'add_batch_group', {
    'batch_group': {
        'asset_id': 'u32',
        'batches': [
            {
                'end_date': 'u16',
                'issuance_year': 'u16',
                'minted': 'u128',
                'name': 'Bytes',
                'retired': 'u128',
                'start_date': 'u16',
                'total_supply': 'u128',
                'uuid': 'Bytes',
            },
        ],
        'minted': 'u128',
        'name': 'Bytes',
        'retired': 'u128',
        'total_supply': 'u128',
        'uuid': 'Bytes',
    },
    'project_id': 'u32',
}
)
```

---------
### approve_project
Set the project status to approve/reject
#### Attributes
| Name | Type |
| -------- | -------- | 
| project_id | `T::ProjectId` | 
| is_approved | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'CarbonCredits', 'approve_project', {
    'is_approved': 'bool',
    'project_id': 'u32',
}
)
```

---------
### create
Register a new project onchain
This new project can mint tokens after approval from an authorised account
#### Attributes
| Name | Type |
| -------- | -------- | 
| params | `ProjectCreateParams<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CarbonCredits', 'create', {
    'params': {
        'batch_groups': [
            {
                'asset_id': 'u32',
                'batches': [
                    {
                        'end_date': 'u16',
                        'issuance_year': 'u16',
                        'minted': 'u128',
                        'name': 'Bytes',
                        'retired': 'u128',
                        'start_date': 'u16',
                        'total_supply': 'u128',
                        'uuid': 'Bytes',
                    },
                ],
                'minted': 'u128',
                'name': 'Bytes',
                'retired': 'u128',
                'total_supply': 'u128',
                'uuid': 'Bytes',
            },
        ],
        'description': 'Bytes',
        'documents': ['Bytes'],
        'images': ['Bytes'],
        'location': 'Bytes',
        'name': 'Bytes',
        'registry_details': [
            {
                'id': 'Bytes',
                'name': 'Bytes',
                'reg_name': (
                    'Verra',
                    'GoldStandard',
                    'AmericanCarbonRegistry',
                    'ClimateActionReserve',
                ),
                'summary': 'Bytes',
            },
        ],
        'royalties': (
            None,
            [
                {
                    'account_id': 'AccountId',
                    'percent_of_fees': 'u8',
                },
            ],
        ),
        'sdg_details': [
            {
                'description': 'Bytes',
                'references': 'Bytes',
                'sdg_type': (
                    'NoPoverty',
                    'ZeroHunger',
                    'GoodHealthAndWellBeing',
                    'QualityEducation',
                    'GenderEquality',
                    'CleanWaterAndSanitation',
                    'AffordableAndCleanEnergy',
                    'DecentWorkAndEconomicGrowth',
                    'IndustryInnovationAndInfrastructure',
                    'ReducedInequalities',
                    'SustainableCitiesAndCommunities',
                    'ResponsibleConsumptionAndProduction',
                    'ClimateAction',
                    'LifeBelowWater',
                    'LifeOnLand',
                    'PeaceJusticeAndStrongInstitutions',
                    'ParternshipsForTheGoals',
                ),
            },
        ],
        'videos': ['Bytes'],
    },
}
)
```

---------
### force_add_authorized_account
Add a new account to the list of authorised Accounts
The caller must be from a permitted origin
#### Attributes
| Name | Type |
| -------- | -------- | 
| account_id | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'CarbonCredits', 'force_add_authorized_account', {'account_id': 'AccountId'}
)
```

---------
### force_approve_and_mint_credits
Single function to approve project and mint credits
Can only be called by ForceOrigin
#### Attributes
| Name | Type |
| -------- | -------- | 
| sender | `T::AccountId` | 
| project_id | `T::ProjectId` | 
| amount_to_mint | `T::Balance` | 
| list_to_marketplace | `bool` | 
| group_id | `T::GroupId` | 

#### Python
```python
call = substrate.compose_call(
    'CarbonCredits', 'force_approve_and_mint_credits', {
    'amount_to_mint': 'u128',
    'group_id': 'u32',
    'list_to_marketplace': 'bool',
    'project_id': 'u32',
    'sender': 'AccountId',
}
)
```

---------
### force_remove_authorized_account
Remove an account from the list of authorised accounts
#### Attributes
| Name | Type |
| -------- | -------- | 
| account_id | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'CarbonCredits', 'force_remove_authorized_account', {'account_id': 'AccountId'}
)
```

---------
### force_remove_project
Force remove an project asset from storage, can be used by ForceOrigin to remove
unapproved projects Can only be called by ForceOrigin
#### Attributes
| Name | Type |
| -------- | -------- | 
| project_id | `T::ProjectId` | 

#### Python
```python
call = substrate.compose_call(
    'CarbonCredits', 'force_remove_project', {'project_id': 'u32'}
)
```

---------
### force_set_next_asset_id
Force modify NextAssetId storage
Can only be called by ForceOrigin
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 

#### Python
```python
call = substrate.compose_call(
    'CarbonCredits', 'force_set_next_asset_id', {'asset_id': 'u32'}
)
```

---------
### force_set_next_item_id
Force modify NextItemId storage
Can only be called by ForceOrigin
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| item_id | `T::ItemId` | 

#### Python
```python
call = substrate.compose_call(
    'CarbonCredits', 'force_set_next_item_id', {'asset_id': 'u32', 'item_id': 'u32'}
)
```

---------
### force_set_project_storage
Force modify a project storage
Can only be called by ForceOrigin
#### Attributes
| Name | Type |
| -------- | -------- | 
| project_id | `T::ProjectId` | 
| detail | `ProjectDetail<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CarbonCredits', 'force_set_project_storage', {
    'detail': {
        'approved': 'bool',
        'batch_groups': 'scale_info::319',
        'created': 'u32',
        'description': 'Bytes',
        'documents': ['Bytes'],
        'images': ['Bytes'],
        'location': 'Bytes',
        'name': 'Bytes',
        'originator': 'AccountId',
        'registry_details': [
            {
                'id': 'Bytes',
                'name': 'Bytes',
                'reg_name': (
                    'Verra',
                    'GoldStandard',
                    'AmericanCarbonRegistry',
                    'ClimateActionReserve',
                ),
                'summary': 'Bytes',
            },
        ],
        'royalties': (
            None,
            [
                {
                    'account_id': 'AccountId',
                    'percent_of_fees': 'u8',
                },
            ],
        ),
        'sdg_details': [
            {
                'description': 'Bytes',
                'references': 'Bytes',
                'sdg_type': (
                    'NoPoverty',
                    'ZeroHunger',
                    'GoodHealthAndWellBeing',
                    'QualityEducation',
                    'GenderEquality',
                    'CleanWaterAndSanitation',
                    'AffordableAndCleanEnergy',
                    'DecentWorkAndEconomicGrowth',
                    'IndustryInnovationAndInfrastructure',
                    'ReducedInequalities',
                    'SustainableCitiesAndCommunities',
                    'ResponsibleConsumptionAndProduction',
                    'ClimateAction',
                    'LifeBelowWater',
                    'LifeOnLand',
                    'PeaceJusticeAndStrongInstitutions',
                    'ParternshipsForTheGoals',
                ),
            },
        ],
        'updated': (None, 'u32'),
        'videos': ['Bytes'],
    },
    'project_id': 'u32',
}
)
```

---------
### force_set_retired_carbon_credit
Force modify retired CarbonCredits storage
Can only be called by ForceOrigin
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset_id | `T::AssetId` | 
| item_id | `T::ItemId` | 
| credits_data | `RetiredCarbonCreditsData<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CarbonCredits', 'force_set_retired_carbon_credit', {
    'asset_id': 'u32',
    'credits_data': {
        'account': 'AccountId',
        'count': 'u128',
        'retire_data': [
            {
                'count': 'u128',
                'issuance_year': 'u16',
                'name': 'Bytes',
                'uuid': 'Bytes',
            },
        ],
        'timestamp': 'u32',
    },
    'item_id': 'u32',
}
)
```

---------
### mint
Mint tokens for an approved project
The tokens are always minted in the ascending order of credits, for example, if the
`amount_to_mint` is 150 and the project has 100 tokens of 2019 and 2020 year. Then we
mint 100 from 2019 and 50 from 2020.
#### Attributes
| Name | Type |
| -------- | -------- | 
| project_id | `T::ProjectId` | 
| group_id | `T::GroupId` | 
| amount_to_mint | `T::Balance` | 
| list_to_marketplace | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'CarbonCredits', 'mint', {
    'amount_to_mint': 'u128',
    'group_id': 'u32',
    'list_to_marketplace': 'bool',
    'project_id': 'u32',
}
)
```

---------
### resubmit
Resubmit a approval rejected project data onchain
An approved project data cannot be resubmitted
#### Attributes
| Name | Type |
| -------- | -------- | 
| project_id | `T::ProjectId` | 
| params | `ProjectCreateParams<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CarbonCredits', 'resubmit', {
    'params': {
        'batch_groups': [
            {
                'asset_id': 'u32',
                'batches': [
                    {
                        'end_date': 'u16',
                        'issuance_year': 'u16',
                        'minted': 'u128',
                        'name': 'Bytes',
                        'retired': 'u128',
                        'start_date': 'u16',
                        'total_supply': 'u128',
                        'uuid': 'Bytes',
                    },
                ],
                'minted': 'u128',
                'name': 'Bytes',
                'retired': 'u128',
                'total_supply': 'u128',
                'uuid': 'Bytes',
            },
        ],
        'description': 'Bytes',
        'documents': ['Bytes'],
        'images': ['Bytes'],
        'location': 'Bytes',
        'name': 'Bytes',
        'registry_details': [
            {
                'id': 'Bytes',
                'name': 'Bytes',
                'reg_name': (
                    'Verra',
                    'GoldStandard',
                    'AmericanCarbonRegistry',
                    'ClimateActionReserve',
                ),
                'summary': 'Bytes',
            },
        ],
        'royalties': (
            None,
            [
                {
                    'account_id': 'AccountId',
                    'percent_of_fees': 'u8',
                },
            ],
        ),
        'sdg_details': [
            {
                'description': 'Bytes',
                'references': 'Bytes',
                'sdg_type': (
                    'NoPoverty',
                    'ZeroHunger',
                    'GoodHealthAndWellBeing',
                    'QualityEducation',
                    'GenderEquality',
                    'CleanWaterAndSanitation',
                    'AffordableAndCleanEnergy',
                    'DecentWorkAndEconomicGrowth',
                    'IndustryInnovationAndInfrastructure',
                    'ReducedInequalities',
                    'SustainableCitiesAndCommunities',
                    'ResponsibleConsumptionAndProduction',
                    'ClimateAction',
                    'LifeBelowWater',
                    'LifeOnLand',
                    'PeaceJusticeAndStrongInstitutions',
                    'ParternshipsForTheGoals',
                ),
            },
        ],
        'videos': ['Bytes'],
    },
    'project_id': 'u32',
}
)
```

---------
### retire
Retire existing credits from owner
The tokens are always retired in the ascending order of credits, for example, if the
`amount` is 150 and the project has 100 tokens of 2019 and 2020 year. Then we retire
100 from 2019 and 50 from 2020.
#### Attributes
| Name | Type |
| -------- | -------- | 
| project_id | `T::ProjectId` | 
| group_id | `T::GroupId` | 
| amount | `T::Balance` | 

#### Python
```python
call = substrate.compose_call(
    'CarbonCredits', 'retire', {
    'amount': 'u128',
    'group_id': 'u32',
    'project_id': 'u32',
}
)
```

---------
### update_project_details
Modify the details of an approved project
Can only be called by the ProjectOwner
#### Attributes
| Name | Type |
| -------- | -------- | 
| project_id | `T::ProjectId` | 
| params | `ProjectCreateParams<T>` | 

#### Python
```python
call = substrate.compose_call(
    'CarbonCredits', 'update_project_details', {
    'params': {
        'batch_groups': [
            {
                'asset_id': 'u32',
                'batches': [
                    {
                        'end_date': 'u16',
                        'issuance_year': 'u16',
                        'minted': 'u128',
                        'name': 'Bytes',
                        'retired': 'u128',
                        'start_date': 'u16',
                        'total_supply': 'u128',
                        'uuid': 'Bytes',
                    },
                ],
                'minted': 'u128',
                'name': 'Bytes',
                'retired': 'u128',
                'total_supply': 'u128',
                'uuid': 'Bytes',
            },
        ],
        'description': 'Bytes',
        'documents': ['Bytes'],
        'images': ['Bytes'],
        'location': 'Bytes',
        'name': 'Bytes',
        'registry_details': [
            {
                'id': 'Bytes',
                'name': 'Bytes',
                'reg_name': (
                    'Verra',
                    'GoldStandard',
                    'AmericanCarbonRegistry',
                    'ClimateActionReserve',
                ),
                'summary': 'Bytes',
            },
        ],
        'royalties': (
            None,
            [
                {
                    'account_id': 'AccountId',
                    'percent_of_fees': 'u8',
                },
            ],
        ),
        'sdg_details': [
            {
                'description': 'Bytes',
                'references': 'Bytes',
                'sdg_type': (
                    'NoPoverty',
                    'ZeroHunger',
                    'GoodHealthAndWellBeing',
                    'QualityEducation',
                    'GenderEquality',
                    'CleanWaterAndSanitation',
                    'AffordableAndCleanEnergy',
                    'DecentWorkAndEconomicGrowth',
                    'IndustryInnovationAndInfrastructure',
                    'ReducedInequalities',
                    'SustainableCitiesAndCommunities',
                    'ResponsibleConsumptionAndProduction',
                    'ClimateAction',
                    'LifeBelowWater',
                    'LifeOnLand',
                    'PeaceJusticeAndStrongInstitutions',
                    'ParternshipsForTheGoals',
                ),
            },
        ],
        'videos': ['Bytes'],
    },
    'project_id': 'u32',
}
)
```

---------
## Events

---------
### AuthorizedAccountAdded
A new AuthorizedAccount has been added
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```

---------
### AuthorizedAccountRemoved
An AuthorizedAccount has been removed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| account_id | `T::AccountId` | ```AccountId```

---------
### BatchGroupAdded
A new batch group was added to the project
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| project_id | `T::ProjectId` | ```u32```
| group_id | `T::GroupId` | ```u32```

---------
### CarbonCreditMinted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| project_id | `T::ProjectId` | ```u32```
| group_id | `T::GroupId` | ```u32```
| recipient | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```

---------
### CarbonCreditRetired
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| project_id | `T::ProjectId` | ```u32```
| group_id | `T::GroupId` | ```u32```
| asset_id | `T::AssetId` | ```u32```
| account | `T::AccountId` | ```AccountId```
| amount | `T::Balance` | ```u128```
| retire_data | `BatchRetireDataList<T>` | ```[{'name': 'Bytes', 'uuid': 'Bytes', 'issuance_year': 'u16', 'count': 'u128'}]```

---------
### ProjectApproved
Project has been approved
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| project_id | `T::ProjectId` | ```u32```
| asset_ids | `Vec<T::AssetId>` | ```['u32']```

---------
### ProjectCreated
A new CarbonCredits has been created
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| project_id | `T::ProjectId` | ```u32```

---------
### ProjectRejected
Project has been rejected
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| project_id | `T::ProjectId` | ```u32```

---------
### ProjectResubmitted
A project details has been resubmitted
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| project_id | `T::ProjectId` | ```u32```

---------
### ProjectUpdated
A project details has been updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| project_id | `T::ProjectId` | ```u32```

---------
## Storage functions

---------
### AssetIdLookup
 AssetId details for project/group

#### Python
```python
result = substrate.query(
    'CarbonCredits', 'AssetIdLookup', ['u32']
)
```

#### Return value
```python
('u32', 'u32')
```
---------
### AuthorizedAccounts

#### Python
```python
result = substrate.query(
    'CarbonCredits', 'AuthorizedAccounts', []
)
```

#### Return value
```python
['AccountId']
```
---------
### NextAssetId

#### Python
```python
result = substrate.query(
    'CarbonCredits', 'NextAssetId', []
)
```

#### Return value
```python
'u32'
```
---------
### NextItemId

#### Python
```python
result = substrate.query(
    'CarbonCredits', 'NextItemId', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### NextProjectId

#### Python
```python
result = substrate.query(
    'CarbonCredits', 'NextProjectId', []
)
```

#### Return value
```python
'u32'
```
---------
### Projects
 The details of a CarbonCredits

#### Python
```python
result = substrate.query(
    'CarbonCredits', 'Projects', ['u32']
)
```

#### Return value
```python
{
    'approved': 'bool',
    'batch_groups': 'scale_info::319',
    'created': 'u32',
    'description': 'Bytes',
    'documents': ['Bytes'],
    'images': ['Bytes'],
    'location': 'Bytes',
    'name': 'Bytes',
    'originator': 'AccountId',
    'registry_details': [
        {
            'id': 'Bytes',
            'name': 'Bytes',
            'reg_name': (
                'Verra',
                'GoldStandard',
                'AmericanCarbonRegistry',
                'ClimateActionReserve',
            ),
            'summary': 'Bytes',
        },
    ],
    'royalties': (None, [{'account_id': 'AccountId', 'percent_of_fees': 'u8'}]),
    'sdg_details': [
        {
            'description': 'Bytes',
            'references': 'Bytes',
            'sdg_type': (
                'NoPoverty',
                'ZeroHunger',
                'GoodHealthAndWellBeing',
                'QualityEducation',
                'GenderEquality',
                'CleanWaterAndSanitation',
                'AffordableAndCleanEnergy',
                'DecentWorkAndEconomicGrowth',
                'IndustryInnovationAndInfrastructure',
                'ReducedInequalities',
                'SustainableCitiesAndCommunities',
                'ResponsibleConsumptionAndProduction',
                'ClimateAction',
                'LifeBelowWater',
                'LifeOnLand',
                'PeaceJusticeAndStrongInstitutions',
                'ParternshipsForTheGoals',
            ),
        },
    ],
    'updated': (None, 'u32'),
    'videos': ['Bytes'],
}
```
---------
### RetiredCredits
 The retired CarbonCredits record

#### Python
```python
result = substrate.query(
    'CarbonCredits', 'RetiredCredits', ['u32', 'u32']
)
```

#### Return value
```python
{
    'account': 'AccountId',
    'count': 'u128',
    'retire_data': [
        {
            'count': 'u128',
            'issuance_year': 'u16',
            'name': 'Bytes',
            'uuid': 'Bytes',
        },
    ],
    'timestamp': 'u32',
}
```
---------
## Constants

---------
### PalletId
 The CarbonCredits pallet id
#### Value
```python
'0x626974672f766375'
```
#### Python
```python
constant = substrate.get_constant('CarbonCredits', 'PalletId')
```
---------
## Errors

---------
### AmountGreaterThanSupply
The Amount of CarbonCredits units is greater than supply

---------
### AuthorizedAccountAlreadyExists
Cannot add a duplicate authorised account

---------
### CannotCreateProjectWithoutCredits
The project cannot be created without credits

---------
### CannotGenerateAssetId
Cannot generate asset id

---------
### CannotModifyApprovedProject
Cannot resubmit an approved project

---------
### CannotUpdateUnapprovedProject
Can only update an approved project, use resubmit for rejected projects

---------
### GroupNotFound
the group does not exist

---------
### KYCAuthorisationFailed
Account failed KYC checks

---------
### NotAuthorised
The account is not authorised

---------
### Overflow
Calculcation triggered an Overflow

---------
### ProjectAlreadyExists
Cannot create duplicate Projects

---------
### ProjectIdLowerThanPermitted
ProjectId is lower than permitted

---------
### ProjectNotApproved
The project is not approved

---------
### ProjectNotFound
The given Project was not found in storage

---------
### SupplyAmountMismatch
The token accounting generated an error

---------
### TooManyAuthorizedAccounts
Adding a new authorized account failed

---------
### TooManyGroups
group max exceeded

---------
### UnitPriceIsZero
The unit price for CarbonCredits cannot be zero

---------