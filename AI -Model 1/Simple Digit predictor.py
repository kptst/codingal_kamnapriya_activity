from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Load the digits dataset (0-9 images)
digits = datasets.load_digits()

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    digits.data, digits.target, test_size=0.2, random_state=42
)

# Train a KNN model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Function to display and predict a digit
def predict_digit(index):
    image = X_test[index].reshape(8, 8)
    plt.imshow(image, cmap='gray')
    plt.title("Digit Image")
    plt.axis('off')
    plt.show()

    prediction = model.predict([X_test[index]])
    print(f"🤖 Predicted Digit: {prediction[0]}")
    print(f"✅ Actual Digit: {y_test[index]}")

# Run the predictor
if __name__ == "__main__":
    print("🔢 Simple Digit Predictor using KNN")

    while True:
        try:
            idx = int(input(f"\nEnter a number between 0 and {len(X_test)-1}: "))
            if 0 <= idx < len(X_test):
                predict_digit(idx)
            else:
                print("❗ Please enter a valid number.")
        except ValueError:
            print("❗ Invalid input. Enter an integer.")

        again = input("Try another digit? (yes/no): ").strip().lower()
        if again != "yes":
            print("👋 Exiting. Thanks!")
            break
