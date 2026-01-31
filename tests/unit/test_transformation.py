from data_processing.data_transformation.transformation import main

def test_transformation_runs():
    """
    Transformation should run without errors
    """
    result = main()
    assert result is None or result is True
