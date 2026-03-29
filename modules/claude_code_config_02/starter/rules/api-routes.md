---
paths: src/app/api/**/*.ts
---

# API Route Standards

This rule applies to ALL API route files matching `src/app/api/**/*.ts`.

CCA-F Exam Concept: The `paths:` frontmatter directive scopes this rule file
to only apply when Claude is working on files matching the glob pattern.
This is more efficient than putting everything in CLAUDE.md — these rules
only load when relevant files are in context.

## Input Validation (Zod Required)

Every API route MUST validate input using Zod schemas:

```typescript
import { z } from "zod";

const TransferSchema = z.object({
  fromAccountId: z.string().regex(/^ACC-\d{3}$/),
  toAccountId: z.string().regex(/^ACC-\d{3}$/),
  amount: z.number().positive().max(50000),
  currency: z.enum(["USD", "EUR", "GBP"]),
  memo: z.string().max(200).optional(),
});
```

NEVER trust raw `request.json()` without validation. Parse with `.safeParse()` and handle errors.

## Consistent Error Shape

ALL error responses MUST follow this shape:

```typescript
interface ApiError {
  error: {
    code: string;           // Machine-readable: "VALIDATION_ERROR", "NOT_FOUND", "UNAUTHORIZED"
    message: string;        // Human-readable description
    correlationId: string;  // Request trace ID for debugging
    details?: unknown;      // Optional: validation errors, field-level info
  };
}
```

NEVER return plain strings as error responses. NEVER return different error shapes
from different endpoints.

## Correlation IDs

Every request MUST have a correlation ID for tracing:

```typescript
const correlationId = request.headers.get("x-correlation-id") ?? crypto.randomUUID();
// Include in all log entries AND error responses
```

## Authentication

All routes EXCEPT `/api/health` MUST verify the session token:

```typescript
const session = await getServerSession(authOptions);
if (!session) {
  return NextResponse.json(
    { error: { code: "UNAUTHORIZED", message: "Valid session required", correlationId } },
    { status: 401 }
  );
}
```

## HTTP Status Codes

Use correct status codes consistently:
- `200` — Success with body
- `201` — Resource created
- `400` — Validation error (include Zod errors in details)
- `401` — Not authenticated
- `403` — Authenticated but not authorized
- `404` — Resource not found
- `429` — Rate limited
- `500` — Internal server error (log full error, return safe message)
