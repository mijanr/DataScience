"""
Create a Streamlit app that takes in features about the iris flower and returns the species of the flower.
"""
import streamlit as st
from main import IrisModel
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris


def load_data():
    iris = load_iris()
    X = iris.data
    y = iris.target
    return X, y


def app():
    model = IrisModel()
    # load model
    model.load()

    st.title("Predicting Iris Flower Species")

    sepal_length = float(st.number_input("Sepal Length (cm)"))
    sepal_width = float(st.number_input("Sepal Width (cm)"))
    petal_length = float(st.number_input("Petal Length (cm)"))
    petal_width = float(st.number_input("Petal Width (cm)"))

    target_names = ["Setosa", "Versicolor", "Virginica"]
    if st.button("Predict"):
        species = model.predict(
            [[sepal_length, sepal_width, petal_length, petal_width]]
        )
        probas = model.predict_proba(
            [[sepal_length, sepal_width, petal_length, petal_width]]
        )
        st.write(
            f"Species predicted: {target_names[species[0]]} with {probas.max()*100:.2f}% confidence"
        )

    # We will plot how the train data clusters in 2D space and then see how the test data fits in it.
    # First apply PCA to reduce the dimensionality of the data to 2D
    X, y = load_data()
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    data_test = [[sepal_length, sepal_width, petal_length, petal_width]]
    data_test = pca.transform(data_test)

    # add class labels as legend
    fig, ax = plt.subplots()
    for i in range(3):
        ax.scatter(X_pca[y == i, 0], X_pca[y == i, 1], label=target_names[i])
    # Use "test_data" as label for the test data
    ax.scatter(
        data_test[:, 0], data_test[:, 1], c="red", marker="x", s=100, label="test_data"
    )
    ax.set_xlabel("First Principal Component")
    ax.set_ylabel("Second Principal Component")
    ax.set_title("Train data")
    ax.legend()
    st.pyplot(fig)


if __name__ == "__main__":
    app()
