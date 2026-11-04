# AI Review Log

Record of AI-generated test code and how it was reviewed before being kept.

## 2026-11-03 – Negative tests and cleanup (GitHub Copilot)

**Generated:**
- Parametrized negative tests for the contact form (5 invalid inputs with expected validation messages)
- Parametrized tests for invalid room IDs, marked as xfail
- Extra assertion that the room list is not empty
- Cleanup of duplicated code in test_rooms.py

**Kept:**
- Contact form negative tests – one invalid field per run, clear test-case structure, error messages match the real site
- `validation_error()` in the ContactForm page object – follows the existing page object pattern and uses an exact text match
- Non-empty room list assertion
- Duplicate code removal – the duplicates had caused confusing test results earlier

**Questioned:**
- The xfail reason for invalid room IDs assumes a 500 response. This was not verified separately, and because all /api/room/{id} calls currently fail, the test cannot tell the two problems apart until the main defect is fixed.

**Improvements identified (not yet done):**
- Negative tests should also check that no success message appears
- Add valid boundary cases (phone with 11 characters, subject with 5 characters)

**How I verified:**
- Ran the full suite: 14 passed, 3 xfailed
- Reviewed the full diff with `git diff` before committing
- Compared the expected validation messages with the real website

**Improvements made after review:**
- Negative tests now also check that no success message appears
- Added valid boundary tests: subject with 5 characters, message with 20 characters
- Found that the happy-path test already covers the valid phone boundary (11 characters)