from datasets import load_dataset

# Load the dataset
dataset = load_dataset("liuxuannan/MMFakeBench", "MMFakeBench_test")

# Print the first example in the dataset
print(dataset['train'][0])
