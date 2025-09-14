import pickle

model_path = r'C:\Users\HP\xgb_best_model.pkl'
with open(model_path, 'rb') as f:
    best_model = pickle.load(f)

print("Model loaded successfully!")
