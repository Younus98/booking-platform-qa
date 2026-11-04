Defect
Finding and documenting a real defect is exactly what QA does. In an interview, you can say: “While building my framework, I found that the single-room API returned a server error, which blocked the reservation page. I reported it, wrote a test that documents it, and adjusted my test plan.” That’s a much better story than “all tests passed.”

Title While building my framework, I found that the single-room API returned a server error
Steps to reproduce 
Expected result
Actual result
Severity (think: does it block booking? Check your severity table.)
Environment (browser, date)


# Defects

## DEF-001: Single-room API returns server error, reservation page never loads

**Severity:** Critical – guests cannot complete a booking, no workaround in the UI

**Environment:** https://automationintesting.online, Microsoft Edge (Windows), found 2026-11-01

**Steps to reproduce:**
1. Open https://automationintesting.online/api/room/1 in a browser
2. Alternatively: open the home page, click "Book now" on any room

**Expected result:**
- API returns status 200 with the details of room 1
- Reservation page shows room details, calendar and booking form

**Actual result:**
- API returns a server error
- Reservation page shows a loading spinner indefinitely

**Comparison:** /api/room (list of all rooms) works correctly

**Automated coverage:** `test_single_room_can_be_fetched` and `test_invalid_room_id_returns_not_found` in tests/api/test_rooms.py, marked xfail until fixed

**Impact on testing:** Booking flow cannot be automated through the UI. Contact form used as the main UI journey instead.