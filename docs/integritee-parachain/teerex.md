
# Teerex

---------
## Calls

---------
### register_quoting_enclave
#### Attributes
| Name | Type |
| -------- | -------- | 
| enclave_identity | `Vec<u8>` | 
| signature | `Vec<u8>` | 
| certificate_chain | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Teerex', 'register_quoting_enclave', {
    'certificate_chain': 'Bytes',
    'enclave_identity': 'Bytes',
    'signature': 'Bytes',
}
)
```

---------
### register_sgx_enclave
#### Attributes
| Name | Type |
| -------- | -------- | 
| proof | `Vec<u8>` | 
| worker_url | `Option<Vec<u8>>` | 
| attestation_method | `SgxAttestationMethod` | 

#### Python
```python
call = substrate.compose_call(
    'Teerex', 'register_sgx_enclave', {
    'attestation_method': {
        'Dcap': {'proxied': 'bool'},
        'Ias': None,
        'Skip': {'proxied': 'bool'},
    },
    'proof': 'Bytes',
    'worker_url': (None, 'Bytes'),
}
)
```

---------
### register_tcb_info
#### Attributes
| Name | Type |
| -------- | -------- | 
| tcb_info | `Vec<u8>` | 
| signature | `Vec<u8>` | 
| certificate_chain | `Vec<u8>` | 

#### Python
```python
call = substrate.compose_call(
    'Teerex', 'register_tcb_info', {
    'certificate_chain': 'Bytes',
    'signature': 'Bytes',
    'tcb_info': 'Bytes',
}
)
```

---------
### set_security_flags
#### Attributes
| Name | Type |
| -------- | -------- | 
| allow_skipping_attestation | `bool` | 
| sgx_allow_debug_mode | `bool` | 

#### Python
```python
call = substrate.compose_call(
    'Teerex', 'set_security_flags', {
    'allow_skipping_attestation': 'bool',
    'sgx_allow_debug_mode': 'bool',
}
)
```

---------
### unregister_proxied_enclave
#### Attributes
| Name | Type |
| -------- | -------- | 
| address | `EnclaveInstanceAddress<T::AccountId>` | 

#### Python
```python
call = substrate.compose_call(
    'Teerex', 'unregister_proxied_enclave', {
    'address': {
        'fingerprint': '[u8; 32]',
        'registrar': 'AccountId',
        'signer': {
            'Known': {
                'Ecdsa': '[u8; 33]',
                'Ed25519': '[u8; 32]',
                'Sr25519': '[u8; 32]',
            },
            'Opaque': 'Bytes',
        },
    },
}
)
```

---------
### unregister_sovereign_enclave
#### Attributes
| Name | Type |
| -------- | -------- | 
| enclave_signer | `T::AccountId` | 

#### Python
```python
call = substrate.compose_call(
    'Teerex', 'unregister_sovereign_enclave', {'enclave_signer': 'AccountId'}
)
```

---------
## Events

---------
### AddedSgxEnclave
An Intel SGX enclave has been added to the enclave registry
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| registered_by | `T::AccountId` | ```AccountId```
| worker_url | `Option<Vec<u8>>` | ```(None, 'Bytes')```
| tcb_status | `Option<SgxStatus>` | ```(None, ('Invalid', 'Ok', 'GroupOutOfDate', 'GroupRevoked', 'ConfigurationNeeded'))```
| attestation_method | `SgxAttestationMethod` | ```{'Skip': {'proxied': 'bool'}, 'Ias': None, 'Dcap': {'proxied': 'bool'}}```

---------
### RemovedProxiedEnclave
a proxied enclave has been removed from the enclave registry
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `EnclaveInstanceAddress<T::AccountId>` | ```{'fingerprint': '[u8; 32]', 'registrar': 'AccountId', 'signer': {'Opaque': 'Bytes', 'Known': {'Ed25519': '[u8; 32]', 'Sr25519': '[u8; 32]', 'Ecdsa': '[u8; 33]'}}}```

---------
### RemovedSovereignEnclave
a sovereign enclave has been removed from the enclave registry
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| None | `T::AccountId` | ```AccountId```

---------
### SgxQuotingEnclaveRegistered
An Intel SGX quoting enclave has been registered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| quoting_enclave | `SgxQuotingEnclave` | ```{'issue_date': 'u64', 'next_update': 'u64', 'miscselect': '[u8; 4]', 'miscselect_mask': '[u8; 4]', 'attributes': '[u8; 16]', 'attributes_mask': '[u8; 16]', 'mrsigner': '[u8; 32]', 'isvprodid': 'u16', 'tcb': [{'isvsvn': 'u16'}]}```

---------
### SgxTcbInfoRegistered
Intel SGX TCB info has been registered
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| fmspc | `Fmspc` | ```[u8; 6]```
| on_chain_info | `SgxTcbInfoOnChain` | ```{'issue_date': 'u64', 'next_update': 'u64', 'tcb_levels': [{'cpusvn': '[u8; 16]', 'pcesvn': 'u16', 'tcb_status': ('Unknown', 'UpToDate', 'SWHardeningNeeded', 'ConfigurationAndSWHardeningNeeded', 'OutOfDate', 'OutOfDateConfigurationNeeded', 'Revoked')}]}```

---------
### UpdatedSecurityFlags
the enclave registry security flags have been updated
#### Attributes
| Name | Type | Composition
| -------- | -------- | -------- |
| allow_skipping_attestation | `bool` | ```bool```
| sgx_allow_debug_mode | `bool` | ```bool```

---------
## Storage functions

---------
### AllowSkippingAttestation

#### Python
```python
result = substrate.query(
    'Teerex', 'AllowSkippingAttestation', []
)
```

#### Return value
```python
'bool'
```
---------
### ProxiedEnclaves

#### Python
```python
result = substrate.query(
    'Teerex', 'ProxiedEnclaves', [
    {
        'fingerprint': '[u8; 32]',
        'registrar': 'AccountId',
        'signer': {
            'Known': {
                'Ecdsa': '[u8; 33]',
                'Ed25519': '[u8; 32]',
                'Sr25519': '[u8; 32]',
            },
            'Opaque': 'Bytes',
        },
    },
]
)
```

#### Return value
```python
{
    'Sgx': {
        'attestation_method': {
            'Dcap': {'proxied': 'bool'},
            'Ias': None,
            'Skip': {'proxied': 'bool'},
        },
        'build_mode': ('Debug', 'Production'),
        'mr_enclave': '[u8; 32]',
        'mr_signer': '[u8; 32]',
        'report_data': {'d': '[u8; 64]'},
        'status': (
            'Invalid',
            'Ok',
            'GroupOutOfDate',
            'GroupRevoked',
            'ConfigurationNeeded',
        ),
        'timestamp': 'u64',
        'url': (None, 'Bytes'),
    },
}
```
---------
### SgxAllowDebugMode

#### Python
```python
result = substrate.query(
    'Teerex', 'SgxAllowDebugMode', []
)
```

#### Return value
```python
'bool'
```
---------
### SgxQuotingEnclaveRegistry

#### Python
```python
result = substrate.query(
    'Teerex', 'SgxQuotingEnclaveRegistry', []
)
```

#### Return value
```python
{
    'attributes': '[u8; 16]',
    'attributes_mask': '[u8; 16]',
    'issue_date': 'u64',
    'isvprodid': 'u16',
    'miscselect': '[u8; 4]',
    'miscselect_mask': '[u8; 4]',
    'mrsigner': '[u8; 32]',
    'next_update': 'u64',
    'tcb': [{'isvsvn': 'u16'}],
}
```
---------
### SgxTcbInfo

#### Python
```python
result = substrate.query(
    'Teerex', 'SgxTcbInfo', ['[u8; 6]']
)
```

#### Return value
```python
{
    'issue_date': 'u64',
    'next_update': 'u64',
    'tcb_levels': [
        {
            'cpusvn': '[u8; 16]',
            'pcesvn': 'u16',
            'tcb_status': (
                'Unknown',
                'UpToDate',
                'SWHardeningNeeded',
                'ConfigurationAndSWHardeningNeeded',
                'OutOfDate',
                'OutOfDateConfigurationNeeded',
                'Revoked',
            ),
        },
    ],
}
```
---------
### SovereignEnclaves

#### Python
```python
result = substrate.query(
    'Teerex', 'SovereignEnclaves', ['AccountId']
)
```

#### Return value
```python
{
    'Sgx': {
        'attestation_method': {
            'Dcap': {'proxied': 'bool'},
            'Ias': None,
            'Skip': {'proxied': 'bool'},
        },
        'build_mode': ('Debug', 'Production'),
        'mr_enclave': '[u8; 32]',
        'mr_signer': '[u8; 32]',
        'report_data': {'d': '[u8; 64]'},
        'status': (
            'Invalid',
            'Ok',
            'GroupOutOfDate',
            'GroupRevoked',
            'ConfigurationNeeded',
        ),
        'timestamp': 'u64',
        'url': (None, 'Bytes'),
    },
}
```
---------
## Constants

---------
### MaxAttestationRenewalPeriod
 If a worker does not re-register within `MaxAttestationRenewalPeriod`, it can be unregistered by anyone.
#### Value
```python
172800000
```
#### Python
```python
constant = substrate.get_constant('Teerex', 'MaxAttestationRenewalPeriod')
```
---------
### MomentsPerDay
#### Value
```python
86400000
```
#### Python
```python
constant = substrate.get_constant('Teerex', 'MomentsPerDay')
```
---------
## Errors

---------
### CaVerificationFailed

---------
### CertificateChainIsInvalid

---------
### CertificateChainIsTooShort

---------
### CollateralIsInvalid
The provided collateral data is invalid

---------
### CpuSvnDecodingError

---------
### CpuSvnLengthMismatch

---------
### CpuSvnOidIsMissing

---------
### DcapKeyTypeMismatch

---------
### DcapQuoteDecodingError

---------
### DcapQuoteIsTooLong

---------
### DcapQuoteVersionMismatch

---------
### DerEncodingError

---------
### EmptyEnclaveRegistry
No enclave is registered.

---------
### EnclaveIdentityDecodingError

---------
### EnclaveIdentitySignatureIsInvalid

---------
### EnclaveIsNotRegistered
The enclave is not registered.

---------
### EnclaveSignerDecodeError
Failed to decode enclave signer.

---------
### EnclaveUrlIsTooLong
The worker url is too long.

---------
### FmspcDecodingError

---------
### FmspcLengthMismatch

---------
### FmspcOidIsMissing

---------
### IntelExtensionAmbiguity

---------
### IntelExtensionCertificateDecodingError

---------
### IsvEnclaveReportSignatureIsInvalid

---------
### KeyLengthIsInvalid

---------
### LeafCertificateParsingError

---------
### MissingTcbInfoForFmspc
No TCB info could be found onchain for the examinee&\#x27;s fmspc

---------
### NetscapeDecodingError

---------
### NetscapeDerError

---------
### OtherSgxVerifyError
An error originating in the sgx_verify crate

---------
### PceSvnDecodingError

---------
### PceSvnLengthMismatch

---------
### PceSvnOidIsMissing

---------
### PckCertFormatMismatch

---------
### PublicKeyIsInvalid

---------
### QeHasRejectedEnclave

---------
### QeReportHashMismatch

---------
### QuoteBodyDecodingError

---------
### QuoteBodyIsInvalid

---------
### QuoteBodyMissing

---------
### QuoteStatusMissing

---------
### RaProofIsTooLong
The Remote Attestation proof is too long.

---------
### RemoteAttestationIsTooOld
IAS remote attestation is too old

---------
### RemoteAttestationVerificationFailed
Verifying RA report failed.

---------
### RsaSignatureIsInvalid

---------
### SenderIsNotAttestedEnclave
Sender does not match attested enclave in report.

---------
### SgxModeIsNotAllowed
The enclave cannot attest, because its building mode is not allowed.

---------
### SgxReportParsingError

---------
### SkippingAttestationIsNotAllowed
skipping attestation not allowed by configuration

---------
### TcbInfoIsInvalid

---------
### TcbInfoIsOutdated
Either the enclave TCB has outdated status or the onchain TCB collateral is outdated

---------
### TimestampIsInvalid

---------
### TimestampIsMissing

---------
### UnregisterActiveEnclaveIsNotAllowed
It is not allowed to unregister enclaves with recent activity

---------