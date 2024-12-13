Here’s the extracted text data from the image:

| Algorithm                                 | Time Complexity (Training)              | Time Complexity (Prediction)        |
|-------------------------------------------|-----------------------------------------|-------------------------------------|
| Linear Regression (OLS)                   | \( O(nm^2 + m^3) \)                    | \( O(m) \)                          |
| Linear Regression (SGD)                   | \( O(n_{\text{epoch}} nm) \)           | \( O(m) \)                          |
| Logistic Regression (Binary)              | \( O(n_{\text{epoch}} nm) \)           | \( O(m) \)                          |
| Logistic Regression (Multiclass OvR)     | \( O(n_{\text{epoch}} nmc) \)          | \( O(mc) \)                         |
| Decision Tree                             | \( O(n \log(n) \cdot m) \)             | \( O(n^2 \cdot m) \)               |
| Random Forest Classifier                 | \( O(n_{\text{trees}} \cdot n \log(n) \cdot m) \) | \( O(d_{\text{trees}} \cdot d_{\text{tree}}) \) |
| Support Vector Machines (SVMs)           | \( O(nm^2 + m^3) \)                    | \( O(m \cdot n_{\text{sv}}) \)     |
| k-Nearest Neighbors                       | -                                       | \( O(nm) \)                         |
| Naive Bayes                               | \( O(nm) \)                            | \( O(mc) \)                         |
| Principal Component Analysis (PCA)       | \( O(nm^2 + m^3) \)                    | -                                   |
| t-SNE                                     | \( O(n^2m) \)                          | -                                   |
| KMeans Clustering                         | \( O(ikmn) \)                          | ??                                  |

**Legend:**
- \( n \): samples
- \( m \): dimensions
- \( n_{\text{epoch}} \): epochs
- \( c \): classes
- \( d_{\text{tree}} \): depth
- \( n_{\text{sv}} \): Support vectors
- \( k \): clusters
- \( i \): iterations


-------

