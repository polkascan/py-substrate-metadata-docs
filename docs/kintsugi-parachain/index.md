# kintsugi

---------

## Properties
| Name | Value |
| -------- | -------- |
| Spec name     | kintsugi-parachain     |
| Implementation name     | kintsugi-parachain     |
| Spec version     | 1022000     |
| SS58 Format     | 2092     |
| Token symbol      | ['KINT', 'KBTC', 'KSM', 'INTR', 'IBTC', 'DOT']     |
| Token decimals      | [12, 8, 12, 10, 8, 10]     |

## Pallets
| Name | Calls | Events | Storage functions | Constants | Errors |
| -------- | -------- | -------- | -------- | -------- | -------- |
| [AssetRegistry](assetregistry.md) | [2](assetregistry.md#calls) | [2](assetregistry.md#events) | [3](assetregistry.md#storage-functions) | [0](assetregistry.md#constants) | [5](assetregistry.md#errors) |
| [Aura](aura.md) | [0](aura.md#calls) | [0](aura.md#events) | [2](aura.md#storage-functions) | [0](aura.md#constants) | [0](aura.md#errors) |
| [AuraExt](auraext.md) | [0](auraext.md#calls) | [0](auraext.md#events) | [1](auraext.md#storage-functions) | [0](auraext.md#constants) | [0](auraext.md#errors) |
| [Authorship](authorship.md) | [1](authorship.md#calls) | [0](authorship.md#events) | [3](authorship.md#storage-functions) | [1](authorship.md#constants) | [7](authorship.md#errors) |
| [BTCRelay](btcrelay.md) | [5](btcrelay.md#calls) | [5](btcrelay.md#events) | [12](btcrelay.md#storage-functions) | [1](btcrelay.md#constants) | [49](btcrelay.md#errors) |
| [ClientsInfo](clientsinfo.md) | [2](clientsinfo.md#calls) | [2](clientsinfo.md#events) | [2](clientsinfo.md#storage-functions) | [0](clientsinfo.md#constants) | [0](clientsinfo.md#errors) |
| [CollatorSelection](collatorselection.md) | [5](collatorselection.md#calls) | [5](collatorselection.md#events) | [5](collatorselection.md#storage-functions) | [0](collatorselection.md#constants) | [10](collatorselection.md#errors) |
| [CumulusXcm](cumulusxcm.md) | [0](cumulusxcm.md#calls) | [3](cumulusxcm.md#events) | [0](cumulusxcm.md#storage-functions) | [0](cumulusxcm.md#constants) | [0](cumulusxcm.md#errors) |
| [Currency](currency.md) | [0](currency.md#calls) | [0](currency.md#events) | [0](currency.md#storage-functions) | [3](currency.md#constants) | [2](currency.md#errors) |
| [Democracy](democracy.md) | [10](democracy.md#calls) | [8](democracy.md#events) | [8](democracy.md#storage-functions) | [7](democracy.md#constants) | [16](democracy.md#errors) |
| [DmpQueue](dmpqueue.md) | [1](dmpqueue.md#calls) | [6](dmpqueue.md#events) | [4](dmpqueue.md#storage-functions) | [0](dmpqueue.md#constants) | [2](dmpqueue.md#errors) |
| [Escrow](escrow.md) | [6](escrow.md#calls) | [2](escrow.md#events) | [9](escrow.md#storage-functions) | [2](escrow.md#constants) | [12](escrow.md#errors) |
| [EscrowAnnuity](escrowannuity.md) | [3](escrowannuity.md#calls) | [1](escrowannuity.md#events) | [2](escrowannuity.md#storage-functions) | [2](escrowannuity.md#constants) | [0](escrowannuity.md#errors) |
| [EscrowRewards](escrowrewards.md) | [0](escrowrewards.md#calls) | [4](escrowrewards.md#events) | [6](escrowrewards.md#storage-functions) | [2](escrowrewards.md#constants) | [3](escrowrewards.md#errors) |
| [Fee](fee.md) | [8](fee.md#calls) | [0](fee.md#events) | [8](fee.md#storage-functions) | [2](fee.md#constants) | [2](fee.md#errors) |
| [Identity](identity.md) | [15](identity.md#calls) | [10](identity.md#events) | [4](identity.md#storage-functions) | [6](identity.md#constants) | [18](identity.md#errors) |
| [Issue](issue.md) | [4](issue.md#calls) | [5](issue.md#events) | [4](issue.md#storage-functions) | [1](issue.md#constants) | [9](issue.md#errors) |
| [Multisig](multisig.md) | [4](multisig.md#calls) | [4](multisig.md#events) | [1](multisig.md#storage-functions) | [3](multisig.md#constants) | [14](multisig.md#errors) |
| [Nomination](nomination.md) | [6](nomination.md#calls) | [4](nomination.md#events) | [3](nomination.md#storage-functions) | [0](nomination.md#constants) | [7](nomination.md#errors) |
| [Oracle](oracle.md) | [3](oracle.md#calls) | [4](oracle.md#events) | [7](oracle.md#storage-functions) | [0](oracle.md#constants) | [3](oracle.md#errors) |
| [ParachainInfo](parachaininfo.md) | [0](parachaininfo.md#calls) | [0](parachaininfo.md#events) | [1](parachaininfo.md#storage-functions) | [0](parachaininfo.md#constants) | [0](parachaininfo.md#errors) |
| [ParachainSystem](parachainsystem.md) | [4](parachainsystem.md#calls) | [6](parachainsystem.md#events) | [21](parachainsystem.md#storage-functions) | [0](parachainsystem.md#constants) | [8](parachainsystem.md#errors) |
| [PolkadotXcm](polkadotxcm.md) | [10](polkadotxcm.md#calls) | [17](polkadotxcm.md#events) | [9](polkadotxcm.md#storage-functions) | [0](polkadotxcm.md#constants) | [13](polkadotxcm.md#errors) |
| [Preimage](preimage.md) | [4](preimage.md#calls) | [3](preimage.md#events) | [2](preimage.md#storage-functions) | [0](preimage.md#constants) | [6](preimage.md#errors) |
| [Proxy](proxy.md) | [10](proxy.md#calls) | [5](proxy.md#events) | [2](proxy.md#storage-functions) | [6](proxy.md#constants) | [8](proxy.md#errors) |
| [Redeem](redeem.md) | [7](redeem.md#calls) | [7](redeem.md#events) | [5](redeem.md#storage-functions) | [0](redeem.md#constants) | [9](redeem.md#errors) |
| [Replace](replace.md) | [6](replace.md#calls) | [6](replace.md#events) | [4](replace.md#storage-functions) | [0](replace.md#constants) | [11](replace.md#errors) |
| [Scheduler](scheduler.md) | [6](scheduler.md#calls) | [6](scheduler.md#events) | [3](scheduler.md#storage-functions) | [2](scheduler.md#constants) | [5](scheduler.md#errors) |
| [Security](security.md) | [3](security.md#calls) | [2](security.md#events) | [4](security.md#storage-functions) | [0](security.md#constants) | [1](security.md#errors) |
| [Session](session.md) | [2](session.md#calls) | [1](session.md#events) | [7](session.md#storage-functions) | [0](session.md#constants) | [5](session.md#errors) |
| [Sudo](sudo.md) | [4](sudo.md#calls) | [3](sudo.md#events) | [1](sudo.md#storage-functions) | [0](sudo.md#constants) | [1](sudo.md#errors) |
| [Supply](supply.md) | [1](supply.md#calls) | [1](supply.md#events) | [3](supply.md#storage-functions) | [2](supply.md#constants) | [0](supply.md#errors) |
| [System](system.md) | [8](system.md#calls) | [6](system.md#events) | [16](system.md#storage-functions) | [6](system.md#constants) | [6](system.md#errors) |
| [TechnicalCommittee](technicalcommittee.md) | [7](technicalcommittee.md#calls) | [7](technicalcommittee.md#events) | [6](technicalcommittee.md#storage-functions) | [0](technicalcommittee.md#constants) | [10](technicalcommittee.md#errors) |
| [TechnicalMembership](technicalmembership.md) | [7](technicalmembership.md#calls) | [6](technicalmembership.md#events) | [2](technicalmembership.md#storage-functions) | [0](technicalmembership.md#constants) | [3](technicalmembership.md#errors) |
| [Timestamp](timestamp.md) | [1](timestamp.md#calls) | [0](timestamp.md#events) | [2](timestamp.md#storage-functions) | [1](timestamp.md#constants) | [0](timestamp.md#errors) |
| [Tokens](tokens.md) | [5](tokens.md#calls) | [13](tokens.md#events) | [4](tokens.md#storage-functions) | [2](tokens.md#constants) | [8](tokens.md#errors) |
| [TransactionPayment](transactionpayment.md) | [0](transactionpayment.md#calls) | [1](transactionpayment.md#events) | [2](transactionpayment.md#storage-functions) | [1](transactionpayment.md#constants) | [0](transactionpayment.md#errors) |
| [Treasury](treasury.md) | [5](treasury.md#calls) | [9](treasury.md#events) | [4](treasury.md#storage-functions) | [7](treasury.md#constants) | [5](treasury.md#errors) |
| [TxPause](txpause.md) | [2](txpause.md#calls) | [2](txpause.md#events) | [1](txpause.md#storage-functions) | [2](txpause.md#constants) | [4](txpause.md#errors) |
| [UnknownTokens](unknowntokens.md) | [0](unknowntokens.md#calls) | [2](unknowntokens.md#events) | [2](unknowntokens.md#storage-functions) | [0](unknowntokens.md#constants) | [3](unknowntokens.md#errors) |
| [Utility](utility.md) | [6](utility.md#calls) | [6](utility.md#events) | [0](utility.md#storage-functions) | [1](utility.md#constants) | [1](utility.md#errors) |
| [VaultAnnuity](vaultannuity.md) | [3](vaultannuity.md#calls) | [1](vaultannuity.md#events) | [2](vaultannuity.md#storage-functions) | [2](vaultannuity.md#constants) | [0](vaultannuity.md#errors) |
| [VaultCapacity](vaultcapacity.md) | [0](vaultcapacity.md#calls) | [4](vaultcapacity.md#events) | [6](vaultcapacity.md#storage-functions) | [2](vaultcapacity.md#constants) | [3](vaultcapacity.md#errors) |
| [VaultRegistry](vaultregistry.md) | [11](vaultregistry.md#calls) | [22](vaultregistry.md#events) | [12](vaultregistry.md#storage-functions) | [2](vaultregistry.md#constants) | [27](vaultregistry.md#errors) |
| [VaultRewards](vaultrewards.md) | [0](vaultrewards.md#calls) | [4](vaultrewards.md#events) | [6](vaultrewards.md#storage-functions) | [2](vaultrewards.md#constants) | [3](vaultrewards.md#errors) |
| [VaultStaking](vaultstaking.md) | [0](vaultstaking.md#calls) | [6](vaultstaking.md#events) | [9](vaultstaking.md#storage-functions) | [1](vaultstaking.md#constants) | [3](vaultstaking.md#errors) |
| [Vesting](vesting.md) | [4](vesting.md#calls) | [3](vesting.md#events) | [1](vesting.md#storage-functions) | [1](vesting.md#constants) | [6](vesting.md#errors) |
| [XTokens](xtokens.md) | [6](xtokens.md#calls) | [1](xtokens.md#events) | [0](xtokens.md#storage-functions) | [2](xtokens.md#constants) | [19](xtokens.md#errors) |
| [XcmpQueue](xcmpqueue.md) | [9](xcmpqueue.md#calls) | [8](xcmpqueue.md#events) | [9](xcmpqueue.md#storage-functions) | [0](xcmpqueue.md#constants) | [5](xcmpqueue.md#errors) |