# Architecture Topology Preflight

- Repository root: `/Users/patrick/Library/CloudStorage/OneDrive-Drolet/wip/wgo/wgo-docuseal/docuseal`
- Pinned boundary: tag `3.1.7`, commit `a2d8b855491793870b7b4acf176d2d95ae95ff83`
- Observed: 2026-08-06 (audit cutoff)
- Commands: `codegraph status <absolute-root>` and `codegraph query 'Rails application routes controllers services models jobs storage deployment Dockerfile Procfile Vite frontend' --path <absolute-root>`
- Index status: up to date; 627 files, 4,945 nodes, 8,964 edges.
- Language/topology signal: 468 Ruby, 77 JavaScript, 70 Vue, 12 YAML files; indexed kinds include methods, routes, classes, modules, components, imports, and files.
- Initial anchors returned: `config/application.rb` (`Application`), `config/environment.rb`, `app/controllers/application_controller.rb`, and `app/controllers/storage_settings_controller.rb`.
- Limitation: this is a source-index navigation aid only. It does not prove live deployment, runtime behavior, configuration, ownership, approval, rationale, capacity, or control effectiveness. Collectors must verify every material atom directly in pinned source and must not invoke CodeGraph.
