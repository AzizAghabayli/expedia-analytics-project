if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import dask.dataframe as dd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@transformer
def transform(train_data, test_data, countries_data, *args, **kwargs):
    logging.info('Starting the transformation process with manual chunk processing.')

    # Define a function to process chunks of data
    def process_chunks(data):
        chunk_size = 500000  # Define chunk size, adjust based on memory availability
        num_chunks = len(data) // chunk_size + (1 if len(data) % chunk_size != 0 else 0)
        processed_frames = []

        for i in range(num_chunks):
            start_idx = i * chunk_size
            end_idx = start_idx + chunk_size
            chunk = data.iloc[start_idx:end_idx]
            # Example processing: parsing date columns
            chunk['date_time'] = pd.to_datetime(chunk['date_time'], errors='coerce')
            processed_frames.append(chunk)

        return pd.concat(processed_frames)

    # Process each DataFrame in chunks
    final_train = process_chunks(train_data)
    final_test = process_chunks(test_data)

    logging.info('Date parsing completed for both datasets.')
    logging.info('Transformation process completed. Returning the transformed datasets.')

    return final_train, final_test



@test
def test_output(output, *args) -> None:
    """
    Tests to ensure that the output of the transformer is as expected.
    """
    assert output is not None, 'Output is undefined'
    assert 'date_time' in output[0].columns, 'Date column missing in train dataset'
    assert 'date_time' in output[1].columns, 'Date column missing in test dataset'
    logging.info('All tests passed successfully.')
