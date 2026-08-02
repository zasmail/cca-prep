# GTM Applications: Applied AI in Go-To-Market

## The thread

The people building AI-native GTM at Anthropic converge on one non-obvious claim: **Claude's highest value is as connective tissue, not as a new tool.** Eleanor Dorfman, who rebuilt Anthropic's sales org after the Opus 4.6 demand spike, is blunt about it — "Claude is what makes the tools we've already bought talk to one another" ([ai-native-sales-org](../research/notes/ai-native-sales-org.md)). The stack (Salesforce, Clay, Gong, Ironclad, Slack, Lean Data) stays. Claude threads the seams between them, doing "things around that stack, in between that stack." The lesson for an Applied AI engineer: don't rip-and-replace a customer's system of record; integrate against it and own the synthesis layer. This is a [tool-design-and-mcp](tool-design-and-mcp.md) problem before it's a prompting problem.

The second convergence is on the **unit of deployment: (MCP connectors + skills) shipped together.** Dorfman's "sales plug-in" bundles six MCP connectors with five encoded skills (morning brief, call prep, follow-up, competitive intel, create-asset) and hands it to every new rep on day one. Skills alone are brittle without live-data connectors; connectors alone are undifferentiated without the encoded best-rep practice on top. The plug-in exists to make one thing — "what our best reps do" — the baseline for 500+ people. See [skills-and-progressive-disclosure](skills-and-progressive-disclosure.md) for why skills are the right packaging primitive.

Third, everyone building customer-facing GTM automation lands on the same governance shape: **Claude synthesizes context and drafts; a human approves anything that leaves the building.** Dorfman: "AEs still review/approve all AI drafts... Claude handles decision support and context synthesis, not decision authority." Jared Sires' "Class" email tool (short for "Claude Draft") generates the email but the AE reviews before sending ([claude-in-gtm-engineering](../research/notes/claude-in-gtm-engineering.md)). This is the outbox pattern: the model fills a draft queue, a human clicks send. Where the stakes are lower and internal (deal-desk triage, forecasting reconciliation), the gate loosens — Claude resolves policy-aligned tickets and only escalates the ambiguous ones. Matching gate strictness to blast radius is the core design judgment. This connects directly to [enforcement-reliability](enforcement-reliability.md): the send-gate is programmatic, not a prompt asking the model to be careful.

Finally, a cultural claim runs underneath: the enabling role stops being a gatekeeper. Non-technical AEs become "go-to-market architects" who design production workflows once the friction to Claude collapses to three inputs — name, role, context doc ([claude-in-gtm-engineering](../research/notes/claude-in-gtm-engineering.md)). Sales leaders become "systems thinkers over deal strategists" ([ai-native-sales-org](../research/notes/ai-native-sales-org.md)).

## Patterns

**Morning brief / daily recap skill.** A single scheduled skill aggregates priorities across 9+ systems (Gmail, Gong, Slack, Google Docs, Calendar, Salesforce, Intercom, Greenhouse, historical context) and delivers one prioritized output — "these three actions, these emails" — to Slack at 7am. Use it to replace manual day-planning for any high-context knowledge worker. It is the highest-adoption skill Dorfman ships ([ai-native-sales-org](../research/notes/ai-native-sales-org.md)). See [context-engineering](context-engineering.md) for the multi-source aggregation this depends on.

**Sales plug-in (connectors + skills as atomic unit).** Bundle MCP connectors with the skills that ride on them; deploy together, test integration not tools in isolation. Use when standardizing a workflow across many operators ([ai-native-sales-org](../research/notes/ai-native-sales-org.md)).

**Outbox / human-approval gate.** Claude drafts responses, places them directly in the email provider, sends the operator a summary — but the human must click send, and un-sent drafts resurface in the next morning brief. Use for any outbound customer communication ([ai-native-sales-org](../research/notes/ai-native-sales-org.md), customer-follow-up skill; [claude-in-gtm-engineering](../research/notes/claude-in-gtm-engineering.md)).

**Voice preservation via system-prompt identity.** Encode role + name + customer context + brand into a system prompt so generated drafts carry a consistent voice without re-explaining per query. "Class" builds the prompt from three fields; Dorfman's create-asset skill "knows your brand" to avoid shipping "AI slop" ([claude-in-gtm-engineering](../research/notes/claude-in-gtm-engineering.md), [ai-native-sales-org](../research/notes/ai-native-sales-org.md)).

**Slack as front door.** Route all support-function requests (deal desk, legal, RevOps, billing, compliance) into one Slack channel; Claude triages, resolves policy-aligned items against precedent, and escalates the rest with a context-rich ticket (contacts, history from email/Salesforce/Gong) assigned to a human. Use to give non-sales functions elastic capacity ([ai-native-sales-org](../research/notes/ai-native-sales-org.md)).

**Overnight / background account scoring.** Claude + Clay do account research, prioritization, and record updates up front — before the AE is slotted in — pulling historical context from Slack, Docs, and prior Gong calls. Boris runs "a few thousand overnight" agents; the general shape is long-running unsupervised work that resolves a backlog by morning ([ai-native-sales-org](../research/notes/ai-native-sales-org.md), [cherny-fortune-brainstorm](../research/notes/cherny-fortune-brainstorm.md)).

**Dual funnel.** Run AI-qualified self-serve and sales-led routes in parallel off the same qualification backend (Clay + Claude). Use to capture demand you cannot staff against ([ai-native-sales-org](../research/notes/ai-native-sales-org.md)).

**Dynamic coaching.** Claude surfaces the top ~6 coaching moments per rep per week, recomputed as business priorities shift, instead of a static quarterly methodology ([ai-native-sales-org](../research/notes/ai-native-sales-org.md)).

**Individual-first adoption (then multi-team).** Land by making *one* operator "exponentially more powerful" — a personal multiplier — before attempting broad process reengineering; once the agent is embedded in one person's workflow, extend it to multi-person coordination. Jess Yan frames the constraint shift bluntly: "the limits of what we can achieve will be based off how much we can delegate at once, more so than our personal capacities." Distribution matters as much as capability — put the agent where work already happens (chat, cloud code), not in a separate interface ([behind-craft-jess-yan](../research/notes/behind-craft-jess-yan.md)).

## Numbers & rules of thumb

- **54%** of new enterprise logos came through the self-serve funnel in 2026 YTD ([ai-native-sales-org](../research/notes/ai-native-sales-org.md)).
- **9+ systems** feed the morning brief; **6** core tools define the lead journey; **5** skills in the sales plug-in ([ai-native-sales-org](../research/notes/ai-native-sales-org.md)).
- **7am Eastern** brief delivery; **24-hour SLA** for customer follow-up ([ai-native-sales-org](../research/notes/ai-native-sales-org.md)).
- **~70%+** of support tickets resolved by Claude auto-triage without human escalation ([ai-native-sales-org](../research/notes/ai-native-sales-org.md)).
- **600–700 accounts** per AE at scale; **2–3 hours/day** saved on email via "Class"; AEs previously working to **8–9pm** ([claude-in-gtm-engineering](../research/notes/claude-in-gtm-engineering.md)).
- **3 inputs** (name, role, context doc) is the adoption threshold for non-technical users — not 10 config knobs ([claude-in-gtm-engineering](../research/notes/claude-in-gtm-engineering.md)).
- ROI framing beats cost-cutting: "there's probably a thousand percent opportunity to increase return" — democratize tokens, then optimize back-end controls ([cherny-fortune-brainstorm](../research/notes/cherny-fortune-brainstorm.md)).
- **~6-month enterprise adoption lag** behind raw capability (legal, procurement, security friction); individual developers adopt ~6 months *faster*. Diffusion and capability are "two separate, both-steep exponentials on different clocks" — don't read adoption friction as a capability ceiling; design for early adopters (devs, startups) first ([dwarkesh-dario](../research/notes/dwarkesh-dario.md)).
- **Moats are structural, not model access.** Dario expects a 3–4 player Cournot oligopoly sustained by capital barriers + differentiation (reasoning, coding style, voice), and Cherny argues once model access equalizes the advantage is *organizational process* — how teams restructure workflows — not prompts or model hoarding ([dwarkesh-dario](../research/notes/dwarkesh-dario.md), [cherny-sequoia-ascent](../research/notes/cherny-sequoia-ascent.md)).
- **Internal-first / dogfooding as the product strategy.** Claude Code succeeded because Anthropic engineers built and used it alongside model development — proximity to capability, tight feedback loops, and "get all tacit knowledge into written form" so it's accessible to Claude ([dwarkesh-dario](../research/notes/dwarkesh-dario.md), [behind-craft-alex-albert](../research/notes/behind-craft-alex-albert.md)).

## Where speakers disagree

**How much to trust automation vs. the human gate.** Dorfman holds a hard line on customer-facing outbound: humans review every draft, "Claude handles decision support... not decision authority" ([ai-native-sales-org](../research/notes/ai-native-sales-org.md)). Boris pushes the opposite direction — auto mode is *more* secure than human-in-the-loop because permission prompts cause fatigue, and prompt-injection resistance runs ~1% attack success ([cherny-fortune-brainstorm](../research/notes/cherny-fortune-brainstorm.md)). The reconciliation is blast-radius: internal SDLC actions can go full-auto; a proposal to a customer still gets a human click. But they genuinely weight the same tradeoff differently.

**Deterministic vs. probabilistic workflows.** Dorfman celebrates moving "from just deterministic workflows to probabilistic ones" as an accelerant to embrace. Yet her own governance-critical steps (close-won checklist, billing reconciliation, one-skill-per-step) stay tightly deterministic. The tension: probabilistic freedom for generation, determinism for compliance — she runs both and doesn't fully reconcile which wins where.

**Plan vs. ship.** Cat Wu's "just do things" / build-before-ready ([lennys-cat-wu](../research/notes/lennys-cat-wu.md)) sits against Dorfman still spending "at minimum a 10-minute discussion on how we should forecast" every meeting. Rigorous process persists exactly where the ground is shifting fastest.

## Interview-ready takes

1. **"Connective tissue, not a new tool."** The winning GTM architecture integrates against the existing stack and owns synthesis between systems. Rip-and-replace loses; threading Claude through Salesforce↔Slack↔Gong wins ([ai-native-sales-org](../research/notes/ai-native-sales-org.md)).

2. **Ship connectors and skills as one unit.** Skills without live-data connectors are brittle; the "plug-in" is the deployment primitive that makes one best-rep practice the baseline for hundreds. Test the integration, not the tool in isolation ([ai-native-sales-org](../research/notes/ai-native-sales-org.md)).

3. **The send-gate is programmatic, the draft is probabilistic.** Model fills the outbox; a human clicks send on anything customer-facing; un-sent items resurface in tomorrow's brief. Match gate strictness to blast radius ([ai-native-sales-org](../research/notes/ai-native-sales-org.md), [enforcement-reliability](enforcement-reliability.md)).

4. **Adoption is an interface-design problem.** Non-technical operators became "GTM architects" only when the entry point collapsed to three fields. Map the workflow first, then simplify the interface — don't expose config knobs ([claude-in-gtm-engineering](../research/notes/claude-in-gtm-engineering.md)).

5. **Lead with ROI, not cost.** Democratize tokens to discover emergent use cases; add per-seat budgets and model-selection controls only after the use cases surface. Cost-cutting first strangles the thousand-percent upside ([cherny-fortune-brainstorm](../research/notes/cherny-fortune-brainstorm.md)).
