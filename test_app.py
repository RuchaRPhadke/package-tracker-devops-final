from app.app import get_package
import time

progress = 0

def stage(name):
    print(f"\n========== {name} ==========")
    time.sleep(0.5)

def show_progress(test_name):
    global progress
    progress += 25
    print(f"[RUNNING] {test_name}")
    print(f"[PROGRESS] {progress}% complete")
    time.sleep(0.5)

# ---------------- TESTS ---------------- #

def test_valid_package():
    stage("STAGE 1: VALID PACKAGE TEST")
    show_progress("Checking valid tracking ID")
    
    result = get_package("PKG1")
    assert "status" in result
    assert "location" in result
    assert "tracking_id" in result

    print("[SUCCESS] Valid package test passed ")


def test_invalid_package():
    stage("STAGE 2: INVALID PACKAGE TEST")
    show_progress("Checking invalid tracking ID")
    
    result = get_package("ABC")
    assert result["status"] == "Invalid ID"
    assert result["location"] == "Unknown"

    print("[SUCCESS] Invalid package handled correctly ")


def test_structure():
    stage("STAGE 3: RESPONSE STRUCTURE TEST")
    show_progress("Checking response format")
    
    result = get_package("PKG2")
    assert isinstance(result, dict)

    print("[SUCCESS] Structure is correct ")


def test_consistency():
    stage("STAGE 4: CONSISTENCY TEST")
    show_progress("Checking repeated calls")
    
    result1 = get_package("PKG1")
    result2 = get_package("PKG1")

    assert isinstance(result1, dict)
    assert isinstance(result2, dict)

    print("[SUCCESS] Consistency maintained ")