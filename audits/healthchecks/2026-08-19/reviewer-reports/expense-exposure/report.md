# Expense Exposure

## Audit Question, Depth, And Evidence Boundary

This detailed review asks what actual or potential cash and interruption
exposure Acme can support for pull, make, and buy without treating source
dependencies as spend. The cutoff is 2026-08-19. Evidence is bounded to the
approved brief, completed Architecture and Product Value dependencies, pinned
`HC-CODE-001` source at commit `fafac59eeb00cfdc87166242544fa071ecad1723`,
and current public Healthchecks.io pricing, terms, FAQ, and status material.
Reusable expense evidence is [E-036 through E-038](../../evidence/evidence-ledger.md)
and the [commercial packet](../../evidence/packets/vendor-ownership-commercial.md).

No Acme invoice, order, cloud/provider rate, labor rate, cost horizon, selected
topology, alert-volume forecast, job-to-check mapping, contract, account console,
or incident-loss record was available. Source/license presence is not treated as
actual spend, hosted parity, live service, ownership, or cost avoidance.

## Coverage And Material Gaps

The review examined hosted plan prices, annual/monthly arithmetic, check/history/
message/call limits, renewal, fee-change, refund, payment-failure, account-deletion,
support, availability, and vendor-concentration statements. It also traced the
self-host license and the infrastructure, backup, worker, notification-provider,
watchdog, security, recovery, and fork surfaces that would need supplier or labor
rates before they become cost.

[OI-003](../../controls/open-items.md#OI-003) owns Acme rates and the planning
horizon; [OI-015](../../controls/open-items.md#OI-015) owns hosted plan and credit
selection. OI-004, OI-006, OI-012, OI-013, and OI-014 remain commercial-risk,
receipt, billing-control, recovery-objective, and capacity dependencies. Precise
self-host TCO and all-in option ranking are therefore material omissions, not zeroes.

### Executed Checks

| Working directory | Command/tool | Intended coverage | Result | Dependency/installation state | Bounded conclusion |
|---|---|---|---|---|---|
| Project root | `curl -L --max-time 30 -sS <approved URL>`; curl 8.7.1 | Retrieve current official pricing, terms, FAQ, and public status material | Pass after the standard web retriever returned no content; four approved public surfaces were retrieved read-only | Existing curl; no installation or authentication | Current vendor-authored list price and standard statements were readable; they are not an Acme contract or live-control proof. |
| `HC-CODE-001:./` | `git rev-parse HEAD` and direct source inspection | Verify the source pin, license, quota enforcement, and self-host cost surfaces | Pass: exact pinned SHA matched; relevant source/docs were inspected | Existing Git/text tools; no installation | Source establishes rights and mechanisms, not a bill, hosted parity, deployment, or Acme cost. |
| `HC-CODE-001:./` | Project tests | Determine whether expense conclusions required runtime verification | Not started: 0 passed, 0 failed, 0 errors, 0 skipped | No dependency change authorized; cost facts were inspected from public/source evidence | No runtime or hosted behavior is claimed from this review. Existing upstream/local test evidence remains owned by Code Quality. |
| Audit root | `python3 core:scripts/validate_audit_structure.py <audit-root>` | Validate canonical audit structure, evidence table shape, links, and required handoff sections | Pass after adding missing sensitivity cells to E-036/E-037: 0 errors, 0 warnings | Existing Python; no installation | Expense Exposure artifacts satisfy the structural validator; conclusions remain evidence-bounded. |

## Key Findings

| Finding | Severity | Effort | Evidence links | Confidence and limitation | Consequence | Taxonomy |
|---|---|---|---|---|---|---|
| The hosted Business list price is $20/month or $192/year for 100 jobs; Business Plus is $80/month or $768/year for 1,000. Acme is only described as slightly below 100 jobs, so unmeasured check mapping or growth can trigger a fourfold subscription step. | Medium | S | [E-036](../../evidence/evidence-ledger.md#E-036), [burn control](../../controls/expense/burn-and-renewal.md), [OI-015](../../controls/open-items.md#OI-015) | High for dated list price; exact required checks, taxes/FX, selection, and growth unknown | Budget and plan fit can change abruptly even though the current sticker price looks small. | none |
| Business includes only 50 combined SMS/WhatsApp and 20 calls per month; Plus includes 500 and 100. Pinned source refuses sends after configured monthly limits, while hosted parity and any overage mechanism are unproven. | High | M | [E-036](../../evidence/evidence-ledger.md#E-036), [E-038](../../evidence/evidence-ledger.md#E-038), [OI-006](../../controls/open-items.md#OI-006), [OI-015](../../controls/open-items.md#OI-015) | High for published quotas/source mechanics; alert demand, selected channels, and hosted enforcement unknown | A synchronized incident can exhaust a selected critical metered channel, so the five-minute outcome remains unproven without reserved demand and an independently tested secondary path. | none |
| Standard terms disclaim uninterrupted availability, and the FAQ describes a one-person company and says multi-hour or multi-day outages are possible. Published support is email or priority email with no response target. | High | M | [E-036](../../evidence/evidence-ledger.md#E-036), [E-037](../../evidence/evidence-ledger.md#E-037), [OI-004](../../controls/open-items.md#OI-004) | High for public statements; no negotiated terms, performance history, or live evidence | Buy's low subscription price does not transfer Acme's core-monitoring interruption risk or establish an SLA. | none |
| Failed payment beyond 60 days causes downgrade to the 20-job Hobbyist plan; an over-limit account can eventually be deleted after notices to the owner email. Account/billing ownership is unverified. | High | S | [E-037](../../evidence/evidence-ledger.md#E-037), [OI-012](../../controls/open-items.md#OI-012) | High for vendor-authored lifecycle; no Acme account exists | A preventable billing/owner-mailbox failure can interrupt monitoring for the stated workload and can threaten access to monitoring configuration and retained history. | none |
| Pull and make have permissive BSD source rights but no defensible TCO: production topology, service levels, workload, provider prices, Acme rates, and recovery target are absent. The intake's resource and labor estimates remain unsupported. | High | M | [E-035](../../evidence/evidence-ledger.md#E-035), [E-037](../../evidence/evidence-ledger.md#E-037), [E-038](../../evidence/evidence-ledger.md#E-038), [OI-003](../../controls/open-items.md#OI-003) | High for the evidence gaps and license; no actual self-host bill or labor observation | Treating open-source acquisition as free would omit the operational controls required for a core service and distort the decision. | none |
| Make inherits every pull cash surface and adds fork design, regression, merge, security-backport, and release work, but no source delta or cost-saving/value offset is proposed. | Medium | S | [Product Value handoff](../product-value/handoff.md), [E-038](../../evidence/evidence-ledger.md#E-038), [burn control](../../controls/expense/burn-and-renewal.md) | High for current scope; exact effort belongs to Maintenance Cost and is unknown | Funding a fork before a measured source-level need creates recurring ownership without a costable benefit. | none |

## Mandate-Relevant Strengths

- Hosted pricing and major quotas are public and simple enough to reproduce; annual
  Business is $48 below twelve monthly payments and annual Plus is $192 below.
- The vendor documents fee-change notice, billing-failure notices, a more-than-60-day
  past-due runway, cancellation, and invoices. These provide usable billing controls,
  though no availability protection.
- BSD-3-Clause preserves the legal option to self-host or modify without a stated
  product subscription or royalty requirement. Migration, operation, and exit
  readiness remain unproven.
- Quotas and account-lifecycle hazards are documented rather than hidden, allowing
  Acme to set reserves, deputies, and stop conditions before purchase.

### Decision Insights

1. **Buy is the only option with a published recurring product list price; no option
   has a verified all-in TCO or lowest-cost ranking.** The $192 annual Business price
   is concrete, while pull/make cost is not calculable from approved topology, provider,
   and rate evidence. Security review, job integration, independent detection,
   quota proof, billing control, and exit readiness remain Acme responsibilities.
   Smallest next action: close OI-015 and apply OI-003 only after mandatory controls
   are included.
2. **The 100-job boundary is a step function, not comfortable headroom.** A one-to-one
   mapping could nominally fit, but separate checks for overlaps or growth can move
   the published annual price from $192 to $768. Smallest proof: exact required-check
   mapping and one-year growth under OI-015.
3. **The subscription does not buy the outcome Acme requires.** Quotas, disclaimer,
   one-person operations, and no published support target leave five-minute/no-silent-
   loss and recovery risk with Acme. Smallest proof: OI-004, OI-006, OI-012, and
   OI-013 plus an independent watchdog.
4. **Make should be costed only after a measured source-level blocker exists.** With
   no proposed delta and no added product value, a fork can only add ownership at this
   stage. Smallest proof: demonstrate pull still fails a required case after external
   controls, then scope the exact delta for Maintenance Cost.

## Selected Outputs

- Required: this cost/interruption assessment.
- Triggered: [burn, renewal, and interruption control](../../controls/expense/burn-and-renewal.md).
- Reused: [vendor ownership and commercial packet](../../evidence/packets/vendor-ownership-commercial.md).
- Not owned: Business Continuity's transfer controls and Scalability's capacity
  envelope remain their canonical outputs; this reviewer uses them only to route
  pricing and proof.

## Material Omissions, Unknowns, And Auditor Questions

No exact pull/make amount or all-in option ranking is supportable. Missing Acme
cloud/provider and labor rates, selected topology, job/check/alert volume, RTO/RPO,
security design, taxes/FX, and cost horizon are routed through OI-003, OI-004,
OI-005, OI-013, OI-014, and OI-015. Failure loss is not monetized because no
incident frequency or customer/revenue mapping exists; Revenue Risk owns that
consequence analysis.

The Wave 3 boundary resolved the decision portion of [OI-003](../../controls/open-items.md): Acme selected a 36-month horizon, engineering time is opportunity cost rather than cash spend, and no application-architecture-change effort is assigned to pull or make ([E-040](../../evidence/evidence-ledger.md)). Provider rates and any requested opportunity-cost conversion rate remain absent, so cash and engineering time stay separate.

## Reconciliation

This is a fresh Expense Exposure review; no prior expense findings or open items
were retained or superseded. Public pricing offers annual billing, while the
standard terms last updated in 2018 describe monthly billing cycles and automatic
renewal. The public pages do not establish annual order, renewal, and cancellation
mechanics. Pricing also states no prorated refunds while terms permit discretionary
case-by-case refunds. The report preserves these ambiguities and routes order-time
confirmation through OI-004/OI-015 instead of choosing one text.

The `vendor_commercial_collector` completed once with one terminal outcome and
wrote no reviewer conclusion. It could not write the approved path; the coordinator
applied its exact ledger/packet patch. The single required `expense_quality` worker
completed once with one terminal outcome and wrote no audit state. This one revision
removed an unsupported lowest-cost ranking and sole-channel premise, tightened
annual-billing/vendor/licensing boundaries, and preserved the verified arithmetic.
No child task remains running, open, multiply terminated, or ambiguously correlated.

## Bounded Conclusion And Downstream Guidance

Buy has the only published recurring product list price: over 36 months, Business is $720 paid monthly or $576 as three annual payments if Acme's required checks and critical alert volume fit. No option has a verified all-in TCO or lowest-cost ranking.
It is not approved: the 100-job cliff, alert credits, billing ownership, cloud/
security review, standard no-warranty terms, vendor concentration, five-minute
receipt, and recovery/exit evidence remain open. Pull and make cannot be assigned
responsible dollar totals from the approved evidence; make has no present cost-
justified delta and necessarily adds fork ownership.

Maintenance Cost should estimate setup and recurring labor after topology and
RTO/RPO are chosen. Revenue Risk should assess interruption consequence without
turning it into dollars absent exposure data. Neither may assume buy is all-in
cheapest, open source is free to operate, the sample footprint is production fit,
or every required alert fits a published credit quota.
