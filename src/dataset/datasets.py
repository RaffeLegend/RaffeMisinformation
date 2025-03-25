from datasets import load_dataset

# Load the dataset
dataset = load_dataset('your_dataset_name')

# Print the first example in the dataset
print(dataset['train'][0])