import pandas as pd
import random

# Function to generate a random spy key while avoiding consecutive repeats
def generate_spy_key(previous_spy_keys):
    all_spy_keys = list(df.index)
    
    for key in previous_spy_keys:
        all_spy_keys.remove(key)
    
    return random.choice(all_spy_keys)

# Function to draw a single spy key
def draw_spy_key(previous_spy_keys):
    spy_key = generate_spy_key(previous_spy_keys)
    print(f'Spy Key: {spy_key}')
    previous_spy_keys.append(spy_key)
        
    # Keep only the last 5 spy keys
    if len(previous_spy_keys) > 5:
        previous_spy_keys.pop(0)

# Function to reset the stored previous_spy_keys
def reset_spy_keys():
    global previous_spy_keys
    previous_spy_keys = []

# Create a dataframe with 'spy_id' and 'spy_name'
data = {'spy_key': [''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=10)) for _ in range(5)],
        'spy_name': ['Allen', 'Kasper', 'Hao', 'Haotian', 'Chef Liz']}

df = pd.DataFrame(data)
df.set_index('spy_key', inplace=True)

# Export individual csvs
for index, row in df.iterrows():
    row.to_csv(f'{row["spy_name"]}.csv', index_label='spy_key', header=True)

# Initialize an empty list to store previous spy keys
previous_spy_keys = []

# Print out the spy table
# print(df)

# Draw a single spy key
draw_spy_key(previous_spy_keys)

# Resetting spy keys
# reset_spy_keys()
