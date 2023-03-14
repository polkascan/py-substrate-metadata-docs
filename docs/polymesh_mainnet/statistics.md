
# Statistics

---------
## Calls

---------
### batch_update_asset_stats
Allow a trusted issuer to init/resync ticker/company stats.

\# Arguments
- `origin` - a signer that has permissions to act as an agent of `asset`.
- `asset` - the asset to change the active stats on.
- `stat_type` - stat type to update.
- `values` - Updated values for `stat_type`.

\# Errors
- `StatTypeMissing` - `stat_type` is not enabled for the `asset`.
- `UnauthorizedAgent` if `origin` is not agent-permissioned for `asset`.

\# Permissions
- Agent
- Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetScope` | 
| stat_type | `StatType` | 
| values | `BTreeSet<StatUpdate>` | 

#### Python
```python
call = substrate.compose_call(
    'Statistics', 'batch_update_asset_stats', {
    'asset': {'Ticker': '[u8; 12]'},
    'stat_type': {
        'claim_issuer': (
            None,
            (
                {
                    'Accredited': None,
                    'Affiliate': None,
                    'Blocked': None,
                    'BuyLockup': None,
                    'Custom': 'u32',
                    'CustomerDueDiligence': None,
                    'Exempted': None,
                    'InvestorUniqueness': None,
                    'InvestorUniquenessV2': None,
                    'Jurisdiction': None,
                    'KnowYourCustomer': None,
                    'NoType': None,
                    'SellLockup': None,
                },
                '[u8; 32]',
            ),
        ),
        'op': ('Count', 'Balance'),
    },
    'values': 'scale_info::507',
}
)
```

---------
### set_active_asset_stats
Set the active asset stat_types.

\# Arguments
- `origin` - a signer that has permissions to act as an agent of `asset`.
- `asset` - the asset to change the active stats on.
- `stat_types` - the new stat types to replace any existing types.

\# Errors
- `StatTypeLimitReached` - too many stat types enabled for the `asset`.
- `CannotRemoveStatTypeInUse` - can not remove a stat type that is in use by transfer conditions.
- `UnauthorizedAgent` if `origin` is not agent-permissioned for `asset`.

\# Permissions
- Agent
- Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetScope` | 
| stat_types | `BTreeSet<StatType>` | 

#### Python
```python
call = substrate.compose_call(
    'Statistics', 'set_active_asset_stats', {
    'asset': {'Ticker': '[u8; 12]'},
    'stat_types': 'scale_info::506',
}
)
```

---------
### set_asset_transfer_compliance
Set asset transfer compliance rules.

\# Arguments
- `origin` - a signer that has permissions to act as an agent of `asset`.
- `asset` - the asset to change the active stats on.
- `transfer_conditions` - the new transfer condition to replace any existing conditions.

\# Errors
- `TransferConditionLimitReached` - too many transfer condititon enabled for `asset`.
- `StatTypeMissing` - a transfer condition requires a stat type that is not enabled for the `asset`.
- `UnauthorizedAgent` if `origin` is not agent-permissioned for `asset`.

\# Permissions
- Agent
- Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| asset | `AssetScope` | 
| transfer_conditions | `BTreeSet<TransferCondition>` | 

#### Python
```python
call = substrate.compose_call(
    'Statistics', 'set_asset_transfer_compliance', {
    'asset': {'Ticker': '[u8; 12]'},
    'transfer_conditions': 'scale_info::508',
}
)
```

---------
### set_entities_exempt
Set/unset entities exempt from an asset&\#x27;s transfer compliance rules.

\# Arguments
- `origin` - a signer that has permissions to act as an agent of `exempt_key.asset`.
- `is_exempt` - enable/disable exemption for `entities`.
- `exempt_key` - the asset and stat type to exempt the `entities` from.
- `entities` - the entities to set/unset the exemption for.

\# Errors
- `UnauthorizedAgent` if `origin` is not agent-permissioned for `asset`.

\# Permissions
- Agent
- Asset
#### Attributes
| Name | Type |
| -------- | -------- | 
| is_exempt | `bool` | 
| exempt_key | `TransferConditionExemptKey` | 
| entities | `BTreeSet<ScopeId>` | 

#### Python
```python
call = substrate.compose_call(
    'Statistics', 'set_entities_exempt', {
    'entities': 'scale_info::509',
    'exempt_key': {
        'asset': {
            'Ticker': '[u8; 12]',
        },
        'claim_type': (
            None,
            {
                'Accredited': None,
                'Affiliate': None,
                'Blocked': None,
                'BuyLockup': None,
                'Custom': 'u32',
                'CustomerDueDiligence': None,
                'Exempted': None,
                'InvestorUniqueness': None,
                'InvestorUniquenessV2': None,
                'Jurisdiction': None,
                'KnowYourCustomer': None,
                'NoType': None,
                'SellLockup': None,
            },
        ),
        'op': ('Count', 'Balance'),
    },
    'is_exempt': 'bool',
}
)
```

---------
## Events

---------
### AssetStatsUpdated
Asset stats updated.

(Caller DID, Asset, Stat type, Updates)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AssetScope` | ```{'Ticker': '[u8; 12]'}```
| None | `StatType` | ```{'op': ('Count', 'Balance'), 'claim_issuer': (None, ({'Accredited': None, 'Affiliate': None, 'BuyLockup': None, 'SellLockup': None, 'CustomerDueDiligence': None, 'KnowYourCustomer': None, 'Jurisdiction': None, 'Exempted': None, 'Blocked': None, 'InvestorUniqueness': None, 'NoType': None, 'InvestorUniquenessV2': None, 'Custom': 'u32'}, '[u8; 32]'))}```
| None | `Vec<StatUpdate>` | ```[{'key2': {'NoClaimStat': None, 'Claim': {'Accredited': 'bool', 'Affiliate': 'bool', 'Jurisdiction': (None, 'scale_info::64')}}, 'value': (None, 'u128')}]```

---------
### SetAssetTransferCompliance
Set Transfer compliance rules for asset.

(Caller DID, Asset, Transfer conditions)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AssetScope` | ```{'Ticker': '[u8; 12]'}```
| None | `Vec<TransferCondition>` | ```[{'MaxInvestorCount': 'u64', 'MaxInvestorOwnership': 'u32', 'ClaimCount': ({'Accredited': 'bool', 'Affiliate': 'bool', 'Jurisdiction': (None, 'scale_info::64')}, '[u8; 32]', 'u64', (None, 'u64')), 'ClaimOwnership': ({'Accredited': 'bool', 'Affiliate': 'bool', 'Jurisdiction': (None, 'scale_info::64')}, '[u8; 32]', 'u32', 'u32')}]```

---------
### StatTypesAdded
Stat types added to asset.

(Caller DID, Asset, Stat types)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AssetScope` | ```{'Ticker': '[u8; 12]'}```
| None | `Vec<StatType>` | ```[{'op': ('Count', 'Balance'), 'claim_issuer': (None, ({'Accredited': None, 'Affiliate': None, 'BuyLockup': None, 'SellLockup': None, 'CustomerDueDiligence': None, 'KnowYourCustomer': None, 'Jurisdiction': None, 'Exempted': None, 'Blocked': None, 'InvestorUniqueness': None, 'NoType': None, 'InvestorUniquenessV2': None, 'Custom': 'u32'}, '[u8; 32]'))}]```

---------
### StatTypesRemoved
Stat types removed from asset.

(Caller DID, Asset, Stat types)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AssetScope` | ```{'Ticker': '[u8; 12]'}```
| None | `Vec<StatType>` | ```[{'op': ('Count', 'Balance'), 'claim_issuer': (None, ({'Accredited': None, 'Affiliate': None, 'BuyLockup': None, 'SellLockup': None, 'CustomerDueDiligence': None, 'KnowYourCustomer': None, 'Jurisdiction': None, 'Exempted': None, 'Blocked': None, 'InvestorUniqueness': None, 'NoType': None, 'InvestorUniquenessV2': None, 'Custom': 'u32'}, '[u8; 32]'))}]```

---------
### TransferConditionExemptionsAdded
Add `ScopeId`s exempt for transfer conditions matching exempt key.

(Caller DID, Exempt key, Entities)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `TransferConditionExemptKey` | ```{'asset': {'Ticker': '[u8; 12]'}, 'op': ('Count', 'Balance'), 'claim_type': (None, {'Accredited': None, 'Affiliate': None, 'BuyLockup': None, 'SellLockup': None, 'CustomerDueDiligence': None, 'KnowYourCustomer': None, 'Jurisdiction': None, 'Exempted': None, 'Blocked': None, 'InvestorUniqueness': None, 'NoType': None, 'InvestorUniquenessV2': None, 'Custom': 'u32'})}```
| None | `Vec<ScopeId>` | ```['[u8; 32]']```

---------
### TransferConditionExemptionsRemoved
Remove `ScopeId`s exempt for transfer conditions matching exempt key.

(Caller DID, Exempt key, Entities)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `TransferConditionExemptKey` | ```{'asset': {'Ticker': '[u8; 12]'}, 'op': ('Count', 'Balance'), 'claim_type': (None, {'Accredited': None, 'Affiliate': None, 'BuyLockup': None, 'SellLockup': None, 'CustomerDueDiligence': None, 'KnowYourCustomer': None, 'Jurisdiction': None, 'Exempted': None, 'Blocked': None, 'InvestorUniqueness': None, 'NoType': None, 'InvestorUniquenessV2': None, 'Custom': 'u32'})}```
| None | `Vec<ScopeId>` | ```['[u8; 32]']```

---------
## Storage functions

---------
### ActiveAssetStats
 Active stats for a ticker/company.  There should be a max limit on the number of active stats for a ticker/company.

#### Python
```python
result = substrate.query(
    'Statistics', 'ActiveAssetStats', [{'Ticker': '[u8; 12]'}]
)
```

#### Return value
```python
'scale_info::506'
```
---------
### AssetStats
 Asset stats.

#### Python
```python
result = substrate.query(
    'Statistics', 'AssetStats', [
    {
        'asset': {
            'Ticker': '[u8; 12]',
        },
        'stat_type': {
            'claim_issuer': (
                None,
                (
                    {
                        'Accredited': None,
                        'Affiliate': None,
                        'Blocked': None,
                        'BuyLockup': None,
                        'Custom': 'u32',
                        'CustomerDueDiligence': None,
                        'Exempted': None,
                        'InvestorUniqueness': None,
                        'InvestorUniquenessV2': None,
                        'Jurisdiction': None,
                        'KnowYourCustomer': None,
                        'NoType': None,
                        'SellLockup': None,
                    },
                    '[u8; 32]',
                ),
            ),
            'op': ('Count', 'Balance'),
        },
    },
    {
        'Claim': {
            'Accredited': 'bool',
            'Affiliate': 'bool',
            'Jurisdiction': (
                None,
                (
                    'AF',
                    'AX',
                    'AL',
                    'DZ',
                    'AS',
                    'AD',
                    'AO',
                    'AI',
                    'AQ',
                    'AG',
                    'AR',
                    'AM',
                    'AW',
                    'AU',
                    'AT',
                    'AZ',
                    'BS',
                    'BH',
                    'BD',
                    'BB',
                    'BY',
                    'BE',
                    'BZ',
                    'BJ',
                    'BM',
                    'BT',
                    'BO',
                    'BA',
                    'BW',
                    'BV',
                    'BR',
                    'VG',
                    'IO',
                    'BN',
                    'BG',
                    'BF',
                    'BI',
                    'KH',
                    'CM',
                    'CA',
                    'CV',
                    'KY',
                    'CF',
                    'TD',
                    'CL',
                    'CN',
                    'HK',
                    'MO',
                    'CX',
                    'CC',
                    'CO',
                    'KM',
                    'CG',
                    'CD',
                    'CK',
                    'CR',
                    'CI',
                    'HR',
                    'CU',
                    'CY',
                    'CZ',
                    'DK',
                    'DJ',
                    'DM',
                    'DO',
                    'EC',
                    'EG',
                    'SV',
                    'GQ',
                    'ER',
                    'EE',
                    'ET',
                    'FK',
                    'FO',
                    'FJ',
                    'FI',
                    'FR',
                    'GF',
                    'PF',
                    'TF',
                    'GA',
                    'GM',
                    'GE',
                    'DE',
                    'GH',
                    'GI',
                    'GR',
                    'GL',
                    'GD',
                    'GP',
                    'GU',
                    'GT',
                    'GG',
                    'GN',
                    'GW',
                    'GY',
                    'HT',
                    'HM',
                    'VA',
                    'HN',
                    'HU',
                    'IS',
                    'IN',
                    'ID',
                    'IR',
                    'IQ',
                    'IE',
                    'IM',
                    'IL',
                    'IT',
                    'JM',
                    'JP',
                    'JE',
                    'JO',
                    'KZ',
                    'KE',
                    'KI',
                    'KP',
                    'KR',
                    'KW',
                    'KG',
                    'LA',
                    'LV',
                    'LB',
                    'LS',
                    'LR',
                    'LY',
                    'LI',
                    'LT',
                    'LU',
                    'MK',
                    'MG',
                    'MW',
                    'MY',
                    'MV',
                    'ML',
                    'MT',
                    'MH',
                    'MQ',
                    'MR',
                    'MU',
                    'YT',
                    'MX',
                    'FM',
                    'MD',
                    'MC',
                    'MN',
                    'ME',
                    'MS',
                    'MA',
                    'MZ',
                    'MM',
                    'NA',
                    'NR',
                    'NP',
                    'NL',
                    'AN',
                    'NC',
                    'NZ',
                    'NI',
                    'NE',
                    'NG',
                    'NU',
                    'NF',
                    'MP',
                    'NO',
                    'OM',
                    'PK',
                    'PW',
                    'PS',
                    'PA',
                    'PG',
                    'PY',
                    'PE',
                    'PH',
                    'PN',
                    'PL',
                    'PT',
                    'PR',
                    'QA',
                    'RE',
                    'RO',
                    'RU',
                    'RW',
                    'BL',
                    'SH',
                    'KN',
                    'LC',
                    'MF',
                    'PM',
                    'VC',
                    'WS',
                    'SM',
                    'ST',
                    'SA',
                    'SN',
                    'RS',
                    'SC',
                    'SL',
                    'SG',
                    'SK',
                    'SI',
                    'SB',
                    'SO',
                    'ZA',
                    'GS',
                    'SS',
                    'ES',
                    'LK',
                    'SD',
                    'SR',
                    'SJ',
                    'SZ',
                    'SE',
                    'CH',
                    'SY',
                    'TW',
                    'TJ',
                    'TZ',
                    'TH',
                    'TL',
                    'TG',
                    'TK',
                    'TO',
                    'TT',
                    'TN',
                    'TR',
                    'TM',
                    'TC',
                    'TV',
                    'UG',
                    'UA',
                    'AE',
                    'GB',
                    'US',
                    'UM',
                    'UY',
                    'UZ',
                    'VU',
                    'VE',
                    'VN',
                    'VI',
                    'WF',
                    'EH',
                    'YE',
                    'ZM',
                    'ZW',
                    'BQ',
                    'CW',
                    'SX',
                ),
            ),
        },
        'NoClaimStat': None,
    },
]
)
```

#### Return value
```python
'u128'
```
---------
### AssetTransferCompliances
 Asset transfer compliance for a ticker (AssetScope -&gt; AssetTransferCompliance)

#### Python
```python
result = substrate.query(
    'Statistics', 'AssetTransferCompliances', [{'Ticker': '[u8; 12]'}]
)
```

#### Return value
```python
{'paused': 'bool', 'requirements': 'scale_info::508'}
```
---------
### StorageVersion
 Storage migration version.

#### Python
```python
result = substrate.query(
    'Statistics', 'StorageVersion', []
)
```

#### Return value
```python
'u8'
```
---------
### TransferConditionExemptEntities
 Entities exempt from a Transfer Compliance rule.

#### Python
```python
result = substrate.query(
    'Statistics', 'TransferConditionExemptEntities', [
    {
        'asset': {
            'Ticker': '[u8; 12]',
        },
        'claim_type': (
            None,
            {
                'Accredited': None,
                'Affiliate': None,
                'Blocked': None,
                'BuyLockup': None,
                'Custom': 'u32',
                'CustomerDueDiligence': None,
                'Exempted': None,
                'InvestorUniqueness': None,
                'InvestorUniquenessV2': None,
                'Jurisdiction': None,
                'KnowYourCustomer': None,
                'NoType': None,
                'SellLockup': None,
            },
        ),
        'op': ('Count', 'Balance'),
    },
    '[u8; 32]',
]
)
```

#### Return value
```python
'bool'
```
---------
## Constants

---------
### MaxStatsPerAsset
#### Value
```python
10
```
#### Python
```python
constant = substrate.get_constant('Statistics', 'MaxStatsPerAsset')
```
---------
### MaxTransferConditionsPerAsset
#### Value
```python
4
```
#### Python
```python
constant = substrate.get_constant('Statistics', 'MaxTransferConditionsPerAsset')
```
---------
## Errors

---------
### CannotRemoveStatTypeInUse
A Stattype is in use and can&\#x27;t be removed.

---------
### InvalidTransfer
Transfer not allowed.

---------
### StatTypeLimitReached
The limit of StatTypes allowed for an asset has been reached.

---------
### StatTypeMissing
StatType is not enabled.

---------
### StatTypeNeededByTransferCondition
StatType is needed by TransferCondition.

---------
### TransferConditionLimitReached
The limit of TransferConditions allowed for an asset has been reached.

---------