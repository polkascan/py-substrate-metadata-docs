
# Identity

---------
## Calls

---------
### accept_primary_key
Call this with the new primary key. By invoking this method, caller accepts authorization
to become the new primary key of the issuing identity. If a CDD service provider approved
this change (or this is not required), primary key of the DID is updated.

The caller (new primary key) must be either a secondary key of the issuing identity, or
unlinked to any identity.

Differs from rotate_primary_key_to_secondary in that it will unlink the old primary key
instead of leaving it as a secondary key.

\# Arguments
* `owner_auth_id` Authorization from the owner who initiated the change
* `cdd_auth_id` Authorization from a CDD service provider
#### Attributes
| Name | Type |
| -------- | -------- | 
| rotation_auth_id | `u64` | 
| optional_cdd_auth_id | `Option<u64>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'accept_primary_key', {
    'optional_cdd_auth_id': (
        None,
        'u64',
    ),
    'rotation_auth_id': 'u64',
}
)
```

---------
### add_authorization
Adds an authorization.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `Signatory<T::AccountId>` | 
| data | `AuthorizationData<T::AccountId>` | 
| expiry | `Option<T::Moment>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'add_authorization', {
    'data': {
        'AddMultiSigSigner': 'AccountId',
        'AddRelayerPayingKey': (
            'AccountId',
            'AccountId',
            'u128',
        ),
        'AttestPrimaryKeyRotation': '[u8; 32]',
        'BecomeAgent': (
            '[u8; 12]',
            {
                'Custom': 'u32',
                'ExceptMeta': None,
                'Full': None,
                'PolymeshV1CAA': None,
                'PolymeshV1PIA': None,
            },
        ),
        'JoinIdentity': {
            'asset': {
                'Except': 'scale_info::44',
                'These': 'scale_info::44',
                'Whole': None,
            },
            'extrinsic': {
                'Except': 'scale_info::53',
                'These': 'scale_info::53',
                'Whole': None,
            },
            'portfolio': {
                'Except': 'scale_info::59',
                'These': 'scale_info::59',
                'Whole': None,
            },
        },
        'PortfolioCustody': {
            'did': '[u8; 32]',
            'kind': {
                'Default': None,
                'User': 'u64',
            },
        },
        'RotatePrimaryKey': None,
        'RotatePrimaryKeyToSecondary': {
            'asset': {
                'Except': 'scale_info::44',
                'These': 'scale_info::44',
                'Whole': None,
            },
            'extrinsic': {
                'Except': 'scale_info::53',
                'These': 'scale_info::53',
                'Whole': None,
            },
            'portfolio': {
                'Except': 'scale_info::59',
                'These': 'scale_info::59',
                'Whole': None,
            },
        },
        'TransferAssetOwnership': '[u8; 12]',
        'TransferTicker': '[u8; 12]',
    },
    'expiry': (None, 'u64'),
    'target': {
        'Account': 'AccountId',
        'Identity': '[u8; 32]',
    },
}
)
```

---------
### add_claim
Adds a new claim record or edits an existing one.

Only called by did_issuer&\#x27;s secondary key.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `IdentityId` | 
| claim | `Claim` | 
| expiry | `Option<T::Moment>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'add_claim', {
    'claim': {
        'Accredited': {
            'Custom': 'Bytes',
            'Identity': '[u8; 32]',
            'Ticker': '[u8; 12]',
        },
        'Affiliate': {
            'Custom': 'Bytes',
            'Identity': '[u8; 32]',
            'Ticker': '[u8; 12]',
        },
        'Blocked': {
            'Custom': 'Bytes',
            'Identity': '[u8; 32]',
            'Ticker': '[u8; 12]',
        },
        'BuyLockup': {
            'Custom': 'Bytes',
            'Identity': '[u8; 32]',
            'Ticker': '[u8; 12]',
        },
        'Custom': (
            'u32',
            (
                None,
                {
                    'Custom': 'Bytes',
                    'Identity': '[u8; 32]',
                    'Ticker': '[u8; 12]',
                },
            ),
        ),
        'CustomerDueDiligence': '[u8; 32]',
        'Exempted': {
            'Custom': 'Bytes',
            'Identity': '[u8; 32]',
            'Ticker': '[u8; 12]',
        },
        'Jurisdiction': (
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
            {
                'Custom': 'Bytes',
                'Identity': '[u8; 32]',
                'Ticker': '[u8; 12]',
            },
        ),
        'KnowYourCustomer': {
            'Custom': 'Bytes',
            'Identity': '[u8; 32]',
            'Ticker': '[u8; 12]',
        },
        'SellLockup': {
            'Custom': 'Bytes',
            'Identity': '[u8; 32]',
            'Ticker': '[u8; 12]',
        },
    },
    'expiry': (None, 'u64'),
    'target': '[u8; 32]',
}
)
```

---------
### add_secondary_keys_with_authorization
Adds secondary keys to target identity `id`.

Keys are directly added to identity because each of them has an authorization.

\# Arguments:
    - `origin` which must be the primary key of the identity `id`.
    - `id` to which new secondary keys will be added.
    - `additional_keys` which includes secondary keys,
       coupled with authorization data, to add to target identity.

\# Errors
    - Can only called by primary key owner.
    - Keys should be able to linked to any identity.
#### Attributes
| Name | Type |
| -------- | -------- | 
| additional_keys | `Vec<SecondaryKeyWithAuth<T::AccountId>>` | 
| expires_at | `T::Moment` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'add_secondary_keys_with_authorization', {
    'additional_keys': [
        {
            'auth_signature': '[u8; 64]',
            'secondary_key': {
                'key': 'AccountId',
                'permissions': {
                    'asset': {
                        'Except': 'scale_info::44',
                        'These': 'scale_info::44',
                        'Whole': None,
                    },
                    'extrinsic': {
                        'Except': 'scale_info::53',
                        'These': 'scale_info::53',
                        'Whole': None,
                    },
                    'portfolio': {
                        'Except': 'scale_info::59',
                        'These': 'scale_info::59',
                        'Whole': None,
                    },
                },
            },
        },
    ],
    'expires_at': 'u64',
}
)
```

---------
### cdd_register_did
Register `target_account` with a new Identity.

\# Failure
- `origin` has to be a active CDD provider. Inactive CDD providers cannot add new
claims.
- `target_account` (primary key of the new Identity) can be linked to just one and only
one identity.
- External secondary keys can be linked to just one identity.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target_account | `T::AccountId` | 
| secondary_keys | `Vec<SecondaryKey<T::AccountId>>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'cdd_register_did', {
    'secondary_keys': [
        {
            'key': 'AccountId',
            'permissions': {
                'asset': {
                    'Except': 'scale_info::44',
                    'These': 'scale_info::44',
                    'Whole': None,
                },
                'extrinsic': {
                    'Except': 'scale_info::53',
                    'These': 'scale_info::53',
                    'Whole': None,
                },
                'portfolio': {
                    'Except': 'scale_info::59',
                    'These': 'scale_info::59',
                    'Whole': None,
                },
            },
        },
    ],
    'target_account': 'AccountId',
}
)
```

---------
### cdd_register_did_with_cdd
Register `target_account` with a new Identity and issue a CDD claim with a blank CddId

\# Failure
- `origin` has to be a active CDD provider. Inactive CDD providers cannot add new
claims.
- `target_account` (primary key of the new Identity) can be linked to just one and only
one identity.
- External secondary keys can be linked to just one identity.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target_account | `T::AccountId` | 
| secondary_keys | `Vec<SecondaryKey<T::AccountId>>` | 
| expiry | `Option<T::Moment>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'cdd_register_did_with_cdd', {
    'expiry': (None, 'u64'),
    'secondary_keys': [
        {
            'key': 'AccountId',
            'permissions': {
                'asset': {
                    'Except': 'scale_info::44',
                    'These': 'scale_info::44',
                    'Whole': None,
                },
                'extrinsic': {
                    'Except': 'scale_info::53',
                    'These': 'scale_info::53',
                    'Whole': None,
                },
                'portfolio': {
                    'Except': 'scale_info::59',
                    'These': 'scale_info::59',
                    'Whole': None,
                },
            },
        },
    ],
    'target_account': 'AccountId',
}
)
```

---------
### change_cdd_requirement_for_mk_rotation
Set if CDD authorization is required for updating primary key of an identity.
Callable via root (governance)

\# Arguments
* `auth_required` CDD Authorization required or not
#### Attributes
| Name | Type |
| -------- | -------- | 
| auth_required | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'change_cdd_requirement_for_mk_rotation', {'auth_required': 'bool'}
)
```

---------
### create_child_identities
Create a child identities.

The new primary key for each child identity will need to sign (off-chain)
an authorization.

Only the primary key can create child identities.

\# Arguments
- `child_keys` the keys that will become primary keys of their own child identity.

\# Errors
- `KeyNotAllowed` only the primary key can create a new identity.
- `AlreadyLinked` one of the keys is already linked to an identity.
- `DuplicateKey` one of the keys is included multiple times.
- `IsChildIdentity` the caller&\#x27;s identity is already a child identity and can&\#x27;t create child identities.
#### Attributes
| Name | Type |
| -------- | -------- | 
| child_keys | `Vec<CreateChildIdentityWithAuth<T::AccountId>>` | 
| expires_at | `T::Moment` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'create_child_identities', {
    'child_keys': [
        {
            'auth_signature': '[u8; 64]',
            'key': 'AccountId',
        },
    ],
    'expires_at': 'u64',
}
)
```

---------
### create_child_identity
Create a child identity and make the `secondary_key` it&\#x27;s primary key.

Only the primary key can create child identities.

\# Arguments
- `secondary_key` the secondary key that will become the primary key of the new identity.

\# Errors
- `KeyNotAllowed` only the primary key can create a new identity.
- `NotASigner` the `secondary_key` is not a secondary key of the caller&\#x27;s identity.
- `AccountKeyIsBeingUsed` the `secondary_key` can&\#x27;t be unlinked from it&\#x27;s current identity.
- `IsChildIdentity` the caller&\#x27;s identity is already a child identity and can&\#x27;t create child identities.
#### Attributes
| Name | Type |
| -------- | -------- | 
| secondary_key | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'create_child_identity', {'secondary_key': 'AccountId'}
)
```

---------
### freeze_secondary_keys
It disables all secondary keys at `did` identity.

\# Errors

#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Identity', 'freeze_secondary_keys', {}
)
```

---------
### gc_add_cdd_claim
Assuming this is executed by the GC voting majority, adds a new cdd claim record.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `IdentityId` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'gc_add_cdd_claim', {'target': '[u8; 32]'}
)
```

---------
### gc_revoke_cdd_claim
Assuming this is executed by the GC voting majority, removes an existing cdd claim record.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `IdentityId` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'gc_revoke_cdd_claim', {'target': '[u8; 32]'}
)
```

---------
### invalidate_cdd_claims
Invalidates any claim generated by `cdd` from `disable_from` timestamps.

You can also define an expiration time,
which will invalidate all claims generated by that `cdd` and remove it as CDD member group.
#### Attributes
| Name | Type |
| -------- | -------- | 
| cdd | `IdentityId` | 
| disable_from | `T::Moment` | 
| expiry | `Option<T::Moment>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'invalidate_cdd_claims', {
    'cdd': '[u8; 32]',
    'disable_from': 'u64',
    'expiry': (None, 'u64'),
}
)
```

---------
### join_identity_as_key
Join an identity as a secondary key.
#### Attributes
| Name | Type |
| -------- | -------- | 
| auth_id | `u64` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'join_identity_as_key', {'auth_id': 'u64'}
)
```

---------
### leave_identity_as_key
Leave the secondary key&\#x27;s identity.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Identity', 'leave_identity_as_key', {}
)
```

---------
### register_custom_claim_type
Register custom claim type.

\# Errors
* `CustomClaimTypeAlreadyExists` The type that is being registered already exists.
* `CounterOverflow` CustomClaimTypeId has overflowed.
* `TooLong` The type being registered is too lang.
#### Attributes
| Name | Type |
| -------- | -------- | 
| ty | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'register_custom_claim_type', {'ty': 'Bytes'}
)
```

---------
### remove_authorization
Removes an authorization.
_auth_issuer_pays determines whether the issuer of the authorisation pays the transaction fee
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `Signatory<T::AccountId>` | 
| auth_id | `u64` | 
| _auth_issuer_pays | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'remove_authorization', {
    '_auth_issuer_pays': 'bool',
    'auth_id': 'u64',
    'target': {
        'Account': 'AccountId',
        'Identity': '[u8; 32]',
    },
}
)
```

---------
### remove_secondary_keys
Removes specified secondary keys of a DID if present.

\# Errors

The extrinsic can only called by primary key owner.
#### Attributes
| Name | Type |
| -------- | -------- | 
| keys_to_remove | `Vec<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'remove_secondary_keys', {'keys_to_remove': ['AccountId']}
)
```

---------
### revoke_claim
Marks the specified claim as revoked.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `IdentityId` | 
| claim | `Claim` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'revoke_claim', {
    'claim': {
        'Accredited': {
            'Custom': 'Bytes',
            'Identity': '[u8; 32]',
            'Ticker': '[u8; 12]',
        },
        'Affiliate': {
            'Custom': 'Bytes',
            'Identity': '[u8; 32]',
            'Ticker': '[u8; 12]',
        },
        'Blocked': {
            'Custom': 'Bytes',
            'Identity': '[u8; 32]',
            'Ticker': '[u8; 12]',
        },
        'BuyLockup': {
            'Custom': 'Bytes',
            'Identity': '[u8; 32]',
            'Ticker': '[u8; 12]',
        },
        'Custom': (
            'u32',
            (
                None,
                {
                    'Custom': 'Bytes',
                    'Identity': '[u8; 32]',
                    'Ticker': '[u8; 12]',
                },
            ),
        ),
        'CustomerDueDiligence': '[u8; 32]',
        'Exempted': {
            'Custom': 'Bytes',
            'Identity': '[u8; 32]',
            'Ticker': '[u8; 12]',
        },
        'Jurisdiction': (
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
            {
                'Custom': 'Bytes',
                'Identity': '[u8; 32]',
                'Ticker': '[u8; 12]',
            },
        ),
        'KnowYourCustomer': {
            'Custom': 'Bytes',
            'Identity': '[u8; 32]',
            'Ticker': '[u8; 12]',
        },
        'SellLockup': {
            'Custom': 'Bytes',
            'Identity': '[u8; 32]',
            'Ticker': '[u8; 12]',
        },
    },
    'target': '[u8; 32]',
}
)
```

---------
### revoke_claim_by_index
Revokes a specific claim using its [Claim Unique Index](/pallet_identity/index.html\#claim-unique-index) composed by `target`,
`claim_type`, and `scope`.

Please note that `origin` must be the issuer of the target claim.
#### Attributes
| Name | Type |
| -------- | -------- | 
| target | `IdentityId` | 
| claim_type | `ClaimType` | 
| scope | `Option<Scope>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'revoke_claim_by_index', {
    'claim_type': {
        'Accredited': None,
        'Affiliate': None,
        'Blocked': None,
        'BuyLockup': None,
        'Custom': 'u32',
        'CustomerDueDiligence': None,
        'Exempted': None,
        'Jurisdiction': None,
        'KnowYourCustomer': None,
        'SellLockup': None,
    },
    'scope': (
        None,
        {
            'Custom': 'Bytes',
            'Identity': '[u8; 32]',
            'Ticker': '[u8; 12]',
        },
    ),
    'target': '[u8; 32]',
}
)
```

---------
### rotate_primary_key_to_secondary
Call this with the new primary key. By invoking this method, caller accepts authorization
to become the new primary key of the issuing identity. If a CDD service provider approved
this change, (or this is not required), primary key of the DID is updated.

The caller (new primary key) must be either a secondary key of the issuing identity, or
unlinked to any identity.

Differs from accept_primary_key in that it will leave the old primary key as a secondary
key with the permissions specified in the corresponding RotatePrimaryKeyToSecondary authorization
instead of unlinking the old primary key.

\# Arguments
* `owner_auth_id` Authorization from the owner who initiated the change
* `cdd_auth_id` Authorization from a CDD service provider
#### Attributes
| Name | Type |
| -------- | -------- | 
| auth_id | `u64` | 
| optional_cdd_auth_id | `Option<u64>` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'rotate_primary_key_to_secondary', {
    'auth_id': 'u64',
    'optional_cdd_auth_id': (
        None,
        'u64',
    ),
}
)
```

---------
### set_secondary_key_permissions
Sets permissions for an specific `target_key` key.

Only the primary key of an identity is able to set secondary key permissions.
#### Attributes
| Name | Type |
| -------- | -------- | 
| key | `T::AccountId` | 
| perms | `Permissions` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'set_secondary_key_permissions', {
    'key': 'AccountId',
    'perms': {
        'asset': {
            'Except': 'scale_info::44',
            'These': 'scale_info::44',
            'Whole': None,
        },
        'extrinsic': {
            'Except': 'scale_info::53',
            'These': 'scale_info::53',
            'Whole': None,
        },
        'portfolio': {
            'Except': 'scale_info::59',
            'These': 'scale_info::59',
            'Whole': None,
        },
    },
}
)
```

---------
### unfreeze_secondary_keys
Re-enables all secondary keys of the caller&\#x27;s identity.
#### Attributes
No attributes

#### Python
```python
call = substrate.compose_call(
    'Identity', 'unfreeze_secondary_keys', {}
)
```

---------
### unlink_child_identity
Unlink a child identity from it&\#x27;s parent identity.

Only the primary key of the parent or child identities can unlink the identities.

\# Arguments
- `child_did` the child identity to unlink from its parent identity.

\# Errors
- `KeyNotAllowed` only the primary key of either the parent or child identity can unlink the identities.
- `NoParentIdentity` the identity `child_did` doesn&\#x27;t have a parent identity.
- `NotParentOrChildIdentity` the caller&\#x27;s identity isn&\#x27;t the parent or child identity.
#### Attributes
| Name | Type |
| -------- | -------- | 
| child_did | `IdentityId` | 

#### Python
```python
call = substrate.compose_call(
    'Identity', 'unlink_child_identity', {'child_did': '[u8; 32]'}
)
```

---------
## Events

---------
### AssetDidRegistered
Asset&\#x27;s identity registered.

(Asset DID, ticker)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Ticker` | ```[u8; 12]```

---------
### AuthorizationAdded
New authorization added.

(authorised_by, target_did, target_key, auth_id, authorization_data, expiry)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Option<IdentityId>` | ```(None, '[u8; 32]')```
| None | `Option<AccountId>` | ```(None, 'AccountId')```
| None | `u64` | ```u64```
| None | `AuthorizationData<AccountId>` | ```{'AttestPrimaryKeyRotation': '[u8; 32]', 'RotatePrimaryKey': None, 'TransferTicker': '[u8; 12]', 'AddMultiSigSigner': 'AccountId', 'TransferAssetOwnership': '[u8; 12]', 'JoinIdentity': {'asset': {'Whole': None, 'These': 'scale_info::44', 'Except': 'scale_info::44'}, 'extrinsic': {'Whole': None, 'These': 'scale_info::53', 'Except': 'scale_info::53'}, 'portfolio': {'Whole': None, 'These': 'scale_info::59', 'Except': 'scale_info::59'}}, 'PortfolioCustody': {'did': '[u8; 32]', 'kind': {'Default': None, 'User': 'u64'}}, 'BecomeAgent': ('[u8; 12]', {'Full': None, 'Custom': 'u32', 'ExceptMeta': None, 'PolymeshV1CAA': None, 'PolymeshV1PIA': None}), 'AddRelayerPayingKey': ('AccountId', 'AccountId', 'u128'), 'RotatePrimaryKeyToSecondary': {'asset': {'Whole': None, 'These': 'scale_info::44', 'Except': 'scale_info::44'}, 'extrinsic': {'Whole': None, 'These': 'scale_info::53', 'Except': 'scale_info::53'}, 'portfolio': {'Whole': None, 'These': 'scale_info::59', 'Except': 'scale_info::59'}}}```
| None | `Option<Moment>` | ```(None, 'u64')```

---------
### AuthorizationConsumed
Authorization consumed.

(authorized_identity, authorized_key, auth_id)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Option<IdentityId>` | ```(None, '[u8; 32]')```
| None | `Option<AccountId>` | ```(None, 'AccountId')```
| None | `u64` | ```u64```

---------
### AuthorizationRejected
Authorization rejected by the user who was authorized.

(authorized_identity, authorized_key, auth_id)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Option<IdentityId>` | ```(None, '[u8; 32]')```
| None | `Option<AccountId>` | ```(None, 'AccountId')```
| None | `u64` | ```u64```

---------
### AuthorizationRetryLimitReached
Accepting Authorization retry limit reached.

(authorized_identity, authorized_key, auth_id)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Option<IdentityId>` | ```(None, '[u8; 32]')```
| None | `Option<AccountId>` | ```(None, 'AccountId')```
| None | `u64` | ```u64```

---------
### AuthorizationRevoked
Authorization revoked by the authorizer.

(authorized_identity, authorized_key, auth_id)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `Option<IdentityId>` | ```(None, '[u8; 32]')```
| None | `Option<AccountId>` | ```(None, 'AccountId')```
| None | `u64` | ```u64```

---------
### CddClaimsInvalidated
CDD claims generated by `IdentityId` (a CDD Provider) have been invalidated from
`Moment`.

(CDD provider DID, disable from date)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Moment` | ```u64```

---------
### CddRequirementForPrimaryKeyUpdated
CDD requirement for updating primary key changed.

(new_requirement)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `bool` | ```bool```

---------
### ChildDidCreated
Child identity created.

(Parent DID, Child DID, primary key)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```

---------
### ChildDidUnlinked
Child identity unlinked from parent identity.

(Caller DID, Parent DID, Child DID)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `IdentityId` | ```[u8; 32]```
| None | `IdentityId` | ```[u8; 32]```

---------
### ClaimAdded
Claim added to identity.

(DID, claim)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `IdentityClaim` | ```{'claim_issuer': '[u8; 32]', 'issuance_date': 'u64', 'last_update_date': 'u64', 'expiry': (None, 'u64'), 'claim': {'Accredited': {'Identity': '[u8; 32]', 'Ticker': '[u8; 12]', 'Custom': 'Bytes'}, 'Affiliate': {'Identity': '[u8; 32]', 'Ticker': '[u8; 12]', 'Custom': 'Bytes'}, 'BuyLockup': {'Identity': '[u8; 32]', 'Ticker': '[u8; 12]', 'Custom': 'Bytes'}, 'SellLockup': {'Identity': '[u8; 32]', 'Ticker': '[u8; 12]', 'Custom': 'Bytes'}, 'CustomerDueDiligence': '[u8; 32]', 'KnowYourCustomer': {'Identity': '[u8; 32]', 'Ticker': '[u8; 12]', 'Custom': 'Bytes'}, 'Jurisdiction': (('AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BV', 'BR', 'VG', 'IO', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CA', 'CV', 'KY', 'CF', 'TD', 'CL', 'CN', 'HK', 'MO', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'VA', 'HN', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'KP', 'KR', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MK', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'AN', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'SS', 'ES', 'LK', 'SD', 'SR', 'SJ', 'SZ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'GB', 'US', 'UM', 'UY', 'UZ', 'VU', 'VE', 'VN', 'VI', 'WF', 'EH', 'YE', 'ZM', 'ZW', 'BQ', 'CW', 'SX'), {'Identity': '[u8; 32]', 'Ticker': '[u8; 12]', 'Custom': 'Bytes'}), 'Exempted': {'Identity': '[u8; 32]', 'Ticker': '[u8; 12]', 'Custom': 'Bytes'}, 'Blocked': {'Identity': '[u8; 32]', 'Ticker': '[u8; 12]', 'Custom': 'Bytes'}, 'Custom': ('u32', (None, {'Identity': '[u8; 32]', 'Ticker': '[u8; 12]', 'Custom': 'Bytes'}))}}```

---------
### ClaimRevoked
Claim revoked from identity.

(DID, claim)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `IdentityClaim` | ```{'claim_issuer': '[u8; 32]', 'issuance_date': 'u64', 'last_update_date': 'u64', 'expiry': (None, 'u64'), 'claim': {'Accredited': {'Identity': '[u8; 32]', 'Ticker': '[u8; 12]', 'Custom': 'Bytes'}, 'Affiliate': {'Identity': '[u8; 32]', 'Ticker': '[u8; 12]', 'Custom': 'Bytes'}, 'BuyLockup': {'Identity': '[u8; 32]', 'Ticker': '[u8; 12]', 'Custom': 'Bytes'}, 'SellLockup': {'Identity': '[u8; 32]', 'Ticker': '[u8; 12]', 'Custom': 'Bytes'}, 'CustomerDueDiligence': '[u8; 32]', 'KnowYourCustomer': {'Identity': '[u8; 32]', 'Ticker': '[u8; 12]', 'Custom': 'Bytes'}, 'Jurisdiction': (('AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BA', 'BW', 'BV', 'BR', 'VG', 'IO', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CA', 'CV', 'KY', 'CF', 'TD', 'CL', 'CN', 'HK', 'MO', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'VA', 'HN', 'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE', 'KI', 'KP', 'KR', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI', 'LT', 'LU', 'MK', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR', 'NP', 'NL', 'AN', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'SS', 'ES', 'LK', 'SD', 'SR', 'SJ', 'SZ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'GB', 'US', 'UM', 'UY', 'UZ', 'VU', 'VE', 'VN', 'VI', 'WF', 'EH', 'YE', 'ZM', 'ZW', 'BQ', 'CW', 'SX'), {'Identity': '[u8; 32]', 'Ticker': '[u8; 12]', 'Custom': 'Bytes'}), 'Exempted': {'Identity': '[u8; 32]', 'Ticker': '[u8; 12]', 'Custom': 'Bytes'}, 'Blocked': {'Identity': '[u8; 32]', 'Ticker': '[u8; 12]', 'Custom': 'Bytes'}, 'Custom': ('u32', (None, {'Identity': '[u8; 32]', 'Ticker': '[u8; 12]', 'Custom': 'Bytes'}))}}```

---------
### CustomClaimTypeAdded
A new CustomClaimType was added.

(DID, id, Type)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `CustomClaimTypeId` | ```u32```
| None | `Vec<u8>` | ```Bytes```

---------
### DidCreated
Identity created.

(DID, primary key, secondary keys)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `Vec<SecondaryKey<AccountId>>` | ```[{'key': 'AccountId', 'permissions': {'asset': {'Whole': None, 'These': 'scale_info::44', 'Except': 'scale_info::44'}, 'extrinsic': {'Whole': None, 'These': 'scale_info::53', 'Except': 'scale_info::53'}, 'portfolio': {'Whole': None, 'These': 'scale_info::59', 'Except': 'scale_info::59'}}}]```

---------
### PrimaryKeyUpdated
Primary key of identity changed.

(DID, old primary key account ID, new ID)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `AccountId` | ```AccountId```

---------
### SecondaryKeyLeftIdentity
A secondary key left their identity.

(DID, secondary key)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```

---------
### SecondaryKeyPermissionsUpdated
Secondary key permissions updated.

(DID, updated secondary key, previous permissions, new permissions)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `AccountId` | ```AccountId```
| None | `Permissions` | ```{'asset': {'Whole': None, 'These': 'scale_info::44', 'Except': 'scale_info::44'}, 'extrinsic': {'Whole': None, 'These': 'scale_info::53', 'Except': 'scale_info::53'}, 'portfolio': {'Whole': None, 'These': 'scale_info::59', 'Except': 'scale_info::59'}}```
| None | `Permissions` | ```{'asset': {'Whole': None, 'These': 'scale_info::44', 'Except': 'scale_info::44'}, 'extrinsic': {'Whole': None, 'These': 'scale_info::53', 'Except': 'scale_info::53'}, 'portfolio': {'Whole': None, 'These': 'scale_info::59', 'Except': 'scale_info::59'}}```

---------
### SecondaryKeysAdded
Secondary keys added to identity.

(DID, new keys)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Vec<SecondaryKey<AccountId>>` | ```[{'key': 'AccountId', 'permissions': {'asset': {'Whole': None, 'These': 'scale_info::44', 'Except': 'scale_info::44'}, 'extrinsic': {'Whole': None, 'These': 'scale_info::53', 'Except': 'scale_info::53'}, 'portfolio': {'Whole': None, 'These': 'scale_info::59', 'Except': 'scale_info::59'}}}]```

---------
### SecondaryKeysFrozen
All Secondary keys of the identity ID are frozen.

(DID)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```

---------
### SecondaryKeysRemoved
Secondary keys removed from identity.

(DID, the keys that got removed)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```
| None | `Vec<AccountId>` | ```['AccountId']```

---------
### SecondaryKeysUnfrozen
All Secondary keys of the identity ID are unfrozen.

(DID)
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `IdentityId` | ```[u8; 32]```

---------
## Storage functions

---------
### AccountKeyRefCount
 How many &quot;strong&quot; references to the account key.

 Strong references will block a key from leaving it&#x27;s identity.

 Pallets using &quot;strong&quot; references to account keys:
 * Relayer: For `user_key` and `paying_key`


#### Python
```python
result = substrate.query(
    'Identity', 'AccountKeyRefCount', ['AccountId']
)
```

#### Return value
```python
'u64'
```
---------
### Authorizations
 All authorizations that an identity/key has

#### Python
```python
result = substrate.query(
    'Identity', 'Authorizations', [
    {
        'Account': 'AccountId',
        'Identity': '[u8; 32]',
    },
    'u64',
]
)
```

#### Return value
```python
{
    'auth_id': 'u64',
    'authorization_data': {
        'AddMultiSigSigner': 'AccountId',
        'AddRelayerPayingKey': ('AccountId', 'AccountId', 'u128'),
        'AttestPrimaryKeyRotation': '[u8; 32]',
        'BecomeAgent': (
            '[u8; 12]',
            {
                'Custom': 'u32',
                'ExceptMeta': None,
                'Full': None,
                'PolymeshV1CAA': None,
                'PolymeshV1PIA': None,
            },
        ),
        'JoinIdentity': {
            'asset': {
                'Except': 'scale_info::44',
                'These': 'scale_info::44',
                'Whole': None,
            },
            'extrinsic': {
                'Except': 'scale_info::53',
                'These': 'scale_info::53',
                'Whole': None,
            },
            'portfolio': {
                'Except': 'scale_info::59',
                'These': 'scale_info::59',
                'Whole': None,
            },
        },
        'PortfolioCustody': {
            'did': '[u8; 32]',
            'kind': {'Default': None, 'User': 'u64'},
        },
        'RotatePrimaryKey': None,
        'RotatePrimaryKeyToSecondary': {
            'asset': {
                'Except': 'scale_info::44',
                'These': 'scale_info::44',
                'Whole': None,
            },
            'extrinsic': {
                'Except': 'scale_info::53',
                'These': 'scale_info::53',
                'Whole': None,
            },
            'portfolio': {
                'Except': 'scale_info::59',
                'These': 'scale_info::59',
                'Whole': None,
            },
        },
        'TransferAssetOwnership': '[u8; 12]',
        'TransferTicker': '[u8; 12]',
    },
    'authorized_by': '[u8; 32]',
    'count': 'u32',
    'expiry': (None, 'u64'),
}
```
---------
### AuthorizationsGiven
 All authorizations that an identity has given. (Authorizer, auth_id -&gt; authorized)

#### Python
```python
result = substrate.query(
    'Identity', 'AuthorizationsGiven', ['[u8; 32]', 'u64']
)
```

#### Return value
```python
{'Account': 'AccountId', 'Identity': '[u8; 32]'}
```
---------
### CddAuthForPrimaryKeyRotation
 A config flag that, if set, instructs an authorization from a CDD provider in order to
 change the primary key of an identity.

#### Python
```python
result = substrate.query(
    'Identity', 'CddAuthForPrimaryKeyRotation', []
)
```

#### Return value
```python
'bool'
```
---------
### Claims
 (Target ID, claim type) (issuer,scope) -&gt; Associated claims

#### Python
```python
result = substrate.query(
    'Identity', 'Claims', [
    {
        'claim_type': {
            'Accredited': None,
            'Affiliate': None,
            'Blocked': None,
            'BuyLockup': None,
            'Custom': 'u32',
            'CustomerDueDiligence': None,
            'Exempted': None,
            'Jurisdiction': None,
            'KnowYourCustomer': None,
            'SellLockup': None,
        },
        'target': '[u8; 32]',
    },
    {
        'issuer': '[u8; 32]',
        'scope': (
            None,
            {
                'Custom': 'Bytes',
                'Identity': '[u8; 32]',
                'Ticker': '[u8; 12]',
            },
        ),
    },
]
)
```

#### Return value
```python
{
    'claim': {
        'Accredited': {
            'Custom': 'Bytes',
            'Identity': '[u8; 32]',
            'Ticker': '[u8; 12]',
        },
        'Affiliate': {
            'Custom': 'Bytes',
            'Identity': '[u8; 32]',
            'Ticker': '[u8; 12]',
        },
        'Blocked': {
            'Custom': 'Bytes',
            'Identity': '[u8; 32]',
            'Ticker': '[u8; 12]',
        },
        'BuyLockup': {
            'Custom': 'Bytes',
            'Identity': '[u8; 32]',
            'Ticker': '[u8; 12]',
        },
        'Custom': (
            'u32',
            (
                None,
                {
                    'Custom': 'Bytes',
                    'Identity': '[u8; 32]',
                    'Ticker': '[u8; 12]',
                },
            ),
        ),
        'CustomerDueDiligence': '[u8; 32]',
        'Exempted': {
            'Custom': 'Bytes',
            'Identity': '[u8; 32]',
            'Ticker': '[u8; 12]',
        },
        'Jurisdiction': (
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
            {'Custom': 'Bytes', 'Identity': '[u8; 32]', 'Ticker': '[u8; 12]'},
        ),
        'KnowYourCustomer': {
            'Custom': 'Bytes',
            'Identity': '[u8; 32]',
            'Ticker': '[u8; 12]',
        },
        'SellLockup': {
            'Custom': 'Bytes',
            'Identity': '[u8; 32]',
            'Ticker': '[u8; 12]',
        },
    },
    'claim_issuer': '[u8; 32]',
    'expiry': (None, 'u64'),
    'issuance_date': 'u64',
    'last_update_date': 'u64',
}
```
---------
### CurrentDid
 It stores the current identity for current transaction.

#### Python
```python
result = substrate.query(
    'Identity', 'CurrentDid', []
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### CurrentPayer
 It stores the current gas fee payer for the current transaction

#### Python
```python
result = substrate.query(
    'Identity', 'CurrentPayer', []
)
```

#### Return value
```python
'AccountId'
```
---------
### CustomClaimIdSequence
 The next `CustomClaimTypeId`.

#### Python
```python
result = substrate.query(
    'Identity', 'CustomClaimIdSequence', []
)
```

#### Return value
```python
'u32'
```
---------
### CustomClaims
 CustomClaimTypeId -&gt; String constant

#### Python
```python
result = substrate.query(
    'Identity', 'CustomClaims', ['u32']
)
```

#### Return value
```python
'Bytes'
```
---------
### CustomClaimsInverse
 String constant -&gt; CustomClaimTypeId

#### Python
```python
result = substrate.query(
    'Identity', 'CustomClaimsInverse', ['Bytes']
)
```

#### Return value
```python
'u32'
```
---------
### DidKeys
 A reverse double map to allow finding all keys for an identity.

#### Python
```python
result = substrate.query(
    'Identity', 'DidKeys', ['[u8; 32]', 'AccountId']
)
```

#### Return value
```python
'bool'
```
---------
### DidRecords
 DID -&gt; identity info

#### Python
```python
result = substrate.query(
    'Identity', 'DidRecords', ['[u8; 32]']
)
```

#### Return value
```python
{'primary_key': (None, 'AccountId')}
```
---------
### IsDidFrozen
 DID -&gt; bool that indicates if secondary keys are frozen.

#### Python
```python
result = substrate.query(
    'Identity', 'IsDidFrozen', ['[u8; 32]']
)
```

#### Return value
```python
'bool'
```
---------
### KeyRecords
 Map from AccountId to `KeyRecord` that holds the key&#x27;s identity and permissions.

#### Python
```python
result = substrate.query(
    'Identity', 'KeyRecords', ['AccountId']
)
```

#### Return value
```python
{
    'MultiSigSignerKey': 'AccountId',
    'PrimaryKey': '[u8; 32]',
    'SecondaryKey': (
        '[u8; 32]',
        {
            'asset': {
                'Except': 'scale_info::44',
                'These': 'scale_info::44',
                'Whole': None,
            },
            'extrinsic': {
                'Except': 'scale_info::53',
                'These': 'scale_info::53',
                'Whole': None,
            },
            'portfolio': {
                'Except': 'scale_info::59',
                'These': 'scale_info::59',
                'Whole': None,
            },
        },
    ),
}
```
---------
### MultiPurposeNonce
 Nonce to ensure unique actions. starts from 1.

#### Python
```python
result = substrate.query(
    'Identity', 'MultiPurposeNonce', []
)
```

#### Return value
```python
'u64'
```
---------
### OffChainAuthorizationNonce
 Authorization nonce per Identity. Initially is 0.

#### Python
```python
result = substrate.query(
    'Identity', 'OffChainAuthorizationNonce', ['[u8; 32]']
)
```

#### Return value
```python
'u64'
```
---------
### ParentDid
 Parent identity if the DID is a child Identity.

#### Python
```python
result = substrate.query(
    'Identity', 'ParentDid', ['[u8; 32]']
)
```

#### Return value
```python
'[u8; 32]'
```
---------
### StorageVersion
 Storage version.

#### Python
```python
result = substrate.query(
    'Identity', 'StorageVersion', []
)
```

#### Return value
```python
'u8'
```
---------
## Constants

---------
### InitialPOLYX
#### Value
```python
0
```
#### Python
```python
constant = substrate.get_constant('Identity', 'InitialPOLYX')
```
---------
## Errors

---------
### AccountKeyIsBeingUsed
The account key is being used, it can&\#x27;t be unlinked.

---------
### AlreadyLinked
One secondary or primary key can only belong to one DID

---------
### AuthorizationExpired
The offchain authorization has expired.

---------
### AuthorizationHasBeenRevoked
Authorization has been explicitly revoked.

---------
### AuthorizationsNotForSameDids
Authorizations are not for the same DID.

---------
### CannotDecodeSignerAccountId
Cannot convert a `T::AccountId` to `AnySignature::Signer::AccountId`.

---------
### ClaimDoesNotExist
Claim does not exist.

---------
### CustomClaimTypeAlreadyExists
The custom claim type trying to be registered already exists.

---------
### CustomClaimTypeDoesNotExist
The custom claim type does not exist.

---------
### CustomScopeTooLong
A custom scope is too long.
It can at most be `32` characters long.

---------
### DidAlreadyExists
The DID already exists.

---------
### DidDoesNotExist
The DID does not exist.

---------
### DidMustAlreadyExist
The DID must already exist.

---------
### DuplicateKey
The same key was included multiple times.

---------
### ExceptNotAllowedForExtrinsics
Cannot use Except when specifying extrinsic permissions.

---------
### FailedToChargeFee
Couldn&\#x27;t charge fee for the transaction.

---------
### InvalidAccountKey
Account Id cannot be extracted from signer

---------
### InvalidAuthorizationFromCddProvider
An invalid authorization from the CDD provider.

---------
### InvalidAuthorizationFromOwner
An invalid authorization from the owner.

---------
### InvalidAuthorizationSignature
An invalid authorization signature.

---------
### IsChildIdentity
Identity is already a child of an other identity, can&\#x27;t create grand-child identity.

---------
### KeyNotAllowed
This key is not allowed to execute a given operation.

---------
### MissingCurrentIdentity
Missing current identity on the transaction

---------
### MultiSigHasBalance
Multisig can not be unlinked from an identity while it still holds POLYX

---------
### NoParentIdentity
The Identity doesn&\#x27;t have a parent identity.

---------
### NotASigner
Signer is not a secondary key of the provided identity

---------
### NotCddProviderAttestation
Attestation was not by a CDD service provider.

---------
### NotParentOrChildIdentity
The caller is not the parent or child identity.

---------
### NotPrimaryKey
Only the primary key is allowed to revoke an Identity Signatory off-chain authorization.

---------
### SecondaryKeysContainPrimaryKey
The secondary keys contain the primary key.

---------
### TargetHasNoCdd
The target DID has no valid CDD.

---------
### UnAuthorizedCddProvider
Only CDD service providers are allowed.

---------
### Unauthorized
Signatory is not pre authorized by the identity

---------