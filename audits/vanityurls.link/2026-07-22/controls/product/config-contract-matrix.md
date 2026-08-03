# Product Configuration And Outcome Contract

## Evidence Boundary

This matrix traces cutoff-pinned implementation and documentation through July 22, 2026. It does not prove that an instance was built, deployed, accepted, or observed live.

## Contract Matrix

| Operator intent/control | Authoritative source | Transformation/validation | Runtime consumer | User-visible outcome | Demonstration status |
|---|---|---|---|---|---|
| Exact short link | `custom/v8s-links.txt` | Link parser, target validation, registry tree build | Worker exact lookup | HTTP redirect to configured target | Implemented; live request unknown |
| Splat short link | `SLUG/*` plus target containing `:splat` | Splat validation and tree `splat_link` | Worker longest available splat match | Redirect with encoded remainder substitution | Implemented; live request unknown |
| Lifecycle/expiry | State and `expires_at` columns | Build normalizes lifecycle fields | Worker state/expiry resolver | Redirect or 403/410/503/404 status page | Implemented; transition observation unknown |
| Scheduled target | Inline `@schedule` block or compatibility schedule file | Parser validates rule order/timezone and emits schedule | Worker evaluates current scheduled date | Temporary target, else fallback/normal target | Implemented; clock-window observation unknown |
| Destination policy | Default or replacement `custom/v8s-policies.json` | Policy validation plus generated runtime blocklist | Build checks and Worker scanner fallback | Unsafe/blocked targets rejected or hidden | Implemented; safety efficacy/sign-off unknown |
| Languages/branding/operator | Default plus `custom/v8s-site-config.json` | Deep merge, schema/content validation, page rendering | Static assets and Worker page routing | Localized public/trust/status pages | Implemented; rendered/live acceptance unknown |
| Private stats/tests | Access team domain plus audience secret and Terraform policy | Build config plus JWT/JWKS verification | Worker protected-path handler | Access gate, 503 if unconfigured, 403 if invalid | Implemented/intended; applied Access unknown |
| Analytics | `ANALYTICS_PROVIDER` plus provider values/secrets | Provider selection and event normalization | Worker `ctx.waitUntil()` sender | Redirect/page response plus optional event | Disabled in reference instance source; provider observation unknown |
| Product upgrade | Stable tag/ref and protected local paths | Upgrade source selection, file sync, dependency/check step | Instance Git worktree and later build | New product behavior with local choices retained | Implemented/documented; successor upgrade unobserved |

## Material Contract Gaps

- OI-004 must prove the operator-to-outcome path with a non-creator and capture assistance.
- OI-002/OI-006 must prove external Access, deployment, domain, and recovery authority for continuity of the existing service.
- Trust/legal/privacy/accessibility claims require applicable specialist approval before being treated as externally accepted.
