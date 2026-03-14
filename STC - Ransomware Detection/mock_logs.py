import pandas as pd
import numpy as np

def generate_mock_logs(n_samples=100):
    # Benign log samples
    benign = pd.DataFrame({
        'eid_count': np.random.randint(100, 500, n_samples),
        'create_count': np.random.randint(5, 30, n_samples),
        'write_count': np.random.randint(20, 100, n_samples),
        'delete_count': np.random.randint(0, 10, n_samples),
        'unique_extensions': np.random.randint(5, 15, n_samples),
        'avg_event_gap': np.random.uniform(0.5, 2.0, n_samples),
        'label': 0  # benign
    })

    # Ransomware log samples
    ransomware = pd.DataFrame({
        'eid_count': np.random.randint(800, 2000, n_samples),
        'create_count': np.random.randint(20, 100, n_samples),
        'write_count': np.random.randint(200, 800, n_samples),
        'delete_count': np.random.randint(50, 300, n_samples),
        'unique_extensions': np.random.randint(15, 50, n_samples),
        'avg_event_gap': np.random.uniform(0.01, 0.2, n_samples),
        'label': 1  # ransomware
    })

    # Combine, shuffle, and return
    combined = pd.concat([benign, ransomware]).sample(frac=1).reset_index(drop=True)
    return combined

# Generate dataset
df = generate_mock_logs(n_samples=200)

# Save to CSV
df.to_csv("mock_ransomware_logs.csv", index=False)

