# Revenue-Critical Boundaries

```mermaid
flowchart TB
  subgraph CLAIM["Claim and demand boundary"]
    direction LR
    SALES["Prospect, sale, or onboarding intent"] -. "unproved claim approval" .-> GATE["UNKNOWN approved claim and eligibility gate"]
    ARRIVAL["UNKNOWN low/base/high arrivals and value inputs"] -. "approved scenario" .-> GATE
  end

  subgraph ENTRY["Release and integration boundary"]
    direction LR
    CONTRACT["UNKNOWN Community/Pro entitlement and release contract"] -. "must authorize" .-> CLIENT["UNKNOWN organization web/mobile client"]
    CLIENT -. "unobserved target path" .-> DS["Community signing entry points"]
  end

  subgraph CORE["Source-visible signing core"]
    direction LR
    DS --> SQL["Validated signer state and SQL completion"]
    SQL --> QUEUE["Redis/Sidekiq finalization"]
    QUEUE --> ART["Result/audit artifacts"]
    QUEUE --> DEL["Mail and webhook delivery"]
  end

  subgraph READY["Organization readiness and business consequence"]
    direction LR
    ART -. "unproved artifact acceptance" .-> ORACLE["UNKNOWN accepted evidence/readiness oracle"]
    DEL -. "unproved delivery acceptance" .-> ORACLE
    ORACLE -. "only after approval" .-> ACTIVATE["UNKNOWN customer activation or revenue event"]
    PAUSE["Approved interruption pause"] -. "reconcile and controlled resume" .-> ORACLE
  end

  OPS["UNKNOWN measured 99.5% signing / 99% onboarding, 2h RPO, recovery and catch-up"] -. "operating acceptance" .-> ORACLE
  CLAIMAUTH["UNKNOWN legal, compliance, CISO, Product, Operations, and commercial approvals"] -. "claim authority" .-> GATE
```

Solid edges show implemented Community source transitions only. Dotted edges show unproved organization, edition, authority, readiness, and operating boundaries. The diagram does not assert production traffic, revenue recognition rules, contract behavior, loss, probability, or achieved service levels.
