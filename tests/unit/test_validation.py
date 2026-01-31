from data_processing.data_validation.validation import main

def test_validation_passes():
    """
    Validation should return PASS for clean data
    """
    status = main()
    assert status == "PASS"
