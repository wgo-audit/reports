# Component And Contract Boundaries

## Purpose And Evidence Boundary

- Reader question: Which source components and integration contracts share the Community application boundary, and where does unavailable Pro/external code begin?
- Evidence cutoff: 2026-08-06; Community `3.1.7` / `a2d8b855…`.
- Confirmed notation: solid node/edge present in pinned source.
- Inferred notation: dotted relationship is a source-supported consequence, not runtime proof.
- Unknown notation: dashed edge/node requires vendor, target or live evidence.
- Evidence links: [component packet](../../../evidence/packets/architecture-component-api-ui-contracts.md); [ADR-001](../adr/ADR-001-modular-monolith-and-ui-boundary.md); [ADR-003](../adr/ADR-003-edition-specific-integration-boundary.md).

## Evidence Dimensions Used

Implementation and approved public edition statements are present. Runtime, ownership/approval, commercial entitlement, Pro implementation and consumer acceptance are unknown.

## Diagram

```mermaid
flowchart TB
  subgraph CLIENTS["Confirmed source-facing clients"]
    direction LR
    ADMIN["Authenticated admin browser"]
    SIGNER["Public signer browser"]
    REST["REST client"]
    MCP["MCP client"]
  end
  subgraph APP["Confirmed Community Rails application"]
    direction LR
    ROUTES["One Rails route set"] --> UI["ERB and Turbo views"]
    UI --> VUE["Vue builder and signer islands"]
    ROUTES --> API["Community API controllers and serializers"]
    ROUTES --> DOMAIN["Templates, Submissions, Submitters, WebhookUrls"]
    ROUTES --> MCPA["MCP adapter"]
  end
  subgraph CONTRACTS["Confirmed Community contracts"]
    direction LR
    JSON["Implicit template and signer JSON"]
    WH["Webhook envelope and parallel schemas"]
  end
  subgraph DOCUMENTED["Documented applicability not established"]
    direction LR
    OPENAPI["Hosted-server OpenAPI document"]
  end
  subgraph OUTSIDE["Outside inspected implementation"]
    direction LR
    PRO["Pro extensions and entitlement"]
    EMBED["External embed packages and CDN"]
    ORG["Organization web/mobile adapter"]
  end
  CLIENTS --> APP
  APP --> CONTRACTS
  APP -. "release/edition alignment unknown" .-> DOCUMENTED
  APP -. "extension hooks; implementation unknown" .-> PRO
  PRO -. "package/host contract unknown" .-> EMBED
  ORG -. "target integration undecided" .-> APP
```

## Known Gaps And Follow-Up

OI-001/OI-005 must resolve edition entitlement, release-specific alignment between Community routes/serializers and the hosted OpenAPI, Pro package contracts/module topology, supported clients and whether an organization-owned adapter is required. The diagram does not prove live co-location or target acceptance.
