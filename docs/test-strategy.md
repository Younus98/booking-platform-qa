# Test Strategy – Shady Meadows B&B Booking Platform

**Author:** Muhammad Younus
**System under test:** https://automationintesting.online (Restful-Booker Platform)
**Version:** 1.0

---

## 1. Purpose and scope

- **Purpose:** Show how I plan, prioritise and automate testing for a web booking system, using both API and UI tests.
- **In scope:**
  - Room list (what guests see before booking)
  - Booking a room (date selection, guest details, confirmation)
  - Contact form (sending an enquiry to the hotel)
  - Hotel information (name, address, contact details)
  - Public API endpoints behind these features
- **Out of scope:**
  - Admin area beyond login checks (planned for a later phase)
  - Performance and load testing (shared public demo site – load testing would affect other users)
  - Security and penetration testing
  - Native mobile apps (responsive layout checked only at a basic level)

## 2. Product overview

The system is a small hotel website for a B&B.

| Feature | Who uses it | Notes |
|---------|-------------|-------|
| Room list | Guest | Shows room type, price and features |
| Booking | Guest | Choose dates and room, enter details, confirm |
| Contact form | Guest | Name, email, phone, subject, message |
| Hotel information | Guest | Name, address, contact details, map |
| Admin panel | Hotel staff | Manage rooms, bookings and messages |

The front end uses a public REST API (for example `/api/room`, `/api/branding`), which allows testing below the UI.

## 3. Risks

| Risk | Impact | Priority |
|------|--------|----------|
| Guest cannot complete a booking | Direct loss of revenue | High |
| Same room booked twice for the same dates | Angry guests, refunds, reputation damage | High |
| Wrong room price shown | Revenue loss or customer complaints | High |
| Invalid input accepted (e.g. check-out before check-in, bad email) | Bad data, failed bookings | Medium |
| Contact form messages not delivered | Missed enquiries | Medium |
| Room list or hotel details not loading | Guests leave the site | Medium |
| Layout broken on smaller screens | Poor experience for some users | Low |

Testing effort follows this ranking: high-risk areas get the deepest coverage and run in every pipeline.

## 4. Test approach

- **API tests (largest share):** Fast, stable and easy to maintain. Used for business rules and data checks – room data, booking validation, double-booking prevention, error responses, response schema.
- **UI tests (smaller, focused):** Only for critical user journeys – viewing rooms, completing a booking, sending a contact message. Built with the Page Object Model so tests stay readable when the UI changes.
- **Combined API + UI tests:** Create test data through the API, then verify it in the UI. This is faster and more reliable than setting up everything through the browser.
- **Manual exploratory testing:** Short, time-boxed sessions for usability, unusual input and layout – things automation does not judge well.
- **Test design techniques:** Equivalence partitioning and boundary values (dates, field lengths), plus negative tests for invalid input.

This follows the test pyramid: many fast API tests, fewer slow UI tests.

## 5. Tools and environment

| Area | Tool |
|------|------|
| Language | Python 3 |
| Test runner | pytest |
| API testing | requests, JSON schema validation |
| UI testing | Playwright (pytest-playwright) |
| Browsers | Chromium (main), Firefox and WebKit (cross-browser runs) |
| Version control | Git and GitHub |
| CI/CD | GitHub Actions – tests run on every push |
| Reporting | pytest HTML report |

**Environment:** Public demo site. Data may be reset regularly and is shared with other users, so tests create their own data and do not depend on existing bookings.

## 6. Entry and exit criteria

**Entry criteria (testing can start when):**
- The site and API are reachable
- Smoke tests pass (room list API returns data, home page loads)

**Exit criteria (ready to recommend release when):**
- All high-priority tests pass
- No open critical or high-severity defects
- Medium/low defects are documented, with a clear risk statement
- Test results are summarised in a short quality report with a go / no-go recommendation

## 7. Defect management

| Severity | Meaning | Example |
|----------|---------|---------|
| Critical | Core function broken, no workaround | Booking cannot be completed |
| High | Major function wrong, risky workaround | Double booking possible |
| Medium | Function works but incorrectly in some cases | Weak email validation |
| Low | Cosmetic or minor | Text alignment issue |

Each defect report includes: title, steps to reproduce, expected vs. actual result, severity, environment, and evidence (screenshot, API response or Playwright trace).

## 8. Use of AI in testing

- **Where AI helps:** Generating additional test ideas and edge cases from feature descriptions, drafting test code, and summarising test results.
- **How AI output is checked:**
  - Every generated test is reviewed against the requirement before it is added
  - Generated tests are run several times to catch flaky behaviour
  - Tests that check nothing meaningful, duplicate existing tests or assume behaviour that does not exist are rejected
- **Responsibility:** I stay accountable for the test suite. AI suggestions are treated like a junior colleague's work – useful, but always reviewed.
- **Data:** No confidential or personal data is shared with AI tools.

A log of AI-generated tests and review decisions (kept, changed, rejected) is maintained in `docs/ai-review-log.md`.
