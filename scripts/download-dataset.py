import kagglehub

# Download latest version
path = kagglehub.competition_download('the-3lc-low-light-detection-challenge')

print("Path to competition files:", path)