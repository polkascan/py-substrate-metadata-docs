
# PWNftSale

---------
## Calls

---------
### buy_prime_origin_of_shell
Accounts that have been whitelisted can purchase an Origin of Shell. The only Origin of
Shell type available for this purchase are Prime

Parameters:
- origin: The origin of the extrinsic purchasing the Prime Origin of Shell
- message: OverlordMessage with account and purpose
- signature: The signature of the account that is claiming the spirit.
- race: The race that the user has chosen (limited \# of races)
- career: The career that the user has chosen (unlimited careers)
#### Attributes
| Name | Type |
| -------- | -------- | 
| signature | `sr25519::Signature` | 
| race | `RaceType` | 
| career | `CareerType` | 

#### Python
```python
call = substrate.compose_call(
    'PWNftSale', 'buy_prime_origin_of_shell', {
    'career': (
        'HackerWizard',
        'HardwareDruid',
        'RoboWarrior',
        'TradeNegotiator',
        'Web3Monk',
    ),
    'race': (
        'Cyborg',
        'AISpectre',
        'XGene',
        'Pandroid',
    ),
    'signature': '[u8; 64]',
}
)
```

---------
### buy_rare_origin_of_shell
Buy a rare origin_of_shell of either type Magic or Legendary. Both Rarity Types
will have a set price. These will also be limited in quantity and on a first come, first
serve basis.

Parameters:
- origin: The origin of the extrinsic.
- rarity_type: The type of origin_of_shell to be purchased.
- race: The race of the origin_of_shell chosen by the user.
- career: The career of the origin_of_shell chosen by the user or auto-generated based
  on metadata
#### Attributes
| Name | Type |
| -------- | -------- | 
| rarity_type | `RarityType` | 
| race | `RaceType` | 
| career | `CareerType` | 

#### Python
```python
call = substrate.compose_call(
    'PWNftSale', 'buy_rare_origin_of_shell', {
    'career': (
        'HackerWizard',
        'HardwareDruid',
        'RoboWarrior',
        'TradeNegotiator',
        'Web3Monk',
    ),
    'race': (
        'Cyborg',
        'AISpectre',
        'XGene',
        'Pandroid',
    ),
    'rarity_type': (
        'Prime',
        'Magic',
        'Legendary',
    ),
}
)
```

---------
### claim_spirit
Claim a spirit for any account with at least 10 PHA in their account

Parameters:
- origin: The origin of the extrinsic.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'PWNftSale', 'claim_spirit', {}
)
```

---------
### init_rarity_type_counts
Initialize the settings for the non-whitelist preorder period amount of races &amp;
giveaways available for the Origin of Shell NFTs. This is a privileged function and can
only be executed by the Overlord account. This will call the helper function
`set_initial_origin_of_shell_inventory`

Parameters:
- `origin` - Expected Overlord admin account
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'PWNftSale', 'init_rarity_type_counts', {}
)
```

---------
### initialize_world_clock
Phala World Zero Day is set to begin the tracking of the official time starting at the
current timestamp when `initialize_world_clock` is called by the `Overlord`

Parameters:
`origin`: Expected to be called by `Overlord` admin account
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'PWNftSale', 'initialize_world_clock', {}
)
```

---------
### mint_chosen_preorders
This is an admin only function that will mint the list of `Chosen` preorders and will
mint the Origin of Shell NFT to the preorder owner.

Parameters:
`origin`: Expected to come from Overlord admin account
`preorders`: Vec of Preorder IDs that were `Chosen`
#### Attributes
| Name | Type |
| -------- | -------- | 
| preorders | `Vec<PreorderId>` | 

#### Python
```python
call = substrate.compose_call(
    'PWNftSale', 'mint_chosen_preorders', {'preorders': ['u32']}
)
```

---------
### mint_gift_origin_of_shell
This is an admin only function that will be used to mint either a giveaway or a reserved Origin of Shell NFT

Parameters:
`origin`: Expected to come from Overlord admin account
`owner`: Owner to gift the Origin of Shell to
- rarity_type: The type of origin_of_shell to be gifted.
- `race`: The race of the origin_of_shell chosen by the user.
- `career`: The career of the origin_of_shell chosen by the user or auto-generated based
  on metadata
- `nft_sale_type`: Either a `NftSaleType::Giveaway` or `NftSaleType::Reserved`
#### Attributes
| Name | Type |
| -------- | -------- | 
| owner | `T::AccountId` | 
| rarity_type | `RarityType` | 
| race | `RaceType` | 
| career | `CareerType` | 
| nft_sale_type | `NftSaleType` | 

#### Python
```python
call = substrate.compose_call(
    'PWNftSale', 'mint_gift_origin_of_shell', {
    'career': (
        'HackerWizard',
        'HardwareDruid',
        'RoboWarrior',
        'TradeNegotiator',
        'Web3Monk',
    ),
    'nft_sale_type': (
        'ForSale',
        'Giveaway',
        'Reserved',
    ),
    'owner': 'AccountId',
    'race': (
        'Cyborg',
        'AISpectre',
        'XGene',
        'Pandroid',
    ),
    'rarity_type': (
        'Prime',
        'Magic',
        'Legendary',
    ),
}
)
```

---------
### preorder_origin_of_shell
Users can pre-order an Origin of Shell. This will enable users that are non-whitelisted
to be added to the queue of users that can claim Origin of Shells. Those that come after
the whitelist pre-sale will be able to win the chance to acquire an Origin of Shell
based on their choice of race and career as they will have a limited quantity.

Parameters:
- origin: The origin of the extrinsic preordering the origin_of_shell
- race: The race that the user has chosen (limited \# of races)
- career: The career that the user has chosen (limited \# of careers)
#### Attributes
| Name | Type |
| -------- | -------- | 
| race | `RaceType` | 
| career | `CareerType` | 

#### Python
```python
call = substrate.compose_call(
    'PWNftSale', 'preorder_origin_of_shell', {
    'career': (
        'HackerWizard',
        'HardwareDruid',
        'RoboWarrior',
        'TradeNegotiator',
        'Web3Monk',
    ),
    'race': (
        'Cyborg',
        'AISpectre',
        'XGene',
        'Pandroid',
    ),
}
)
```

---------
### pw_create_collection
Privileged function to allow Overlord to mint the Spirit, Origin of Shell or Shell NFT
Collections. This allows for only Overlord to be able to mint Collections on Phala &amp;
prevents other users from calling the RMRK Core `create_collection` function.

Parameters:
- `origin`: Expected to be called by Overlord
- `metadata`: Metadata pertaining to the collection
- `max`: Optional max u32 for the size of the collection
- `symbol`: BoundedString of the collection&\#x27;s symbol i.e &\#x27;OVRLD&\#x27;
#### Attributes
| Name | Type |
| -------- | -------- | 
| metadata | `BoundedVec<u8, T::StringLimit>` | 
| max | `Option<u32>` | 
| symbol | `BoundedCollectionSymbolOf<T>` | 

#### Python
```python
call = substrate.compose_call(
    'PWNftSale', 'pw_create_collection', {
    'max': (None, 'u32'),
    'metadata': 'Bytes',
    'symbol': 'Bytes',
}
)
```

---------
### redeem_spirit
Redeem spirit function is called when an account has a `SpiritClaimTicket` that enables
an account to acquire a Spirit NFT without the 10 PHA minimum requirement, such that,
the account has a valid `SpiritClaimTicket` signed by the Overlord admin account.

Parameters:
- origin: The origin of the extrinsic.
#### Attributes
| Name | Type |
| -------- | -------- | 
| signature | `sr25519::Signature` | 

#### Python
```python
call = substrate.compose_call(
    'PWNftSale', 'redeem_spirit', {'signature': '[u8; 64]'}
)
```

---------
### refund_not_chosen_preorders
This is an admin only function that will be used to refund the preorders that were not
selected during the preorders drawing.

Parameters:
`origin`: Expected to come from Overlord admin account
`preorders`: Preorder ids of the not chosen preorders
#### Attributes
| Name | Type |
| -------- | -------- | 
| preorders | `Vec<PreorderId>` | 

#### Python
```python
call = substrate.compose_call(
    'PWNftSale', 'refund_not_chosen_preorders', {'preorders': ['u32']}
)
```

---------
### set_origin_of_shell_collection_id
Privileged function to set the collection id for the Origin of Shell collection

Parameters:
- `origin` - Expected Overlord admin account to set the Origin of Shell Collection ID
- `collection_id` - Collection ID of the Origin of Shell Collection
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 

#### Python
```python
call = substrate.compose_call(
    'PWNftSale', 'set_origin_of_shell_collection_id', {'collection_id': 'u32'}
)
```

---------
### set_origin_of_shells_metadata
Privileged function to set the metadata for the Origin of Shells in the StorageMap
`OriginOfShellsMetadata` where the key is a tuple of `(RaceType, CareerType)` with a
value of a `BoundedVec&lt;u8, T::StringLimit`.

Parameters:
- `origin`: Expected to be called from the Overlord account
- `origin_of_shells_metadata`: A Vec of `((RaceType, CareerType), BoundedVec&lt;u8, T::StringLimit&gt;&gt;)` to be added in storage
#### Attributes
| Name | Type |
| -------- | -------- | 
| origin_of_shells_metadata | `Vec<(RaceType, BoundedVec<u8, T::StringLimit>)>` | 

#### Python
```python
call = substrate.compose_call(
    'PWNftSale', 'set_origin_of_shells_metadata', {
    'origin_of_shells_metadata': [
        (
            (
                'Cyborg',
                'AISpectre',
                'XGene',
                'Pandroid',
            ),
            'Bytes',
        ),
    ],
}
)
```

---------
### set_overlord
Privileged function set the Overlord Admin account of Phala World

Parameters:
- origin: Expected to be called by `GovernanceOrigin`
- new_overlord: T::AccountId
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_overlord | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'PWNftSale', 'set_overlord', {'new_overlord': 'AccountId'}
)
```

---------
### set_payee
Privileged function set the Payee account of PhalaWorld.

Parameters:
- origin: Expected to be called by `Overlord`.
- new_payee: T::AccountId of the Payee account.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_payee | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'PWNftSale', 'set_payee', {'new_payee': 'AccountId'}
)
```

---------
### set_signer
Privileged function set the Signer account of PhalaWorld.

Parameters:
- origin: Expected to be called by `Overlord`.
- new_signer: T::AccountId of the Signer.
#### Attributes
| Name | Type |
| -------- | -------- | 
| new_signer | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'PWNftSale', 'set_signer', {'new_signer': 'AccountId'}
)
```

---------
### set_spirit_collection_id
Privileged function to set the collection id for the Spirits collection

Parameters:
- `origin` - Expected Overlord admin account to set the Spirit Collection ID
- `collection_id` - Collection ID of the Spirit Collection
#### Attributes
| Name | Type |
| -------- | -------- | 
| collection_id | `CollectionId` | 

#### Python
```python
call = substrate.compose_call(
    'PWNftSale', 'set_spirit_collection_id', {'collection_id': 'u32'}
)
```

---------
### set_spirits_metadata
Privileged function to set the metadata for the Spirits in the StorageValue
`SpiritMetadata` where the value is a `BoundedVec&lt;u8, T::StringLimit`.

Parameters:
- `origin`: Expected to be called from the Overlord account
- `spirits_metadata`: `BoundedVec&lt;u8, T::StringLimit&gt;` to be added in storage
#### Attributes
| Name | Type |
| -------- | -------- | 
| spirits_metadata | `BoundedVec<u8, T::StringLimit>` | 

#### Python
```python
call = substrate.compose_call(
    'PWNftSale', 'set_spirits_metadata', {'spirits_metadata': 'Bytes'}
)
```

---------
### set_status_type
Privileged function to set the status for one of the defined StatusTypes like
ClaimSpirits, PurchaseRareOriginOfShells, or PreorderOriginOfShells to enable
functionality in Phala World

Parameters:
- `origin` - Expected Overlord admin account to set the status
- `status` - `bool` to set the status to
- `status_type` - `StatusType` to set the status for
#### Attributes
| Name | Type |
| -------- | -------- | 
| status | `bool` | 
| status_type | `StatusType` | 

#### Python
```python
call = substrate.compose_call(
    'PWNftSale', 'set_status_type', {
    'status': 'bool',
    'status_type': (
        'ClaimSpirits',
        'PurchaseRareOriginOfShells',
        'PurchasePrimeOriginOfShells',
        'PreorderOriginOfShells',
        'LastDayOfSale',
    ),
}
)
```

---------
### update_rarity_type_counts
Update for the non-whitelist preorder period amount of races &amp; giveaways available for
the Origin of Shell NFTs. This is a privileged function and can only be executed by the
Overlord account. Update the OriginOfShellInventory counts by incrementing them based on
the defined counts

Parameters:
- `origin` - Expected Overlord admin account
- `rarity_type` - Type of Origin of Shell
- `for_sale_count` - Number of Origin of Shells for sale
- `giveaway_count` - Number of Origin of Shells for giveaways
- `reserve_count` - Number of Origin of Shells to be reserved
#### Attributes
| Name | Type |
| -------- | -------- | 
| rarity_type | `RarityType` | 
| for_sale_count | `u32` | 
| giveaway_count | `u32` | 

#### Python
```python
call = substrate.compose_call(
    'PWNftSale', 'update_rarity_type_counts', {
    'for_sale_count': 'u32',
    'giveaway_count': 'u32',
    'rarity_type': (
        'Prime',
        'Magic',
        'Legendary',
    ),
}
)
```

---------
## Events

---------
### ChosenPreorderMinted
Chosen preorder was minted to owner
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| preorder_id | `PreorderId` | ```u32```
| owner | `T::AccountId` | ```AccountId```
| nft_id | `NftId` | ```u32```

---------
### ClaimSpiritStatusChanged
Spirit Claims status has changed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| status | `bool` | ```bool```

---------
### LastDayOfSaleStatusChanged
Last Day of Sale status has changed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| status | `bool` | ```bool```

---------
### NewEra
Start of a new era
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| time | `u64` | ```u64```
| era | `u64` | ```u64```

---------
### NotChosenPreorderRefunded
Not chosen preorder was refunded to owner
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| preorder_id | `PreorderId` | ```u32```
| owner | `T::AccountId` | ```AccountId```

---------
### OriginOfShellCollectionIdSet
Origin of Shell collection id was set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `CollectionId` | ```u32```

---------
### OriginOfShellGiftedToOwner
Gift a Origin of Shell for giveaway or reserved NFT to owner
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| nft_sale_type | `NftSaleType` | ```('ForSale', 'Giveaway', 'Reserved')```

---------
### OriginOfShellInventoryUpdated
Origin of Shell inventory updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| rarity_type | `RarityType` | ```('Prime', 'Magic', 'Legendary')```

---------
### OriginOfShellMinted
Origin of Shell minted from the preorder
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| rarity_type | `RarityType` | ```('Prime', 'Magic', 'Legendary')```
| collection_id | `CollectionId` | ```u32```
| nft_id | `NftId` | ```u32```
| owner | `T::AccountId` | ```AccountId```
| race | `RaceType` | ```('Cyborg', 'AISpectre', 'XGene', 'Pandroid')```
| career | `CareerType` | ```('HackerWizard', 'HardwareDruid', 'RoboWarrior', 'TradeNegotiator', 'Web3Monk')```
| generation_id | `GenerationId` | ```u32```

---------
### OriginOfShellPreordered
A chance to get an Origin of Shell through preorder
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| preorder_id | `PreorderId` | ```u32```
| race | `RaceType` | ```('Cyborg', 'AISpectre', 'XGene', 'Pandroid')```
| career | `CareerType` | ```('HackerWizard', 'HardwareDruid', 'RoboWarrior', 'TradeNegotiator', 'Web3Monk')```

---------
### OriginOfShellsInventoryWasSet
Origin of Shells Inventory was set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| status | `bool` | ```bool```

---------
### OriginOfShellsMetadataSet
Origin of Shells Metadata was set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| origin_of_shells_metadata | `Vec<(RaceType, BoundedVec<u8, T::StringLimit>)>` | ```[(('Cyborg', 'AISpectre', 'XGene', 'Pandroid'), 'Bytes')]```

---------
### OverlordChanged
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_overlord | `Option<T::AccountId>` | ```(None, 'AccountId')```
| new_overlord | `T::AccountId` | ```AccountId```

---------
### PayeeChanged
Payee changed to new account
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_payee | `Option<T::AccountId>` | ```(None, 'AccountId')```
| new_payee | `T::AccountId` | ```AccountId```

---------
### PreorderOriginOfShellsStatusChanged
Preorder Origin of Shells status has changed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| status | `bool` | ```bool```

---------
### PurchasePrimeOriginOfShellsStatusChanged
Purchase Prime Origin of Shells status changed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| status | `bool` | ```bool```

---------
### PurchaseRareOriginOfShellsStatusChanged
Purchase Rare Origin of Shells status has changed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| status | `bool` | ```bool```

---------
### SignerChanged
Signer changed to new account
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| old_signer | `Option<T::AccountId>` | ```(None, 'AccountId')```
| new_signer | `T::AccountId` | ```AccountId```

---------
### SpiritClaimed
Spirit has been claimed
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| owner | `T::AccountId` | ```AccountId```
| collection_id | `CollectionId` | ```u32```
| nft_id | `NftId` | ```u32```

---------
### SpiritCollectionIdSet
Spirit collection id was set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| collection_id | `CollectionId` | ```u32```

---------
### SpiritsMetadataSet
Spirits Metadata was set
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| spirits_metadata | `BoundedVec<u8, T::StringLimit>` | ```Bytes```

---------
### WorldClockStarted
Phala World clock zero day started
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| start_time | `u64` | ```u64```

---------
## Storage functions

---------
### CanClaimSpirits
 Spirits can be claimed

#### Python
```python
result = substrate.query(
    'PWNftSale', 'CanClaimSpirits', []
)
```

#### Return value
```python
'bool'
```
---------
### CanPreorderOriginOfShells
 Origin of Shells can be preordered

#### Python
```python
result = substrate.query(
    'PWNftSale', 'CanPreorderOriginOfShells', []
)
```

#### Return value
```python
'bool'
```
---------
### CanPurchasePrimeOriginOfShells
 Origin of Shells can be purchased by whitelist

#### Python
```python
result = substrate.query(
    'PWNftSale', 'CanPurchasePrimeOriginOfShells', []
)
```

#### Return value
```python
'bool'
```
---------
### CanPurchaseRareOriginOfShells
 Rare Origin of Shells can be purchased

#### Python
```python
result = substrate.query(
    'PWNftSale', 'CanPurchaseRareOriginOfShells', []
)
```

#### Return value
```python
'bool'
```
---------
### CareerTypeCount
 Career StorageMap count

#### Python
```python
result = substrate.query(
    'PWNftSale', 'CareerTypeCount', [
    (
        'HackerWizard',
        'HardwareDruid',
        'RoboWarrior',
        'TradeNegotiator',
        'Web3Monk',
    ),
]
)
```

#### Return value
```python
'u32'
```
---------
### Era
 The current Era from the initial ZeroDay BlockNumber

#### Python
```python
result = substrate.query(
    'PWNftSale', 'Era', []
)
```

#### Return value
```python
'u64'
```
---------
### IsOriginOfShellsInventorySet
 Origin of Shells Inventory has been initialized

#### Python
```python
result = substrate.query(
    'PWNftSale', 'IsOriginOfShellsInventorySet', []
)
```

#### Return value
```python
'bool'
```
---------
### LastDayOfSale
 Last Day of Sale any Origin of Shell can be purchased

#### Python
```python
result = substrate.query(
    'PWNftSale', 'LastDayOfSale', []
)
```

#### Return value
```python
'bool'
```
---------
### NextCollectionId
 Next available Collection ID

#### Python
```python
result = substrate.query(
    'PWNftSale', 'NextCollectionId', []
)
```

#### Return value
```python
'u32'
```
---------
### NextNftId
 Next available NFT ID

#### Python
```python
result = substrate.query(
    'PWNftSale', 'NextNftId', ['u32']
)
```

#### Return value
```python
'u32'
```
---------
### NextResourceId
 Next available Resource ID

#### Python
```python
result = substrate.query(
    'PWNftSale', 'NextResourceId', ['u32', 'u32']
)
```

#### Return value
```python
'u32'
```
---------
### OriginOfShellCollectionId
 Origin of Shell Collection ID

#### Python
```python
result = substrate.query(
    'PWNftSale', 'OriginOfShellCollectionId', []
)
```

#### Return value
```python
'u32'
```
---------
### OriginOfShellsInventory
 Origin of Shells inventory

#### Python
```python
result = substrate.query(
    'PWNftSale', 'OriginOfShellsInventory', [
    ('Prime', 'Magic', 'Legendary'),
    (
        'Cyborg',
        'AISpectre',
        'XGene',
        'Pandroid',
    ),
]
)
```

#### Return value
```python
{
    'race_count': 'u32',
    'race_for_sale_count': 'u32',
    'race_giveaway_count': 'u32',
    'race_reserved_count': 'u32',
}
```
---------
### OriginOfShellsMetadata
 Origin of Shells Metadata

#### Python
```python
result = substrate.query(
    'PWNftSale', 'OriginOfShellsMetadata', [
    (
        'Cyborg',
        'AISpectre',
        'XGene',
        'Pandroid',
    ),
]
)
```

#### Return value
```python
'Bytes'
```
---------
### Overlord
 Overlord Admin account of PhalaWorld

#### Python
```python
result = substrate.query(
    'PWNftSale', 'Overlord', []
)
```

#### Return value
```python
'AccountId'
```
---------
### OwnerHasPreorder
 Owners that have made a preorder during intial preorder phase

#### Python
```python
result = substrate.query(
    'PWNftSale', 'OwnerHasPreorder', ['AccountId']
)
```

#### Return value
```python
'bool'
```
---------
### Payee
 Payee Multi-Sig account for payables in PhalaWorld

#### Python
```python
result = substrate.query(
    'PWNftSale', 'Payee', []
)
```

#### Return value
```python
'AccountId'
```
---------
### PreorderIndex
 Preorder index that is the key to the Preorders StorageMap

#### Python
```python
result = substrate.query(
    'PWNftSale', 'PreorderIndex', []
)
```

#### Return value
```python
'u32'
```
---------
### Preorders
 Preorder info map for user preorders

#### Python
```python
result = substrate.query(
    'PWNftSale', 'Preorders', ['u32']
)
```

#### Return value
```python
{
    'career': (
        'HackerWizard',
        'HardwareDruid',
        'RoboWarrior',
        'TradeNegotiator',
        'Web3Monk',
    ),
    'metadata': 'Bytes',
    'owner': 'AccountId',
    'race': ('Cyborg', 'AISpectre', 'XGene', 'Pandroid'),
}
```
---------
### Signer
 Signer account of PhalaWorld

#### Python
```python
result = substrate.query(
    'PWNftSale', 'Signer', []
)
```

#### Return value
```python
'AccountId'
```
---------
### SpiritCollectionId
 Spirit Collection ID

#### Python
```python
result = substrate.query(
    'PWNftSale', 'SpiritCollectionId', []
)
```

#### Return value
```python
'u32'
```
---------
### SpiritsMetadata
 Spirits Metadata

#### Python
```python
result = substrate.query(
    'PWNftSale', 'SpiritsMetadata', []
)
```

#### Return value
```python
'Bytes'
```
---------
### ZeroDay
 Phala World Zero Day `BlockNumber` this will be used to determine Eras

#### Python
```python
result = substrate.query(
    'PWNftSale', 'ZeroDay', []
)
```

#### Return value
```python
'u64'
```
---------
## Constants

---------
### IterLimit
 Max mint per Race
#### Value
```python
1000
```
#### Python
```python
constant = substrate.get_constant('PWNftSale', 'IterLimit')
```
---------
### LegendaryOriginOfShellPrice
 Price of Legendary Origin of Shell Price
#### Value
```python
15000000000000000
```
#### Python
```python
constant = substrate.get_constant('PWNftSale', 'LegendaryOriginOfShellPrice')
```
---------
### MagicOriginOfShellPrice
 Price of Magic Origin of Shell Price
#### Value
```python
10000000000000000
```
#### Python
```python
constant = substrate.get_constant('PWNftSale', 'MagicOriginOfShellPrice')
```
---------
### MinBalanceToClaimSpirit
 Minimum amount of PHA to claim a Spirit
#### Value
```python
10000000000000
```
#### Python
```python
constant = substrate.get_constant('PWNftSale', 'MinBalanceToClaimSpirit')
```
---------
### PrimeOriginOfShellPrice
 Price of Prime Origin of Shell Price
#### Value
```python
500000000000000
```
#### Python
```python
constant = substrate.get_constant('PWNftSale', 'PrimeOriginOfShellPrice')
```
---------
### SecondsPerEra
 Seconds per Era that will increment the Era storage value every interval
#### Value
```python
86400
```
#### Python
```python
constant = substrate.get_constant('PWNftSale', 'SecondsPerEra')
```
---------
## Errors

---------
### BelowMinimumBalanceThreshold

---------
### InvalidMetadata

---------
### InvalidPurchase

---------
### InvalidSpiritClaim

---------
### InvalidStatusType

---------
### KeyTooLong

---------
### MustOwnSpiritToPurchase

---------
### NoAvailableCollectionId

---------
### NoAvailableNftId

---------
### NoAvailablePreorderId

---------
### NoAvailableRaceGivewayLeft

---------
### NoAvailableRaceReservedLeft

---------
### NoAvailableResourceId

---------
### NotPreorderOwner

---------
### OriginOfShellAlreadyPurchased

---------
### OriginOfShellCollectionIdAlreadySet

---------
### OriginOfShellCollectionNotSet

---------
### OriginOfShellInventoryAlreadySet

---------
### OriginOfShellInventoryCorrupted

---------
### OriginOfShellsMetadataNotSet

---------
### OverlordNotSet

---------
### PayeeNotSet

---------
### PreorderClaimNotAvailable

---------
### PreorderClaimNotDetected

---------
### PreorderIsPending

---------
### PreorderOriginOfShellNotAvailable

---------
### PreordersCorrupted

---------
### PrimeOriginOfShellPurchaseNotAvailable

---------
### RaceMintMaxReached

---------
### RareOriginOfShellPurchaseNotAvailable

---------
### RefundClaimNotDetected

---------
### RequireOverlordAccount

---------
### SignerNotSet

---------
### SpiritAlreadyClaimed

---------
### SpiritClaimNotAvailable

---------
### SpiritCollectionIdAlreadySet

---------
### SpiritCollectionNotSet

---------
### SpiritsMetadataNotSet

---------
### ValueNotDetected

---------
### WhitelistVerificationFailed

---------
### WorldClockAlreadySet

---------
### WrongNftSaleType

---------
### WrongRarityType

---------