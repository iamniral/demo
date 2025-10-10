import time
from app_launch import launch_app
from login import perform_login


def run_test_suite():
    driver = None
    try:
        # 1. EXECUTE APP LAUNCH AND SETUP (Step 1)
        driver = launch_app()

        # 2. EXECUTE LOGIN ACTIONS (Step 2)
        perform_login(driver)

        print("\n*** TEST SUITE COMPLETED SUCCESSFULLY ***")

    except Exception as e:
        print(f"\n*** TEST SUITE FAILED DURING INITIALIZATION OR EXECUTION ***")
        print(f"Error: {e}")

    finally:
        # 3. CLEAN UP AND QUIT DRIVER
        if driver:
            print("\n--- Cleaning up driver session ---")
            time.sleep(3)
            driver.quit()


if __name__ == '__main__':
    # Ensure Appium Server and Emulator are running before executing this script
    run_test_suite()
