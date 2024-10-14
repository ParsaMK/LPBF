On average each layer takes around 6.2 seconds to inference on so probably if we do 4 images per each layer it would be 24-25 seconds. 
I ran the code again a couple of days after and it tooke around 3.5 seconds for each layer so I believe it depends on the Jestson's power consumption mode or the tasks queued on it.



<!-- here's a description of each file:
- photo-extractor.py: Gets the dataset from the datasets folder and extracts all the photos in a dataset and puts them in a folder with the same name under 'extracted' folder
- testing.py: It's there to test sending a Rest call to the Jetson
- area-extractor.py: It gets the dataset from the 'extracted' folder and makes API calls to the jetson to get the areas and then saves it in the inferences folder
- inf-dataset-merger.py: Merges the inferenced areas and the csv files from the dataset of our choice
- ultimate-dataset-maker.py: merges all the datasets, giving each row a unique key (since before the key was LayerID and different datasets have similar LayerIDs) and then saves 3 different datasets; one with the area normalized, one with the area standardized and one with the areas untouched. -->

## File Descriptions
- **`photo-extractor.py`**: Extracts all the photos from the datasets in the `datasets/` folder and saves them in the corresponding subfolders under the `extracted/` folder.
- **`testing.py`**: Contains a simple script to test REST API calls to the Jetson device for inference.
- **`area-extractor.py`**: Retrieves datasets from the `extracted/` folder, makes API calls to the Jetson to extract areas, and saves the results in the `inferences/` folder.
- **`inf-dataset-merger.py`**: Merges the inferenced areas with the CSV files of the selected dataset.
- **`ultimate-dataset-maker.py`**: Merges all datasets, assigns unique keys to each row (to handle duplicate `LayerID`s), and saves three versions of the dataset: 
    - Area Normalized
    - Area Standardized
    - Area Untouched