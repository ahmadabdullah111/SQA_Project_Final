import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages.job_application_page import JobApplicationPage
from playwright.sync_api import sync_playwright

def test_duplicate_apply():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        apply_page = JobApplicationPage(page)

        # Step 1: Login as Md Abdullah Talukdar
        apply_page.login("abdullahtalukdar10@gmail.com", "12345678")

        # Step 2: Navigate to Jobs
        apply_page.go_to_jobs()

        # Step 3: Open a job post
        job_title = apply_page.open_first_job()

        # Step 4: First attempt to apply
        try:
            apply_page.apply_to_job()
        except:
            print("ℹ️ Possibly already applied before. Checking for duplicate message...")

        # Step 5: Try applying again to trigger duplicate application message
        apply_page.try_duplicate_application()

        print(f"✅ Test Passed: Duplicate apply test completed for job: '{job_title}'")

        browser.close()

if __name__ == "__main__":
    test_duplicate_apply()
