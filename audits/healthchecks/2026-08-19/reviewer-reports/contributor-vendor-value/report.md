# Contributor And Vendor Value

## Audit Question, Depth, And Evidence Boundary

This detailed review asks what usable output, knowledge, handoff capacity, and vendor-relative value are supported by approved evidence, and how ownership concentration changes Acme's pull/make/buy decision. The cutoff is 2026-08-19. Evidence includes complete public Git history for `HC-CODE-001` through pinned commit `fafac59eeb00cfdc87166242544fa071ecad1723`, selected linked issues/PRs/commits and source/tests/docs, current contribution policy, public GitHub metadata, E-037's vendor/license facts, and the completed Product Value and Business Continuity boundaries.

No personnel evidence, Acme team evidence, private reviews, hosted internals, contract, support correspondence, or live service evidence was approved. This report therefore assesses source-supported contribution and dependency concentration, not individual performance, contractual acceptance, live vendor capacity, or Acme readiness.

## Coverage And Material Gaps

The public history was expanded from the onboarding snapshot to the complete 3,913-commit history from 2015-06-11 through the cutoff. A card-defined collector created a selective 23-unit feature set spanning every consecutive cutoff-anchored 12-month period plus the founding partial period. Each unit separates outcome value, task magnitude, delivery quality, direct share, and confidence. Public repository and contributor-index metadata corroborated identity/history only; raw counts were not used as value.

The resulting lifetime and annual top-80 sets are valid only for the supported 118-unit sample. The sample is intentionally not exhaustive; reviews, design, debugging, operations, private work, and uncredited work remain unavailable. That limitation prevents project-wide personnel ranking but does not prevent the narrower concentration and successor findings. OI-016 and OI-017 own the material future action/decision.

No project tests were started for this evidence review: 0 passed, 0 failed, 0 errors, and 0 skipped. The collector used Git/history/source inspection and did not invoke CodeGraph. Historical implementation and tests establish delivered source, not current execution.

## Key Findings

| Finding | Severity | Effort | Evidence links | Confidence and limitation | Consequence | Taxonomy |
|---|---|---|---|---|---|---|
| Direct maintainer value is persistent and concentrated: Pēteris Caune holds 69/118 (58.5%) of the selective supported feature-value set and appears in every annual window. Complete history also attributes 3,680 commits across two emails, but that activity count is corroboration, not the value measure. | High | M | [E-041 and E-042](../../evidence/evidence-ledger.md); [assessment](../../controls/contributors/contribution-value.md) | High for the supported set; not an exhaustive project-wide share or performance result | Upstream interruption can slow fixes/releases for pull, remove a vendor dependency for buy only through an unproved exit, and compound make's fork burden | none |
| External contributors have delivered material alert concurrency, API, scheduling, roles, integrations, and tests; the lifetime supported top-80 threshold requires six contributors because several external contributors have five-unit changes. | Medium | S | [E-042](../../evidence/evidence-ledger.md); [feature units](../../controls/contributors/contribution-value.md#featurechange-units) | High for cited units; episodic units do not establish continuing stewardship | Acme may reasonably reuse upstream work, but cannot treat the community as a substitute owner or guaranteed response path | none |
| Current contribution intake is centralized: the first-person policy requires prior discussion for larger work, defines test expectations, and currently disables pull requests in favor of issue-comment branch handoff. | Medium | S | [E-043](../../evidence/evidence-ledger.md) | High for policy text; response time, acceptance rate, and private review quality are unknown | Acme cannot assume a critical patch will be accepted or reviewed on Acme's timeline; pull needs an emergency patch/exit procedure even without a standing fork | none |
| Buy carries explicit vendor concentration: the vendor describes the service operator as a one-person company, while no Acme-specific SLA, support response, succession, or exit assistance is evidenced. | High | M | [E-037](../../evidence/evidence-ledger.md); [ownership map](../../controls/contributors/ownership-and-successor.md) | Vendor-authored ownership statement; actual staffing and live resilience unverified | A vendor or individual interruption can threaten RTO 30 minutes and continued access unless OI-004, OI-012, and OI-016 close | none |
| BSD-3-Clause rights and a long release history make source retention and self-host exit legally possible, but release authorship, security routing, and recent release tips remain concentrated and do not provide a successor. | Medium | M | [E-037 and E-045](../../evidence/evidence-ledger.md) | High for license/tags; account authority, signing, publication approval, and succession unknown | License reduces lock-in but does not give Acme the people, procedure, artifacts, or recovery proof needed to meet service objectives | none |
| Make creates materially more ownership than pull: it adds upstream merge, security response, release, regression, and successor duties, yet no necessary source change, Acme fork owner/deputy, or sustainable capacity is approved. | High | L | [E-041..E-043](../../evidence/evidence-ledger.md); [OI-017](../../controls/open-items.md) | High for missing approved ownership within the source boundary; team ability intentionally unknown | Choosing make without a narrow proven need can consume 36-month opportunity time and turn an upstream dependency into an Acme single-maintainer dependency | none |
| No option currently has an Acme primary/deputy accountable for source/vendor exit and reconstruction; account transfer is separately governed by OI-012. | High | M | [ownership map](../../controls/contributors/ownership-and-successor.md); [OI-016](../../controls/open-items.md) | High absence claim within approved Acme evidence; no team inquiry was permitted | A loss of upstream/vendor access or knowledge can outlast RTO/RPO even if the application itself remains available | none |

## Mandate-Relevant Strengths

- The BSD-3-Clause license permits Acme to retain, modify, and run the source subject to its notice and non-endorsement terms, reducing legal source lock-in without implying support.
- Public source history spans more than eleven years and includes 77 version tags through v4.3, providing a substantial change record for pull/update planning.
- External contributors have delivered source-backed material capabilities, often with focused tests. Upstream value is not literally a one-person codebase even though ongoing direction/release evidence is concentrated.
- Contribution guidance states clear expectations for prior discussion, tests, style, documentation, and integration completeness.

### Decision Insights

1. **Make should remain stopped unless a source change is proven necessary.** The same concentrated upstream dependency exists under pull, but make additionally assigns permanent merge, security, release, regression, and succession duties to Acme. A wrong choice consumes opportunity time without evidence that it improves the five-minute alert, RTO, RPO, security, or capacity outcomes. The smallest next move is OI-017's narrow fork charter and named primary/deputy only after a source-level necessity is demonstrated.
2. **Buy's low list price does not remove ownership risk.** The hosted service concentrates operation in the same vendor boundary described as a one-person company, and public terms do not provide Acme-specific continuity or exit commitments. The smallest next proof is the bounded OI-004 vendor review plus OI-012/OI-016 account and exit rehearsal against RTO 30 minutes and RPO 5 minutes.
3. **Pull preserves optionality with less new source governance than make, but only if Acme owns emergency independence.** License rights and release history make a pinned upstream deployment plausible; centralized contribution intake means Acme still needs an emergency patch acceptance/temporary patch/upgrade/exit procedure. OI-016 is the minimum ownership control; Architecture, Security, Quality, and Continuity gates remain unchanged.

## Selected Outputs

- [Contributor Value Assessment](../../controls/contributors/contribution-value.md), including 23 feature/change units, the lifetime supported top-80 set, and every consecutive cutoff-anchored 12-month set.
- [Ownership, Vendor Dependency, And Successor Map](../../controls/contributors/ownership-and-successor.md), triggered by material source/vendor concentration and missing successor evidence.
- [Feature-Level Contribution Value Evidence Packet](../../evidence/packets/feature-level-contribution-value.md), the collector's reusable evidence slice.

## Material Omissions, Unknowns, And Auditor Questions

- Project-wide exhaustive feature-value attribution is not supported and is not needed for the option decision. The numeric result must remain labelled as the selective supported set.
- Upstream/vender succession, private review quality, account authority, signing/release approval, hosted staffing, and Acme ownership remain unknown.
- Acme team ability remains intentionally untested. OI-002 is still the general skill verification; OI-016 and OI-017 add the specific successor and fork-authority gates.
- No auditor question was raised. The approved RTO 30 minutes, RPO 5 minutes, 36-month horizon, and opportunity-cost treatment were used without broadening them.

## Reconciliation

No material conflict was found between the Product Value, Business Continuity, vendor-commercial packet, license, repository history, and contribution policy. External material contribution and concentrated ongoing maintainer direction coexist; neither cancels the other. The public contributor index and Git shortlog were reconciled as activity/identity evidence only, not feature value.

The feature collector task `root → contributor_vendor_value_review → feature_contribution_collector` completed once. The coordinator-owned independent quality task `root → contributor_value_quality` completed once with `ACCEPT`, verifying the 118-unit arithmetic, lifetime tie handling, every annual set, selective-sample caveats, evidence/claim separation, ownership map, portable IDs, and option gates. Its sole revision decision was **no change** because it identified no corrective edit; no substantive artifact was altered merely to force a revision.

## Bounded Conclusion And Downstream Guidance

The evidence establishes durable product and maintenance value from the primary maintainer plus episodic material external contributions. It also establishes a meaningful source/vendor concentration boundary and no approved Acme successor for any option. It does not establish individual performance, a project-wide value ranking, vendor incapacity, Acme team readiness, or live operational outcomes.

For the pull/make/buy decision, contributor evidence favors **pull over make** on ownership burden unless a specific source change is first proven necessary; it does not approve pull until existing architecture, security, quality, capacity, recovery, and five-minute alert gates close. Buy remains possible only with vendor/account/exit proof. Project Health should use E-041..E-045 and OI-016..OI-017, and must not translate activity, popularity, or selective feature units into a bus-factor number, performance judgment, or guaranteed support capacity.
