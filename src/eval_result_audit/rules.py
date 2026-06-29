from __future__ import annotations

from eval_result_audit.models import Rule

PROJECT_NAME = 'eval-result-audit'
DESCRIPTION = (
                  'Audit LLM evaluation result exports for gaps, weak judges, and missing r'
                  'ationales.'
              )
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "service", "dataset", "route", "metric", "field", "path")
HIGH_SAMPLE = 'case 42 score pass judge: unknown rationale: missing skipped false'
MEDIUM_SAMPLE = '\\b(rationale\\s*[:=]\\s*(missing|none|null)|rationale missing)\\b'
CLEAN_SAMPLE = 'case 42 score pass judge rubric-v2 rationale grounded answer checked'

RULES = (
    Rule(
        code='unknown-judge',
        severity='high',
        pattern='\\bjudge\\s*[:=]\\s*(unknown|none|null)\\b',
        message='judge identity is missing',
        recommendation='Record judge version, model, or rubric name.',
    ),
    Rule(
        code='missing-rationale',
        severity='medium',
        pattern='\\b(rationale\\s*[:=]\\s*(missing|none|null)|rationale missing)\\b',
        message='judge rationale is missing',
        recommendation='Store concise rationale for auditability.',
    ),
    Rule(
        code='skipped-case',
        severity='low',
        pattern='\\b(skipped\\s*[:=]\\s*true|status\\s*[:=]\\s*skipped)\\b',
        message='eval case was skipped',
        recommendation='Track skipped cases separately from passing cases.',
    ),
)
