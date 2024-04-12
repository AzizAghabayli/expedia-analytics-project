if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import logging


@transformer
def transform(train_data, test_data, *args, **kwargs):
    """
    Simple transformer to test basic functionality.

    Args:
        train_data (DataFrame): Data from the training dataset.
        test_data (DataFrame): Data from the test dataset.

    Returns:
        Dictionary with basic data info.
    """
    # Set up basic logging
    logging.basicConfig(level=logging.INFO)

    # Log basic information about the datasets
    logging.info(f'Train data shape: {train_data.shape}')
    logging.info(f'Test data shape: {test_data.shape}')
    
    # Output basic info about the dataframes
    output = {
        'train_data_shape': train_data.shape,
        'train_data_columns': train_data.columns.tolist(),
        'test_data_shape': test_data.shape,
        'test_data_columns': test_data.columns.tolist()
    }

    return output


@test
def test_output(output, *args) -> None:
    """
    Tests to ensure that the output of the transformer is as expected.
    """
    assert output is not None, 'The output is undefined'
    assert 'train_data_shape' in output, 'Train data shape missing'
    assert 'test_data_shape' in output, 'Test data shape missing'
    assert isinstance(output['train_data_shape'], tuple), 'Train data shape should be a tuple'
    assert isinstance(output['test_data_shape'], tuple), 'Test data shape should be a tuple'
    logging.info('All tests passed.')
