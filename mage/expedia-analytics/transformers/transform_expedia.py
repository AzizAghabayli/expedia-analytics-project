if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import logging

@transformer
def transform(test_data, train_data, *args, **kwargs):
    logging.basicConfig(level=logging.INFO)
    logging.info('Starting advanced transformation.')

    # Handling missing values
    test_data.fillna(test_data.mean(), inplace=True)
    train_data.fillna(train_data.mean(), inplace=True)

    logging.info('Missing values handled.')

    # Returning basic data shape info as before
    output = {
        'test_data_shape': test_data.shape,
        'train_data_shape': train_data.shape
    }
    return output

@test
def test_output(output, *args) -> None:
    assert output is not None, 'Output is undefined'
    assert 'test_data_shape' in output, 'Missing test data shape'
    assert 'train_data_shape' in output, 'Missing train data shape'
    logging.info('Test passed successfully.')
